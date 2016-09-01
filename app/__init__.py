#-*- coding:utf-8 -*-

from flask import Flask
from app import views
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')




