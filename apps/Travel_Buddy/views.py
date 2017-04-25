# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import Trips
from .forms import TripCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def render_home(request):
    print "routed to render_home"
    ## Display User Travel Plans
    ## Get trips for user
    displayUserTrips = Trips.objects.filter(user=request.user.id)
    displayOtherTrips = Trips.objects.exclude(user=request.user.id)
    allUsers = User.objects.all()
    displayTravelerTrips = Trips.objects.filter(travelers=request.user)
    #User.objects.filter(trips__)
    ## - Travel Plans link to show Travel Plan object details
    ## Display Other User's Travel Plans
    ## Logout link
    ## Add Travel Plan link

    ## JOIN TRIP FUNC
    context={
        "displayUserTrips":displayUserTrips,
        "displayOtherTrips":displayOtherTrips,
        "allUsers":allUsers,
        "displayTravelerTrips":displayTravelerTrips,
    }
    return render(request, "Travel_Buddy/travels.html", context)

def process_trip_join(request, trip_to_join):
    print "routed to process_trip_join"
    # print trip_to_join
    # tripToJoin = Trips.objects.get(id=trip_to_join)
    # print tripToJoin
    # current_user = request.user
    # print current_user.id
    # userToAdd = User.objects.get(id=request.user.id)
    # tripToJoin.travelers.add(userToAdd)
    # print tripToJoin.travelers

    return redirect(reverse('travel-buddy:render_home'))

def render_trip_view(request, trip_to_view):
    print "routed to render_trip_view"
    tripToShow = Trips.objects.get(id=trip_to_view)
    plannedBy = User.objects.get(id=tripToShow.user_id)
    context={
        "tripToShow":tripToShow,
        "plannedBy":plannedBy,
    }

    return render(request, "Travel_Buddy/show_destination.html", context)

def render_add(request):
    print "routed to render_add"
    tripForm = TripCreateForm()

    context={
        "tripForm":tripForm,
    }

    return render(request, "Travel_Buddy/add_trip.html", context)

def process_add(request):
    print "routed to process_add"
    ## add new Book and new Review
    print(request.POST)
    newTrip = TripCreateForm(request.POST, prefix='trip')
    if newTrip.is_valid():
        print "Trip: valid"
        trip = newTrip.save(user_id = request.user.id, commit=False)
        trip.save()
        # # newReview.user_id = request.user.id
        # # print newReview.user_id
        # review = newReview.save(user_id = request.user.id, commit=False)
        # # save error doesn't see book_id as not NULL
        # review.save()
    else:
        print "Not valid"

    return redirect(reverse('travel-buddy:render_home'))


    def process_trip_join(request, trip_to_join):
        print "routed to process_trip_join"

        # print trip_to_join
        tripToJoin = Trips.objects.get(id=trip_to_join)
        userToAdd = User.objects.get(id=request.user.id)

        tripToEdit = TripCreateForm(instance=tripToJoin)
        tripToEdit.process_traveler(userToAdd)
        # TripCreateForm.process_traveler(instance=tripToJoin,traveler_to_add=userToAdd)
        print "process complete?"
        # print tripToJoin
        # current_user = request.user
        # print current_user.id

        #tripToJoin.travelers = userToAdd.id
        # print tripToJoin.travelers

        return redirect(reverse('travel-buddy:render_home'))
