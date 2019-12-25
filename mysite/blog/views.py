from django.shortcuts import render,get_object_or_404
#创建视图以显示帖子列表
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
# Create your views here.

#把post_list视图修改为基于类的视图，并使用Django提供的通用ListView(这一基视图可显示任意类型的对象)
'''class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'Posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'''

'''基于函数的视图'''
def post_list(request):
    posts=Post.published.all()
    return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day
                           )
    return render(request,'blog/post/detail.html',{'post':post})

#导入Django的分页器类调整post_list视图
def post_list(request):
    object_list=Post.published.all()
    #3 posts in each page
    paginator=Paginator(object_list,3)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        posts=paginator.page(1)
    except EmptyPage:
        #If page is out of range deliver last page of results
        posts=paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',
                  {'page':page,
                   'posts':posts})
