from django.conf import settings

import requests
from rest_framework import viewsets, response, mixins, generics

from real_deal.offers.models import Offer

from .serializers import OfferSerializer


ENGLISH = 1
MONEY_OFF = 35
FREE_TRIAL = 74


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
                'copy': offer_copy(offer['title'], offer['offerCopy']['text']),
                'merchants': [
                    {'name': merchant_name(merchant['merchant'])}
                    for merchant in offer['merchantList']
                ]
            }
            for offer in visa_data['Offers']
            if offer['offerType'][0]['key'] in (MONEY_OFF, FREE_TRIAL)
        ]

        return response.Response(data)


def merchant_name(name):
    '''Convert ugly name to pretty name!'''
    if name == 'Merchant One 1':
        return 'Walmart'
    elif name == 'Merchant Two':
        return 'Target'
    return 'Bath & Body Works'


def offer_copy(offer_title, orig_copy):
    if offer_title == 'Save $30':
        return 'Save $30 on purchases that exceed $125 when you use your visa card'
    elif offer_title == 'Save $40':
        return 'Save $40 on purchases that exceed $150 when you use your visa card'
    elif offer_title == 'Free Trial':
        return 'Exlusive for Visa cardholders, call for availability'
    return orig_copy


class AlexaAskViewSet(viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        r = requests.post('http://localhost:5000/_ask', data=request.data)
        return response.Response(r.json(), status=r.status_code)
