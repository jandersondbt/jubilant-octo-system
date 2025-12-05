class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    #
    def describe_restaurant(self):
        print(f'{self.restaurant_name} is the best restaurant in the world!')

    #
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')

#
restaurant = Restaurant("Billy's Restaurant'", "Manmade material")

# Show restaurant's name
print(restaurant.restaurant_name)

# Show cuisine type
print(restaurant.cuisine_type)
