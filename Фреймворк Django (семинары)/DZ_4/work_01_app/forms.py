from django.forms import Form, CharField, Textarea, FloatField, FileField, ModelForm

from work_01_app.models import Product



# class SampleModel(models.Model): 
#     title = models.CharField(max_length=100) 
#     description = models.CharField(max_length=255) 
#     def __str__(self): return self.title


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "prod_name",
            "description",
            "price",
            "prod_count",
            "photo",
        ]

