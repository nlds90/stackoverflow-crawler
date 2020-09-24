# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowQuestion(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    body = scrapy.Field()
    vote_count = scrapy.Field()
    answer = scrapy.Field()
    answer_vote_count = scrapy.Field()
    link = scrapy.Field()
