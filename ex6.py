# set the amount of types of people
types_of_people = 10
# string stating the amount of types of people
x = f"There are {types_of_people} types of people."

# set string binary to var
binary = "binary"
# set string don't to var do_not
do_not = "don't"
# set string with variables binary and do_not
y= f"Those who know {binary} and those who {do_not}."

# print result of x and y
print(x)
print(y)

# print string with result of x and y
print(f"I said: {x}")
print(f"I also said: '{y}'.")

# set hilarious to false
hilarious = False
# set var to a formatable string
joke_evaluation = "Isn't that joke so funny?! {}"

# print formatted string with variable hilarious
print(joke_evaluation.format(hilarious))

# set w and e to strings
w = "This is the left side of..."
e = "a string with a right side."

# print w and e concatenated
print(w + e)
