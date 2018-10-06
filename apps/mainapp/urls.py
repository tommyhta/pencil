from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^registration$', views.registration, name="reg"),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^welcome$', views.welcome),
    url(r'^logout$', views.logout),
    url(r'^breached$', views.breached),
    url(r'^admins$', views.admin),
    url(r'^changetype$',views.changetype),
    url(r'^deleteuser$', views.deleteuser),
    url(r'^adminsearch$', views.adminsearch),

    url(r'^user/(?P<id>\d+)$', views.user, name="user"),


    url(r'^staff$', views.staff),
    url(r'^addproduct$', views.addproduct),
    url(r'^deleteproduct$', views.deleteproduct),
    url(r'^editproduct$', views.editproduct),

]
