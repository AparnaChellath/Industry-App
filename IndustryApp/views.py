from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,FormView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .models import Method,Man,Machine,Material,Shift,MachineUsage
from django.urls import reverse_lazy
from .forms import MethodForm ,AssignMachineForm,UserRegistrationForm, ManForm,MachineForm,MaterialForm,ShiftForm,MachineUsageForm
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from rest_framework import viewsets,filters
from .models import Shift, Man, Machine, Material, Method, MachineUsage
from .serializers import ShiftSerializer, ManSerializer, MachineSerializer, MaterialSerializer, MethodSerializer, MachineUsageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserRegisterSerializer

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class SignupView(FormView):
    template_name = 'signup.html'
    form_class=UserRegistrationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user_form = UserRegistrationForm()
        return self.render_to_response(self.get_context_data(user_form=user_form))

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        man_form = ManForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  
            user.save()
           
            login(request, user)
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(user_form=user_form))


class MethodListView(LoginRequiredMixin, ListView):
    model = Method
    context_object_name = 'methods'
    template_name = 'method_list.html'

    def get_queryset(self):
        return Method.objects.select_related('responsible_man').prefetch_related('machines', 'materials')



class MethodCreateView(LoginRequiredMixin, CreateView):
    model = Method
    form_class = MethodForm
    template_name = 'method_form.html'
    success_url = reverse_lazy('method_list')

    def form_valid(self, form):
        man = Man.objects.get(user=self.request.user)
        form.instance.responsible_man = man
        return super().form_valid(form)
    




class AssignMachinesView(LoginRequiredMixin, UpdateView):
    model = Man
    form_class = AssignMachineForm
    template_name = 'assign_machine.html'
    pk_url_kwarg = 'id' 
    success_url = reverse_lazy('method_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['man'] = self.object 
        return context
    


class ManListView(ListView):
    model = Man
    template_name = 'man_list.html'

class ManCreateView(CreateView):
    model = Man
    form_class = ManForm
    template_name = 'man_form.html'
    success_url = reverse_lazy('man_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ManUpdateView(UpdateView):
    model = Man
    form_class = ManForm
    template_name = 'man_form.html'
    success_url = reverse_lazy('man_list')

    def dispatch(self, request, *args, **kwargs):
        man = self.get_object()
        if man.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ManDeleteView(DeleteView):
    model = Man
    template_name = 'man_delete.html'
    success_url = reverse_lazy('man_list')



class MachineListView(ListView):
    model = Machine
    template_name = 'machine_list.html'

class MachineCreateView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine_form.html'
    success_url = reverse_lazy('machine_list')

class MachineUpdateView(UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine_form.html'
    success_url = reverse_lazy('machine_list')

class MachineDeleteView(DeleteView):
    model = Machine
    template_name = 'machine_delete.html'
    success_url = reverse_lazy('machine_list')



class MaterialListView(ListView):
    model = Material
    template_name = 'material_list.html'

class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_form.html'
    success_url = reverse_lazy('material_list')
    
    for m in Material.objects.all():
       print(m.pk, m.name)


class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'material_delete.html'
    success_url = reverse_lazy('material_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Remove this material from all methods
        self.object.method_set.clear()
        return super().delete(request, *args, **kwargs)
  


class MethodUpdateView(UpdateView):
    model = Method
    form_class = MethodForm
    template_name = 'method_form.html'
    success_url = reverse_lazy('method_list')

class MethodDeleteView(DeleteView):
    model = Method
    template_name = 'method_delete.html'
    success_url = reverse_lazy('method_list')


class ShiftListView(ListView):
    model = Shift
    template_name = 'shift_list.html'

class ShiftCreateView(CreateView):
    model = Shift
    form_class = ShiftForm
    template_name = 'shift_form.html'
    success_url = reverse_lazy('shift_list')

class ShiftUpdateView(UpdateView):
    model = Shift
    form_class = ShiftForm
    template_name = 'shift_form.html'
    success_url = reverse_lazy('shift_list')

class ShiftDeleteView(DeleteView):
    model = Shift
    template_name = 'shift_delete.html'
    success_url = reverse_lazy('shift_list')


class MachineUsageListView(ListView):
    model = MachineUsage
    template_name = 'machineusage_list.html'

class MachineUsageCreateView(CreateView):
    model = MachineUsage
    form_class = MachineUsageForm
    template_name = 'machineusage_form.html'
    success_url = reverse_lazy('machineusage_list')

class MachineUsageUpdateView(UpdateView):
    model = MachineUsage
    form_class = MachineUsageForm
    template_name = 'machineusage_form.html'
    success_url = reverse_lazy('machineusage_list')

class MachineUsageDeleteView(DeleteView):
    model = MachineUsage
    template_name = 'machineusage_delete.html'
    success_url = reverse_lazy('machineusage_list')




class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny] 

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ManViewSet(viewsets.ModelViewSet):
    queryset = Man.objects.all()
    serializer_class = ManSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MethodViewSet(viewsets.ModelViewSet):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer


class MachineUsageViewSet(viewsets.ModelViewSet):
    queryset = MachineUsage.objects.all()
    serializer_class = MachineUsageSerializer



class MethodViewSet(viewsets.ModelViewSet):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'responsible_man__name']

    @action(detail=False, methods=['get'], url_path='by-man/(?P<man_id>[^/.]+)')
    def methods_by_man(self, request, man_id=None):
        methods = Method.objects.filter(responsible_man__id=man_id)
        serializer = self.get_serializer(methods, many=True)
        return Response(serializer.data)
    



class MethodSearchView(ListView):
    model = Method
    template_name = 'methods_search.html'
    context_object_name = 'methods'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Method.objects.filter(
                Q(name__icontains=query) |
                Q(responsible_man__user__username__icontains=query)
            )
        return Method.objects.all()