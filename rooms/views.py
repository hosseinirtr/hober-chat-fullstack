from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room
from .models import Message
# Create your views here.



@login_required
def rooms(request):
    all_rooms = Room.objects.all()
    return render(request, 'core/rooms.html', {"rooms": all_rooms})


@login_required
def room(request, room_id):
    this_room = Room.objects.get(slug=room_id)
    messages = Message.objects.filter(room=this_room)
    return render(request, 'core/room.html', {"room": this_room, "messages": messages})
