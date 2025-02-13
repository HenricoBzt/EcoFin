from finances.views import ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView,home_view
from django.urls import path

urlpatterns = [
    path('home/',home_view,name='home_ecofin'),
    path('list_expense/', ExpenseListView.as_view(),name='expense_list'),
    path('new_expense/',ExpenseCreateView.as_view(),name= 'expense_create'),
    path('update_expense/<int:pk>/',ExpenseUpdateView.as_view(),name='expense_update'),
    path('delete_expense/<int:pk>/',ExpenseDeleteView.as_view(),name='expense_delete')
]