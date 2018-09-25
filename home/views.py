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

        try:
            query = Dipendente.objects.all()

        except:
            print("not in database")

        # rimuovo dalla query tutto ciò che non matcha grazie a Q che opera da NOT
        else:
            if search_user != "":
                query = query.exclude(~Q(nick=search_user))

            if search_role != "":
                query = query.exclude(~Q(ruolo=search_role))

            if search_city != "":
                query = query.exclude(~Q(sede=search_city))

        # inserisco i risultati in un dizionario
        result = {}
        for k in query:
            result[k] = k.ruolo, k.sede

        return render(request,'home/index.html', result)

    return render(request, 'home/index.html', {})
