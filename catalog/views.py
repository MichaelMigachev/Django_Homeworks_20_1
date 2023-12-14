from django.shortcuts import render
from catalog.models import Product, Blog
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


# Create your views here.

def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


# def categories(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Каталог'
#     }
#     return render(request, 'catalog/category_list.html', context)

class CategoryListView(ListView):
    model = Product


# CreateRUD
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'publication_sign')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            obj.slug = slugify(obj.title)
            obj.save()
        return super().form_valid(form)
# CReadUD
class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()

        return obj


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(publication_sign=True)


# CRUpdateD
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'publication_sign')
    success_url = reverse_lazy('catalog:blog_list')

    #def get_success_url(self):
    #    return reverse('catalog:blog_detail',args=[self.kwargs.get('id')])


# CRUDelete
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

