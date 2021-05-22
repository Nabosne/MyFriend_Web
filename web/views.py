import json
from web.models import *
from web.serializers import BeaconSerializer, LocalSerializer
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers


# Create your views here.
class OndeEstou(APIView):
    def post(self, request):
        try:
            print("Entrou no serializer")
            beacon = request.data
            espacoObj = Beacon.objects.filter(beaconEspaco = beacon["beacon_espaco"])
            espaco = espacoObj.values('nome')
            localObj = Local.objects.filter(beaconLocal = beacon["beacon_local"])
            local = localObj.values('nome')

            return JsonResponse({"local": local[0]['nome'], "espaco": espaco[0]['nome']}, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class DescreverLocal(APIView):
    def post(self, request):
        try:
            print("Entrou no serializer")
            beacon = request.data
            espacoObj = Beacon.objects.filter(beaconEspaco = beacon["beacon_espaco"])
            espaco = espacoObj.values('nome', 'descricao')
            localObj = Local.objects.filter(beaconLocal = beacon["beacon_local"])
            local = localObj.values('nome')

            return JsonResponse({"local": local[0]['nome'], "espaco": espaco[0]['nome'], "descricao": espaco[0]['descricao']}, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Destinos(APIView):
    def post(self, request):
        try:
            print("Entrou no serializer")
            beacon = request.data

            return JsonResponse({"_local": "Faculdade","espaco": "banheiro", "descricao": "aqui vc caga"
            }, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Locais(APIView):
    def get(self, request):
        try:
            list = []
            for e in Local.objects.all().values():
                print(e)
                lapp = LocalApp(e)
                serialized = {
                    'beacon_local': lapp.beacon_local,
                    'nome' : lapp.nome,
                    'telefone' : lapp.telefone,
                    'texto' : lapp.texto
                }
                list.append(serialized)
            locais = {}
            locais['locais'] = list
            return JsonResponse(locais, status=status.HTTP_200_OK)          
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)