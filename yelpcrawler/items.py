import scrapy


class YelpItem(scrapy.Item):
    name = scrapy.Field()
    rating = scrapy.Field()
    number_of_reviews = scrapy.Field()
    yelp_url = scrapy.Field()
    website = scrapy.Field()
    reviews = scrapy.Field()
