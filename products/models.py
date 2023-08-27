from django.db import models
from django.utils.translation import gettext_lazy as _
# hello hello world




class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categories/')
    is_enable = models.BooleanField(_('is_enable'))
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now=True)


    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')




class Product(models.Model):
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products/')
    categories = models.ManyToManyField('Category',verbose_name=_('categories'),blank=True)
    is_enable = models.BooleanField(_('is_enable'))
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey("Product", verbose_name=_("product"), on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    file = models.FileField(_("file"), upload_to='files/%y/%m/%d')
    is_enable = models.BooleanField(_('is_enable'))
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now=True)
    class Meta:
        db_table = 'files'
        verbose_name = _('Files')
        verbose_name_plural = _('files')
    