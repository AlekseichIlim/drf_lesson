from rest_framework import serializers

from vehicle.models import Car, Moto, Milage
from vehicle.services import convert_cur
from vehicle.validators import TitleValidator


class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)
    # milage_set.all.first - объекты millage привязанные к car, first - самый первый
    # milage = MilageSerializer(source='milage_set', many=True)
    # milage_set выводить не надо после вложения реалайзера milage в реалайзер Car
    milage = MilageSerializer(many=True, read_only=True)
    usd_price = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_usd_price(self, obj):
        return convert_cur(obj.amount)


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        # if instance.milage_set.all().first().milage:
        #     return instance.milage_set.all().first().milage
        if instance.milage.all().first().milage:
            return instance.milage.all().first().milage
        return 0
#     instance или obj - объект с которым непосредственно работают
# _set - не надо выводить после добавления related_name='milage' в модель milage


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer(read_only=True)

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto', )


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator(field='title'),
                      serializers.UniqueTogetherValidator(fields=['title', 'descriptions'], queryset=Moto.objects.all())
        ]

    def create(self, validated_data):
        milage_data = validated_data.pop('milage')
        # исключаем поле milage т.к его нет у объекта Moto
        moto_item = Moto.objects.create(**validated_data)
        for m in milage_data:
            Milage.objects.create(**m, moto=moto_item)
        return moto_item