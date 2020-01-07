class MakeMeal:
    def prepare(self):pass
    def cook(self): pass
    def eat(self): pass    
    def go(self):
        self.prepare()
        self.cook()        
        self.eat()
class MakePizza(MakeMeal):
    def prepare(self):
        print ("Prepare pizza!")
    def cook(self):
        print("cook pizza")
    def eat(self):
        print("eat pizza")
makePizza=MakePizza()
makePizza.go()