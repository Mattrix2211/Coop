from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def admin_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped(request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
            return HttpResponseForbidden("Accès réservé aux administrateurs.")
        return view_func(request, *args, **kwargs)
    return _wrapped
