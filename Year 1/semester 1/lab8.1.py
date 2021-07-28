class Animal:
    
    def __init__(self, kind = "", name = "", color = "", features = []):
        self.kind = kind
        self.name = name
        self.color = color
        self.features = features
        os.system('cls' if os.name == 'nt' else 'clear')
print('dadasda')
        
    def get_kind(self):
        print(self.kind)
        
    def get_name(self):
        print(self.name)
    
    def get_color(self):
        print(self.color)
        
    def get_features(self):
        print(self.features)
        
    def set_kind(self,x):
        self.kind = x
    
    def set_name(self,x):
        self.name = x
    
    def set_color(self,x):
        self.color = x
    
    def set_features(self,x):
        self.features = x
        
# dog = Animal()

# dog.kind = "dog"
# dog.set_name("max")
# dog.color = "brown"
# print(dog.kind)
# dog.get_name()
# dog.get_color()

# cat = Animal("cat","ruby","white")
# print(cat.kind)
# cat.get_name()
# cat.get_color()

animals = []
n_animals = int(input("enter number of animals: "))
for i in range(n_animals):
    k = input("enter kind of animal: ")
    n = input("enter name of animal: ")
    c = input("enter color of animal: ")
    j = 0
    f = []
    print("Features of animals... enter 0 to cancel")
    while True:
        j += 1
        temp_f = input(f"enter feature no.{j} of animal: ")
        if temp_f == "0":
            break
        else:
            f.append(temp_f)           
    obj = Animal(k,n,c,f)
    animals.append(obj)

for i in range(n_animals):
    animals[i].get_kind()
    animals[i].get_name()
    animals[i].get_color()
    animals[i].get_features()
