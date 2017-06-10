from rest_framework import viewsets, response, mixins

from real_deal.offers.models import Offer

from .serializers import OfferSerializer


class OffersViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    pagination_class = None
