def make_sandwich(*items):
    print('=== SUMMARY ===')
    for item in items:
        print(f'- {item}')
#
make_sandwich('burguer', 'meat', 'salad', 'tomato', 'cheese')

#
print('\n')
make_sandwich('meat', 'salad', 'tomato')

#
print('\n')
make_sandwich('meat', 'salad')
