

user_input = input("Enter your input: ")
print (user_input)

name = input("Enter yout name: ")
print ("Hello, " + name + "!")
print ("Hello, {}!".format(name))

# Converting User Input
age_str = input("What is your age? ")
age = int(age_str)
dog_years = 15 + 9 + (age-2) * 5
print ("You are {} years old in dog years".format(dog_years))
