from django.contrib import admin
from django.urls import path
from Admin_Panel import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name="Home"),    
    # path('login/',views.login,name="Login"),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name="Login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='logout.html'),name="Logout"),
    path('register/',views.register,name="Register"),    
    path("profile/",views.profile,name="Profile"),
]


































# from Message import views
# urlpatterns = [
#     path('admin/',admin.site.urls),                  
#     path('',views.message,name="Message"),                  
#     path('success/',views.success,name="Success"),                  
#     path('info/',views.info,name="Info"),                  
#     path('error/',views.error,name="Danger"),                  
#     path('warning/',views.warning,name="Warning"),                  

#SQlite Registration
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',views.home,name="home"),# 127.0.0.1:8000/         
#     path('addData',views.addData,name="addData"),
#     path('updateData/<int:id>',views.updateData,name="updateData"),
#     path('deleteData/<int:id>',views.deleteData,name="deleteData"),
# ]


