from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

"""Blogly application."""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def root():
    return redirect("/users")


@app.route('/users')
def users_list():
    """Show all users"""
    users = User.query.all()
    return render_template("list.html", users=users)


@app.route('/users/new')
def add_user_form():
    """Show add user form"""
    return render_template("add_user_form.html")


@app.route('/users/new', methods=["POST"])
def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name,
                    last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route("/users/<int:user_id>")
def show_user_details(user_id):
    """Show user by id"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

# @app.route("/users/<user_id>/edit")

# @app.route("/users/<user_id>/edit", methods=["POST"])


@app.route("/users/<user_id>/delete", methods=["POST"])
def remove_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")
