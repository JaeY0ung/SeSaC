from bs4 import BeautifulSoup
html = '''


'''
soup = BeautifulSoup(html, 'html.parser')
sidebar_div = soup.find('div', class_='sidebar')
sidebar_div = soup.select('sidebar')
sidebar_div = soup.select_one('sidebar')
sidebar_div = soup.select_one('p:nth-child(3)')