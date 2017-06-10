from django.conf import settings

import requests
from rest_framework import viewsets, response, mixins

from real_deal.offers.models import Offer

from .serializers import OfferSerializer


ENGLISH = 1
MONEY_OFF = 35


class OffersViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        url = 'https://sandbox.api.visa.com/vmorc/offers/v1/byfilter'
        r = requests.get(
            url,
            cert=(settings.VISA_CERT_PATH, settings.VISA_PRIVKEY_PATH),
            auth=(settings.VISA_USERNAME, settings.VISA_PASSWORD),
            params={'language': ENGLISH}
        )
        visa_data = r.json()

        data = [
            {
                'title': offer['offerTitle'],
                'short_description': offer['offerShortDescription']['text'],
                'copy': offer['offerCopy']['text'],
                'merchants': [
                    {'name': merchant_name(merchant['merchant'])}
                    for merchant in offer['merchantList']
                ]
            }
            for offer in visa_data['Offers']

        ]

        return response.Response(data)


def merchant_name(name):
    '''Convert ugly name to pretty name!'''
    if name == 'Merchant One 1':
        return 'Bath & Body Works'
    elif name == 'Merchant Two':
        return 'Walmart'
    return name
