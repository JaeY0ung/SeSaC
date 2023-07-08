import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

