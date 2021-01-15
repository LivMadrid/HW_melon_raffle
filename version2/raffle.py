"""Randomly pick customer and print customer info"""

# Add code starting here
import random
#import both random and customers to process through customers.txt and pick a random winner
from customers import get_customers_from_file

def pick_winner(customers):
    """Choose a random winner from list of customers."""
#  copied code from raffle version one 
    chosen_customer = random.choice(customers)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))



def run_raffle():
    """Run the weekly raffle."""
    print("in run raffle fucntion")
    customers = get_customers_from_file("customers.txt")
    print("customers")
    pick_winner(customers)

# Hint: remember to import any functions you need from
# other files or libraries


# I did not realize we had to put this here---- tried to get function to run
#but it wasn't working so looked at solution to see what was different.... 
#running this to see if it changes...
if __name__ == "__main__":
    run_raffle()

# #(env) vagrant@vagrant:~/src/homework/melon-raffle$ 
# (env) vagrant@vagrant:~/src/homework/melon-raffle$ python3 raffle.py
# (env) vagrant@vagrant:~/src/homework/melon-raffle$ python3 -i  raffle.py
# >>> pick_winner(customers)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'customers' is not defined
# >>> pick_winner('customers.txt')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "raffle.py", line 47, in pick_winner
#     chosen_customer = random.choice(customers)
# AttributeError: 'builtin_function_or_method' object has no attribute 'choice'
# >>>      Maybe I am too tired.... why am I getting this error???


# #Turns out I was just exhausted and entering the wrong file into python3
# (env) vagrant@vagrant:~/src/homework/melon-raffle/version2$ 
# (env) vagrant@vagrant:~/src/homework/melon-raffle/version2$ python3 customers.py
# (env) vagrant@vagrant:~/src/homework/melon-raffle/version2$ python3 -i customers.py
# >>> run_raffle()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'run_raffle' is not defined
# >>> 
# (env) vagrant@vagrant:~/src/homework/melon-raffle/version2$ python3 raffle.py
# in run raffle fucntion
# customers
# Tell Pamela Fletcher at tempus@lectus.co.uk that they've won?