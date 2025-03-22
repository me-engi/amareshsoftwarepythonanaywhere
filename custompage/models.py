from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class customPage(models.Model):  # Use PascalCase for class names (recommended)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Ensure uniqueness
    content = RichTextField()

    def save(self, *args, **kwargs):
        # Generate a unique slug based on the 'title' field
        if not self.slug:  # Only generate a slug if it doesn't already exist
            original_slug = slugify(self.title) if self.title else "untitled"
            queryset = customPage.objects.exclude(pk=self.pk)
            slug = original_slug
            counter = 1
            while queryset.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or "Untitled Page"

    class Meta:
        verbose_name_plural = "Custom Pages"  # Plural name for admin interface