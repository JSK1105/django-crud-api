from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = Message.objects.create(
            sender=data["sender"],
            recipient=data["recipient"],
            content=data["content"]
        )
        return JsonResponse({"message": "Message created", "id": message.id}, status=201)
def read_messages(request):
    messages = Message.objects.all().values()
    return JsonResponse(list(messages), safe=False)
@csrf_exempt
def update_message(request, message_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        message = Message.objects.get(id=message_id)
        message.content = data["content"]
        message.is_edited = True
        message.save()
        return JsonResponse({"message": "Message updated"})
@csrf_exempt
def delete_message(request, message_id):
    if request.method == "DELETE":
        message = Message.objects.get(id=message_id)
        message.delete()
        return JsonResponse({"message": "Message deleted"})

