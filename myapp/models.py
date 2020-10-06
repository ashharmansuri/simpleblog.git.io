from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    description = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title

    def total_likes(self):
         return self.likes.count()    

STATUS_CHOICES =[
  ('Single','Single'),
  ('Married','Married'),
  ('Complicated','Complicated'),
  ('Open-Relationship','Open-Relationship')
]

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='download.png',upload_to='profileimg')
    follower =models.IntegerField(default =0)
    following = models.IntegerField(default =0)
    about = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS_CHOICES)
    qualification = models.CharField(max_length=90,blank=True)
    profession = models.CharField(max_length=90,blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'




class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.ForeignKey('BlogComment',on_delete=models.CASCADE, related_name='replies',null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
       return '{}-{}'.format(self.post.title, str(self.user.username))


class Following(models.Model):
    ''' following of the user '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followed = models.ManyToManyField(User,related_name='followed')
    follower = models.ManyToManyField(User, related_name='follower')

    @classmethod
    def follow(cls,user,another_account):
        obj,create = cls.objects.get_or_create(user=user)
        obj.followed.add(another_account)
        print("followed")

    @classmethod
    def unfollow(cls,user,another_account):
        obj,create = cls.objects.get_or_create(user=user)
        obj.followed.remove(another_account)
        print("unfollowed")  

        def __str__(self):
            return str(self.user)
