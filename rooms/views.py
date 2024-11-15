from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Room
from .models import Message
from django.contrib.auth.models import User


@login_required
def rooms(request):
    user = request.user
    all_rooms = Room.objects.filter(members=user)
    print("users", all_rooms[0].members)
    return render(request, "core/rooms.html", {"rooms": all_rooms})


def create_or_get_private_room(user1, user2):
    # Sort user IDs to ensure uniqueness regardless of order
    sorted_ids = sorted([str(user1.id), str(user2.id)])
    unique_room_id = "-".join(sorted_ids)

    # Check if the room exists based on the slug
    room, created = Room.objects.get_or_create(slug=unique_room_id)
    if created:
        room.members.set([user1, user2])
    return room


@login_required
def room(request, user_id):  # room_id is slug and it hash
    this_username = request.user
    second_user = get_object_or_404(
        User, username=user_id
    )  # Use get_object_or_404 for better error handling
    this_room = create_or_get_private_room(this_username, second_user)
    messages = Message.objects.filter(room=this_room)
    return render(request, "core/room.html", {"room": this_room, "messages": messages})
