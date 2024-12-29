

from django.shortcuts import render, redirect
from django.views import generic
from .models import Budget, Transaction, SavingsGoal
from django.urls import reverse_lazy


class NewrecordView(generic.CreateView):
    template_name = 'tracker/trans_new.html'
    model = Transaction
    fields = ['trans_name', 'amt']
    success_url = reverse_lazy('All-transactions')

class TransactionUpdateView(generic.UpdateView): 
    model = Transaction 
    fields = ['trans_name', 'amt'] 
    template_name = 'tracker/trans_update.html' 
    success_url = reverse_lazy('All-transactions')

class NewBudgetView(generic.CreateView):
    template_name = 'tracker/newbudget.html'
    model = Budget
    fields = ['budget_amt']
    success_url = reverse_lazy('Your-Budget')

class HomePageView(generic.TemplateView):
    template_name = 'tracker/home.html'

class AlltransView(generic.ListView):
    template_name = "tracker/alltrans.html"
    model = Transaction
    context_object_name = 'transactions'

class BudgetView(generic.ListView):
    template_name = "tracker/budget.html"
    model = Budget
    context_object_name = 'budgets'


class BudgetUpdateView(generic.UpdateView): 
    model = Budget 
    fields = ['budget_amt'] 
    template_name = 'tracker/budget_update.html' 
    success_url = reverse_lazy('Your-Budget')

class AddSavingsGoalView(generic.View): 
    template_name = 'tracker/add_saving_goal.html' 
    success_url = reverse_lazy('Your-Budget') 
    def get(self, request, *args, **kwargs): 
        budgets = Budget.objects.all() 
        return render(request, self.template_name, {'budgets': budgets}) 
    
    def post(self, request, *args, **kwargs): 
        budget_id = request.POST.get('budget') 
        goal_name = request.POST.get('goal_name') 
        goal_amount = request.POST.get('goal_amount') 
        if budget_id and goal_name and goal_amount: 
            budget = Budget.objects.get(id=budget_id) 
            goal_amount = int(goal_amount) 
            SavingsGoal.objects.create(budget=budget, goal_name=goal_name, goal_amount=goal_amount) 
            return redirect(self.success_url) 
        budgets = Budget.objects.all() 
        return render(request, self.template_name, {'budgets': budgets, 'error': 'All fields are required.'})

def delete_transaction(request, pk): 
    transaction = Transaction.objects.get(pk=pk) 
    transaction.delete() 
    return redirect('All-transactions')

def delete_budget(request, pk): 
    budget = Budget.objects.get(pk=pk) 
    budget.delete() 
    return redirect('Your-Budget')
