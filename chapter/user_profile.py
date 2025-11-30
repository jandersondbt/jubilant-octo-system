def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
#
user_profile = build_profile('janderson', 'candido', location='Brazil', field='NEET', skin_color='white', turbo='False')

#
print(user_profile)
