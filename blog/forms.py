from .models import Comment, Post, Contact
from django import forms


# category_choices = Category.objects.all().values_list('name', 'name')
# category_list = []

# for item in category_choices:
#     category_list.append(item)


class UploadForm(forms.ModelForm):
    '''
    Creates the form when uploading a post
    '''
    class Meta:
        model = Post
        fields = ('title', 'description',
                  'armor', 'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'armor': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    '''
    Edits the post
    '''
    class Meta:
        model = Post
        fields = ('title', 'description',
                  'armor', 'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'armor': forms.Select(attrs={'class': 'form-control'}),
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
                                          'placeholder': 'Write something about this post...'}),
        }


class ContactForm(forms.ModelForm):
    '''
    Contact form for users to send a message
    '''
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }