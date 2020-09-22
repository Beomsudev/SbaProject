import sys
sys.path.insert(0, '/Users/bumsu/SbaProject')
from crawler.entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, shutil
from pandas import DataFrame
import pandas as pd
"""

feature.....

"""

class Service:
    def __init__(self):
        self.entity = Entity()  
        pass

    def bugs_music(self):
        pass
    
    def naver_movie(self):
        pass

    # 크롤링 url get
    def get_url(self, url):
        myparser = 'html.parser'
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        # print(soup)
        return soup

    # 폴더 생성 및 사진 저장
    def create_folder(self, src, name, category):
        myfolder = 'C:\\Users\\bumsu\\SbaProject\\test01\\' + category + '\\'
        image_open = urlopen(src)
        filename = myfolder + name + '.jpg'
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

        except FileExistsError as err :
            print(err)

        myfile = open(filename, mode='wb')
        myfile.write(image_open.read())
        myfile.close()



    # 네이버 웹툰 크롤링
    def naver_webtoon(self, soup):
        category = 'webtoon'
        mytarget = soup.find_all('div', attrs={'class':'thumb'})
        print(str(len(mytarget)) + '개의 {} 데이터 수집'.format(category))

        mylist = [] # 데이터를 저장할 리스트

        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')
            # print(myhref)
            # print(result)
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]
            # print(mytitleid)
            # print(myweekday)

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
            # print(mytitle)

            mysrc = imgtag.attrs['src']
            # print(mysrc)

            service = Service()
            service.create_folder(mysrc, mytitle, category)
            # break

            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)

        mycolumns = ['타이틀번호', '요일', '제목', '링크']
        myframe = DataFrame(mylist, columns=mycolumns)

        filename = 'cartoon.csv'

        myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + ' 파일로 저장됨')
        print(category + '사진 저장 완료')



    # 네이버 영화 랭킹 크롤링
    def naver_movie_rank(self, soup):
        category = 'movie_rank'    
        mytarget_title = soup.findAll('div', attrs={'class':'thumb'})
        mytarget_star = soup.findAll('dd', attrs={'class':'star'})

        print(str(len(mytarget_title)) + '개의 %s 데이터 수집' % (category))

        mylist0 = []
        mylist1 = []

        for aaa0 in mytarget_title:
            movie_name = aaa0.find('img').attrs['alt']
            movie_name = movie_name.replace('?', '').replace(':', '')
            movie_src_full = aaa0.find('img').attrs['src']
            movie_src = movie_src_full.replace('?type=m99_141_2', '')
            sublist = []

            sublist.append(movie_name)
            sublist.append(movie_src)

            mylist0.append(sublist)

            service = Service()
            service.create_folder(movie_src, movie_name, category)

        for aaa1 in mytarget_star:
            myhref0 = aaa1.find('a')
            movie_point_full = myhref0.find('span', attrs={'class':'num'})
            movie_point = movie_point_full.contents

            movie_reserve_full = aaa1.find('div', attrs={'class':'star_t1 b_star'})

            try:
                movie_reserve = movie_reserve_full.find('span', attrs={'class':'num'}).contents

            except AttributeError as err:
                # print(err)
                movie_reserve = '미개봉'

            sublist = []

            sublist.append(movie_point)
            sublist.append(movie_reserve)

            mylist1.append(sublist)

        # print(mylist0)
        # print('-'*30)
        # print(mylist1)

        mycolumns0 = ['제목', '스크린샷']
        mycolumns1 = ['별점', '예매율']
        myindex = range(0, len(mylist0))
        myframe0 = DataFrame(mylist0, index=myindex, columns=mycolumns0)
        myframe1 = DataFrame(mylist1, index=myindex, columns=mycolumns1)

        myframe = pd.concat([myframe0, myframe1],axis=1)
        filename = '0920_naver_movie_ranking.csv'
        myframe.to_csv(filename, encoding='utf-8')
        print(filename + ' 파일로 저장됨')

