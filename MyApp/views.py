# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import scrum_db
from django.core.context_processors import csrf
import json

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/login")
    return render_to_response("accounts/profile.html", {'uname' : request.user.first_name + ' ' + request.user.last_name,
                                                        'email' : request.user.email,
                                                        'll' : request.user.last_login,
                                                        'dj' : request.user.date_joined})

def dash_board(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/login")
    tasks_dict = scrum_db.get_all_tasks()
    bugs_dict = scrum_db.get_all_bugs()
    print(tasks_dict, bugs_dict)
    return render_to_response("dash_dev.html", {'uname' : request.user.first_name + ' ' + request.user.last_name,
                                                'tasks' : tasks_dict,
                                                'bugs' : bugs_dict})

def scrum_board(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/login")
    return render_to_response("board.html", {'uname' : request.user.first_name + ' ' + request.user.last_name})

def diagrams(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/login")
    return render_to_response("diagrams.html", {'uname' : request.user.first_name + ' ' + request.user.last_name})

def add(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/login")
    print("222")
    if request.method == 'POST':
        message = (str(request.POST['description']),
               str(request.POST['assign_to']),
               str(request.POST['status']),
               str(request.POST['type_of_entity']))
        features_model.add_item(message)
    else:
        message = "POST request error!"
        print(message)
        return HttpResponse(message)
    return HttpResponseRedirect("/dash_board/")

def add_entity(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/login")
    print("111")
    c = {}
    c.update(csrf(request))
    print(c)
    return render_to_response('add_entity.html', c)

#def ajax_example(request):
#    if not request.POST:
#        return render_to_response('weblog/ajax_example.html', {})
#    response_dict = {}
#    name = request.POST.get('name', False)
#    total = request.POST.get('total', False)
#    response_dict.update({'name': name, 'total': total})
#    if total:
#        try:
#            total = int(total)
#        except:
#            total = False
#    if name and total and int(total) == 10:
#        response_dict.update({'success': True })
#    else:
#        response_dict.update({'errors': {}})
#        if not name:
#            response_dict['errors'].update({'name': 'This field is required'})
#        if not total and total is not False:
#            response_dict['errors'].update({'total': 'This field is required'})
#        elif int(total) != 10:
#            response_dict['errors'].update({'total': 'Incorrect total'})
#    return render_to_response('weblog/ajax_example.html', response_dict)

def get_json(request):
    JSONObj = features_model.get_all()
    obj = json.dumps(JSONObj)
    print(obj)
    return HttpResponse(obj)