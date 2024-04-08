from django.shortcuts import redirect, render
from . models import ConceptNote
from . forms import CNoteForm
from django.contrib import messages

def concept_note(request):
    cnoteObj = ConceptNote.objects.all()
    form = CNoteForm()
    
    if request.method == 'POST':
        form = CNoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concept note successfully submited')
            return redirect('projects')
        
    context = {'cnoteObj':cnoteObj, 'form':form}
    return render(request, 'cnote/cnote_form.html', context)
