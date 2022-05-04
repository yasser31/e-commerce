from django.db import models


class CategoryMixin(models.Model):
    category = models.CharField(max_length=255, default="")
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.DO_NOTHING, related_name="children")
    slug = models.SlugField(max_length=255, default="")

    class Meta:
        abstract = True
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class ProductMixin(models.Model):

    name = models.CharField(max_length=255, default='name')
    sulg = models.SlugField()
    details = models.TextField(blank=True, null=True, default="text")
    

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

"""
class ColorMixin(models.Model):
    color = models.CharField(max_length=265, blank=True, null=True)

    class Meta:
        abstract = True"""