from rest_framework import serializers

from main.models import Profesor, Predmet

class PredmetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Predmet
        fields = ('predmet_naslov', 'predmet_sadrzaj','predmet_nositelj')

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    predmeti = PredmetSerializer(many=True,read_only=True)
    class Meta:
        model = Profesor
        fields = ('prof_ime', 'prof_prezime','prof_email','predmeti')


