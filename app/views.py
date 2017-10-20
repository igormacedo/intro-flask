from flask import render_template, request
from app import app, db, models

@app.route('/')
@app.route('/index')
def index():
    posts = models.PostSimple.query.all()
    
    return render_template("home.html",
                           posts=posts)

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():

    if request.method == "POST":
        text = request.form['cd_body']
        name = request.form['cd_name']
        newpost = models.PostSimple(body=text, user_name=name)
        db.session.add(newpost)
        try:
            db.session.commit()
        except:
            print("Aconteceu algum erro")

    return render_template("newpost.html",
                           title='Home')
