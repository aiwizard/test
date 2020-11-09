class Person: 
    def __init__(self, name, age, phone): 
        self.name = name 
        self.age = age 
        self.phone = phone 
    
    def __str__(self): 
        s = f'이름: {self.name}\n' 
        s += f'나이: {self.age}, 전화번호: {self.phone}' 
        return s 
        
    # def show_info(self): 
    #   print(f'이름: {self.name}') 
    #   print(f'나이: {self.age}, 전화번호: {self.phone}') 

king = Person('세종', '23', '010-1234-1234')
print(king)
