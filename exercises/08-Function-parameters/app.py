# Your code goes here:
def render_person(nombre, fecha_nacimiento, color_ojos, edad, genero):
    return f"{nombre} is a {edad} years old {genero} born in {fecha_nacimiento} with {color_ojos} eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))