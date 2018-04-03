import csv,sys,os,sys

project_dir = "../.."
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'graphsite.settings'

import django

django.setup()

from management.models import Dipendente

data = csv.reader(open("dipendenti.csv"),delimiter=',')


for row in data:
    if row[0] != None:
        Dip = Dipendente()
        Dip.nick=row[0]
        Dip.ruolo=row[1]
        if row[2] == "05387": Dip.sede = "BANCA POPOLARE DELL'EMILIA ROMAGNA"
        if row[2] == "01015": Dip.sede = "BANCO DI SARDEGNA"
        if row[2] == "90012": Dip.sede = "BPER SERVICES S.C.P.A."
        if row[2] == "90013": Dip.sede = "MODENA TERMINAL S.R.L."
        if row[2] == "90036": Dip.sede = "BPER CREDIT MANAGEMENT S.C.P.A."
        if row[2] == "05676": Dip.sede = "BANCA DI SASSARI"
        if row[2] == "00057": Dip.sede = "OPTIMA S.P.A."
        if row[2] == "19257": Dip.sede = "SARDALEASING SPA"
        if row[2] == "06095": Dip.sede = "CASSA DI RISPARMIO DI BRA S.P.A."
        if row[2] == "90023": Dip.sede = "FAP - FONDO AGGIUNTIVO PENSIONI BDS"
        if row[2] == "90035": Dip.sede = "BPER TRUST COMPANY"
        if row[2] == "90078": Dip.sede = "ITALIANA VALORIZZAZIONI IMMOBILIARI SRL"
        if row[2] == "19432": Dip.sede = "EMIL.RO FACTOR"
        if row[2] == "90076": Dip.sede = "SIFA' SOC. ITALIANA FLOTTE AZIENDALI SPA"
        Dip.name = row[0]
        Dip.save()
