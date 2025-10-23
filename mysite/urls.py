from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 💥 BU SƏTRİ ƏLAVƏ EDİN 💥
    # Boş yolu '' (yəni /) polls tətbiqinin urls.py faylına yönəldir
    path('', include('polls.urls')), 
    
    # İdarəetmə paneli üçün mövcud yol
    path('admin/', admin.site.urls),
    
    # Əgər əvvəlki path('polls/', include('polls.urls')) sətri var idisə, 
    # onu artıq silə bilərsiniz, çünki bütün / ünvanı polls-a yönəltdiniz.
]