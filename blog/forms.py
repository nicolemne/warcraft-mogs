from .models import Comment, Post, Category, Contact
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


category_choices = Category.objects.all().values_list('name', 'name')
category_list = []

for item in category_choices:
    category_list.append(item)


class UploadForm(forms.ModelForm):
    '''
    Creates the form when uploading a post
    '''
    class Meta:
        model = Post
        fields = ('title', 'content', 'description',
                  'category', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            'content': SummernoteWidget(),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    '''
    Edits the post
    '''
    class Meta:
        model = Post
        fields = ('title', 'content', 'description',
                  'category', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            'content': SummernoteWidget(),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    '''
    Creates the form when commenting on a post
    '''
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Write something...'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'name', 'email',
                  'message', 'featured_image',)

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }