from django.contrib.auth.models import User, Group
from .models import Account, Customer, Product
from rest_framework import viewsets
from bank.serializers import User_Serializers, Group_Serializers, Account_Serializers, Customer_Serializers, Product_Serializers

class User_Viewset( viewsets.ModelViewSet ):
	"""
		API endpoint that allows users to viewed or edited 
	"""

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = User_Serializers

class Group_Viewset( viewsets.ModelViewSet):
	"""
		API endpoint that allows groups to be viewed or edited 
	"""
	queryset = Group.objects.all()
	serializer_class = Group_Serializers

class Account_Viewset( viewsets.ModelViewSet ):
    """
		API endpoint that allows groups to be viewed or edited 
	"""
    queryset = Account.objects.all()
    serializer_class = Account_Serializers

class Customer_Viewset( viewsets.ModelViewSet):
	"""
		API endpoint that allows groups to be viewed or edited 
	"""
	queryset = Customer.objects.all()
	serializer_class = Customer_Serializers

class Product_Viewset( viewsets.ModelViewSet):
	"""
		API endpoint that allows groups to be viewed or edited 
	"""
	queryset = Product.objects.all()
	serializer_class = Product_Serializers
