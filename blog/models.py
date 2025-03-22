from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class blogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it doesn't exist
            original_slug = slugify(self.title)
            queryset = blogCategory.objects.exclude(pk=self.pk)
            slug = original_slug
            counter = 1

            while queryset.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            self.slug = slug

        # Call the parent class's save method
        super().save(*args, **kwargs)

class Blogs(models.Model):
    thumbnail = models.ImageField(upload_to='blog_images', blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(blogCategory, null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it doesn't exist
            original_slug = slugify(self.title)
            queryset = Blogs.objects.exclude(pk=self.pk)
            slug = original_slug
            counter = 1

            while queryset.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            self.slug = slug

        # Call the parent class's save method
        super().save(*args, **kwargs)

    def getTHumb(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return 'https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg'

class blogPageSEO(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.meta_title