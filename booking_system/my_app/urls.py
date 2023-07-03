from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,register,book,signin,house,checkout,adminpage,addpage,deletepage,update,Logout

urlpatterns=[
    path('',home,name='home'),
    path('signin/',signin,name='signin'),
    path('register/',register,name='register'),
    path('house/',house,name='house'),
    path('adminpage/',adminpage,name='adminpage'),
    path('add/',addpage,name='addpage'),
    path('update/<str:pk>',update,name='update'),
    path('delete/<str:pk>',deletepage,name='deletepage'),
    path('book/<str:pk>/',book,name='book'),
    path('checkout/',checkout,name='checkout'),
    path('Logout/',Logout,name='Logout'),

     path('passwordreset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
     path('passwordresetdone/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
     path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
     path('passwordresetcomplete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


]