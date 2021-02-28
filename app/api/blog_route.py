from flask import Blueprint, request, current_app as app
from app.repos.blogs import Blogs


blog_route = Blueprint('blog_route', __name__)

@blog_route.route('/', methods=['GET'])
def index():
    try:
        object = Blogs()
        print(object)
        _all_blogs = object.get_all_blogs()
        return _all_blogs, 200
    except Exception as e:
        print(e)


@blog_route.route('/addblog', methods=['POST'])
def add_blog():
    try:
        data = request.get_json()
        object = Blogs()
        _res = object.add_blog(data)
        return _res
    except Exception as e:
        print(e)
