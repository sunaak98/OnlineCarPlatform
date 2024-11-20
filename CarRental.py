#Complete progam made by Claude
#To be modified into OOP


import car_rental as cr
import customer as cs




#Main Function
def main():
    # Main function implementation stays the same
    rental_system = cr.CarRental()
    
    while True:
        print("\n--- Car Rental System ---")
        print("1. Display Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            rental_system.display_available_cars()
        
        elif choice == '2':
            name = input("Enter your name: ")
            customer = cs.Customer(name)
            
            print("\nRental Types:")
            print("1. Hourly")
            print("2. Daily")
            print("3. Weekly")
            
            rental_type = input("Choose rental type (1-3): ")
            rental_types = ['hourly', 'daily', 'weekly']
            
            num_cars = int(input("Enter number of cars to rent: "))
            
            rental_system.rent_car(
                rental_types[int(rental_type)-1], 
                num_cars, 
                customer
            )
        
        elif choice == '3':
            name = input("Enter your name: ")
            customer_id = int(input("Enter your customer ID: "))
            
            print("\nRental Types:")
            print("1. Hourly")
            print("2. Daily")
            print("3. Weekly")
            
            rental_type = input("Choose rental type (1-3): ")
            rental_types = ['hourly', 'daily', 'weekly']
            
            num_cars = int(input("Enter number of cars to return: "))
            
            customer = Customer(name)
            customer.customer_id = customer_id
            
            rental_system.return_car(
                customer, 
                rental_types[int(rental_type)-1], 
                num_cars
            )
        
        elif choice == '4':
            print("Thank you for using Car Rental System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()