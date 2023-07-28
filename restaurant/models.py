from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    items = models.TextField()

    def __str__(self):
        return str(self.restaurant)


class MenuVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'menu')

    def __str__(self):
        return f"{self.user} voted for {self.menu}"
