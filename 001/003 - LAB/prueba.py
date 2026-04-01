import py5

#Prueba de instalación de py5, para crear una PIZARRA con un rectángulo rosa
def setup():
    py5.size(500, 500)
    py5.fill("#ff0080")
    py5.rect(150, 150, 200, 200)
    py5.save("/img/testing/000_intro_py5.png")


py5.run_sketch()


#No pude avanzar más por un tema de configuración de VS que no reconocio la instalacion de JAVA. No abrio la pantalla para ver lo que estaba creando.
#Pero si lo pude ver desde Simbolo de Sistema, ejecute el comando E:\>python e:/py5/prueba.py y se abrió la pantalla con el rectángulo rosa.
