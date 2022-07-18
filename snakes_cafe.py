print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

# initialize empty meal dictionary

# start loop here until user enters quit


# create variable to store user response
order = input('> ')

# print out response of order
num_items = 1 # TODO properly tally items that haven't been ordered
response = f"** {num_items} order of {order} have been added to your meal **"

print(response)

order = input('> ')

print(order)

# end loop when user quits
