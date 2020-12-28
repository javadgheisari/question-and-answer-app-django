from django.urls import path
from . import views

app_name = 'posts'
# در app_name همان اسمی که در url اصلی به عنوان namespace پاس داده ایم را فراخونی میکنیم به نوعی
urlpatterns = [path('', views.all_posts, name='all_posts'),
               path('<int:year>-<int:month>-<int:day>-<slug:slug>', views.post_detail,
                    name='post_detail')
               # چیزهایی که در بالا داده ایم، دقیقا داخل views هم باید داده باشیم
               ]
