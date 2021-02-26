from scrapy.exceptions import IgnoreRequest
import scrapy

class RecipeMiddleware(object):
    
    def process_request(self, request, spider):
        if "/gallery/" in request.url:
            raise IgnoreRequest()
        else:
            pass