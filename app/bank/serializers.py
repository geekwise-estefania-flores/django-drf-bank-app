from django.contrib.auth.models import User, Group
from rest_framework import serializers 
	class User_Serilizers( serializers.HyperlinkedModelSerializer ):
		class Meta:
			model = User 
			fields = ['url', 'username', 'email', 'groups']

    class Group_Serilializer(serializers.HyperlinkedModelSerialzer ):
	    class Meta:
		    model = Group 
		    fields = ['url', 'name']
