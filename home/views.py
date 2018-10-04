from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from management.models import Dipendente


@login_required(login_url='/authentication/login/')
def index(request):
    if request.method == 'GET':
        search_user = request.GET.get('searchuser', "").upper()
        search_role = request.GET.get('searchrole', "").upper()
        search_city = request.GET.get('searchcity', "").upper()
        result = {}

        if search_user == "" and search_role == "" and search_city == "":
            return render(request, 'home/index.html', {})

        if not checkinput(search_user, search_role, search_city):
            result['Error'] = "item not in database"
            return render(request, 'home/index.html', {'result': result})

        try:
            query = Dipendente.objects.all()

        except:
            print("Error reading the database")

        # rimuovo dalla query tutto ciò che non matcha grazie a Q che opera da NOT
        else:
            if search_user != "":
                query = query.exclude(~Q(nick=search_user))

            if search_role != "":
                query = query.exclude(~Q(ruolo=search_role))

            if search_city != "":
                query = query.exclude(~Q(sede=search_city))

        # inserisco i risultati in un dizionario
        for k in query:
            result[k] = k.ruolo, k.sede

        return render(request, 'home/index.html', {'result': result})

    return render(request, 'home/index.html', {})


# controllo che i dati inseriti siano presenti nel database
def checkinput(search_user, search_role, search_city):
    if search_user != "":
        try:
            Dipendente.objects.get(nick=search_user)
        except:
            return False

    if search_role != "":
        try:
            check = Dipendente.objects.filter(ruolo=search_role)
        except:
            print("error reading db")
        if not check:  # se il queryset è vuoto la stringa inserita è errata
            return False

    if search_city != "":
        try:
            check = Dipendente.objects.filter(sede=search_city)
        except:
            print("error reading db")
        if not check:
            return False

    return True
