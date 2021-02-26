# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IngredientItem(scrapy.Item):
    ingredient_name = scrapy.Field()


class AllrecipeItem(scrapy.Item):

    title = scrapy.Field()
    author = scrapy.Field()
    # category = scrapy.Field()
    photo = scrapy.Field()
    first_paragraph = scrapy.Field()
    ingredients = scrapy.Field()
    directions = scrapy.Field()
    nutrition_facts = scrapy.Field()
    preptime = scrapy.Field(serializer=str)
    cook_time = scrapy.Field()
    recipe_yield = scrapy.Field()
    date_published = scrapy.Field()
    rating_value = scrapy.Field()
    rating_count = scrapy.Field()
    calorie = scrapy.Field()
    date_published = scrapy.Field()
    desc = scrapy.Field()
    recipe_ingredient = scrapy.Field()
    recipe_instructions = scrapy.Field()
