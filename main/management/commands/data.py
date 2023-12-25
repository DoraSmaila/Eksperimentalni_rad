import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Profesor, Predmet
from main.factories import (
    ProfesorFactory,
    PredmetFactory
)

NUM_PROFESORS= 10
NUM_PREDMETS = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Profesor, Predmet]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PROFESORS):
            profesor = ProfesorFactory()

        for _ in range(NUM_PREDMETS):
            predmet = PredmetFactory()