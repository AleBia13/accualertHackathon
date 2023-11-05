from ._anvil_designer import ProductsTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Products(ProductsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.repeating_panel_locations.items = anvil.server.call('get_locations')

  def add_location_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(self.text_box_1.text)
    if(str(self.text_box_1.text) != "" and (self.text_box_2.text) != ""):
      isFound = app_tables.locations.get(Name=str(self.text_box_1.text))
      items =  self.repeating_panel_locations.items
      if isFound is None :
        row = app_tables.locations.add_row(Name=str(self.text_box_1.text),
                                  Address=str(self.text_box_2.text),
                                          Latitude = 0,
                                          Longitude= 0)
      else:
        alert("Location is already in the database", title="An error has occurred")
      isAdded = app_tables.locations.get(Name=str(self.text_box_1.text))
      if isAdded is not None:
        self.repeating_panel_locations.items = anvil.server.call('get_locations')
      else:
        alert("Cannot add location", title="An error has occurred")
    else:
      alert("Please enter all values", title="An error has occurred")
    pass
