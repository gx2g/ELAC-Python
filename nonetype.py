
# how to check none type in python
# Using is operator
# using Assignment Operator
# using type() method
# using if condition



x = None
# x = " " test empty str considered falsy which is a bool value

#using the (is) operator 
if x is None:
    print(x)
    print(type(x))
else:
    print("X is not None.")

# using the assignment operator
if x==None:
    print("The result is None.")
else:
    print("The result is not None.")

# using the type() method
if type(x)==type(None):
    print("The variable is of NoneType.")
else:
    print("The variable is not of NoneType.")

# using the if condition, if None is considered falsy
if None:
    print(0)
else:
    print(10)

# Understanding how none behaves in Conditionals is important
# In python, serveral values are considered falsy:


# 'None'
# 'False'
# Zero of any numeric  type (0, 0.0, 0j)
# Empty sequences and collections ('', [], {})
# Objects where 'len(obj)' returns 0
# Objects that defeind '__bool__()' to return 'False'
# None is a singleton object 

type(none)

# Best Practice 
# Use explicit comparisons with None when checking for None specifically

# Be aware of the difference between None and other falsy values in your logic.
# Use type hints and proper documentation to clarify when a function might return None.

