from django.db import models

# Create your models here.
class Hero:
    def __init__(self, name, s_name, desc, img):
        self.name = name
        self.s_name = s_name
        self.desc = desc
        self.img = img