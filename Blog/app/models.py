from genericpath import exists
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingFormField

class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS=(
        ('0', 'Draft'),
        ('1', 'Published'),
    )
    SECTION=(
        ('Main_post','Main_post'),
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editors_Pick','Editors_Pick'),
        ('Trending','Trending'),
        ('Inspiration','Inspiration'),
        ('Latest_Post','Latest_Post'),
   
    )

    featured_image = models.ImageField(upload_to='images')
    title= models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    date =models. DateField(auto_now_add=True)
    content =models.TextField()
    slug=models.SlugField(max_length=500, null=True, blank=True, unique=True)
    status=models.CharField(choices= STATUS, max_length=100 )
    section=models.CharField(choices=SECTION, max_length=200)
    Main_post=models.BooleanField(default=False)


    def __str__(self):
        return self.title
    

def create_slug(instance, new_slug=None):
        slug=slugify(instance.title)
        if new_slug is not None:
            slug = new_slug
        QS = Post.objects.filter(slug=slug).order_by('-id')
        exists = QS.exists()
        if exists:
            new_slug="%S-%S"% (slug, QS.filter().id)
            return create_slug(instance, new_slug= new_slug)
        return new_slug


def pre_save_post_reciver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = create_slug(instance)

        pre_save.connect(pre_save_post_reciver, Post)


class Tag(models.Model):
    name=models. CharField(max_length=100)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    