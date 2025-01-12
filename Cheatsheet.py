# Komente dhe printime 

# Ky është një koment  (#)
#ky eshte nje printim ne ekran (print)
print("Përshëndetje!")  

# VARIABLAT (int / float / str / chr / bool / list)
product_name: str = "Pizza"
person_gender : chr(1) = "M"
product_price: float = 2.6  
person_age: int = 27  
is_free_product: bool = True
products : list[str] = ["Rizoto", "Pasta", "Patato"]

print(f"Produkti: {product_name}, Çmimi: {product_price}")

# leximi nga tastiera (input)
name: str = input("Si quheni? ")  
print(f"Miresevini {name}!")  

# Veprime aritmetike  (+ - * /)
x: int = 2  
y: int = 5  
print(f"Shuma: {x + y}, Diferenca: {x - y}, Prodhimi: {x * y}, Pjesëtimi: {x / y}")  

# KUSHTET  (if / elif / else)
if x > y:  
    print("x është më i madh se y")
elif x == y:
    print" x eshte i barabarte me y")
else:  
    print("x nuk është më i madh se y")  

# Krahasimet  (>, <, >=, <=, ==, !=)
if x == y:
    print("x dhe y janë të barabartë")  
if x != y:
    print("x dhe y janë të ndryshëm")  

# LIDHJET LOGJIKE (and / or / not)
has_money: bool = True  
has_card: bool = False  
if has_money and not has_card:  
    print("Paguaj me para")
print("Hello")
