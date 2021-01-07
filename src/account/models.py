from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# ایمپورت خط 3 برای اضافه کردن اطلاعات کلاس پروفایل به یوزر است تا بدین ترتیب بعد از سیو و ایجاد هر یوزر این
# آپشن ها اضافه شود.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# signals(جلسه8):
def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()


post_save.connect(save_profile, sender=User)
# از طریق خط بالا به یوزر وصل شده و اطلاعات یوزر رو میگیریم
# post_save دو مقدار created و instance رو برمیگردونه
