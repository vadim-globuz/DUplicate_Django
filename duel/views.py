from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post, User


def index(request):
    template = loader.get_template('pages/index.html')
    context = {
        'pass': 'Hello',
    }
    return HttpResponse(template.render(context, request))


@login_required()
def profile(request):
    template = loader.get_template('pages/dashboard.html')
    models = Post.objects.all().filter(key=request.user.id)
    counter = models.count()
    context = {
        'works': models,
        'count': counter,
    }
    return HttpResponse(template.render(context, request))


@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.key = request.user

            post.save()
            return redirect('main:profile')
    else:
        form = PostForm()
    return render(request, 'pages/post.html', {'form': form})


@login_required()
def album_view(request):
    template = loader.get_template('pages/album.html')
    model = Post.objects.filter(key=request.user.id)
    context = {
        'images': model
    }
    if request.method == "POST":
        id_deleted_work = request.POST['id_picture']
        del_obj = Post.objects.get(pk=id_deleted_work)
        del_obj.delete()

    return HttpResponse(template.render(context, request))


@login_required()
def duel_get_works(request):
    model = Post.objects.exclude(key_id=request.user.id)
    user = User.objects.get(pk=request.user.id)
    ex_query = user.middleTab.all()
    query_for_template = model.difference(ex_query)
    print(ex_query)
    print(query_for_template)
    context = {
        'deuce': query_for_template[:2],

    }
    if request.method == "POST":

        checked_value = request.POST['customRadioInline1']
        fist_work_id = request.POST['work_id_1']
        second_work_id = request.POST['work_id_2']
        if checked_value == fist_work_id:
            looser_id = second_work_id
        else:
            looser_id = fist_work_id

        post = Post.objects.get(id=checked_value)
        looser = Post.objects.get(id=looser_id)
        post.rate += 1
        looser.loses += 1
        post.voted_users.add(user)
        looser.voted_users.add(user)
        post.save()
        looser.save()

    return render(request, 'pages/duel_main.html', context)
