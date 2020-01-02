from rest_framework import serializers

from app_dir.casino.models import Casino, Deals, Bonus


class CasinoSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    logo_background = serializers.SerializerMethodField()

    def get_logo(self, obj):
        return obj.logo

    def get_logo_background(self, obj):
        return obj.logo_background

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
