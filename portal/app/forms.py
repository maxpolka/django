from django import forms
from .models import DesignRequest, Category

        
class DesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        exclude = ['user']
        fields = ['title', 'content', 'image', 'category', 'status', 'comment', 'image_after']
        labels = {
            "status": "Статус",
            "title": "Название",
            "content": "Содержание",
            "image": "Изображение",
            "category": "Категория",
            "comment": "Комментарий",
            "image_after": "Изображение после работы"
        }
        widgets = {
            "category": forms.Select(attrs={'class': "form-control"}),
            "comment": forms.Textarea(attrs={'class': "form-control"}),
            "status": forms.Select(attrs={'class': "form-control"}),
            # "image_after": forms.ImageField(attrs={'class': "form-control"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['status'].widget.attrs['class'] = 'form-control'
    #     self.fields['comment'].widget.attrs['class'] = 'form-control'
    #     self.fields['image_after'].widget.attrs['class'] = 'form-control'
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        labels = {
            "title": "Название категории"
        }
        