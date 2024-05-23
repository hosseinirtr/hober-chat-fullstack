from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room
from .models import Message
from django.contrib.auth.models import User

@login_required
def rooms(request):
    user = request.user
    public_rooms = Room.objects.filter(is_private=False)
    user_rooms = Room.objects.filter(members=user)
    all_rooms = public_rooms.union(user_rooms)
    return render(request, 'core/rooms.html', {"rooms": all_rooms})



@login_required
def room(request, room_id):
    this_room, created = Room.objects.get_or_create(slug=room_id)
    this_username = request.user.username
    this_user = User.objects.get(username=room_id.replace(request.user.username, ''))
    this_room.members.add(this_user)

    if created:
        this_room.is_private = True  # Set is_private to True only if the room is newly created
        second_user = User.objects.get(username=room_id.replace(this_username, ''))
        this_room.members.add(second_user)
        this_room.save()

    messages = Message.objects.filter(room=this_room)
    return render(request, 'core/room.html', {"room": this_room, "messages": messages})
