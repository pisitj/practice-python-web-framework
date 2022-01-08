# Previous Tutorial
a simple pastebin code highlighting Web API. 


### Serialization
https://www.django-rest-framework.org/tutorial/1-serialization/

### Class-based Views
https://www.django-rest-framework.org/tutorial/3-class-based-views/


# This Tutorial
Currently our API doesn't have any restrictions on who can edit or delete code snippets. We'd like to have some more advanced behavior in order to make sure that:

- Code snippets are always associated with a creator.
- Only authenticated users may create snippets.
- Only the creator of a snippet may update or delete it.
- Unauthenticated requests should have full read-only access.

# Authentication & Permissions

### models.py
- models.ForeignKey

### serializers.py
- serializers.ReadOnlyField
- serializers.PrimaryKeyRelatedField

### permissions.py
- custom permissions class

### views.py
- permission_classes

