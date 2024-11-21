#Customer Module

import random

#Class Customer
class Customer:
    def __init__(self, name):
        """Initialize customer with a unique ID"""
        self.name = name
        self.customer_id = self.generate_customer_id()

    def generate_customer_id(self):
        """Generate a unique customer ID"""
        return random.randint(1000, 9999)