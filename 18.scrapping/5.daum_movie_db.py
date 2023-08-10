import sqlite3
from bs4 import BeautifulSoup
import requests
from datetime import datetime

created_on = datetime.now().strftime('%Y-%m-%d')
print(created_on)

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

conn = sqlite3.connect('movie_data.db')
cur = conn.cursor()

#! movie 테이블 생성
cur.execute(''' create table if not exists movie(
                id integer primary key autoincrement,
                title text,
                poster_url text,
                short_description text,
                poster_img text,
                created_on datetime
                )'''
            )
conn.commit()

#! daily_ranking 테이블 생성
cur.execute('''create table if not exists daily_ranking(
                id integer primary key autoincrement,
                movie_id integer,
                rank integer,
                rating text,
                reservation_rate text,
                created_on datetime,
                FOREIGN KEY('movie_id') REFERENCES movie(id)
                )'''
            )
conn.commit()

movies = soup.select('.list_movieranking > li')
for i in range(len(movies)):
    movie = movies[i]
    content = movie.select_one('div > div.thumb_cont')

    rank = i+1
    
    title = content.select_one('strong > a').text

    poster_url = 'https://movie.daum.net' + content.select_one('strong > a')['href']
    # print(poster_url)

    #? 평점
    rating = content.select_one('span.txt_append > span.info_txt > span.txt_grade').text

    reservation_rate = content.select_one('span.txt_append > span.info_txt > span.txt_num').text

    short_description = movie.select_one('div > div.thumb_item > div.poster_info > a').text.strip()

    data2 = requests.get(poster_url)
    soup2 = BeautifulSoup(data2.text, 'html.parser')
    poster_img = soup2.select_one('.bg_img')['style'][21:][:-1]
    # print(poster_img)

    # print(f'{rank}위: {title} 평점: {rating} 예매율: {reservation_rate}\n{short_description}\n{poster_url}\n{created_on}')

    #! 1. movie가 있는지 없는지 체크해서 movie 테이블에 추가 (title 같으면 안 들어감!)
    cur.execute('SELECT id FROM movie WHERE title = ?',(title,))
    res = cur.fetchone()
    if not res:
        cur.execute('''INSERT INTO movie
                    (title, poster_url, short_description, poster_img, created_on) values (?,?,?,?,?)''', 
                    (title, poster_url, short_description, poster_img, created_on) )
        conn.commit()
    cur.execute('SELECT id FROM movie WHERE title = ?',(title,))
    movie_id = cur.fetchone()[0]


    cur.execute('SELECT id FROM daily_ranking WHERE movie_id = ? AND created_on = ?', (movie_id, created_on))
    isMovieUpdateToday = cur.fetchone()
    print(isMovieUpdateToday)
    
    #! 이 날짜에 이미 movie 크롤링을 해 왔으면 -> update
    if isMovieUpdateToday:
        cur.execute('''
                    UPDATE daily_ranking
                    SET rank = ?, rating = ?, reservation_rate = ?, created_on = ?
                    WHERE movie_id = ?
                    ''',
                    (rank, rating, reservation_rate, created_on, movie_id))
    #! 오늘은 처음 크롤링해 온 것이거나 아예 처음 들어오는 영화정보이면
    else:
        cur.execute('''
                    INSERT INTO daily_ranking
                    (movie_id, rank, rating, reservation_rate, created_on)
                    VALUES (?, ?, ?, ?, ?)
                    ''',
                    (movie_id, rank, rating, reservation_rate, created_on))

    conn.commit()


conn.close()