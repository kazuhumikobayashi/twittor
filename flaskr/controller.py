from flask import request, redirect, url_for, render_template, flash

from flaskr import app, db
from flaskr.models import User, Post


@app.route('/')
def show():
    user = User.query.filter(User.id == 2).first()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('show.html', user=user, posts=posts)

@app.route('/add/<user_id>', methods=['POST'])
def post_content(user_id):
    post = Post(
            post_user_id = user_id,
            content = request.form['content'],
            )
    db.session.add(post)
    db.session.commit()
    flash('New content was successfully posted')
    return redirect(url_for('show'))

@app.route('/delete_user/<user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    db.session.delete(user)
    db.session.commit()
    flash('user was successfully deleted')
    return redirect(url_for('show'))
