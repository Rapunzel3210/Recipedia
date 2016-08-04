import jinja2
import os
from google.appengine.ext import ndb
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/home.html')

        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/search.html')

        self.response.write(template.render())

class NewRecipeHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/new_recipe.html')

        self.response.write(template.render())

class ResultsHandler(webapp2.RequestHandler):

    def post(self):
        template = jinja_environment.get_template('templates/results.html')
        author_value=self.request.get('author')
        name_value=self.request.get('name')
        level_value=(self.request.get('level'))
        ingredient_value=self.request.get('ingredient', allow_multiple=True)
        time_value=self.request.get('time')
        steps_value=self.request.get('steps')
        notes_value=self.request.get('notes')
        # loop through each element in ingredient_value and concatenate to a string variable
        added_ingredient=""
        for index in range(len(ingredient_value)):
            if index == len(ingredient_value) - 1:
                added_ingredient += ingredient_value[index]
            else:
                added_ingredient += ingredient_value[index] + ", "
        new_recipe = {

        'author_answer': author_value,
        'name_answer': name_value,
        'level_answer': level_value,
        'ingredient_answer': added_ingredient,
        'time_answer': time_value,
        'steps_answer': steps_value,
        'notes_answer': notes_value
        }
        recipe_record = Recipe(author=author_value, recipe_name=name_value, level=level_value, ingredient=added_ingredient, time=time_value, steps=steps_value, notes=notes_value)
        recipe_key = recipe_record.put()

        self.response.write(template.render(new_recipe))


class Recipe(ndb.Model):
    author = ndb.StringProperty(required=True)
    recipe_name = ndb.StringProperty(required=True)
    level = ndb.StringProperty(required=True)
    ingredient = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    steps = ndb.StringProperty(required=True)
    notes = ndb.StringProperty(required=True)

    @classmethod #This should work as a search
    def query_recipe(cls, level_value):
        return cls.query(level=level_value)

class Ingredient(ndb.Model):
    ingredient_name = ndb.StringProperty(required=True)


class RecipeResultsHandler(webapp2.RequestHandler):
    GREETINGS_PER_PAGE = 20
    def get(self):
        level = self.request.get('level')
        # recipes = [r for r in Recipe.query().filter(Recipe.level==level).order('recipe_name')]
        recipes = Recipe.query()
        recipes = recipes.filter(Recipe.level==level)
        recipes = recipes.order(Recipe.recipe_name)
        recipes_results = recipes.fetch(self.GREETINGS_PER_PAGE)

        self.response.out.write('<html><body>')

        for recipe in recipes:
            self.response.out.write(
                '<p><a href="/display?name=%s&author=%s&level=%s&ingredients=%s&time=%s&steps=%s&notes=%s">%s</a></p>' % (recipe.recipe_name, recipe.author, recipe.level, recipe.ingredient, recipe.time, recipe.steps, recipe.notes, recipe.recipe_name))

        self.response.out.write('<p><a href="/search"><input type="button" name="button" value="Search For Another Recipe"></a></p>')
        self.response.out.write('<p><a href="/"><input type="button" name="button" value="Back to Home Page"></a></p>')

        self.response.out.write('</body></html>')

class DisplayRecipeHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/display_recipe.html')
        name = self.request.get('name')
        author = self.request.get('author')
        level = self.request.get('level')
        ingredients=self.request.get('ingredients')
        time = self.request.get('time')
        steps = self.request.get('steps')
        notes = self.request.get('notes')

        author_value = author
        name_value = name
        level_value = level
        ingredients_value=ingredients
        time_value = time
        steps_value = steps
        notes_value = notes


        displayed_recipe = {

        'author_answer': author_value,
        'name_answer': name_value,
        'level_answer': level_value,
        'ingredients_answer': ingredients_value,
        'time_answer': time_value,
        'steps_answer': steps_value,
        'notes_answer': notes_value
        }

        self.response.write(template.render(displayed_recipe))

app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/new_recipe', NewRecipeHandler),
  ('/results', ResultsHandler),
  ('/search', SearchHandler),
  ('/recipe_results', RecipeResultsHandler),
  ('/display', DisplayRecipeHandler),
], debug=True)
