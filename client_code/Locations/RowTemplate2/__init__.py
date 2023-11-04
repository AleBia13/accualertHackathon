from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def deleteButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    var = confirm(f"Are you sure you want to delete {self.item['Name']}?")
    if var is True:
        self.remove_from_parent()
        row = self.item
        anvil.server.call('delete_location',row)
    pass
