from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Storage
from .forms import StorageForm
from django.forms import modelformset_factory

# Create your views here.
class DisplayView(TemplateView): 
    template_name = 'view.html'

class ModelStorageCreateView(CreateView, ListView):
    model = Storage
    form_class = StorageForm
    template_name = 'pages/create.html'
    success_url = reverse_lazy('storage_create')
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Create New Storage'
        return context
    
    def form_valid(self, form):
        storage_initials = self.request.POST.getlist('storage_initial')  # Menangani multiple storage_initial
        descriptions = self.request.POST.getlist('description')  # Menangani multiple description

        for storage, desc in zip(storage_initials, descriptions):
            self.model.objects.create(
                storage_initial=storage,
                description=desc,
            )

        return redirect(self.request.META.get('HTTP_REFERER'))

    '''def post(self, request, *args, **kwargs):
        # Menangani formset ketika data POST dikirimkan
        formset = StorageFormSet(request.POST)
        if formset.is_valid():
            formset.save()  # Simpan data jika formset valid
            return redirect(self.success_url)  # Redirect setelah berhasil menyimpan
        return self.render_to_response(self.get_context_data(formset=formset))'''

