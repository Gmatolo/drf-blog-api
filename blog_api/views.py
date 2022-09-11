# utilise generic views from rest_framework generics
# reference the blog database models==table
# srialize API data 

from rest_framework import generics

# import local data
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass


