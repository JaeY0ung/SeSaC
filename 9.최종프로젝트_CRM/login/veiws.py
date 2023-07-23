from flask import Blueprint, render_template, request
import sqlite3

login_bp = Blueprint('login', __name__)

conn = sqlite3.connect('user.db', check_same_thread=False)
cursor = conn.cursor()

@login_bp.route('/login')
def login():
    pass