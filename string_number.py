print("100 is a great number")
print(2)
print(2.7)
print(-8)
print(20*24*60)
print(f"20 days are {24*60} minutes.")# you can use this '{}' if u have installed python3 otherwise write like below line
print("20 days are " + str(50) + " minutes") #concatenation
#VARIABLES are containers for storing values.
conversion_to_seconds = 24*60*60
name_of_unit = "seconds"
print(f' 20 days are {20*conversion_to_seconds} {name_of_unit}')
print(f" 20 days are {40*conversion_to_seconds} {name_of_unit}")
print(f'30 days are {30*conversion_to_seconds} seconds')
#A FUNCTION is defined using the def keyword and block of codes which only runs when it is called.
#calling a function = execute the function

def days_to_units():
    print(f"2 days are {2*conversion_to_seconds} {name_of_unit}")
    print("Alright!")
days_to_units()
def programming():
    print("Programming is literally enjoyable.")
programming()
#PARAMERERS: Informations can be passed into functions as parameters and parameters are also called arguments
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*conversion_to_seconds} {name_of_unit}")
days_to_units(8)