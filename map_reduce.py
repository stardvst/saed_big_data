import json
from functools import reduce

with open('cities.json', 'r') as f:
    data = json.load(f)

    all_reviews = map(
        lambda city: list(map(lambda bar: bar['reviews'], city['bars'])), data)

    reviews_per_city = map(
        lambda city_reviews:
            list(map(lambda reviews: len(reviews), city_reviews)),
            all_reviews)

    average_in_cities = map(
        lambda reviews: reduce(lambda r1, r2: (r1 + r2) / 2, reviews),
        list(reviews_per_city))

    average_more_than_9 = filter(lambda avg: avg > 9, average_in_cities)

    print(*average_more_than_9, sep='\n')

    # averages = filter(
    #     lambda avg: avg >= 9,
    #     map(
    #         int,
    #         map(lambda reviews: reduce(lambda x, y: (x + y) / 2, reviews),
    #             list(map(
    #                 lambda city_reviews:
    #                     list(map(lambda reviews: len(reviews),
    #                       city_reviews)),
    #                     map(lambda city: list(map(lambda bar: bar['reviews'],
    #                         city['bars'])), data))))))

    # print(*averages)
