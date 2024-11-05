from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','description','content','date','author']
        read_only_fields = ['date','author']

        def create(self,validated_data):
            validated_data['author'] = self.context['request'].author
            return super().create(validated_data)
        

from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name','password']
        #this for hidding the password
        extra_kwargs = {'password':{'write_only':True}}
    
    # this method is called to hash passwords
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance       
       