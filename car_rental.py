# car_rental.py
import datetime
import random

class CarRental:
    def __init__(self, stock=10):
        """Initialize car rental with default or specified stock"""
        self.stock = {
            'hourly': stock,
            'daily': stock,
            'weekly': stock
        }
        self.rental_history = []

    def display_available_cars(self):
        """Display available cars for each rental type"""
        print("\n--- Available Cars ---")
        for rental_type, count in self.stock.items():
            print(f"{rental_type.capitalize()} Rental: {count} cars available")

    def rent_car(self, request_type, num_cars, customer):
        """Rent cars based on rental type"""
        if num_cars <= 0:
            print("Number of cars should be positive.")
            return False

        if num_cars > self.stock[request_type]:
            print(f"Sorry, only {self.stock[request_type]} {request_type} cars available.")
            return False

        # Update stock and record rental
        self.stock[request_type] -= num_cars
        rental_record = {
            'customer_id': customer.customer_id,
            'customer_name': customer.name,
            'rental_type': request_type,
            'num_cars': num_cars,
            'start_time': datetime.datetime.now()
        }
        self.rental_history.append(rental_record)
        
        # NEW: Display customer ID when renting
        print(f"{num_cars} {request_type} car(s) rented successfully.")
        print(f"Your Customer ID is: {customer.customer_id}")
        print("Please save this ID for returning the car.")
        
        return True

    # Rest of the code remains the same as previous implementation
    def return_car(self, customer, request_type, num_cars):
        """Process car return and generate bill"""
        # Find the matching rental record
        rental_record = next(
            (record for record in self.rental_history 
             if record['customer_id'] == customer.customer_id and 
             record['rental_type'] == request_type and 
             record['num_cars'] == num_cars), 
            None
        )

        if not rental_record:
            print("No matching rental found.")
            return False

        # Calculate rental duration and bill
        end_time = datetime.datetime.now()
        rental_duration = end_time - rental_record['start_time']

        # Rate calculation (in Indian Rupees)
        rates = {
            'hourly': 100,   # ₹100 per hour
            'daily': 1000,   # ₹1000 per day
            'weekly': 5000   # ₹5000 per week
        }

        if request_type == 'hourly':
            bill = rates['hourly'] * rental_duration.total_seconds() / 3600
        elif request_type == 'daily':
            bill = rates['daily'] * rental_duration.days
        else:  # weekly
            bill = rates['weekly'] * (rental_duration.days // 7)

        # Update stock
        self.stock[request_type] += num_cars
        self.rental_history.remove(rental_record)

        # Print bill
        print("\n--- Rental Bill ---")
        print(f"Customer: {customer.name}")
        print(f"Customer ID: {customer.customer_id}")
        print(f"Rental Type: {request_type}")
        print(f"Number of Cars: {num_cars}")
        print(f"Rental Duration: {rental_duration}")
        print(f"Total Bill: ₹{bill:.2f}")

        return True