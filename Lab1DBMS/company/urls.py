from django.urls import path
from . import views

urlpatterns = [
    path("front/",views.allinterns,name='front'),
    path('location/<str:location>/', views.location_page_view, name='location_page'),
    # path('locations/', views.location_buttons_view, name='location_buttons'),
    # path('location/<str:location>/', views.location_page_view, name='location_page')
    path('', views.intern_list_view, name='intern_list'),
    path("search/",views.search_intern,name="searchintern")
]
