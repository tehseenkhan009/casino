from rest_framework import serializers

from app_dir.casino.models import Casino, Deals, Bonus


class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = [
            'name',
            'logo',
            'description',
            'logo_background'
        ]


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = [
            'name',
            'percent',
            'price'
        ]


class DealsSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer()
    bonus = BonusSerializer()

    class Meta:
        model = Deals
        fields = [
            'name',
            'casino',
            'bonus',
        ]
