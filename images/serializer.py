from rest_framework import serializers
from .models import MyProfile,MyProject

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ('name', 'bio', 'contact','profile_image') 

class ProjectSerializer(serializers.ModelSerializer):  
    class Meta:
        model = MyProject
        fields = ('title', 'image', 'detail','poster','link') 


        