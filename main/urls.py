from django.urls import path
from .views import home, detail, posts, registerPage, loginPage, logoutUser, homeTwo , search, detailTwo 

urlpatterns = [
    path("register/", registerPage, name="register"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),

    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),

    #cooking
    path("homeTwo/", homeTwo, name="homeTwo"),
    path("search/", search, name="search"),
    path("<slug>/", detailTwo, name="detailTwo"),
]