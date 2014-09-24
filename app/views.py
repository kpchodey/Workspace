# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Price
from app.forms import UserForm, UserProfileForm
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/index.html",
        RequestContext(request,
        {
            "title":"Home Page",
            "year":datetime.now().year,
        })
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/contact.html",
        RequestContext(request,
        {
            "title":"Contact",
            "message":"Your contact page.",
            "year":datetime.now().year,
        })
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/about.html",
        RequestContext(request,
        {
            "title":"About",
            "message":"Your application description page.",
            "year":datetime.now().year,
        })
    )
#################
## Event Views ##
#################

from app.models import Event

def event_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/events/index.html",
        RequestContext(request,
        {
            "title":"Events",
            "year":datetime.now().year,
        })
    )
def all_events(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/events/events_list.html",
        RequestContext(request,
        {
            "title":"All Events",
            "message":"Here is a list of all the event that they are. If you want to view upcoming events, then click on the currently non exsistent button below...",
            "year":datetime.now().year,
            "event_list": Event.objects.filter()
        })
    )

def upcoming_events(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/events/events_list.html",
        RequestContext(request,
        {
            "title":"Upcoming Events",
            "message":"All Upcoming Events",
            "year":datetime.now().year,
            "event_list": Event.objects.filter(date__now>datetime.now()),
        })
    )
def event_year(request, year):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/events/events_list.html",
        RequestContext(request,
        {
            "title":"Events By year",
            "message":"All Event's in " + year,
            "year":datetime.now().year,
            "event_year": year,
            "event_list": Event.objects.filter(date__year=year)
        })
    )
def event_month(request, year, month):
    assert isinstance(request, HttpRequest)
    event_list = Event.objects.filter(date__year=year)
    event_list = event_list.filter(date__month=month)
    return render(
        request,
        "app/events/events_list.html",
        RequestContext(request,
        {
            "title":"Events By year",
            "message":"All Event's in " + year + "-" + month,
            "year":datetime.now().year,
            "event_year": year,
            "event_month":month,
            "event_list": event_list
        })
    )

def event_day(request, year, month, day):
    assert isinstance(request, HttpRequest)
    event_list = Event.objects.filter(date__year=year)
    event_list = event_list.filter(date__month=month)
    event_list = event_list.filter(date__day=day)
    return render(
        request,
        "app/events/events_list.html",
        RequestContext(request,
        {
            "title":"Events By year",
            "message":"All Event's in " + year+"-"+month+"-"+day,
            "year":datetime.now().year,
            "event_year": year,
            "event_month":month,
            "event_day":day,
            "event_list": event_list
        })
    )
def event_details(request, event_id):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/events/event_detail.html",
        RequestContext(request,
        {
            "title":"Event Details",
            "message":"test",
            "year":datetime.now().year,
            "event_details": Event.objects.filter(id=event_id),
            ##"booked_percentage":((Event.seats_avalable)/(Event.total_seats)+"%"),
            "ticket_prices":(Price.objects.filter(event=event_id))

        })
    )


#################
## Venue Views ##
#################

from app.models import Venue

def venue_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venues/index.html",
        RequestContext(request,
        {
            "title":"Venues",
            "year":datetime.now().year,
        })
    )

def all_venues(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venues/venue_list.html",
        RequestContext(request,
        {
            "title":"All Venues",
            "message":"Here is a list of all the venues that they are.",
            "year":datetime.now().year,
            "venue_list": Venue.objects.filter()
        })
    )

def venue_details(request, venue_id):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venues/venue_detail.html",
        RequestContext(request,
        {
            "title":"Venue Details",
            "message":"Detail for this venue thingy",
            "year":datetime.now().year,
            "venue_details": Venue.objects.filter(id=venue_id)
        })
    )
def venue_events(request, venue_id):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/events/events_list.html",
        RequestContext(request,
        {
            "title":"Events at venue",
            "message":"A list of events at venue",
            "year":datetime.now().year,
            "event_list": Event.objects.filter(venue=venue_id)
        })
    )

def register(request):
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            pass

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(
            'app/user/register_form.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)