import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'vijetha0110'
DB_PASSWORD = '' # not required for cloud9
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS='True'
UPLOADED_IMAGES_DEST='/home/ubuntu/workspace/flask_blog/static/images'
UPLOADED_IMAGES_URL='/static/images/'