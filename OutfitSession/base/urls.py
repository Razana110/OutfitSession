from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path("", views.home_page ,name = "home_page"),
    path("register", views.register_page, name="register_page"),
    path('login/',views.login_page, name="login_page"),
    path('logout/', views.logout_page, name='logout_page'),
    path('designers/', views.designers_page, name='designers_page'),
    path('designer/<str:pk>', views.designer_page, name='designer_page'),
    path('hire/<str:pk>', views.hire_page, name='hire_page'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('session/', views.session_page, name='session_page'),
    path('status/<str:pk>', views.status_page, name='status_page'),
    path('connect/', views.connect_page, name='connect_page'),
]
