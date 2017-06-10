from django.db import models


class Merchant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    copy = models.TextField()

    def __str__(self):
        return self.title


class MerchantOffer(models.Model):
    merchant = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.merchant)} - {str(self.offer)}'
