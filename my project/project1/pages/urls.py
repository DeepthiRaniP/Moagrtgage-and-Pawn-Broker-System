from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('empregistration',views.empregistration,name="empregistration"),
    path('emplogin',views.emplogin,name="emplogin"),
    path('pawnregistration',views.pawnregistration,name="pawnregistration"),
    path('pawnlogin',views.pawnlogin,name="pawnlogin"),
    path('checkpawnlogin',views.checkpawnlogin,name="checkpawnlogin"),
    path('checkemplogin',views.checkemplogin,name="checkemplogin"),
    path('emphome',views.emphome,name="emphome"),
    path('empprofile',views.empprofile,name="empprofile"),
    path('pawnprofile',views.pawnprofile,name="pawnprofile"),
    path('empchangepwd',views.empchangepwd,name="empchangepwd"),
    path('empupdatepwd', views.empupdatepwd, name="empupdatepwd"),
    path("vieweproducts",views.vieweproducts,name="vieweproducts"),
    path("displayeproducts",views.displayeproducts,name="displayeproducts"),
    path('emplogout',views.emplogout,name='emplogout'),
    path("displayitems", views.displayitems, name="displayitems"),

    path('admin/login',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path("adddept",views.adddepartment,name="adddept"),
    path("updatedept",views.updatedepartment,name="updatedept"),

    path("addproduct", views.addproduct, name="addproduct"),
    path("additem", views.additem, name="additem"),
    path("viewaproducts",views.viewaproducts,name="viewaproducts"),
    path('viewemps',views.viewemployees,name="viewemps"),
    path('viewpawn',views.viewpawnshops,name="viewpawn"),
    path("deleteemp/<int:eid>",views.deleteemp,name="deleteemp"),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('feedback', views.feedback, name='feedback'),
    path('profile', views.profile, name='profile'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

