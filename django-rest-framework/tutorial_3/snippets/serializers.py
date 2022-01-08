from rest_framework import serializers

from snippets.models import Snippet, LANGAUGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# serializer.ModelSerializer
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='ownser.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']