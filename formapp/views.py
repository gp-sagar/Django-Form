from django.shortcuts import render
from .forms import colorfulcontactform

def index(request):
    if request.method == 'POST':
        form = colorfulcontactform(request.POST)
        if form.is_valid():
            print(form.errors)
            pass  # does nothing, just trigger the validation
    else:
        form = colorfulcontactform()
    return render(request, 'index.html', {'form': form})
