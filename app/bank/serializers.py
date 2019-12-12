from django.contrib.auth.models import User, Group
from rest_framework import serializers 

class User_Serializers( serializers.HyperlinkedModelSerializer ):
	class Meta:
		model = User 
		fields = ['url', 'username', 'email', 'groups']

class Group_Serializers( serializers.HyperlinkedModelSerializer ):
	class Meta:
		model = Group 
		fields = ['url', 'name']

class Account_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'account_number']

# class Branch_Serializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Branch
#         fields = []

class Customer_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email']

class Product_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_options', 'card_options']