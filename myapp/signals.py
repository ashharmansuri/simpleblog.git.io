from django.db.models.signals import post_save,m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwrags):
    if created:
        Profile.objects.create(user=instance)
        Following.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwrags):
    instance.profile.save()

@receiver(m2m_changed,sender=Following.follower.through)
def add_follower(sender,instance,action,reverse,pk_set, **kwrags):
    """
    sender= model which will send signal(Following)
    instance = username of user who is logged in(request.user)
    action = pre_add(is user followed someone, else pre_remove is user unfollowed someone)
    reverse = to be honest, i dont know
    pk_set = set of primary key of users whom i have followed
    """
    followed_users = [] #list of users (logged) user have followed
    logged_user = User.objects.get(id=instance)
    for i in pk_set:
        user = User.objects.get(pk=i)
        following_obj = Following.objects.get(user=user)
        followed_users.append(following_obj)

    if action == "pre_add":
        for i in followed_users:
            i.follower.add(logged_user)
            i.save()
   
    if action == "pre_remove":
        for i in followed_users:
            i.follower.remove(logged_user)
            i.save()