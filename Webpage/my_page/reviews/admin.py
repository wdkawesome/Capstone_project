from django.contrib import admin

from .models import Reviews
"""
Register the 'Reviews' model with the Django admin site.

This code registers the 'Reviews' model with the Django admin site, allowing administrators
to manage and edit reviews in the database using the Django admin interface.

The 'Reviews' model should be defined in your Django application's models.py file, and
this registration code is typically placed in the admin.py file of the same application.

Example:
    To use this registration in your Django project, ensure that:
    1. The 'Reviews' model is defined in your application's models.py file.
    2. You've created an admin.py file in the same application directory.
    3. In the admin.py file, add the import statement for 'Reviews':
       ```python
       from .models import Reviews
       ```
    4. Register the 'Reviews' model with the admin site using the 'admin.site.register' method:
       ```python
       admin.site.register(Reviews)
       ```
"""
