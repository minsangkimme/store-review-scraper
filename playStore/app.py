import pprint
import json
from collections import OrderedDict
from google_play_scraper import Sort, reviews_all

file_data = OrderedDict()

rvws = reviews_all(
    'com.washswat.android',
    sleep_milliseconds=1000,
    lang='ko',  # defaults to 'en'
    country='kr',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
)


# 앱 리뷰 스크랩 json 파일
# file_data['data'] = json.dumps(rvws, indent=4, sort_keys=True, default=str, ensure_ascii=False)


# with open('reviews.json', 'w', encoding='utf-8') as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent=4)


pprint.pprint(rvws.__len__())
