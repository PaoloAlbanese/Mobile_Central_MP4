from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# We're in producto models.


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    reviewDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
