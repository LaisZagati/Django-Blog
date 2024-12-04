# Import Django's models module to define database tables using Python classes
from django.db import models

# Import Django's built-in User model to handle user authentication and relationships
from django.contrib.auth.models import User

# Import CloudinaryField to integrate with Cloudinary for managing media uploads
from cloudinary.models import CloudinaryField



# - The first element is the internal value (stored in the database).
# - The second element is the human-readable label (displayed in forms or the admin interface).
STATUS = (
    (0, "Draft"),      # '0' represents the "Draft" status (internal value), displayed as "Draft"
    (1, "Published")   # '1' represents the "Published" status (internal value), displayed as "Published"
)

class Post(models.Model): 
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()  
    feature_image = CloudinaryField('image', default = 'placeholder')
    excerpt_on = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField (User, related_name = 'blog_likes', blank=True)
    
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    
    
    
