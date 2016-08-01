import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class NewRecipeHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/new_recipe.html')

        self.response.write(template.render())



    def post(self):
        template = jinja_environment.get_template('templates/recipe_list.html')
        author_value=self.request.get('author')
        name_value=self.request.get('name')
        level_value=float(self.request.get('level'))
        

app = webapp2.WSGIApplication([
  ('/', NewRecipeHandler),
], debug=True)