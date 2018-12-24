class Dog:
    def __init__(self,color,height,weight):
        self.color = color
        self.height = height
        self.weight = weight

    def sound(self):
        print ("wow wow")

    def eat(self):
        print ("I eat bones")

class BabyDog(Dog):

    '''
    Method over-riding. Here sound method in parent class is over-ridden by the chilld method sound. Thus any baby dog object
    will only sound like weep weep
    '''
    def sound(self):
        print ("weep weep")

cute_dog = BabyDog('brown', 2,6)
cute_dog.sound()
cute_dog.eat()