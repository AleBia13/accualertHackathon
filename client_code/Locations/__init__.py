from ._anvil_designer import LocationsTemplate
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

class Locations(LocationsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.repeating_panel_locations.items = anvil.server.call('get_locations')

  def add_location_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    isFound = app_tables.locations.get(Name=self.text_box_1.text)
    if isFound is not None :
         row = app_tables.locations.add_row(Name=self.text_box_1.text,
                                Address=self.text_box_2.text)
    pass
