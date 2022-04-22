const fs = require('fs');
const reviews = require('../playStore/extract_reviews.json');
const parsedJsonReviews = JSON.parse(reviews.data);
const result = parsedJsonReviews.reduce((acc, curr) => (curr.content + acc), '');
fs.writeFileSync('리뷰 문자열 변환.txt', result);