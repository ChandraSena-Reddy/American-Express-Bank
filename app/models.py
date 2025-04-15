from django.db import models

# Create your models here.
class bank(models.Model):
    name=models.CharField(max_length=32)
    gender=models.CharField(max_length=10)
    phone=models.IntegerField()
    aadhar=models.IntegerField()
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=32)
    acc=models.BigIntegerField(unique=True)
    pin=models.IntegerField(default=0)
    bal=models.IntegerField(default=1000)

    def save(self, *args, **kwargs):
        if not self.acc:
            last_account = bank.objects.all().order_by('-acc').first()
            if last_account:
                self.acc = last_account.acc + 1
            else:
                self.acc = 1234567890
        super().save(*args, **kwargs)
