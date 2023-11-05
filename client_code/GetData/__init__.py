from ._anvil_designer import GetDataTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class GetData(GetDataTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.googleMap.center = GoogleMap.LatLng(45.9442858,25.0094303)
    self.googleMap.zoom = 5
    self.locationDropdown.items = [(row["Name"], row) for row in app_tables.locations.search()]
    # Any code you write here will run before the form opens.

  def LoadColab_click(self, **event_args):
    """This method is called when the button is clicked"""
     # Call the google colab function and pass it the iris measurements
    self.soilTempImg.visible = true
    # If a category is returned set our species 
  def addressLabel_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    address = self.text_box_1.text
    results = GoogleMap.geocode(address)
    m = Marker(position=results[0].geometry.location)
    map.add_component(m)