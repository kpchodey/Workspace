from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    # Examples:
    url(r"^$", "app.views.home", name="home"),
    url(r"^contact$", "app.views.contact", name="contact"),
    url(r"^about", "app.views.about", name="about"),
    url(r"^user/login/$",
        "django.contrib.auth.views.login",
        {
            "template_name": "app/login.html",
            "authentication_form": BootstrapAuthenticationForm,
            "extra_context":
            {
                "title":"Log in",
                "year":datetime.now().year,
            }
        },
        name="login"),
    url(r"^logout$",
        "django.contrib.auth.views.logout",
        {
            "next_page": "/",
        },
        name="logout"),


## Event"s

    url(r"^events/$", "app.views.event_index", name="events"),
    url(r"^events/all", "app.views.all_events", name="events"),
    url(r"^events/date/([0-9]{4})/$", "app.views.event_year"),
    url(r"^events/date/([0-9]{4})/([0-9]{2})/$", "app.views.event_month"),
    url(r"^events/date/([0-9]{4})/([0-9]{2})/([0-9]+)/$", "app.views.event_day"),
    ## Ensure that if date without trailing 0 is entered, we don't get a 404
    url(r"^events/date/([0-9]{4})/([0-9]{1})/$", "app.views.event_month"),
    url(r"^events/date/([0-9]{4})/([0-9]{1})/([0-9]+)/$", "app.views.event_day"),
    # url(r"^events/date/upcoming/$", "app.views.upcoming_events"),
    url(r"^events/detail/([0-9]{1})/$", "app.views.event_details"),

## Venue's
    url(r"^venues/$", "app.views.venue_index", name="venues"),
    url(r"^venues/all", "app.views.all_venues", name="venues"),
    url(r"^venues/detail/([0-9]{1})/$", "app.views.venue_details"),
    url(r"^venues/detail/([0-9]{1})/events/$", "app.views.venue_events"),
    
## User stuff

    url(r"^user/login/$",
        "django.contrib.auth.views.login",
        {
            "template_name": "app/login.html",
            "authentication_form": BootstrapAuthenticationForm,
            "extra_context":
            {
                "title":"Log in",
                "year":datetime.now().year,
            }
        },
        name="login"),

    url(r"^logout$",
        "django.contrib.auth.views.logout",
        {
            "next_page": "/",
        },
        name="logout"),


    url(r"^user/register/$", "app.views.register", name="register"),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

    # Uncomment the next line to enable the admin:
    url(r"^admin/", include(admin.site.urls)),
)
