import scrapy
from scrapy.http import Response

from YelpAPI import get_biz
from get_url import get_url
from yelpcrawler.items import YelpItem


class BusinessesSpider(scrapy.Spider):
    name = "businesses"

    allowed_domains = ["www.yelp.com"]
    start_urls = ["https://www.yelp.com/search?find_desc=contractors&find_loc=San+Francisco%2C+CA"]

    def parse(self, response: Response, **kwargs):
        urls = response.css(".css-1agk4wl > span > a::attr(href)").extract()
        for url in urls:
            url = "http://www.yelp.com" + url
            business_id = url.split("/")[-1]
            yield scrapy.Request(url=url, callback=self.parse_details, cb_kwargs={'business_id': business_id})

        next_page = response.css(".pagination-links__09f24__bmFj8  .css-foyide .next-link::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_details(self, response, business_id):
        page = YelpItem()
        website = get_url(response.css(".css-1vhakgw .css-1p9ibgf > a[href*='biz_redir']::attr(href)").extract())
        business_data = get_biz(business_id)
        reviews = []
        for item in response.css(".review__09f24__oHr9V")[:5]:
            name = item.css(".review__09f24__oHr9V .css-1m051bw::text").get(),
            location = item.css(".css-qgunke::text").get(),
            date = item.css(".css-chan6m::text").get(),

            reviews.append({
                "name": name,
                "location": location,
                "date": date,
            })
        page["name"] = business_data["name"]
        page["rating"] = business_data["rating"]
        page["number_of_reviews"] = business_data["review_count"]
        page["yelp_url"] = business_data["url"]
        page["website"] = website
        page["reviews"] = reviews
        return page