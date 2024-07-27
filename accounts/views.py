from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView
from .models import CustomUser

class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/customuser_detail.html'
    context_object_name = 'user'

    def get_object(self):
        # Get the user by email from the URL
        email = self.kwargs.get('email')
        return get_object_or_404(CustomUser, email=email)

class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'accounts/customuser_confirm_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('customuser-list')

    def get_object(self):
        # Get the user by email from the URL
        email = self.kwargs.get('email')
        return get_object_or_404(CustomUser, email=email)

class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'accounts/customuser_list.html'
    context_object_name = 'users'
    paginate_by = 10
