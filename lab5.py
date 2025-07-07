# lab 5 Oliver

#step 1
def cat_greeting(word):
    print(f'cat says {word}')
    print('dog say woof')

cat_greeting("meow")

#step 2
def generate_super_power():
    name = "John"
    power = "flying"
    print(f"{name}'s power is {power}")

generate_super_power()

#step 3
def generate_super_power1():
    power = "flying"
    return power

print(generate_super_power1())

#step 4
def generate_super_power2(user_name, super_power):
    message = user_name + " has a power of" + super_power + "!"
    return message

print(generate_super_power2("oliver", " shape shift"))

#step 5
def cat_greeting_loop(greeting):
    greeting = "meow"
    for i in range(0,5):
        print(f'the cat says {greeting}')

cat_greeting_loop("meow")

#step 6
def generate_multiple_powers(powers):
    for i in powers:
        print(i)

powers_test = ["teleport", "shape shift", "flying", "invisibility"]
generate_multiple_powers(powers_test)
