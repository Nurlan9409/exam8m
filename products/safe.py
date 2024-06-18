import uuid
from django.db import models


class SaveMediaFile(object):

    def product_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/{uuid.uuid4()}.{image_extension}"

    def category_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"category/{uuid.uuid4()}.{image_extension}"


class PriceType(models.TextChoices):
    USD = "$", '$'
    UZB = "Som", "SOM"





