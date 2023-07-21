from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# this function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) # retrieve transaction form
    if request.method == 'POST':
        pk = request.POST['account'] # if the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) # call balance function to render that account's Balance Sheet
    content = {'form': form} # pass content to the template in a dictionary
    # adds content of form to page
    return render(request, 'Checkbook/index.html', content)


# this function will render the create new account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieve the Account form
    # checks if reqeust method is POST
    if request.method == 'POST':
        if form.is_valid(): # check to see if the submitted form is valid and if so, saves the form
            form.save() # saves new account
            return redirect('index') # returns user back to the home page
    content = {'form': form} # saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'Checkbook/CreateNewAccount.html', content)


# this function will render the balance page when requested
def balance(request):
    account = get_object_or_404(Account, pk=pk) # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) # retrieve all of that account's transactions
    current_total = account.initial_deposit # create account total variable, starting with initial deposit value
    table_contents = {} # create a dictionary into which transaction and determine which is a deposit or withdrawal
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount # if deposit add amount to balance
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
        else:
            current_total -= t.amount # if withdrawal, subtract amount from balance
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
    # pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'Checkbook/BalanceSheet.html', content)


# this function will render the transaction pager when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) #retrieve the transaction form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']
            form.save() # saves the transaction form
            return balance(request, pk) #redirects the user to the home page after form submission
    # pass content to the template in a dictionary
    content = {'form': form}
    # adds content of form to page
    return render(request, 'Checkbook/AddTransaction.html', content)
