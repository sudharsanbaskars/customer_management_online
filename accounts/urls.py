from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name = "products"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('user/', views.userPage, name = "user-page"),
    path('account/', views.accountSettings, name = "account"),

    path('create_order/<int:pk>', views.createOrder, name="create_order"),
    path('update_order/<int:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>', views.deleteOrder, name="delete_order"),

    path('create_product/', views.createProduct, name="create_product"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"),
     name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),
     name="password_change_done"),


    # path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
