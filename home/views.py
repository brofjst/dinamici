from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from management.models import Dipendente

@login_required(login_url='/authentication/login/')
def index(request):
    if request.method == 'GET': # If the form is submitted
        search_user = request.GET.get('searchuser', None)
        search_role = request.GET.get('searchrole', None)
        search_city = request.GET.get('searchcity', None)

        query = 0

        if search_user != "":
            if query == 0:
                query = Dipendente.objects.filter(nick=search_user)
            else:
                query = query.objects.filter(nick=search_user)

        if search_role != "":
            if query == 0:
                query = Dipendente.objects.filter(ruolo=search_role)
            else:
                query = query.objects.filter(nick=search_role)

        if search_city != "":
            if query == 0:
                query = Dipendente.objects.filter(sede=search_city)
            else:
                query = query.objects.filter(nick=search_city)

        """try:
            for dip in Dipendente.objects.filter(nick=search_user, ruolo=search_role, sede=search_city):
                list.append(str(dip))
        except Dipendente.DoesNotExist:
            print("Apress isn't in the database yet.")
        else:
            print (list)
        """

        query = str(query)

        print (query)

    return render(request, 'home/index.html', {})
