#-*- coding:utf-8 -*-
import sys
sys.path.append('C:\\Users\\kaish\\OneDrive\\doc\\code\\web\\flasky\\micblog\\app')

from flask import render_template, flash, redirect
from  forms import LoginForm
from app import app


@app.route('/')

@app.route('/index')
def index():
	user = { 'nickname': 'Miguel' } # 用户名
	posts = [ # 提交内容
		{ 
			'author': { 'nickname': 'John' }, 
			'body': 'Beautiful day in Portland!' 
		},
		{ 
			'author': { 'nickname': 'Susan' }, 
			'body': 'The Avengers movie was so cool!' 
		}
	]
	return render_template("index.html",
						   title = 'Home',
						   user = user,
						   posts = posts)
    
@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('login requested for name:'+form.name.data)
		flash('password:'+str(form.password.data))
		flash('remember_me:'+str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',title='sign in',form=form)
	