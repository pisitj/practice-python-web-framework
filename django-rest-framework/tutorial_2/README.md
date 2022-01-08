# Introduction
- This tutorial will cover creating a simple pastebin code highlighting Web API. 
- Along the way it will introduce the various components that make up REST framework, and give you a comprehensive understanding of how everything fits together.

# Serialization
https://www.django-rest-framework.org/tutorial/1-serialization/

### serializers_v1.py
- serializers.Serializer

### serializers_v2.py
- serializers.ModelSerializer

### views_v1.py
- function-based views
- request.method
- SnippetSerializer
- JsonResponse

# Class-based Views
https://www.django-rest-framework.org/tutorial/3-class-based-views/

### views_v2.py
- APIView

### urls_v2.py
- as_view

### views_v3.py
- mixins.ListModelMixin
- mixins.CreateModelMixin
- mixins.RetrieveModelMixin
- mixins.UpdateModelMixin
- mixins.DestroyModelMixin
- generics.GenericAPIView

### views_v4.py
- generics.ListCreateAPIView
- generics.RetrieveUpdateDestroyAPIView