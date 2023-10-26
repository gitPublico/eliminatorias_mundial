from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Selection, Player

# Create your views here.
class SelectionListView(ListView):
    model = Selection

class SelectionDetailView(DetailView):
    model = Selection

class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    model = Player
    
class PlayerUpdate(UpdateView):
    # UpdateView es automática solamente referenciando el modelo y le puedo decir que campos va a tener el formulario para que automaticamente cree los campos que quiero actualizar
    model = Player
    fields = '__all__' 

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    # Aquí le dice a donde redirigirse en caso de que se pueda eliminar
    success_url = reverse_lazy('player-list')