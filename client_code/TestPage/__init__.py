from ._anvil_designer import TestPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def LoadColab_click(self, **event_args):
    """This method is called when the button is clicked"""
     # Call the google colab function and pass it the iris measurements
    iris_category = anvil.server.call('predict_iris')
    # If a category is returned set our species 
    if iris_category:
      self.label_1.visible = True
      self.label_1.text = "The species is " + iris_category.capitalize()
