"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FirstProject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Course/',views.Course),
    path('course/<courseid>',views.courseDetails),
    path('home',views.homePage,name='home'),
    path('userform',views.userForm,name='form'),
    # path('submitform/',views.submitform,name='submitform'),
    path('calculator/',views.calculator,name='calci'),
    path('evenodd/',views.evenodd),
    path('',views.signupview,name='signup'),
    path('login',views.Login,name='login'),
    path('newDetails/<slug>',views.newDetails),
    path('Images',views.Imageuploader,name='uploader'),


    # path('next',views.Next,name='next'),

]
print(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
