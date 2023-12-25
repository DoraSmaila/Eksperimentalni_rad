from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
import json
from rest_framework.renderers import JSONRenderer

from main.serializers import ProfesorSerializer,PredmetSerializer
from main.models import Profesor,Predmet
# Create your views here.
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer



class ProfesorList(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class PredmetList(generics.ListCreateAPIView):
    queryset = Predmet.objects.all()
    serializer_class = PredmetSerializer

class PredmetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Predmet.objects.all()
    serializer_class = PredmetSerializer



#Ažuriranje jednog polja: Napravite putanju koja će samo ažurirati polje u ParentModel-u.
@api_view(['PUT'])
def update_single_field(request, pk):
    profesor_instance = get_object_or_404(Profesor, pk=pk)

    # Provera da li POST zahtev sadrži vrednost za polje koje želimo da ažuriramo
    if 'new_value' not in request.data:
        return Response({'error': 'New value not provided'}, status=status.HTTP_400_BAD_REQUEST)

    new_value = request.data['new_value']
    profesor_instance.field_to_update = new_value
    profesor_instance.save()

    serializer = ProfesorSerializer(profesor_instance)
    return Response(serializer.data)

#Ažuriranje cele liste: Napravite putanju koja će ažurirati sve ChildModel-e povezane sa određenim ParentModel-om. NE RADI
@api_view(['PUT'])
def update_all_predmeti_for_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    # Provera da li PUT zahtev sadrži nove vrednosti za polja predmeta
    if 'predmeti' not in request.data:
        return Response({'error': 'Predmeti not provided'}, status=status.HTTP_400_BAD_REQUEST)

    predmeti_data = request.data['predmeti']

    for predmet_data in predmeti_data:
        predmet_naslov = predmet_data.get('predmet_naslov')
        predmet = get_object_or_404(Predmet, predmet_naslov=predmet_naslov, predmet_nositelj=profesor)

        # Ažurirajte polja predmeta prema potrebi
        predmet.predmet_naslov = predmet_data.get('predmet_naslov', predmet.predmet_naslov)
        predmet.predmet_sadrzaj = predmet_data.get('predmet_sadrzaj', predmet.predmet_sadrzaj)
        # Izbegavajte direktno postavljanje predmet_nositelj ovde, jer ste već filtrirali po njemu
        predmet.save()

    serializer = PredmetSerializer(profesor.predmeti.all(), many=True)
    return Response(serializer.data)


#    • Čitanje: Normalizovana struktura: Uzmi vreme čitanja ParentModel-a i vreme čitanja ChildModel-a odvojeno.
@api_view(['GET'])
def read_profesori(request):
    profesori = Profesor.objects.all()
    serializer = ProfesorSerializer(profesori, many=True,context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def read_predmeti(request):
    predmeti = Predmet.objects.all()
    serializer = PredmetSerializer(predmeti, many=True,context={'request': request})
    return Response(serializer.data)


#JSON kao string: Poredi vreme čitanja ParentModel-a i vreme čitanja ChildModel-a kad koristite JSON kao string za listu.
@api_view(['GET'])
def read_profesori_j_string(request):
    profesori = Profesor.objects.all()
    serializer = ProfesorSerializer(profesori, many=True, context={'request': request})
    data = serializer.data
    json_data = json.dumps(data)
    return Response(json_data)

@api_view(['GET'])
def read_predmeti_j_string(request):
    predmeti = Predmet.objects.all()
    serializer = PredmetSerializer(predmeti, many=True, context={'request': request})
    data = serializer.data
    json_data = json.dumps(data)
    return Response(json_data)


#JSON type Poredi vreme čitanja Profesora i vreme čitanja Predmeta 
@api_view(['GET'])
def read_profesori_j_type(request):
    profesori = Profesor.objects.all()
    serializer = ProfesorSerializer(profesori, many=True, context={'request': request})
    json_data = JSONRenderer().render(serializer.data)
    return Response(json_data)

@api_view(['GET'])
def read_predmeti_j_type(request):
    predmeti = Predmet.objects.all()
    serializer = PredmetSerializer(predmeti, many=True, context={'request': request})
    json_data = JSONRenderer().render(serializer.data)
    return Response(json_data)
