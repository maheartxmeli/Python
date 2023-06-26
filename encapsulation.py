class Encapsulated:
    def __init__(self):
        self._encapsulated1 =12 #creates a protected variable for Encapsulated class
        self.__encapsulated2 = 12 #creates a private variable for Encapsulated class

    def getEncapsulated(self):
        print(self.__encapsulated)

    def setEncapsulated(self, private):
        self.__encapsulated = private 

object = Encapsulated()
object.getEncapsulated()
object.setEncapsulated(25) #sets a new value for encapsulated
object.getEncapsulated()
