import json
from web.models import *
from web.serializers import BeaconSerializer, LocalSerializer
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers


# Create your views here.
class OndeEstou(APIView):
    def post(self, request):
        try:
            beacon = request.data
            espacoObjs = Espaco.objects.filter(beacon_espaco = beacon["beacon_espaco"])
            localObjs = Local.objects.filter(beacon_local = beacon["beacon_local"])
            espaco= espacoObjs[0]
            local = localObjs[0]
            o_a = ["o", "a"]
            texto = "Você está n"+o_a[espaco.auxiliar]+" "+espaco.nome+ " d"+o_a[local.auxiliar]+" "+local.nome
            response = {
            'local': local.nome,
            'espaco': espaco.nome,   
            'texto' : texto         
            }

            return JsonResponse(response, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class DescreverLocal(APIView):
    def post(self, request):
        try:
            beacon = request.data
            espacoObjs = Espaco.objects.filter(beacon_espaco = beacon["beacon_espaco"])
            localObjs = Local.objects.filter(beacon_local = beacon["beacon_local"])
            espaco= espacoObjs[0]
            local = localObjs[0]
            O_A = ["O", "A"]
            o_a = ["o", "a"]
            texto = O_A[espaco.auxiliar]+ " "+espaco.nome+ " d"+o_a[local.auxiliar]+" "+local.nome+", "+espaco.descricao
            response = {
            'local': local.nome,
            'espaco': espaco.nome,   
            'texto' : texto         
            }

            return JsonResponse(response, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Destinos(APIView):
    def post(self, request):
        try:
            beacon = request.data
            espacoObjs = Espaco.objects.filter(beacon_espaco = beacon["beacon_espaco"])
            destinos = []
            for d in Destino.objects.filter(espaco_inicio = espacoObjs[0]):
                percursos = []
                print(d)
                for p in Percurso.objects.filter(destino = d):
                    serialized = {
                        'espaco_inicio': p.espaco_inicio.nome,
                        'espaco_fim' : p.espaco_fim.nome,
                        'sequencia' : p.sequencia,
                        'instrucao' : p.instrucao
                    }
                    percursos.append(serialized)
                    print(p.instrucao)
                #destino_final = Espaco.objects.filter(id = d.espaco_final)
                serialized_ = {
                    'nome' : d.espaco_final.nome,
                    'percursos' : percursos
                }
                destinos.append(serialized_)
            response = {}
            response['destinos'] = destinos
            print(response)
        
            return JsonResponse(response, status=status.HTTP_200_OK)
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
            print(locais)
            return JsonResponse(locais, status=status.HTTP_200_OK)          
        except Exception:
            return JsonResponse({'mensagem': "deu ruim"}, status.HTTP_500_INTERNAL_SERVER_ERROR)