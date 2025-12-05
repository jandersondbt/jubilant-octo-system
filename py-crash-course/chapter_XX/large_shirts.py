def make_shirt(size='L', message='I love Python'):
    return f"Shirt size: {size} \nMessage on shirt: {message}"

# Large shirt; default message
print(make_shirt())

# Medium size; default message
print(make_shirt('M'))

# Any size; any message
print(make_shirt('G', 'NoctoruneP51'))
