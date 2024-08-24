from django.db import models

class CardDatabase(models.Model):
    managed = True
    id_image = models.IntegerField()
    name_image = models.CharField(max_length=1000)
    type_image = models.CharField(max_length=1000)
    desc_image = models.CharField(max_length=1000)
    card_image = models.CharField(max_length=1000)

class CardClassic(models.Model):
    managed = True
    id_image = models.IntegerField()
    name_image = models.CharField(max_length=1000)
    type_image = models.CharField(max_length=1000)
    race_image = models.CharField(max_length=1000)
    level_image = models.CharField(max_length=1000)
    desc_image = models.CharField(max_length=1000)
    card_image_small = models.CharField(max_length=1000)
    card_image_ori = models.CharField(max_length=1000)

class CardByNumber(models.Model):
    managed = True
    id_image = models.IntegerField()
    name_image = models.CharField(null=True, blank=True, max_length=1000)
    type_image = models.CharField(null=True, blank=True, max_length=1000)
    race_image = models.CharField(null=True, blank=True, max_length=1000)
    level_image = models.CharField(null=True, blank=True, max_length=1000)
    desc_image = models.CharField(null=True, blank=True, max_length=1000)
    card_image_small = models.CharField(null=True, blank=True, max_length=1000)
    card_image_ori = models.CharField(null=True, blank=True, max_length=1000)

class CardByName(models.Model):
    managed = True
    id_image = models.IntegerField()
    name_image = models.CharField(null=True, blank=True, max_length=1000)
    type_image = models.CharField(null=True, blank=True, max_length=1000)
    race_image = models.CharField(null=True, blank=True, max_length=1000)
    level_image = models.CharField(null=True, blank=True, max_length=1000)
    desc_image = models.CharField(null=True, blank=True, max_length=1000)
    card_image_small = models.CharField(null=True, blank=True, max_length=1000)
    card_image_ori = models.CharField(null=True, blank=True, max_length=1000)

class CardBySpell(models.Model):
    managed = True
    id_image = models.IntegerField()
    name_image = models.CharField(null=True, blank=True, max_length=1000)
    type_image = models.CharField(null=True, blank=True, max_length=1000)
    race_image = models.CharField(null=True, blank=True, max_length=1000)
    level_image = models.CharField(null=True, blank=True, max_length=1000)
    desc_image = models.CharField(null=True, blank=True, max_length=1000)
    card_image_small = models.CharField(null=True, blank=True, max_length=1000)
    card_image_ori = models.CharField(null=True, blank=True, max_length=1000)

class CardByTrap(models.Model):
    managed = True
    id_image = models.IntegerField()
    name_image = models.CharField(null=True, blank=True, max_length=1000)
    type_image = models.CharField(null=True, blank=True, max_length=1000)
    race_image = models.CharField(null=True, blank=True, max_length=1000)
    level_image = models.CharField(null=True, blank=True, max_length=1000)
    desc_image = models.CharField(null=True, blank=True, max_length=1000)
    card_image_small = models.CharField(null=True, blank=True, max_length=1000)
    card_image_ori = models.CharField(null=True, blank=True, max_length=1000)