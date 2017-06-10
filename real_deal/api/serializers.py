from rest_framework import serializers

from real_deal.offers.models import Offer, MerchantOffer


class MerchantOfferSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='merchant.name', read_only=True)

    class Meta:
        model = MerchantOffer
        fields = ('name',)


class OfferSerializer(serializers.ModelSerializer):
    merchants = MerchantOfferSerializer(source='merchantoffer_set', many=True)

    class Meta:
        model = Offer
        fields = ('title', 'short_description', 'copy', 'merchants')
