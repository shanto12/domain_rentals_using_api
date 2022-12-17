import requests

BASE_URL = "https://api.domain.com.au/v1"
API_KEY = "key_0f2bacb30ed7a5860891088f107d7890"


def rest_call(endpoint, params):
    url = BASE_URL + f"/{endpoint}"
    r = requests.get(url=url, params=params)
    return r, r.json()


def get_all_agencies(params):
    end_point = "agencies"
    params["q"] = "Pyrmont"
    params["pageSize"] = 100
    page_number = 1
    agency_name_list = []
    while 1:
        params["pageNumber"] = page_number
        # rest_call(endpoint=end_point, params=params)
        r, r_json = rest_call(endpoint=end_point, params=params)
        if r.ok:
            agency_name_list.extend([x.get("name") for x in r_json])

        else:
            break

        page_number += 1
        print(f"page_number: {page_number}")
        print(f"agency_name_list: {agency_name_list}")

    print(agency_name_list)


def get_all_listings(params):
    end_point = "listings"
    params["q"] = "Pyrmont"
    params["pageSize"] = 100
    page_number = 1
    listing_name_list = []
    while 1:
        params["pageNumber"] = page_number
        # rest_call(endpoint=end_point, params=params)
        r, r_json = rest_call(endpoint=end_point, params=params)
        if r.ok:
            listing_name_list.extend([x.get("name") for x in r_json])

        else:
            break

        page_number += 1
        print(f"page_number: {page_number}")
        print(f"agency_name_list: {listing_name_list}")

def authentication(params):
    params["ids"] = 1
    end_point = "disclaimers"
    r = rest_call(endpoint=end_point, params=params)


params = dict()
params["api_key"] = API_KEY

# params = {"ids": 1, "api_key": API_KEY}
# authentication(params=params)
get_all_listings(params)
