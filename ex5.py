#在print里添加可变量
my_name='Zed A.shaw'
my_age=35 # not a lie
my_height=74 # inches
my_weight= 180 # lbe
my_eye='blue'
my_teeth='white'
my_hair='brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eye} eyes and {my_teeth} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffe")

# this line is trick ,try to get it exactly right
total = my_age + my_height + my_weight 
print(f"If i add {my_age},{my_height},and  {my_weight} I get {total}.")