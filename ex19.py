# define cheese and cracker function to print out line of string base off of args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print string base off of frist arg cheese_count
    print(f"You have {cheese_count} cheeses!")
    # print string base off of second arg boxes_of_crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# pass intergers into function cheese_and_crackers to print strings
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# define two variables with intergers
amount_of_cheese = 10
amount_of_crackers = 50

# pass variables into cheese_and_crackers function to print strings
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# pass calculation of integers into cheese_and_crackers function to print strings
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# pass a calculation of integer and variable into function cheese_and_crackers to print strings
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
