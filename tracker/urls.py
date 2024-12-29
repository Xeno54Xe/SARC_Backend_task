
from django.urls import path, re_path, include
from tracker.views import HomePageView, BudgetView, AlltransView, NewrecordView, NewBudgetView, delete_transaction, TransactionUpdateView, BudgetUpdateView, delete_budget, AddSavingsGoalView
 
urlpatterns = [
    re_path(r'^$', HomePageView.as_view(), name='home'),
    re_path(r'^budget/$', BudgetView.as_view(), name = 'Your-Budget'),
    re_path(r'^record/$', NewrecordView.as_view(), name = 'Record-Transaction'),
    re_path(r'^alltrans/$', AlltransView.as_view(), name = 'All-transactions'),
    re_path(r'^setbudget/$', NewBudgetView.as_view(), name = 'New-Budget'),
    path('transaction/delete/<int:pk>/', delete_transaction, name='transaction-delete'),
    path('transaction/update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('budget/update/<int:pk>/', BudgetUpdateView.as_view(), name='budget-update'), 
    path('budget/delete/<int:pk>/', delete_budget, name='budget-delete'),
    path('add_savings_goal/', AddSavingsGoalView.as_view(), name='Add-saving-goal'),
]
 
