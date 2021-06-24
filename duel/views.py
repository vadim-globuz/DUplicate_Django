from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import PostForm, AddOrg, CreateProfile
from .models import Post, User, Organisation, Profile


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


@login_required()
def leaderboards(request):
    order_works = Post.objects.all().order_by('-rate')[:10]
    context = {
        'order_works': order_works,
    }
    return render(request, 'pages/leaderboard.html', context)


@login_required()
def organisation_new(request):
    org_obj = Organisation.objects.filter(admin_id=request.user.id)
    check_member = Profile.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        form = AddOrg(request.POST)
        if form.is_valid():
            org = form.save(commit=False)
            org.admin_id = request.user.id
            org.save()

            prof = Profile.objects.create(user_id=request.user.id, org_id=org_obj.id)
            prof.save()

            return redirect('main:profile')
    else:
        form = AddOrg()
    return render(request, 'pages/create_organisations.html', {'form': form, 'state': check_member})


@login_required()
def enter_org(request):
    check_member = Profile.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        form = CreateProfile(request.POST)
        if form.is_valid():
            profile_add = form.save(commit=False)
            profile_add.user_id = request.user.id
            profile_add.save()
            return redirect('main:profile')
    else:
        form = CreateProfile()
    return render(request, 'pages/redact_profile.html', {'form': form, 'state': check_member})


@login_required()
def org_menu(request):
    template = loader.get_template('pages/organisation_menu.html')
    context = {
        'pass': 'null',
    }
    return HttpResponse(template.render(context, request))


@login_required()
def duel_get_works_organisation(request):
    objects_to_filter = Profile.objects.all()
    names_to_filter = [o.user_id for o in objects_to_filter]

    model = Post.objects.filter(key_id__in=names_to_filter).exclude(key_id=request.user.id)
    print(model)
    user = User.objects.get(pk=request.user.id)
    ex_query = user.middleTab.all()
    query_for_template = model.difference(ex_query)
    organisation_id = Profile.objects.get(user_id=request.user.id)
    organisation_flag = Organisation.objects.get(id=organisation_id.org_id)

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
        post.organisation_rate += 1
        looser.organisation_loses += 1
        post.voted_users.add(user)
        if not organisation_flag.vote_type:
            looser.voted_users.add(user)

        post.save()
        looser.save()

    return render(request, 'pages/duel_main.html', context)
