from .models import Comment, Post
from django import forms


class UploadForm(forms.ModelForm):
    '''
    Creates the form when uploading a post
    '''
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Write something...'}),
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
