# utilise generic views from rest_framework generics
# reference the blog database models==table
# srialize API data 

# import local data
from blog.models import Post
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass


