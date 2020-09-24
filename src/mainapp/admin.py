from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *
from PIL import Image


class NotebookAdminForm(ModelForm):

    MIN_VALID_RESOLUTION = (400, 400)
    MAX_VALID_RESOLUTION = (800, 800)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображения с разрешением не меньше {}x{}, и не больше {}x{}'.format(
            *self.MIN_VALID_RESOLUTION,
            *self.MAX_VALID_RESOLUTION,
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        if img.width < self.MIN_VALID_RESOLUTION[0] or img.height < self.MIN_VALID_RESOLUTION[1]:
            raise ValueError('Разрашение изображения меньше минимального')
        if img.width > self.MAX_VALID_RESOLUTION[0] or img.height > self.MAX_VALID_RESOLUTION[1]:
            raise ValueError('Разрашение изображения больше максимального')

        return image


class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone)
