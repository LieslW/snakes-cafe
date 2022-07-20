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

# EMPTY MEAL DICTIONARY
menu_items = {
    "Wings": 0, "Cookies": 0, "Spring Rolls": 0,
    "Salmon": 0, "Steak": 0, "Meat Tornado": 0, "A Literal Garden": 0,
    "Ice Cream": 0, "Cake": 0, "Pie": 0,
    "Coffee": 0, "Tea": 0, "Unicorn Tears": 0
}

# VARIABLES
# sing_response = f"** {num_items} order of {order} has been added to your meal **"
# plur_response = f"** {num_items} orders of {order} have been added to your meal **"
customer_ticket = {}

# start loop and repeat until user enters 'quit'

while True:
    order = input('> ').capitalize()
    if order == "Quit":
        break
    elif order not in menu_items:
        print('**Sorry! We don\'t seem to carry that. Would you like to order anything else?**')
        continue
    elif order not in customer_ticket:
        customer_ticket.update({order: 0})
    customer_ticket[order] += 1
    print(f'** {customer_ticket[order]} order of {order} have been added to your meal.**')
    # else:
    # print(f'** {customer_ticket[order]} orders of {order} have been added to your meal.**')

# end/break loop when user quits

