class class_1:
    score = 10
    def function_1(self):
        self.score = 5
        print(self.score)
    def function_2(self):
        print(self.score)

class Parent:
    __first_name = 'Dam'
    last_name = 'Ma'
    def __print_me(self):
        print(self.__first_name)
    def print(self):
        self.__print_me()
class child(Parent):
    score = 0
 
parent = Parent()
parent.print()
a = child()
print(a.__first_name)
