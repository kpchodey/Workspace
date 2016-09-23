# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Revo
from app.forms import UserForm
from app.models import Storm
from app.models import Appium
from app.models import Set_Top_Box
from django.contrib.auth.decorators import login_required

def view_report(request):
    Serial_Number=request.POST.get('Serial_Number','default_value')
    return render_to_response('url',{'app/layout.html':r})

# @login_required
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/layout.html",
        RequestContext(request,
        {
            "title":"Home Page",
            "year":datetime.now().year,
        })
    )

#################
## Revo Views ##
#################
# @login_required
def Revo(request):
    if request.method == 'GET':
        import jenkins
        import urllib2 
        import urllib

        j = jenkins.Jenkins('http://localhost:8080', 'jenkins', 'jenkins123')

        #Getting the list of plugins 
        info = j.run_script("println(Jenkins.instance.pluginManager.plugins)")
        print(info)

        #'sample' is an existing job
        #Fetch configuration details of this job
        jobConfig = j.get_job_config('sample')
        print(jobConfig)

        #Replace contents of config file.'python connectivity.py' is replaced with 'python testing.py'.
        shellCommand = jobConfig.replace('<command>python command#2.py</command>', '<command>cd C:\git_new\evo_automation\ tests\TestRunner\npython C:\git_new\evo_automation\ tests\TestRunner\TestRunner.py VMS_01 REG_AGREED_SUITE02 True\nC:\git_new\evo_automation\ tests\TestRunner\ReportFile C:\git_new\evo_automation\ reports\nC:\git_new\evo_automation\ tests\TestRunner\Test_Suite.json REG_AGREED_SUITE02 %BUILD_NUMBER%</command>')
        j.reconfig_job('sample',shellCommand)
        print(jobConfig)

        #Build 'sample' jobq
        j.build_job('sample')
            
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/layout.html",
        RequestContext(request,
        {
            "title":"Revo",
            "message":"Stuff about revo goes here.",
            "year":datetime.now().year,
        })
    )

def GetSerialNum(request):
    if request.method == 'GET':
        import socket
        import time
        import string
        import re
        import urllib2
        from xml.etree import ElementTree as ET
        from xml.dom.minidom import parse
        import os

        print 'calling SETTOPBOX function'

        msg = \
            'M-SEARCH * HTTP/1.1\r\n' \
            'HOST:239.255.255.250:1900\r\n' \
            'MX:2\r\n' \
            'MAN:ssdp:discover\r\n' \
            'ST:urn:schemas-upnp-org:device:ManageableDevice:2\r\n'

        # Set up UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.settimeout(1000)
        s.sendto(msg, ('239.255.255.250', 1900) )

        try:
            os.remove('serialnumbers.txt')
        except OSError:
            pass

        def logToFile(logTxt):
            logFile = open("serialnumbers.txt", "a+")
            logFile.write(logTxt+"\n")
            # print logTxt

        def getCurrentTimeStamp():
            return strftime("%Y-%m-%d %H:%M:%S")

        try:
            while True:
                data, addr = s.recvfrom(65507)
                mylist=data.split('\r')
                url = re.findall('http?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
                print url[0]
                response = urllib2.urlopen(url[0])
                the_page = response.read()
                # print the_page

                tree = ET.XML(the_page)
                with open("temp.xml", "w") as f:
                    f.write(ET.tostring(tree))

                document = parse('temp.xml')
                actors = document.getElementsByTagName("ns0:serialNumber")
                for act in actors:
                    for node in act.childNodes:
                        if node.nodeType == node.TEXT_NODE:
                            r = "{}".format(node.data)
                            print r
                            logToFile(str(r))

            time.sleep(10)
            s.sendto(msg, ('239.255.255.250', 1900) )


        except socket.timeout:
            pass

    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/layout.html",
        RequestContext(request,
        {
            "title":"Revo",
            "message":"Stuff about revo goes here.",
            "year":datetime.now().year,
        })
    )


@login_required
def Storm(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/Storm/Storm.html",
        RequestContext(request,
        {
            "title":"Storm",
            "message":"Stuff about Storm goes here",
            "year":datetime.now().year,
        })
    )

#################
## Appium Views ##
#################
# @login_required
def Appium(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/Appium/Appium.html",
        RequestContext(request,
        {
            "title":"Appium",
            "message":"Stuff about Appium goes here.",
            "year":datetime.now().year,
        })
    )

def Reports(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/Reports.html",
        RequestContext(request,
        {
            "title":"Reports",
            "message":"Stuff about Reports goes here.",
            "year":datetime.now().year,
        })
    )


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            pass
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(
            'app/user/register_form.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)