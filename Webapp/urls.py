from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    url(r"^$", "app.views.home", name="home"),
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

## Revo"s

    url(r"^Revo", "app.views.Revo", name="Revo"),

#Set Top Box
    url(r"^Set_Top_Box", "app.views.GetSerialNum", name="Set_Top_Box"),


## Storm"s

    url(r"^Storm", "app.views.Storm", name="Storm"),

## Json"s

    url(r"^Json", "app.views.Json", name="Json"),


## Appium's
    url(r"^Appium", "app.views.Appium", name="Appium"),

## Report's
    url(r"^Reports", "app.views.Reports", name="Reports"),

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

    url(r"^admin/", include(admin.site.urls)),
)
