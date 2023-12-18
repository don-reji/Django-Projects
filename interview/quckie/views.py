from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from quckie.models import Task
from quckie.serializer import TaskSerializer

# Create your views here.

def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        # getting the list of tasks
        serializer = TaskSerializer(tasks, many=True)
        # serializing the list of tasks
        return JsonResponse(serializer.data, safe=False)
        # json output
    # for listing our tasks if GET request
    
    # for creating a new task if Post request
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # parse json data from request
        serializer = TaskSerializer(data=data)
        # deserialize task
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
            #success status
        return JsonResponse(serializer.errors, status=400)
        # client error status


def task_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        task = Task.objects.get(pk=pk)
        # find task using primary key
    except Task.DoesNotExist:
        return HttpResponse(status=404)
        # means didn't find particular task 

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)
    # to view the specific task

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        # this is to update/change the specific task. can be used to mark 
        # complete the specific  task


    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)
    # delete specific task


    
