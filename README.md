# Yelp Crawler

This is the **Crawler**  used Scrapy and YelpAPI to scrape yelp businesses information from https://www.yelp.com/ .

You can enter `pip install -r requirements.txt` in cmd/shell to make sure you have installed all the requirements.

### Extracted data

This project extracts information: business name, business rating, number of reviews,  business yelp url
business website, list of first 5 reviews(reviewer name, reviewer location, review date). The extracted data looks like this sample:
{
 "name": "Yelp BIZ",
 "rating": "5.0",
 "number_of_reviews": 8,
 "yelp_url": "https://www.yelp.com/biz/yelp-biz/",
 "website": "https://yelp-biz.com",
 "reviews": [{"name": ["J Rowling"], "location": ["San Francisco, CA"], "date": ["12/19/2022"],},
}

### Spiders

This project contains one spider and you can list them using the list command:

```shell
$ scrapy list
```

### Running the spiders

You can run a spider using the scrapy crawl command, such as:

```powershell
$ scrapy crawl businesses -o businesses_data.json
```
