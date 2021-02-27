
from flask import Flask,jsonify, request
from src.repositories.blogs import Blogs


app = Flask(__name__)

#let it be a blog application
#1 /(initial route) : list of blog (authentication required to see more)
#2 /onboard-user : create new user if doesnt exists/ return the user_id
#3 /blog-detail: get the detailed blog data with it's id
#4 /create-blog: to create the blog
#5 /update-blog : to update the existing blog
#6 /delete-blog : to create an existing blog

# Gonna use pandas to manipulate sql queries, and a db singleton!


@app.route('/', methods=['GET'])
def index():
    try:
        object = Blogs()
        _all_blogs = object.get_all_blogs()
        return _all_blogs, 200
    except Exception as e:
        print(e)



@app.route('/addblog', methods=['POST'])
def add_user():
    try:
        data = request.get_json()

        object = Blogs()
        _user = object.add_blog(data)
        return _user
    except Exception as e:
        print(e)


