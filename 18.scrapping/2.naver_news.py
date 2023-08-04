import requests
from bs4 import BeautifulSoup


def get_naver_sportsnews():
    data = requests.get('https://sports.news.naver.com/index')
    soup = BeautifulSoup(data.text, 'html.parser')

    news = soup.select('.today_list > li')

    print(len(news))

    for li in news:
        title = li.a['title']
        # print(title)
        yield title

def get_naver_land_headlines():
    data = requests.get('https://land.naver.com/news/')
    soup = BeautifulSoup(data.text, 'html.parser')

    headline1 = soup.select_one('.group > dl > dt > span').text
    print(f'{headline1}')

    headlines2 = soup.select('.group2 > .list > li')
    # print(f'{headlines2}\n')

    headlines3 = soup.select('.group2 > .list2 > li')
    # print(headlines3)

    for headline in headlines2+headlines3:
        print(headline.span.text)
        print(headline.select_one('span').text)


def get_naver_land_main():
    data = requests.get('https://land.naver.com/news/')
    soup = BeautifulSoup(data.text, 'html.parser')

    links = []

    headline1_link = soup.select_one('.group > dl > dt > a')['href']
    links.append(headline1_link)
    # print(f'{headline1_link}')

    headlines2 = soup.select('.group2 > .list > li')
    for headline in headlines2:
        headline_link = headline.select_one('.title > a')['href']
        links.append(headline_link)
        # print(f'{headline_link}\n')

    headlines3 = soup.select('.group2 > .list2 > li')
    for headline in headlines3:
        headline_link = headline.select_one('.title > a')['href']
        links.append(headline_link)
        # print(f'{headline_link}\n')

    for link in links:
        print(link)
        data = requests.get('https://land.naver.com'+link)
        soup = BeautifulSoup(data.text, 'html.parser')
        text = soup.select_one('#articleBody').text
        print(text)

def get_movie_ranking():
    data = requests.get('https://movie.daum.net/ranking/reservation')
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select('.list_movieranking > li')
    links= []
    for i in range(len(movies)):
        movie = movies[i]
        rank = i+1
        content = movie.select_one('div > div.thumb_cont')

        movie_name = content.select_one('strong > a').text
        movie_link = 'https://movie.daum.net/' + content.select_one('strong > a')['href']
        links.append(movie_link)

        # print(movie_name)

        movie_grade = content.select_one('span.txt_append > span.info_txt > span.txt_grade').text
        # print(movie_grade)

        movie_reservation_rate = content.select_one('span.txt_append > span.info_txt > span.txt_num').text
        movie_info = movie.select_one('div > div.thumb_item > div.poster_info > a').text.strip()
        print(f'{rank}위: {movie_name} 평점: {movie_grade} 예매율: {movie_reservation_rate}\n{movie_info}\n{movie_link}')

    for link in links:
        data = requests.get(link)
        soup = BeautifulSoup(data.text, 'html.parser')
        try:
            poster_url = soup.select_one('div > div.box_basic > div.info_poster > a')['href']
        except:
            poster_url = '정보 없음'
        print(poster_url)


def print_news():
    data = requests.get('https://sports.news.naver.com/index')
    soup = BeautifulSoup(data.text, 'html.parser')
    news_content = soup.select_one('.news_end')


if __name__ == "__main__":
    # get_naver_sportsnews()
    # get_naver_land_headlines()
    # get_naver_land_main()
    get_movie_ranking()
    