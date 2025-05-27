from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views import View
from .models import Product, Category, Order, User

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'admin'

class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'wbchina/admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_count'] = Product.objects.count()
        context['categories_count'] = Category.objects.count()
        context['orders_count'] = Order.objects.count()
        context['users_count'] = User.objects.count()
        context['recent_orders'] = Order.objects.all().order_by('-created_at')[:5]
        context['recent_users'] = User.objects.all().order_by('-date_joined')[:5]
        return context

class ProductAdminListView(AdminRequiredMixin, ListView):
    model = Product
    template_name = 'wbchina/admin/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = Product
    template_name = 'wbchina/admin/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image', 'stock', 'is_active']
    success_url = reverse_lazy('admin_product_list')

class ProductAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = Product
    template_name = 'wbchina/admin/product_confirm_delete.html'
    success_url = reverse_lazy('admin_product_list')

class CategoryAdminListView(AdminRequiredMixin, ListView):
    model = Category
    template_name = 'wbchina/admin/category_list.html'
    context_object_name = 'categories'

class CategoryAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = Category
    template_name = 'wbchina/admin/category_form.html'
    fields = ['name', 'parent']
    success_url = reverse_lazy('admin_category_list')

class CategoryAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = Category
    template_name = 'wbchina/admin/category_confirm_delete.html'
    success_url = reverse_lazy('admin_category_list')

class CategoryAdminCreateView(AdminRequiredMixin, CreateView):
    model = Category
    template_name = 'wbchina/admin/category_form.html'
    fields = ['name', 'parent']
    success_url = reverse_lazy('admin_category_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Категория успешно создана.')
        return response

class OrderAdminListView(AdminRequiredMixin, ListView):
    model = Order
    template_name = 'wbchina/admin/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

class OrderAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = Order
    template_name = 'wbchina/admin/order_form.html'
    fields = ['status']
    success_url = reverse_lazy('admin_order_list')

class UserAdminListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'wbchina/admin/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

class UserAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = User
    template_name = 'wbchina/admin/user_form.html'
    fields = ['username', 'email', 'role', 'is_active']
    success_url = reverse_lazy('admin_user_list')

class UserAdminToggleView(AdminRequiredMixin, View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user == request.user:
            messages.error(request, 'Вы не можете заблокировать самого себя.')
            return redirect('admin_user_list')
        
        user.is_active = not user.is_active
        user.save()
        
        status = 'разблокирован' if user.is_active else 'заблокирован'
        messages.success(request, f'Пользователь {user.username} успешно {status}.')
        return redirect('admin_user_list') 