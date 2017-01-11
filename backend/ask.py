from auth import requires_login
from backend.common import *
from template_engine import render
from db import db_api as db
from auth import requires_login, authenticate_cookie

@requires_login
def ask_handler(request):
    name = request.get_field("name")
    request.write(render("ask.html", {'username': 'rand', 'signed_in': authenticate_cookie(request)}))

@requires_login
def ask_handler_post(request):
    photo_files = request.get_file("fileupload")
    title = request.get_field("question")
    description = request.get_field("description")
    url = request.get_field("url")
    if photo_files != (None, None, None):
        if photo_files[1].startswith('image/'):
            user_id = request.get_secure_cookie("current_user")
            '''photo_files from database needs to be discussed regarding single/multiple photo uploads'''
            post = db.Post.create(user_id, description, title, get_current_time(), [photo_files[2]])
            request.write("Your image was uploaded! name=%s"%(photo_files[0]))
            request.redirect('/view/' + str(post.id))
        else:
            request.write("uploaded file type not supported")

    else:
        user_id = request.get_secure_cookie("current_user")
        # TODO discussed regarding single/multiple photo uploads
        fname = fetch_file(url, os.path.join(UPLOADS_DIR, url.split('/')[-1].split('#')[0]))
        db.Post.create(user_id, description, title, get_current_time(), fname)
        request.redirect('/')



        # TODO Actually handle any errors of any kind???

        # TODO Put some handling of the edge case where neither photo nor URL is entered
        # request.write('We couldn\'t find an uploaded file.')
