from django.urls import path

from .views import PostDetail, PostList

app_name = 'blog_api'

urlpatterns = [
    # single api endpoint
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), 
    # list all endpoints in db
    path('', PostList.as_view(), name='listcreate')
]
