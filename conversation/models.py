from django.db import models
from django.contrib.auth.models import User


# Import the Product model
from product.models import Product

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='conversations',
        on_delete=models.CASCADE
    )
    users = models.ManyToManyField(
        User,
        related_name='conversations'
       
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
    auto_now=True
   )

    class Meta:
        ordering = ['-modified_at',]  # ensures that conversations are retrieved in descending order


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        related_name='messages',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='created_messages',
        on_delete=models.CASCADE
    )