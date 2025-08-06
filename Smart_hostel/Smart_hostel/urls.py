"""
URL configuration for Smart_hostel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from hostel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('roomsinfo/',views.Roomsinfo,name="Roomsinfo"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('booking',views.booking,name="booking"),
    path('admin',views.admin,name="admin"),
    path('admin_register', views.admin_register, name="admin_register"),
    path('students',views.admin_panel_students,name="admin_panel_students"),
    path('staff',views.admin_panel_staff,name="admin_panel_staff"),
    path('delete_student/<int:id>/',views.delete_student,name="delete_student"),
    path('admin_panel',views.admin_panel,name="admin_panel")
]
