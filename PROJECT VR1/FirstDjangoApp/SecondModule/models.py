from django.db import models

# Create your models here.


class UserData(models.Model):
    username = models.CharField(max_length=50,)
    password = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)

    def _str_(self) -> str:
        return self.username+" "+self.password+""+str(self.isAdmin)
