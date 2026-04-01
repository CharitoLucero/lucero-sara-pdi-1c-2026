'''
   Profe no tuve ningun problema con la clonacion de los repo... mi tema fue el tiempo. Mi maquina se puso lenta
   Fue mi error querer ejecutar mientras copiaba el resto para optimizar el tiempo. Al final fue peor.
   Para la prox no lo vuelvo a hacer, y espero al tiempo de ejecucucion para seguir con el resto de las tareas.

   El codigo se entiende y es facil de seguir.Continuo analzando para terminar con el trabajo.
'''





import py5

img = None

def setup():
    global img
    py5.size(800, 400) #ajusta el tamaño de la ventana para mostrar la imagen y la lupa
    img = py5.load_image("img/images.jpg")  # Usá una imagen disponible en tu carpeta img/
    img.resize(400, 400)

def draw():
    py5.background(255)

    # Mostrar la imagen en la mitad izquierda
    py5.image(img, 0, 0)

    # Limitar las coordenadas del mouse al área de la imagen
    # Esto evita errores si el cursor sale de la imagen
    mx = py5.constrain(py5.mouse_x, 0, 399)
    my = py5.constrain(py5.mouse_y, 0, 399)


    #Sin protección:
    # mx = py5.mouse_x
    # my = py5.mouse_y

 # ¿Qué mensaje de error aparece en la terminal? ¿Qué tipo de error es?
    '''
    No se si habre hecho algo mal, pero no me aparece ningun msj en la terminal
    '''


# Obtener el color del píxel en esa posición
    color_pixel = py5.get_pixels(int(mx), int(my))

    # Separar el color en sus tres canales
    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    # Mostrar el color como un cuadrado en la mitad derecha (la "lupa")
    # py5.fill(color_pixel)

    # #Color negativo:
    py5.fill(255 - r, 255 - g, 255 - b)
    #¿Qué color aparece sobre un rojo puro? ¿Y sobre el blanco?
    '''
    Sobre el color rojo puro aparece un color celeste grisaceo
    Sobre el blanco grises oscuros casi negro

    '''

    # #Aislamiento de canal:
    # py5.fill(r, 0, 0)

    '''
       Ahora la imagen me muestra escalas de color del rojo
       Donde es blanco se muestra rojo inenso
    '''

    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    # Mostrar los valores numéricos
    py5.fill(0)
    py5.text_size(18)
    py5.text(f"Posición: ({mx}, {my})", 450, 30)
    py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)

py5.run_sketch()

