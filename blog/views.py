from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView  # noqa
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm, UploadForm, EditForm, ContactForm


class PostList(ListView):
    '''
    Displays all approved posts in a list on the home page (index.html)
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(View):
    '''
    The view to display a posts and comments, as well as
    approving comments
    '''

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post.detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,
                             'Comment successfully added! Now awaiting approval...')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post.detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    '''
    View to display if the post is liked
    '''
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UploadPost(CreateView):
    '''
    Allows user to create a post
    '''
    model = Post
    form_class = UploadForm
    template_name = 'upload_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        '''
        Below code sets the forms instance to the logged
        in user and assigns them as the post author
        when uploading a post. The status is set to indicate
        that this is a draft Post, so it can later be
        approved in the admin site.
        '''
        form.instance.author = self.request.user
        form.instance.status = 0
        '''
        The following code takes the title of the post
        and converts it into a slug and turns it into
        a URL-friendly format. We then check if there is
        any posts with the same slug that already exist
        with a while loop, and if it does, we add a random
        string to make it unique and add this to the slug
        URL that is generated from the title.
        '''
        title = form.cleaned_data['title']
        slug = slugify(title)
        unique_slug = slug
        while Post.objects.filter(slug=unique_slug).exists():
            random_string = get_random_string(length=4)
            unique_slug = f"{slug}-{random_string}"

        form.instance.slug = unique_slug

        return super().form_valid(form)


class EditPost(UpdateView):
    '''
    Allows user to edit a post
    '''
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm

    def get_success_url(self):
        return reverse('home')


class DeletePost(DeleteView):
    '''
    Allows user to delete a post
    '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AboutPage(View):
    """
    Renders the About page
    """
    model = Post
    template_name = 'about'

    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


def contact(request):
    """
    Renders the Contact page
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    
    submitted = request.GET.get('submitted', False)
    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'contact.html', context)