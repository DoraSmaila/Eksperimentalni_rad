import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class ProfesorFactory(DjangoModelFactory):
    class Meta:
        model = Profesor

    prof_ime = factory.Faker("first_name")
    prof_prezime = factory.Faker("last_name")
    prof_email = factory.Faker("email")


class PredmetFactory(DjangoModelFactory):
    class Meta:
        model = Predmet

    predmet_naslov = factory.Faker("sentence", nb_words=4)
    predmet_sadrzaj = factory.Faker("sentence", nb_words=50)
    predmet_nositelj = factory.Iterator(Profesor.objects.all())