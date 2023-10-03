from rest_framework import generics
from django.core.exceptions import PermissionDenied

from .models import Post
from .permissions import IsAuthorOrReadOnly 
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            # If the user is not authenticated, prevent the creation of new entries
            raise PermissionDenied("You must be authenticated to create new entries.")
        serializer.save(author=self.request.user)
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer