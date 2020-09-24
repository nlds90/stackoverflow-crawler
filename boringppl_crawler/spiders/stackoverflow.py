# -*- coding: utf-8 -*-
import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python-3.x?tab=Votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

        next_page = response.css('a.js-pagination-item[rel=next]::attr(href)').get()

        if next_page is not None:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_question(self, response):
        texts = response.css('.question .js-post-body :not(div)::text').extract()
        body = "".join(texts)

        answer_texts = response.css('.accepted-answer .js-post-body :not(div)::text').extract()
        answer = "".join(answer_texts)

        vote_count = response.css('.question .js-vote-count::text').get()
        answer_vote_count = response.css('.accepted-answer .js-vote-count::text').get()

        yield {
            'title': response.css('h1 a::text').get(),
            'body': body,
            'vote_count': vote_count,
            'answer': answer,
            'answer_vote_count': answer_vote_count,
            'link': response.url,
        }
