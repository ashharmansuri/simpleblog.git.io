
from django.urls import path
from .import views
from .views import PostListView
urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('register',views.user_register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout, name='logout'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('password-change',views.password_change,name='password-change'),

    path('dashboard',views.dashboard,name='dashboard'),
    path('add-post',views.add_post,name='add-post'),
    path('view-post/<int:pk>',views.view_post,name='view-post'),
    path('edit-post/<int:pk>',views.edit_post,name='edit-post'),
    path('delete-post/<int:pk>',views.delete_post,name='delete-post'),
    path('search',views.search_post,name='search'),
    path('post-like/<int:pk>',views.post_like,name='like-post'),

    # path('post-comment',views.post_comment,name='post-comment'),

    path('account-settings',views.account_settings,name='account-settings'),
    # path('user/follow/<int:pk>',views.follow,name='user-follow')
]
