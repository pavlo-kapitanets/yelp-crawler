def get_start_url(category_name: str, location: str) -> str:
    location = [i.strip().replace(" ", "+") for i in location.split(",")]
    start_url = f"https://www.yelp.com/search?find_desc={category_name}&find_loc={location[0]}%2C+{location[1]}"
    return start_url
