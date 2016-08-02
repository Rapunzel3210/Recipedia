import jinja2
import os
from google.appengine.ext import ndb
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class NewRecipeHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/new_recipe.html')

        self.response.write(template.render())



    def post(self):
        template = jinja_environment.get_template('templates/results.html')
        author_value=self.request.get('author')
        name_value=self.request.get('name')
        level_value=float(self.request.get('level'))
        new_recipe = {

        'author_answer': author_value,
        'name_answer': name_value,
        'level_answer': level_value,
        }
        recipe_record = Recipe(author=author_value, recipe_name=name_value, level=level_value)
        recipe_key = recipe_record.put()

        self.response.write(template.render(new_recipe))

class Recipe(ndb.Model):
    author = ndb.StringProperty(required=True)
    recipe_name = ndb.StringProperty(required=True)
    difficulty = ndb.StringProperty(required=True)

app = webapp2.WSGIApplication([
  ('/', NewRecipeHandler),
], debug=True)
