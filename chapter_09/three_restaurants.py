class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    #
    def describe_restaurant(self):
        print(f'{self.restaurant_name} is the best restaurant in the world! And it has the sorts of {self.cuisine_type}')

    #
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')

#
restaurant = Restaurant("Billy's Restaurant'", "Manmade material")

# Show restaurant's name
print(restaurant.restaurant_name)

# Show cuisine type
print(restaurant.cuisine_type)

# Instances

# 1.
your_restaurant = Restaurant("Jason's Restaurant'", "Not-so-good-food")

# 2.
their_restaurant = Restaurant("Trash's bin", "A lot of trash food")

# 3.
spong_bob_restaurant = Restaurant("Siri Casc", "very high quality food")

# Calling each Instances
print('\n')
your_restaurant.describe_restaurant()
their_restaurant.describe_restaurant()
spong_bob_restaurant.describe_restaurant()
