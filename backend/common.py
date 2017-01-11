import os
import hashlib
from datetime import datetime
UPLOADS_DIR = os.path.join('static', 'uploads')
IMAGE_DIR = os.path.join('static', 'images')
HASH_SALT = b'1U+q8L!TXEyws+5+OKEzf=q~ffCo>8-u/QJyL}cSqcg~~Ar`C{u{ZPP{Ky6M`l|b'

def hash_string(s):
    return hashlib.sha512(HASH_SALT + s).hexdigest()

def get_upload_path(filename):
    return os.path.join(UPLOADS_DIR, filename)

def get_image_path(filename):
    return os.path.join(IMAGE_DIR, filename)

def get_current_time():
    return datetime.now().isoformat()