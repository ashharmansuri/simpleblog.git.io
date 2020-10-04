from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,BlogComment
from .forms import PostForm,ProfileForm,UserUpdateForm,FormPasswordChange
from django.views.generic import ListView
from django.urls import reverse


# Create your views here.
# def home(request):
#     post = Post.objects.all().order_by('-posted_date')
#     params={'posts':post}
#     return render(request, 'home.html',params)

class PostListView(ListView):
    model = Post
    template_name='home.html'
    context_object_name ='posts'   
    ordering = ['-posted_date']
    paginate_by = 3


# each post particular retrieve view
def view_post(request,pk):
    post = Post.objects.get(id=pk)
    comments = BlogComment.objects.filter(post=post,reply=None).order_by('-id')
    
    is_liked =False
    if post.likes.filter(id=request.user.id).exists():
        is_liked=True

    if request.method=="POST":
        comment = request.POST.get('comment')
        reply_id = request.POST.get('com_id')
        comment_qs = None
        if reply_id:
            comment_qs = BlogComment.objects.get(id=reply_id)
        comments = BlogComment.objects.create(post=post,user=request.user,comment=comment,reply=comment_qs)
        comments.save()
        return HttpResponseRedirect(reverse('view-post',args=[str(pk)]))

    context ={'posts':post,'comments':comments,'is_liked':is_liked,'total_likes':post.total_likes()}
    return render(request,'view-post.html',context)



# User Dashboard view
@login_required(login_url ='login')
def dashboard(request):
    current_user = request.user
    all_post = Post.objects.filter(author=current_user).order_by('-posted_date')
    context ={'allposts':all_post}
    return render(request,'dashboard.html',context)

#Password Change view
@login_required(login_url ='login')
def password_change(request):
    fm = FormPasswordChange(request.user)
    if request.method == "POST":
        fm = FormPasswordChange(request.user,request.POST)
        if fm.is_valid():
            cp = fm.save()
            update_session_auth_hash(request,cp)
            return redirect('account-settings')

    context = {'form':fm}
    return render(request,'password-change.html',context)

# Add Post view
@login_required(login_url ='login')
def add_post(request):
    fm = PostForm()
    if request.method == "POST":
        fm = PostForm(request.POST)
        if fm.is_valid():
            own_post = fm.save(commit=False)
            own_post.author = request.user # add the logged in user, as the# author
            own_post.save()
            return redirect('dashboard')

    params={'form':fm}
    return render(request,'add-post.html',params)

# Edit Post
@login_required(login_url ='login')
def edit_post(request,pk):
    post = Post.objects.get(id=pk)
    if post.author != request.user:
       return redirect('dashboard')
    else:   
        fm = PostForm(instance=post)
        if request.method == "POST":
            fm = PostForm(request.POST, instance=post)
            if fm.is_valid():
                fm.save()
                return redirect('dashboard')
        context ={'form':fm}
        return render(request,'add-post.html',context)

# delete post view
@login_required(login_url ='login')
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('dashboard')



# search post view
@login_required(login_url ='login')
def search_post(request):
    search_query = request.GET.get('search_query')
    if len(search_query) > 75:
        allposts = []
    else:    
        allpoststitle = Post.objects.filter(title__icontains=search_query)
        allpostscontent = Post.objects.filter(description__icontains=search_query)
        allposts = allpoststitle.union(allpostscontent)

    context={'posts':allposts,'search_query':search_query}
    return render(request,'search-post.html',context)



#  post likes view
@login_required(login_url ='login')
def post_like(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('posts_id'))
    is_liked =False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:    
        post.likes.add(request.user)
        is_liked=False
    return HttpResponseRedirect(reverse('view-post',args=[str(pk)]))



#account settings view
@login_required(login_url ='login')
def account_settings(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileForm(instance=request.user.profile)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('account-settings')


    context ={'pform':p_form,'uform':u_form}
    return render(request,'account-settings.html',context)


#post-comment views
# def post_comment(request):
#     if request.method=="POST":
#         comment = request.POST.get('comment')
#         user = request.user
#         post_id = request.POST.get('postId')
#         post = Post.objects.get(pk=pk)

#         comment = BlogComment(comment=comment,user=user,post=post)
#         comment.save()

#         return redirect('view-post/{post.id}')

#     post = Post.objects.filter(pk=pk)
#     comments = BlogComment.objects.filter(post=post)
#     context ={'post':post,'comments':comments}
#     return render(request,'view-post.html',context)



# User registeration view
def user_register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:    
        fm= UserRegisterForm()
        if request.method =="POST":
           fm = UserRegisterForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            fm.save()
            return redirect('login')
        params ={'fm':fm}
        return render(request, 'register.html', params)    


# User login View
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:    
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        return render(request,'login.html')


def profile(request,pk):
    user_profile = User.objects.get(id=pk)
    context = {'user_profile':user_profile}
    return render(request,'profile_page.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')    