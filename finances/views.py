from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from finances.models import Expense, Category
from .forms import ExpenseForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

def home_view(request):
    return render(request,'finances/home.html')



class ExpenseListView(LoginRequiredMixin,ListView):
    model = Expense
    template_name = 'finances/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(userfk=self.request.user)
    
class ExpenseCreateView(LoginRequiredMixin,CreateView):
    model = Expense
    template_name = 'finances/expense_form.html'
    form_class = ExpenseForm
    success_url = '/finances/list_expense/'
    title = 'Criar Despesa'

    def form_valid(self, form):
        form.instance.userfk = self.request.user
        return super().form_valid(form)

        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    success_url = '/finances/list_expense/'
    template_name = 'finances/expense_update.html'

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'finances/expense_delete.html'
    success_url = reverse_lazy('expense_list')
  
