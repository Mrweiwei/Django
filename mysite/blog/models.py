from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#博客定义数据模型（模型表示一个Python类，并定义为django.db.models.Model的子类。其中每个属性视为一个数据库
# 的字段。Django针对定义于models.py文件中的每个模型创建一个表。当创建一个模型时，Django提供一个实用的API
# 从而可方便地查询数据库中的对象。首先定义一个Post模型）
class Post(models.Model):
    '''博客的帖子的数据模型'''
    STATUS_CHOICES=(
        ('draft','Dtaft'),
        ('published','Published'),
    )
    #title表示为帖子标题字段。该字段定义为CharField,在SQL数据库中将转换为VARCHAR列
    title=models.CharField(max_length=250)
    #slug字段用于URL中，作为一个简短的标记，slug仅包含字母、数值、下画线以及连字符。根据slug字段，可针对
    #博客帖子构建具有较好外观的、SEO友好的URL。之间曾向该字段中添加unique_for_date参数，进而可采用发布日
    #期和slug对帖子构建URL。Django不支持多个帖子在既定日期拥有相同的slug
    slug=models.SlugField(max_length=250,
                          unique_for_date='publish')
    #author字段表示一个外键，定义了多对一的关系。具体来说，我们将通知Django,每个帖子由某位用户编写，但一个
    #用户可以编写多个帖子。对于该字段，Django通过相关模型的主键在数据库中生成了一个外键。
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='blog_posts')
    #body为帖子的主体，且设置为文本字段
    body=models.TextField()
    #帖子的发布日期
    publish=models.DateTimeField(default=timezone.now)
    #帖子的创建时间
    created=models.DateTimeField(auto_now_add=True)
    #帖子的最后一次更新时间
    updated=models.DateTimeField(auto_now=True)
    #帖子的状态
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

class Meta:
    ordering=('-publish',)

def __str__(self):
    return self.title