from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Tasks(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    due_date=models.DateField()
    completed=models.BooleanField(default=False)
    dependency=models.ManyToManyField('self',symmetrical=False,blank=True)
    # can have multiple relationships with same model instances
    # symmetrical=False means relationship is not bidirectional, ie, A=B but B!=A

    # string representation of the instance
    def __str__(self):
        return self.title
    
    # performing validations
    def clean(self):
        super().clean()
        # calling super of parent class so that the normal validations happen
        # and then adding our custom validation on top of it

        if self.due_date and self.due_date<=timezone.now().date():
            raise ValidationError('Due date must be in the future.')
        # checking if due_date is in the future
        
        # checking if any incomplete dependencies are there for the current instance before 
        # marking it completed, if yes error raised
        incomplete_dependency=self.dependency.filter(completed=False)
        if self.completed and incomplete_dependency.exists():
            # exists() used to check a queryset
            raise ValidationError("Dependent task's not completed. So cannot be marked as complete.")

    def save(self, *args, **kwargs):
        
        # save the task to db
        super(Tasks, self).save(*args, **kwargs)
        # the instance should be saved to db first to create a id, 
        # which is necessary for adding manyToMany relationship
        
        # Check if any child dependencies are incomplete, and set parent task's completed
        #  to False if yes
        if self.dependency.filter(completed=False).exists():
            self.completed = False


        # if this task has parent tasks and if this task is incomplete then set parent 
        # tasks as incomplete
        self.update_parent_completed_status()

        # Reload the instance from db to ensure it has an id (which is needed for adding )
        # dependency, this also makes the instance in-memory
        # self.refresh_from_db()

    # not needed
    # def add_dependency(self, dependency_task):
    #     if self.pk is not None:
    #         self.dependency.add(dependency_task)
    #     else:
    #         # Handle the case where the instance hasn't been saved yet
    #         raise ValueError("Cannot add dependencies to an unsaved instance. Save the instance first.")


    # changes parent's tasks to incomplete if child task is incomplete 
    def update_parent_completed_status(self):
        # If this task has any parent, update their completed status
        parents = Tasks.objects.filter(dependency=self)
        for parent in parents:

            if self.completed==False :
                # changing parent's completed, to False value only if child's completed=False
                parent.completed = self.completed
                parent.save()