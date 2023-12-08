from django.shortcuts import render
from .forms import ThingForm
def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('some-view-name')
    else:
        form = ThingForm()
        
    return render(request, 'home.html', {'form': form})
