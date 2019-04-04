from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import ProfileForm,ProjectForm
from .models import Project,Profile,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

     

@login_required(login_url='/accounts/login/')
def home(request):
   
    profile = Profile.objects.all()
    project = Project.objects.all()
    post= Post.objects.all() 
    
    return render(request,'welcome.html', {"profile":profile,"project":project,"post": post})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

    else:    
        form = ProfileForm()
        
    return render(request,'profile.html', {"form": form})   

def profil(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user).all()
    form=ProfileForm()
    return render(request,"all-images/profil.html",{"profile":profile,"user":user,"projects":project,"form":form})

# # @login_required(login_url='/accounts/login/')
# # def detail(request,project_id):
# #     project = Project.objects.get(id = project_id)
# #     comments = Comments.objects.filter(project = project.id).all() 
# #     return render(request,'detail.html',{"project":project,"comments":comments})



def project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()

        return redirect(home)
    else:
        form = ProjectForm()
    return render(request, 'proj.html', {"form": form})
    
@login_required(login_url='/accounts/login/')
def projects(request,project_id):
    project = Project.objects.get(id = project_id)
    
    return render(request,"proj.html", {"project":project})


@login_required(login_url='/accounts/login/')
def view_post(post_id):
    post = ProjectPost.objects.get(id=post_id)
    if request.args.get("vote"):
       post.likes = post.likes + 1
       post.save()
       return redirect(home)
    else:
        form = ProjectForm()
    return render(request,"post.html",{"form": form})
