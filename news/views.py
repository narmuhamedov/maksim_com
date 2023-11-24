from django.shortcuts import get_object_or_404
from django.views import generic
from . import models, forms


class NewsListView(generic.ListView):
    template_name = 'news_list.html'
    model = models.NewsModel

    def get_queryset(self):
        return self.model.objects.all()


class NewsDetailView(generic.DetailView):
    template_name = 'news_detail.html'

    def get_object(self, **kwargs):
        news_id = self.kwargs.get('id')
        return get_object_or_404(models.NewsModel, id=news_id)


class NewsCreateView(generic.CreateView):
    template_name = 'news_create.html'
    model = models.NewsModel
    form_class = forms.NewsForm
    success_url = "/news_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(NewsCreateView, self).form_valid(form=form)


class NewsDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/news_list/'

    def get_object(self, **kwargs):
        news_id = self.kwargs.get("id")
        return get_object_or_404(models.NewsModel, id=news_id)


class NewsUpdateView(generic.UpdateView):
    template_name = "news_update.html"
    form_class = forms.NewsForm
    success_url = "/news_list/"

    def get_object(self, **kwargs):
        person_id = self.kwargs.get("id")
        return get_object_or_404(models.NewsModel, id=person_id)

    def form_valid(self, form):
        return super(NewsUpdateView, self).form_valid(form=form)
