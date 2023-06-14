from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView  # noqa
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm, UploadForm


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return HttpResponseRedirect(reverse('home'))


class EditPost(UpdateView):
    '''
    Allows user to edit a post
    '''
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'content', 'excerpt',]


class DeletePost(DeleteView):
    '''
    Allows user to delete a post
    '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')