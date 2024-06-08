from rest_framework import serializers
from .models import CustomUser,Category,Product,Order,OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
    

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Set read_only to True for category field

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'description', 'image']

        def create(self, validated_data):
            category_data = validated_data.pop('category')
            category,created = Category.objects.get_or_create(**category_data)
            print(category,created)
            product = Product.objects.create(category=category, **validated_data)
            return product
        

        def update(self, instance, validated_data):
            category_data = validated_data.pop('category')
            category,created = Category.objects.get_or_create(**category_data)

            print(instance)
            instance.category = category
            instance.name = validated_data.get('name', instance.name)
            instance.price = validated_data.get('price', instance.price)
            instance.description = validated_data.get('description', instance.description)
            instance.image = validated_data.get('image', instance.image)

            instance.save()

            return instance



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']
           

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'ordered_date', 'is_ordered']

        def create(self, validated_data):
            items_data = validated_data.pop('items')
            order = Order.objects.create(**validated_data)

            for item_data in items_data:
                OrderItem.objects.create(order=order, **item_data)
            return order
        

        def update(self, instance, validated_data):
         
            items_data = validated_data.pop('items')
            instance.user = validated_data.get('user', instance.user)
            instance.total_price = validated_data.get('total_price', instance.total_price)
            instance.ordered_date = validated_data.get('ordered_date', instance.ordered_date)
            instance.is_ordered = validated_data.get('is_ordered', instance.is_ordered)
            instance.save()

                  # Handle order items
            for item_data in items_data:
                order_item_id = item_data.get('id')
                if order_item_id:
                    order_item = OrderItem.objects.get(id=order_item_id, order=instance)
                    order_item.quantity = item_data.get('quantity', order_item.quantity)
                    order_item.save()
            else:
                OrderItem.objects.create(order=instance, **item_data)

            return instance


    