from auth import requires_login
from backend.common import *
from template_engine import render
from os import path
from db import db_api as db
from auth import requires_login, authenticate_cookie


def view_question_handler(request, question_id):
    # try:
    post = db.Post.find(question_id)
    post_info = {
        'user': post.user_id,
        'description': post.description,
        'question': post.title,
        'date': post.date,
        'file': post.file,
        'signed_in': authenticate_cookie(request),
        'username': get_username(request),
        'comments': post.all_comments(),
        'user_ids': db.User.find_multiple(),
        'photo_id': post.id,
    }
    for i in post_info['comments']:
        curid = i.user_id
        curuser = db.User.find(curid)
        print(curuser.picture)
        i.image = path.join("uploads", "user_image", curuser.picture) if curuser.picture else ""

    request.write(render('view_question.html', post_info))
    # except Exception as e:
        # print(e.with_traceback)
        # request.write('Invalid Id')

def comment_handler_post(request, photo_id):
    text = request.get_field('addComment')
    print(text, 'gotten')
    user_cookie = request.get_secure_cookie(USER_COOKIE)
    if user_cookie is not None:
        user_cookie = user_cookie.decode()
        if db.User.find_by_username(user_cookie):
            print(user_cookie)
            user = db.User.find_by_username(user_cookie)
            user.create_comment(db.Post.find(photo_id), text, None)
            request.redirect("/view/" + str(photo_id))
    else:

        request.write("your not logged in")



