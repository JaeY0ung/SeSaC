from flask import Flask, render_template, url_for, redirect, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('movie_data.db', check_same_thread=False)
cur = conn.cursor()

@app.route('/')
def index():
    date_choice = request.args.get('date_choice', default="", type=str)

    #! 날짜 정보들만 가져오기
    cur.execute('''
                SELECT DISTINCT created_on
                FROM daily_ranking
                ''')
    date_choices = sorted([data[0] for data in cur.fetchall()], reverse=True)

    if date_choice:
        cur.execute('''
                SELECT * 
                FROM movie
                JOIN daily_ranking ON movie.id = daily_ranking.movie_id
                WHERE daily_ranking.created_on = ?
                ''',(date_choice,))
    else:
        #! 최근 날짜 가져오기
        cur.execute('''
                    SELECT * 
                    FROM movie
                    JOIN daily_ranking ON movie.id = daily_ranking.movie_id
                    WHERE daily_ranking.created_on = ?
                    ''',(date_choices[0],))

    movies = cur.fetchall()
    # print(movies)

    results = []
    for movie in movies:
        #! 페이지에 보여주는 정보
        movie_info = {
            #? 'movie_id' : movie[0],
            'title' : movie[1],
            'poster_url' : movie[2],
            'short_description' : movie[3],
            #? 'movie_created_on':movie[4],
            #? 'daily_ranking_id' : movie[5],
            #? 'daily_ranking_movie_id':movie[6],
            'rank' : movie[7],
            'rating' : movie[8],
            'reservation_rate' : movie[9],
            #? 'daily_ranking_created_on' : movie[10]
        }
        results.append(movie_info)
        # print(movie_info)

    return render_template('index.html', results=results, date_choices = date_choices, date_choice = date_choice)

if __name__ =="__main__":
    app.run(port=8080, debug=True)