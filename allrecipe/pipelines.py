
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from flask.json import jsonify
from itemadapter import ItemAdapter
from pySpintax import spin



class AllrecipePipeline:
    
    # output = jsonloads['recipe']['bodyspintax']
    folderpath = 'recipemd/'
    spintax = '{ one | two | three }'

    def process_item(self, item, spider):

        # spintax = " { cake | cookie | pastry | last course | custard } "
        spintax = self.spintax
        spinned = spin(spintax)
            
        # filename = 'md/' + item['title'] + '.md'
        filename =  self.folderpath + item['title'] + '.md'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('---' + '\n')
            f.write('type: ' + 'post' + '\n')
            f.write('title: '  + str(item['title']).replace('"', "").replace(":", ",") + '\n')
            if item['author'] is None:
                f.write('author: ' + '' + '\n')
            else:
                f.write('author: ' + '\"' + str(item['author']) + '\"' + '\n')

            f.write('tag:' + ' ' + '\"' + spinned + '\"' + '\n')
 
            # Kategori dibuat statis demi memudahkan (nanti bisa dibuat statis jika ingin buat aplikasi)
            # category = str(item['category']).replace('\n', '').replace(' ', '')
            f.write('category: ' + 'dessert' + '\n')
            if item['photo'] is None:
                f.write('photo: ' + '\"' + '/recipe-photo.jpg' + '\"' + '\n')
            else:
                f.write('photo: ' + '\"' + str(item['photo']) +'\"' + '\n')

            if item['preptime'] is None:
                f.write('prep_time: ' + '' + '\n')
            else:
                f.write('prep_time: ' + '\"' + item['preptime'] + '\"' +'\n')

            if item['cook_time'] is None:
                f.write('cook_time: ' + '' + '\n')
            else:
                f.write('cook_time: ' + '\"' + str(item['cook_time']) + '\"' + '\n')

            if item['recipe_yield'] is None:
                f.write('recipe_yield: ' + '' + '\n')
            else:
                f.write('recipe_yield: ' + '\"' + str(item['recipe_yield']) + '\"' + '\n')

            try:
                f.write('rating_value: ' + str(item['rating_value'])  + '\n')
                f.write('review_count: '  + str(item['rating_count']) + '\n')
            except KeyError :
                print('value & count not exist')

            if item['calorie'] is None:
                f.write('calories: ' + ' ' + '\n')
            else:
                f.write('calories: ' +'\"' + str(item['calorie']) + '\"' +'\n')

            f.write('date_published: ' + str(item['date_published']) + '\n')

            if item['desc'] is None:
                f.write('description: ' + '' + '\n')
            else:
                f.write('description: '  + str(item['desc']).replace('"', "'").replace(':', ",").replace("\'s", "").replace("\'re", "").replace("\'t", "").replace("\'", "") + '\n')

            if item['recipe_ingredient'] is list:
                f.write('recipe_ingredient: ' +'' + '\n')
            else:
                f.write('recipe_ingredient: ' + str(item['recipe_ingredient']) + '\n')

            if item['recipe_instructions'] is list:
                f.write('recipe_instructions: ' + '' + '\n')
            else:
                f.write('recipe_instructions: ' + str(item['recipe_instructions']).replace("\'s", "") + '\n')

            # print('recipe_instructions: ' +
            #       str(item['recipe_instructions']))
            f.write('---' + '\n\n')

            if item['first_paragraph'] is None:
                f.write('' + '\n\n')
            else:
                f.write(str(item['first_paragraph']) + '\n\n')

            f.write('{{< boldheading >}}' + '\n\n')

            # ingredient list
            ingredients = item['ingredients']
            for ingredient in ingredients:
                for ingre in ingredient:
                    ingr = str(ingre).strip()
                    f.write('{{< checkbox ' + '\"' + ingr + '\"' + ' >}}' + '\n')

            f.write('\n\n')

            f.write('{{< direction >}}' + '\n\n')

            # direction list
            directions = item['directions']

            # double list direction
            for direction in directions:
                length = len(direction)
                for direct in range(length):
                    f.write('**Step: ' + str(direct+1) + '**' + '\n\n')
                    dire = str(direction[direct]).strip()
                    f.write(dire + '{{< span >}}' + '\n\n')

            f.write('{{< nutrition >}}' + '\n\n')

            nutrition = item['nutrition_facts']
            f.write('**Per Serving:** ' + str(nutrition).strip())
        
            # return item
