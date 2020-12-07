from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('cyberschool/', include('cyberschool.urls')),
    path('accounts/', include('accounts.urls')),
    path('initiation/', include('initiation.urls')),
    path('teachers/', include('initiation.urls_teacher')),
    path('competency_standard/', include('operating_standard.urls')),
    path('competency_nasional/', include('operating_standard.urls_competency')),
    path('competency_international/', include('operating_standard.urls_competency_eng')),
    path('competency_local/', include('operating_standard.urls_competency_loc')),\
    path('admin/', admin.site.urls),
]
