from base_api import ApiTemplate, ApiAuth


class CatFacts(ApiTemplate):
    # https://alexwohlbruck.github.io/cat-facts/
    base_url = 'https://cat-fact.herokuapp.com{}'

    def get_random_fact(self, animal_type='cat', amount=5):
        # [
        #     {
        #         "_id": "591f9894d369931519ce358f",
        #         "__v": 0,
        #         "text": "A female cat will be pregnant for approximately 9 weeks - between 62 and 65 days from conception to delivery.",
        #         "updatedAt": "2018-01-04T01:10:54.673Z",
        #         "deleted": false,
        #         "source": "api",
        #         "sentCount": 5
        #     },
        #     {
        #         "_id": "591f9854c5cbe314f7a7ad34",
        #         "__v": 0,
        #         "text": "It has been scientifically proven that stroking a cat can lower one's blood pressure.",
        #         "updatedAt": "2018-01-04T01:10:54.673Z",
        #         "deleted": false,
        #         "source": "api",
        #         "sentCount": 3
        #     }
        # ]
        return self.objectify_response('/facts/random?animal_type={}&amount={}'.format(animal_type, amount))

    def get_fact_by_id(self, fact_id=None):
        # {
        #     "_id": "591f98803b90f7150a19c229",
        #     "__v": 0,
        #     "text": "In an average year, cat owners in the United States spend over $2 billion on cat food.",
        #     "updatedAt": "2018-01-04T01:10:54.673Z",
        #     "deleted": false,
        #     "source": "api",
        # }
        return self.objectify_response('/facts/{}'.format(fact_id))


class AxolotlFacts(ApiTemplate):
    # https://theaxolotlapi.netlify.app/
    base_url = 'https://axoltlapi.herokuapp.com'

    def get_fact(self):
        return self.objectify_response('')


class CatsAsService(ApiTemplate):
    # https://cataas.com
    base_url = 'https://cataas.com{}'

    def get_cat_tags(self):
        return self.objectify_response('/api/tags')

    def get_cats(self, tags='', skip=0, limit=5):
        #/api/cats?tags=tag1,tag2&skip=0&limit=10
        return self.objectify_response('/api/cats?tags={}&skip={}&limit{}'.format(tags, skip, limit))


class DogApi(ApiTemplate):

    base_url = 'https://api.thedogapi.com/v1{}'

    def get_dog_breeds(self):
        return self.objectify_response('/breeds')

    def get_search_dog_breeds(self, query):
        return self.objectify_response('/breeds/search?q={}'.format(query))

    def get_search_dog_images(self, query_data):
        # order_choice = ('RANDOM', 'ASC', 'DESC')
        # size_choice = ('full', 'med', 'small', 'thumb')
        # 'breed_id=1&category_ids=1&format=1&limit=1&mime_types=1&order=1&page=1&size=1'
        return self.objectify_response('/images/search', query_data)
