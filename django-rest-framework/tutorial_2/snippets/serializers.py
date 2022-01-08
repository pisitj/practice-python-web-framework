from rest_framework import serializers
from snippets.models import Snippet, LANGAUGE_CHOICES, STYLE_CHOICES

# serializer.ModelSerializer
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
