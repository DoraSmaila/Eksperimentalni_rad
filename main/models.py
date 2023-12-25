from django.db import models

# Create your models here.
class Profesor(models.Model):
    prof_ime = models.CharField(max_length=30)
    prof_prezime = models.CharField(max_length=30)
    prof_email = models.EmailField()

    def __str__(self):
        return self.prof_email

class Predmet(models.Model):
    predmet_naslov = models.CharField(max_length=100)
    predmet_sadrzaj = models.TextField()
    predmet_nositelj = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.predmet_naslov