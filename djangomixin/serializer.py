from rest_framework import serializers

from .models import Name  , Person




class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields= ('id' , 'name' , 'age')
    

class NameSerializer(serializers.ModelSerializer):
    age = PersonSerializer(read_only=True,many=True)

    class Meta:
        model = Name
        fields = ('id','first_name' , 'last_name','age')


    def create(self, validated_data):
        age_datas = validated_data.pop('age')
        name = Name.objects.create(**validated_data)
        for age_data in age_datas:
            Person.objects.create(name=name, **age_data)
        return name




    
    
