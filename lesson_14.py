# 1. Modify the Country class to include a third instance attribute called capital as a string. 
# Store your new class in a script and test it out by adding the following code at the bottom of the script:
# ```
# japan = Country('Japan', 140_000_000, 'Tokyo')
# print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
# ```
# The output of your script should be:

# Japan population is 140000000 and capital is Tokyo.

# 2. Add increase_population method to country class. This method should take an argument and increase population of the country on this number.

# Create add method to add two countries together. 
# This method should create another country object with the name of the two countries combined and population 
# of the two countries added together.

#bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)

# bosnia_herzegovina = bosnia.add(herzegovina)
# bosnia_herzegovina.population -> 15_000_000
# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

# (Optional) Implement previous method with magic method 

class Country:
    def __init__(self, name, population, capital = ''):
        self.name = name
        self.population = population
        self.capital = capital

    def increase_population(self,arg):
        return self.population + arg
    
    def __str__(self):
        return f"{self.name} population is {self.population} and capital is {self.capital}."
    
    def __add__(self, second):
        return Country(self.name + " " + second.name , self.population + second.population)
    
    def add(self, second):
        return Country(self.name + ' ' + second.name, self.population + second.population)
    
japan = Country('Japan', 140_000_000, 'Tokio') 

print(japan)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population, bosnia_herzegovina.name)





