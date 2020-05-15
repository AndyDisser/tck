from django.db import models

TRAINING_CHOICES = [
    ("Einzeln","Einzelstunden"),
    ("Abo", "Abo"),
    ("Camp", "Tenniscamp")
    ]

class Trainingsangebot(models.Model):
    name = models.CharField(max_length=50)
    add_info = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField()
    category = models.CharField(max_length=64, choices=TRAINING_CHOICES)

    def __str__(self):
        return f"{self.name} €{self.price}"
