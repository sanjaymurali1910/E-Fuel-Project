"""efuel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from efuelapp import views

from django.urls import path
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Registration/$',views.Registration,name='Registration'),
    re_path(r'^Forgot_password$',views.Forgot_password, name='Forgot_password'),

    re_path(r'^Owner_index/$', views.Owner_index, name='Owner_index'),
    re_path(r'^Owner_home/$',views.Owner_home,name='Owner_home'),
    re_path(r'^Owner_addbunk/$',views.Owner_addbunk,name='Owner_addbunk'),
    re_path(r'^Owner_view_booking/$',views.Owner_view_booking,name='Owner_view_booking'),
    re_path(r'^Owner_change_time(?P<i_id>[0-9]+)/$',views.Owner_change_time,name='Owner_change_time'),
    re_path(r'^change_time(?P<booking_id>[0-9]+)/$',views.change_time,name='change_time'),
    re_path(r'^Owner_add_payment(?P<i_id>[0-9]+)/$',views.Owner_add_payment,name='Owner_add_payment'),
    re_path(r'^add_payment(?P<pay_user_ide>[0-9]+)/$',views.add_payment,name='add_payment'),
    re_path(r'^Owner_contact/$',views.Owner_contact,name='Owner_contact'),
    re_path(r'^Owner_contact_view/$',views.Owner_contact_view,name='Owner_contact_view'),
    re_path(r'^Owner_addcategory$',views.Owner_addcategory,name='Owner_addcategory'),
    re_path(r'^Owner_addproduct/$',views.Owner_addproduct,name='Owner_addproduct'),
    re_path(r'^Owner_addpro/$',views.Owner_addpro,name='Owner_addpro'),
    re_path(r'^Owner_view_product/$',views.Owner_view_product,name='Owner_view_product'),
    re_path(r'^Owner_product_edit(?P<p_id>[0-9]+)/$',views.Owner_product_edit,name='Owner_product_edit'),
    re_path(r'^edit_product_details(?P<products_id>[0-9]+)$',views.edit_product_details,name='edit_product_details'),
    re_path(r'^delete_product(?P<p_id>[0-9]+)$',views.delete_product,name='delete_product'),
    re_path(r'^Owner_logout/$',views.Owner_logout,name='Owner_logout'),
    re_path(r'^Owner_profile/$',views.Owner_profile,name='Owner_profile'),
    re_path(r'^Owner_edit_profile/$',views.Owner_edit_profile,name='Owner_edit_profile'),


    re_path(r'^User_index/$',views.User_index,name='User_index'),
    re_path(r'^User_home/$',views.User_home,name='User_home'),
    re_path(r'^User_about/$',views.User_about,name='User_about'),
    re_path(r'^User_allbunk/$',views.User_allbunk,name='User_allbunk'),
    re_path(r'^User_contact/$',views.User_contact,name='User_contact'),
    re_path(r'^User_addcart/$',views.User_addcart,name='User_addcart'),
    re_path(r'^User_booking(?P<i_id>[0-9]+)/$',views.User_booking,name='User_booking'),
    re_path(r'^book_bunk(?P<book_owner_ide>[0-9]+)/$',views.book_bunk,name='book_bunk'),
    re_path(r'^User_mybooking/$',views.User_mybooking,name='User_mybooking'),
    re_path(r'^cancel_booking(?P<i_id>[0-9]+)$',views.cancel_booking,name='cancel_booking'),
    re_path(r'^cancel_order(?P<i_id>[0-9]+)$',views.cancel_order,name='cancel_order'),
    re_path(r'^User_payment_history/$',views.User_payment_history,name='User_payment_history'),
    re_path(r'^add_userorder/$',views.add_userorder,name='add_userorder'),
    re_path(r'^User_logout/$',views.User_logout,name='User_logout'),
    re_path(r'^logouttwo/$',views.logouttwo,name='logouttwo'),
    re_path(r'^User_myorders/$',views.User_myorders,name='User_myorders'),
    re_path(r'^User_profile/$',views.User_profile,name='User_profile'),
    re_path(r'^User_edit_profile/$',views.User_edit_profile,name='User_edit_profile'),
    

    

    re_path(r'^SuperAdmin_index/$',views.SuperAdmin_index,name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_home/$',views.SuperAdmin_home,name='SuperAdmin_home'),
    re_path(r'^SuperAdmin_bunkrequest/$',views.SuperAdmin_bunkrequest,name='SuperAdmin_bunkrequest'),
    re_path(r'^decline_bunk(?P<i_id>[0-9]+)$',views.decline_bunk,name='decline_bunk'),
    re_path(r'^SuperAdmin_bunkbookings/$',views.SuperAdmin_bunkbookings,name='SuperAdmin_bunkbookings'),
    re_path(r'^SuperAdmin_ownerview/$',views.SuperAdmin_ownerview,name='SuperAdmin_ownerview'),
    re_path(r'^SuperAdmin_change_desig/(?P<i_id>[0-9]+)/$',views.SuperAdmin_change_desig,name='SuperAdmin_change_desig'),
    re_path(r'^change_designation/(?P<usrs_id>[0-9]+)/$',views.change_designation,name='change_designation'),
    re_path(r'^SuperAdmin_view_contacts/$',views.SuperAdmin_view_contacts,name='SuperAdmin_view_contacts'),
    
    re_path(r'^delete_user(?P<i_id>[0-9]+)$',views.delete_user,name='delete_user'),
    re_path(r'^SuperAdmin_logout/$', views.SuperAdmin_logout, name='SuperAdmin_logout'),

    re_path(r'^store/$',views.store,name='store'),
    re_path(r'^cart/$',views.cart,name='cart'),
    re_path(r'^checkout/$',views.checkout,name='checkout'),
    re_path(r'^update_item/$',views.updateItem,name='update_item'),
    re_path(r'^process_order/$',views.processOrder,name='process_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
