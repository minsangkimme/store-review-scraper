import json
from collections import OrderedDict

reviews = []
file_data = OrderedDict()

with open('reviews.json', 'r', encoding='utf-8') as data_file:
    json_data = json.load(data_file, strict=False)

_reviews = json.loads(json_data.get('data'))

for dict in _reviews:
    obj ={}

    for key in dict:
        if (key == 'content' or key == 'repliedAt' or key == 'score' or key == 'reviewId'):
            obj[key] = dict[key]                            
    reviews.append(obj)    



#  리뷰, 별점, 작성일시, 리뷰아이디 추출
# file_data['data'] = json.dumps(
#     reviews, indent=4, sort_keys=True, default=str, ensure_ascii=False)

# with open('extract_reviews.json', 'w', encoding='utf-8') as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent=4)
