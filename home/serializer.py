from .models import Attractions, DosDonts, NearbyHotels, ThingsToExplore

from rest_framework import serializers


class DosDontsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosDonts
        fields = '__all__'


class NearbyHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearbyHotels
        fields = '__all__'


class ThingsToExploreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThingsToExplore
        fields = '__all__'


class AttractionsSerializer(serializers.ModelSerializer):
    dos_donts = serializers.SerializerMethodField()
    nearby_hotels = NearbyHotelsSerializer(many=True, read_only=True)
    things_to_explore = ThingsToExploreSerializer(many=True, read_only=True)

    class Meta:
        model = Attractions
        fields = ['id', 'name', 'location', 'description', 'image_url', 'rating', 'price', 'duration', 'category',
                  'dos_donts', 'nearby_hotels', 'things_to_explore']

    def get_dos_donts(self, obj):
        result = DosDonts.objects.filter(attraction=obj)
        dos_donts = {
            'dos': [],
            'donts': []
        }
        for item in result:
            dos_donts['dos'].append(item.dos)
            dos_donts['donts'].append(item.donts)
        return dos_donts