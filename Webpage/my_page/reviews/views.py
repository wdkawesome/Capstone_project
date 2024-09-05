from django.shortcuts import render
from .models import Reviews

def header(request):
    """
    Render a webpage displaying student reviews.

    This view function renders a webpage that displays student reviews stored in the database.
    It fetches a list of review objects from the 'Reviews' model and passes them to a template
    for rendering.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response displaying student reviews.
     """
    object_list = Reviews.objects.all()

    return render(request, "reviews/review.html", {"reviews": object_list})

