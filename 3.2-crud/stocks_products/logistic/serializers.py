from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', ]


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'stock', 'product', 'quantity', 'price', ]
        extra_kwargs = {'stock': {'required': False}}

    def validate_quantity(self, value):
        if value > 1000:
            raise ValidationError("Не больше тысячи штук на одном складе")

        return value

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Цена должна быть больше нуля")

        return value


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['id', 'address', "positions", ]

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for position in positions:
            position_object = StockProduct.objects.create(stock=stock, **position)
            stock.positions.add(position_object)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        # print(validated_data)
        # print(positions)
        for position in positions:
            product = position.pop("product")

            position_object, created = StockProduct.objects.update_or_create(stock=stock, product=product,
                                                                             defaults={**position})

            # stockproduct_object = StockProduct.objects.filter(stock=stock, product=product)
            # print(stockproduct_object)
            # stock.positions.add(position_object)
            # print(position)
            # print(**position)

        return stock
