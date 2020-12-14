from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [path('', views.all_posts, name='all_posts'),
               path('<int:year>-<int:month>-<int:day>-<slug:slug>', views.post_detail,
                    name='post_detail')
               # چیزهایی که در بالا داده ایم، دقیقا داخل views هم باید داده باشیم
               ]
