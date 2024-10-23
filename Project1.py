# Let's rewrite the code to allow user input for each part of the madlib.

def madlib_user_input():
    # Getting inputs from the user
    adjective = input("Enter an adjective: ")
    large_objects_plural = input("Enter a large object (plural): ")
    body_part = input("Enter a body part: ")
    restaurant = input("Enter the name of a restaurant: ")
    food1 = input("Enter a type of food: ")
    food2 = input("Enter another type of food: ")
    large_object_singular = input("Enter a large object (singular): ")
    
    # Returning the madlib with the user inputs
    return f"""I’ve had a very {adjective} day.
This morning, I dropped a box of {large_objects_plural} on my {body_part}.
Then, at lunch, I went to {restaurant} for their delicious {food1},
But the waiter brought me {food2}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {large_object_singular} strapped to the roof."""

print (madlib_user_input())

