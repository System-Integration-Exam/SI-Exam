from src import __version__
import unittest
from src.clients import warehouse
from src.entities.warehouse.store import Store


class TestWarehouse(unittest.TestCase):
        
    def create_store(self):
        response = warehouse.create_store(Store(
            address="some address from gateway tests", 
            phone_number="some phone number from gateway tests",
            email="some email from gateway tests"
        ))
        self.assertEqual(response,"201")
        
    
    

