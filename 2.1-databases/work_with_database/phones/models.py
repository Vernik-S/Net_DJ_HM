from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    # slug =  AutoSlugField(populate_from='name')
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return self.name
