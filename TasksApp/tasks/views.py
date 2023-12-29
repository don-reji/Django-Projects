from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class TasksListView(generics.ListCreateAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # gets the current instance
        completed = request.data.get('completed', False)
        # request -> http request object
        # request.data -> dictionary like object, contains parsed data of http request body
        # get('completed', False) -> gets the value of completed field 
        # can also use get('completed') since completed field has default value of False

        # Check if the task can be marked as complete only if all dependency instances are completed=True
        # else error message and instance not updated
        if completed and not self.check_dependencies(instance):
            return Response({"error": "Cannot mark task as complete until dependencies are completed."}, status=400)

        # updates the instance. 
        return super().update(request, *args, **kwargs)

        # Check if all dependencies are completed
    def check_dependencies(self, task):
        dependencies_completed = all(dep.completed for dep in task.dependency.all())
        # is a generator expression, iterates over all dependency instances associated with the 
        # given task instance and retrieves the value of their completed field.

        # task.dependency.all() returns all instances related to the current task through the ManyToMany relationship
        # all() returns True if all elements of the provided iterable are True
        # so if all dependency instances,completed =true then all() returns true else False
        return dependencies_completed