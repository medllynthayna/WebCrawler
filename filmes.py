# -*- coding: utf-8 -*-
import scrapy


class FilmesSpider(scrapy.Spider):
    name = 'filmes'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/moviemeter']

    def parse(self, response):
        for filme in response.css('td.titleColumn'):
            yield {
                'titulo' : filme.css('td a::text').get(),
                'ranking' : filme.css('td div::text').get()
            }
