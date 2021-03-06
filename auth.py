from typing import Callable
from template_engine.parser import render
from db import db_api as db
from backend.common import get_username

USER_COOKIE = "current_user"

ALL_USER = {} # username : USER (object)

def authenticate_cookie(request):
    """Returns True if cookies can be authenicated"""
    user_cookie = request.get_secure_cookie(USER_COOKIE)
    if user_cookie:
        user_cookie = user_cookie.decode("utf-8")
        print(user_cookie)
        user = db.User.find_by_username(user_cookie)  # type: User
        if user is not None:
            print('user_cookie in alluser')
            return True
    return False

def render_no_login(request):
    request.write(render('notsignedin.html', {'signed_in':authenticate_cookie(request), 'username': get_username(request)}))

def requires_login(func: Callable):
    """
    Function decorator for requiring login
    """
    def ret(request, *args, **kwargs):
        if authenticate_cookie(request):
            # noinspection PyCallingNonCallable
            return func(request, *args, **kwargs)
        else:
            return render_no_login(request)
    return ret

def require_specific_user(func):
    """Decorator that requires the user to = to the cookie set in request"""
    def ret(request, username, *args, **kwargs):
        cookie_user = request.get_secure_cookie(USER_COOKIE).decode("UTF-8")
        print(username, cookie_user)
        if cookie_user is not None and username == cookie_user:
            return func(request, username, *args, **kwargs)
        else:
            request.write("you cannot edit someone elses profile you hacker!")
    return ret



@requires_login
def foo(request, *args, **kwargs):
    print(request)
