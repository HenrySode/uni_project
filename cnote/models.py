from django.db import models

class ConceptNote(models.Model):
    title = models.CharField(max_length = 200)
    problem_statement = models.TextField(null = True, blank = True)
    main_object = models.CharField(max_length = 200,null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)


    
    def __str__(self):
        return self.title
