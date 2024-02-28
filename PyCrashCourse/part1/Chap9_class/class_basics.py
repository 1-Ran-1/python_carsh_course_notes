# Creating and Using a Class

# dog class sample

class Dog:
    """
    A simple attempt to model a dog.
    """
    
    def __init__(self, name, age):
        """
        Initialize name and age attributes.
        """
        self.name = name
        self.age = age
    
    def sit(self):
        """
        Simulate a dog sitting in response to a command.
        """
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """
        Simulate rolling over in response to a command.
        """
        print(f"{self.name} rolled over!")
    
# ================================================

# __init__() Method

# the __init__() method is a special method
# that Python runs automatically whenever we
# create a new instance based on the Dog Class.

#  3 params
# self : required in the method definition, must come first
#       Because when Python calls this method later (to create an instance)
#       the method will automatically pass the 'self' arg

#       'self' is a reference to the instance itself.
#           give individual instance access to attributes / methods in Class

# variables prefixed with 'self' is available to every method in the class

# =================================================

# Making an Instance from a Class

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
# instance_name.method_name(args..)
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
your_dog = Dog('Lucy', 3)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

# Note EVEN IF use SAME name and age for second dog.
# Python would still create a seperate instance.