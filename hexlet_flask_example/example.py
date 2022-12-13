from flask import Flask, render_template, request


app = Flask(__name__)

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route("/")
def hello_world():
    return "Welcome to Flask!"


@app.route("/users")
def all_users():
    name = request.args.get('name', default=None)
    filtered_users = filter(function, iterable)
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=name,
    )


@app.route('/users/<id>')
def users(id):
    return render_template(
        'users/show.html',
        name=id,
    )
