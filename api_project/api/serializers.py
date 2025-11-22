from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    
    class Meta:
        model = MyModel
        fields = ['title']

    class Meta:
        model = MyModel
        fieldS = ['author']

    class Meta:
        model = MyModel
        fields = ['published_date']

    def published_date(self, obj):
        from datetime import datetime, timezone
        return (datetime.now(timezone.utc)- obj.published_at).days