from rest_framework import serializers

from app_dir.casino.models import Casino, Deals, Bonus, Country, CountryUrl


class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = [
            'name',
            'logo',
            'description',
            'url_casino',
            'slug',
            'background',
            'is_recommended',
            'logo_background'
        ]


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = [
            'name',
            'percent',
            'price',
        ]


class CountryUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryUrl
        fields = [
            'url',
        ]


class DealsSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer()
    bonus = BonusSerializer()
    url_country = CountryUrlSerializer(many=True)

    class Meta:
        model = Deals
        fields = [
            'id',
            'name',
            'casino',
            'bonus',
            'deal_message',
            'free_spins',
            'wager',
            'deal_url',
            'url_country',
            'deal_disclaimer',
            'rating_number'
        ]
