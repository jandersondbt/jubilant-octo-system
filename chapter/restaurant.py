class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  # describe the restaurant (name and cuisine type)
  def describe_restaurant(self):
    print(f"{self.restaurant_name} is the best restaurant in the world! And its catalog includes a lot of {self.cuisine_type} food")

  # say if the restaurant is open
  def open_restaurant(self):
    print(f"{self.restaurant_name} is open!")

# Make an instance called restaurant
restaurant = Restaurant("Burguer Shot", "trash")

# 1. attribute
print(restaurant.restaurant_name)

# 2. attribute 
print(restaurant.cuisine_type)

  
