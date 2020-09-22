import sys
sys.path.insert(0, '/Users/bumsu/SbaProject')
from crawler.entity import Entity
from crawler.service import Service


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()


if __name__ == '__main__':
    api = Controller()
    service = Service()

    soup_webtoon = service.get_url('https://comic.naver.com/webtoon/weekday.nhn')
    service.naver_webtoon(soup_webtoon)

    soup_movie_rank = service.get_url('https://movie.naver.com/movie/running/current.nhn')
    service.naver_movie_rank(soup_movie_rank)