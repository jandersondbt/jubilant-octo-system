def make_shirt(size, message):
    return f"Shirt size: {size} \nMessage on shirt: {message}"

# Using positional arguments
print(make_shirt('G', 'NoctoruneP41\n'))

# Using keyword arguments
print(make_shirt(size='G', message='NoctoruneP41'))
