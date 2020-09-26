from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from webapp.forms import ReviewForm
from webapp.models import Review, Product
from django.views.generic import CreateView, UpdateView, DeleteView


class ReviewCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'review/review_create.html'
    form_class = ReviewForm
    model = Review
    permission_required = 'webapp.add_review'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_view', pk=product.pk)

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'review/review_update.html'
    form_class = ReviewForm
    model = Review
    permission_required = 'webapp.change_review'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Review
    permission_required = 'webapp.delete_review'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})