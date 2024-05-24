from django.shortcuts import redirect, render
from . models import ConceptNote
from . forms import CNoteForm
from django.contrib import messages

def concept_note(request):
    form = CNoteForm()
    
    if request.method == 'POST':
        form = CNoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concept note successfully submited')
            return redirect('view-cnote')
        
    context = {'form':form}
    return render(request, 'cnote/cnote_form.html', context)

def view_cnote(request):
    objects = ConceptNote.objects.all()
    context = {'objects':objects}
    return render(request, 'cnote/view-cnote.html', context)