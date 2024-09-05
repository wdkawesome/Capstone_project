from django.shortcuts import render
from django.http import HttpRequest


# a definition to display the home content
def home(request):
    """
    Render the 'home.html' template.

    This view function renders the 'home.html' template when a user accesses the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response displaying the 'home.html' template.
    """
    return render(request, "home.html")
