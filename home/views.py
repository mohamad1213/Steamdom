from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required(login_url='/accounts/')
def index(req):
    # group = req.user.groups.first()
    # if group is not None and group.name == 'cyberschooladmin':
    #     return render(req, 'cyberschooladmin/index.html')
    # elif group is not None and group.name == 'schooladmin':
    #     return render(req, 'schooladmin/index.html')
    # elif group is not None and group.name == 'teacher':
    #     return render(req, 'teacher/index.html')
    # else:
        return render(req, 'schoolmaster/index.html')
        