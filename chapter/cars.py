def make_car(manufacturer, model, **more_info):
    """Return information about a car"""
    return manufacturer, model, more_info

# Calling the function
print(make_car('subaru', 'outback', turbo='True', color='Blue', lts_support='True'))
