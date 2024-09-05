from django.db import models


class Reviews(models.Model):
    """
    Model for Reviews

    This model represents reviews with fields for 'title', 'body', and 'name'.
    It is used to store information about reviews.

    Attributes:
        title (CharField): A field for the review title with a maximum length of 140 characters.
        body (TextField): A field for the review body.
        name (CharField): A field for the name of the reviewer with a maximum length of 140 characters.

    Methods:
        __str__(): Returns the title of the review as its string representation.

    Example usage:
        review = Reviews.objects.create(title="Great Product", body="I loved it!", name="John Doe")
    """

    title = models.CharField(max_length=140)
    body = models.TextField()
    name = models.CharField(max_length=140)

    def __str__(self):
        """
        String representation of the review.

        Returns:
            str: The title of the review.
        """
        return self.title
