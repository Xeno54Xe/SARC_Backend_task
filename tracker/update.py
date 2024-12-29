from tracker.models import Budget, Transaction
from django.db.models import Sum
def run(self):

    total = 0
    amt_list = Transaction.objects.values_list('amt')
    for each_trans in amt_list: 

        total += int(each_trans[0])
    Budget.transtot = total 
    Budget.save(self)
    print("starting script done")

    return