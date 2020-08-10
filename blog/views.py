from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from datetime import datetime


class MainView(View):

    def get(self, request, *args, **kwargs):
        posts_list = Post.objects.order_by('-created_on')
        context_dict = {"posts": posts_list}
        return render(request, 'blog/index.html', context=context_dict)

    def post(self, request):
        context_dict = {"posts": []}
        post_list = list(Post.objects.all())
        for item in post_list:
            if str(request.POST['q']) in item.title:
                context_dict["posts"].append(item)
        return render(request, 'blog/index.html', context=context_dict)


class CreateNoteView(View):
    def post(self, request):
        if request.POST.get('title'):
            title_var = request.POST.get('title')
        if request.POST.get('content'):
            content_var = request.POST.get('content')
        time_var = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if request.POST.get('!!!') == "1":
            obj = Post(title=title_var, content=content_var, created_on=time_var)
            obj.save(force_insert=True)
            return HttpResponseRedirect('/')
        return render(request, 'blog/creating.html')
