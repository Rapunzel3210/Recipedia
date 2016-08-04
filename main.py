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
        new_ingredients_value=self.request.get('new_ingredients')
        time_value=self.request.get('time')
        steps_value=self.request.get('steps')
        notes_value=self.request.get('notes')

        new_recipe = {

        'author_answer': author_value,
        'name_answer': name_value,
        'level_answer': level_value,
        'new_ingredients_answer': new_ingredients_value,
        'time_answer': time_value,
        'steps_answer': steps_value,
        'notes_answer': notes_value
        }
        recipe_record = Recipe(author=author_value, recipe_name=name_value, level=level_value, new_ingredients=new_ingredients_value, time=time_value, steps=steps_value, notes=notes_value)
        recipe_key = recipe_record.put()

        self.response.write(template.render(new_recipe))

class Recipe(ndb.Model):
    author = ndb.StringProperty(required=True)
    recipe_name = ndb.StringProperty(required=True)
    level = ndb.StringProperty(required=True)
    new_ingredients = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    steps = ndb.StringProperty(required=True)
    notes = ndb.StringProperty(required=True)

    @classmethod #This should work as a search
    def query_recipe(cls, level_value):
        return cls.query(level=level_value)


class RecipeResultsHandler(webapp2.RequestHandler):
    GREETINGS_PER_PAGE = 20
    def get(self):
        level = self.request.get('level')
        recipes = Recipe.query().filter(Recipe.level==level).fetch(
            self.GREETINGS_PER_PAGE)

        self.response.out.write('<html><body>')

        for recipe in recipes:
            self.response.out.write(
                '<a href="/get?name=%s">%s</a>' % (recipe.recipe_name, recipe.recipe_name))

        self.response.out.write('<p><a href="/search"><input type="button" name="button" value="Search For Another Recipe"></a></p>')
        self.response.out.write('<p><a href="/"><input type="button" name="button" value="Back to Home Page"></a></p>')

        self.response.out.write('</body></html>')

# class DisplayRecipeHandler(webapp2.RequestHandler):
#
#     def get(self):
#         template = jinja_environment.get_template('templates/display_recipe.html')
#
#         displayed_recipe = {
#
#         'author_answer': Recipe.author,
#         'name_answer': Recipe.name,
#         'level_answer': Recipe.level,
#         'new_ingredients_answer': Recipe.new_ingredients,
#         'time_answer': Recipe.time,
#         'steps_answer': Recipe.steps,
#         'notes_answer': Recipe.notes
#         }
#
#         self.response.write(template.render(displayed_recipe))

app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/new_recipe', NewRecipeHandler),
  ('/results', ResultsHandler),
  ('/search', SearchHandler),
  ('/recipe_results', RecipeResultsHandler),
], debug=True)
