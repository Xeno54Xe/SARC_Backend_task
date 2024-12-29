from django.db import models
from django.db.models import Sum
class Budget(models.Model):

    budget_amt = models.IntegerField() 
    transtot = models.IntegerField(default=0)
    def __str__(self): return f"Budget: {self.budget_amt}, Total Transactions: {self.transtot}"

class SavingsGoal(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='savings_goals', default=1) 
    goal_name = models.CharField(max_length=100) 
    goal_amount = models.IntegerField() 
    saved_amount = models.IntegerField(default=0)
    def __str__(self): 
        return f"{self.goal_name}: {self.saved_amount}/{self.goal_amount}"
    
class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions', default=1)
    trans_at = models.DateTimeField(auto_now_add=True)
    amt = models.IntegerField()                 #Rs units lena best
    trans_name = models.CharField(max_length=100)
    trans_id = models.AutoField(primary_key=True, default=1)

    def __str__(self): 
        return self.trans_name
     
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) 
        self.budget.transtot = self.budget.transactions.aggregate(total=Sum('amt'))['total'] or 0 
        self.budget.save() 
    
    def delete(self, *args, **kwargs): 
        budget = self.budget 
        super().delete(*args, **kwargs) 
        budget.transtot = budget.transactions.aggregate(total=Sum('amt'))['total'] or 0 
        budget.save()
    
