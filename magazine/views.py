from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from .models import Post, Comment


class HomeView(ListView):
    """
    This class shows all posts, and adds the newest post on top of the page.
    The posts are ordered by date in decreasing order.
    """

    template_name = 'magazine/home.html'
    queryset = Post.objects.all()
    paginate_by = 6


class AllPostsView(ListView):
    """
    This class shows all posts, and adds the newest post on top of the page.
    The posts are ordered by date in decreasing order.
    """

    template_name = 'magazine/all_posts.html'
    queryset = Post.objects.all()


class AdminPage(LoginRequiredMixin, ListView):
    """
    This class adds all the models data in one area for the superuser.
    """

    model = Post
    template_name = 'admin_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['comments'] = Comment.objects.all()
        context['comments_approved'] = Comment.objects.filter(approved=True)
        context['count'] = Post.objects.all().count()
        context['comment'] = Comment.objects.all().count()
        return context


# Rouizi
class PostView(DetailView):
    """
    This class handles the detail view. When the user clicks 'read more'
    the user get redirected to post.html.
    This class also handles the comments.
    """
    model = Post
    template_name = "magazine/post.html"

    def get_context_data(self, **kwargs):
        """
        This function handles the comments that have been made.
        This function gets the primary key of a specific post.
        This function gets the comments that have been made on that post.

        """
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        This function handles the comment form in the posts DetailView.
        When a post request is made, when a user has commented, the function gets all comments from that post.
        If the form is valid, the function saves the comment and add it to the post.
        """
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    This class handles the view where the user can write and publish a blog post.
    It gives the user fields where they can fill in a title,
    a decription of the post, post content and they can add an image.
    """
    model = Post
    fields = ['title', 'article_description', 'content', 'image']

    def get_success_url(self):
        """
        This method redirects the user to the home page.
        It also displays a message.
        """
        messages.success(
            self.request, 'Your post has been created successfully')
        return reverse_lazy('magazine:home')

# Rouizi
    def form_valid(self, form):
        """
        This method saves the model if the form is valid.
        """
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    This class handles the view where the user can edit their blog post.
    It gives the user fields where they can change the title,
    the decription of the post, the post content and they can change the image.
    This function redirects the user to home.html when the update is done.
    """
    model = Post
    fields = ['title', 'article_description', 'content', 'image']

    # Rouizi
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully')
        return reverse_lazy('magazine:home')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    This class redirects the user to home.html when they have deleted their post.
    It also displays a message.
    """
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully')
        return reverse_lazy('magazine:home')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class UserPostView(generic.ListView):
    """
    This class filters the posts made by a specific user.
    The posts are shown on user_posts.html.
    The posts are ordered by date, where the latest post is shown on top of the page.
    """
    model = Post
    template_name = 'users/user_posts.html'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('-created_on')


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    """
    This class handles the comment deleted by the admin.
    It displays a message if the deletion is successfull.
    """
    model = Comment

    def get_success_url(self):
        messages.success(
            self.request, 'Comment has been deleted successfully')
        return reverse_lazy('magazine:admin_page')


class AdminPostDeleteView(LoginRequiredMixin, DeleteView):
    """
    This class handles the posts deleted by the admin.
    It displays a message if the deletion is successfull.
    """
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Post has been deleted successfully')
        return reverse_lazy('magazine:admin_page')
