# """
# URL configuration for IndustryProject project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from IndustryApp.views import HomeView, SignupView,MethodListView, MethodCreateView, AssignMachinesView,ManListView, ManCreateView,ManUpdateView,ManDeleteView,MachineListView,MachineCreateView,MachineUpdateView,MachineDeleteView,MaterialCreateView,MaterialListView,MaterialDeleteView,MaterialUpdateView,MethodUpdateView,MethodDeleteView,ShiftListView,ShiftCreateView,ShiftUpdateView,ShiftDeleteView,MachineUsageListView,MachineUsageCreateView,MachineUsageUpdateView,MachineUsageDeleteView,MethodSearchView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as authview
from IndustryApp import views

router = DefaultRouter()
router.register('shift',views.ShiftViewSet,basename="shift"),
router.register('men',views.ManViewSet,basename="men"),
router.register('machines',views.MachineViewSet,basename="machines"),
router.register('materials',views.MaterialViewSet,basename="materials"),
router.register('methods',views.MethodViewSet,basename="methods"),
router.register('machineusage',views.MachineUsageViewSet,basename="machineusage")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('token/', authview.obtain_auth_token),
    path('',HomeView.as_view(),name='home_view'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('methods/', MethodListView.as_view(), name='method_list'),
    path('methods/add/', MethodCreateView.as_view(), name='add_method'),
    path('man/<int:id>/assign-machines/', AssignMachinesView.as_view(), name='assign_machines'),

    path('men/', ManListView.as_view(), name='man_list'),
    path('men/add/', ManCreateView.as_view(), name='man_add'),
    path('men/<int:pk>/edit/', ManUpdateView.as_view(), name='man_edit'),
    path('men/<int:pk>/delete/', ManDeleteView.as_view(), name='man_delete'),

    path('machines/', MachineListView.as_view(), name='machine_list'),
    path('machines/add/', MachineCreateView.as_view(), name='machine_add'),
    path('machines/<int:pk>/edit/', MachineUpdateView.as_view(), name='machine_edit'),
    path('machines/<int:pk>/delete/', MachineDeleteView.as_view(), name='machine_delete'),

    path('materials/', MaterialListView.as_view(), name='material_list'),
    path('materials/add/', MaterialCreateView.as_view(), name='material_add'),
    path('materials/<int:pk>/edit/', MaterialUpdateView.as_view(), name='material_edit'),
    path('materials/<int:pk>/delete/', MaterialDeleteView.as_view(), name='material_delete'),

    path('methods/<int:pk>/edit/', MethodUpdateView.as_view(), name='method_edit'),
    path('methods/<int:pk>/delete/', MethodDeleteView.as_view(), name='method_delete'),

    path('shifts/', ShiftListView.as_view(), name='shift_list'),
    path('shifts/add/', ShiftCreateView.as_view(), name='shift_add'),
    path('shifts/<int:pk>/edit/', ShiftUpdateView.as_view(), name='shift_edit'),
    path('shifts/<int:pk>/delete/', ShiftDeleteView.as_view(), name='shift_delete'),

    path('machineusages/', MachineUsageListView.as_view(), name='machineusage_list'),
    path('machineusages/add/', MachineUsageCreateView.as_view(), name='machineusage_add'),
    path('machineusages/<int:pk>/edit/', MachineUsageUpdateView.as_view(), name='machineusage_edit'),
    path('machineusages/<int:pk>/delete/', MachineUsageDeleteView.as_view(), name='machineusage_delete'),

    path('methods/search/', MethodSearchView.as_view(), name='method_search'),

]+router.urls



