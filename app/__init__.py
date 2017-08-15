from flask import Flask, render_template, request, session, url_for, redirect, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SERVER_NAME'] = 'bucketlist.local:5000'
from app import views
