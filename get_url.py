from urllib import parse


def get_url(redirect_url: str) -> str | None:
    if not redirect_url:
        return None
    full_url = 'https://www.yelp.com' + redirect_url[0]
    query_def = parse.parse_qs(parse.urlparse(full_url).query)['url'][0]
    return query_def
