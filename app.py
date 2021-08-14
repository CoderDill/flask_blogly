from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

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


@app.route("/users/<int:user_id>/edit")
def show_edit_form(user_id):
    """Show edit form"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_form.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user = User.query.get(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route("/users/<user_id>/delete", methods=["POST"])
def remove_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>/posts/new")
def show_post_form(user_id):
    """Show form to add a post for that user"""
    user = User.query.get_or_404(user_id)
    return render_template("add_post.html", user=user)


@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def handle_add_post(user_id):
    """Handle add form; add post and redirect to the user detail page."""
    title = request.form["title"]
    content = request.form["content"]

    new_post = Post(title=title, content=content, user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/posts/{new_post.id}")


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Show Post and buttons for edit/delete"""
    

    post = Post.query.get(post_id)
    user_id = post.user_id
    user = User.query.get_or_404(user_id)

    return render_template("post_detail.html", post=post, user=user)


@app.route("/posts/<int:post_id>/edit")
def show_edit_post_form(post_id):
    """Show form to edit post, cancel to go back"""


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def handle_edit_post(post_id):
    """Handle editing of a post. Redirect back to the post view"""


@app.route("/posts/<int:post_id>/delete")
def delete_post(post_id):
    """Delete Post"""

    post = Post.query.get(post_id)
    db.session.delete(post)

    db.session.commit()

    return redirect(f"/posts/{post_id}")
