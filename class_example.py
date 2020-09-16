class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_info(self):
        print('Pet Information:')
        print('   Name:', self.name)
        print('   Age:', self.age)

class Dog(Pet):
    def __init__(self):
        Pet.__init__(self) 
        self.breed = ''
        
    def print_info(self):
        Pet.print_info(self)
        print('   Breed:', self.breed)
        

my_pet = Pet()
my_dog = Dog()

pet_name = input()
pet_age = int(input())
dog_name = input()
dog_age = int(input())
dog_breed = input()

# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()
generic_pet = Pet()
generic_pet.name = pet_name
generic_pet.age = pet_age

generic_pet.print_info()

# TODO: Create dog pet (using dog_name, dog_age, dog_breed) and then call print_info()
dog_pet = Dog()
dog_pet.name = dog_name
dog_pet.age = dog_age
dog_pet.breed = dog_breed
dog_pet.print_info()

# TODO: Use my_dog.breed to output the breed of the dog
