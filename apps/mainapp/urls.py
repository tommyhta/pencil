from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^registration$', views.registration, name="reg"),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

    url(r'^breached$', views.breached),

    url(r'^admins$', views.admin),
    url(r'^changetype$',views.changetype),
    url(r'^deleteuser$', views.deleteuser),
    url(r'^adminsearch$', views.adminsearch),
    url(r'^pwreset$', views.resetpassword),

    
    url(r'^store$', views.store),
    url(r'^store/cart$', views.cart),
    url(r'^store/searchstandard$', views.searchstandard),
    url(r'^store/searchxl$', views.searchxl),
    url(r'^store/searchall$', views.searchall),
    url(r'^store/searchgoldmixed$', views.searchgoldmixed),
    url(r'^store/searchaccessories$', views.searchaccessories),
    url(r'^store/addToCart$', views.addToCart),
    


    url(r'^user/(?P<id>\d+)$', views.user, name="user"),
    url(r'^user/(?P<id>\d+)/edit$', views.edituser),
    url(r'^user/(?P<id>\d+)/changepw', views.changePW),


    url(r'^staff$', views.staff),
    url(r'^staff/addproduct$', views.addproduct),
    url(r'^staff/deleteproduct$', views.deleteproduct),
    url(r'^staff/editproduct$', views.editproduct),
    url(r'^staff/addCat', views.addCategory),
    url(r'^staff/deleteCategory$', views.deleteCategory),
    url(r'^staff/removeCat$', views.removeCat),
    url(r'^staff/addcategory$', views.addCatToProduct),

]
