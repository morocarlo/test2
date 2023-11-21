from random import randint
from django.http import HttpResponse, JsonResponse
from gestionale.models import Esame, Paziente

def index(request):
    id = request.GET.get('id')
    valore = request.GET.get('valore')

    p = Paziente.objects.get(id=id)
    
    e = Esame()
    e.valore = valore
    e.unita_misura = 'mg'
    e.paziente = p
    e.save()

    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    esami = Esame.objects.filter(valore__gte=10)
    risultati = []
    for esame in esami:
        risultati.append({
            'esame_valore': esame.valore,
            'codice_fiscale': esame.paziente.codice_fiscale,
        })

    return JsonResponse(risultati, safe=False)