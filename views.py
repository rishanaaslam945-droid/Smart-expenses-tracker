from django.shortcuts import render, redirect
from .models import Expense
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == "POST":
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        date = request.POST.get("date")

        # Save expense with logged-in user
        Expense.objects.create(
            user=request.user,
            description=description,
            amount=amount,
            category=category,
            date=date
        )

        return redirect('home')

    expenses = Expense.objects.filter(user=request.user)

    return render(request, 'tracker/home.html', {'expenses': expenses})