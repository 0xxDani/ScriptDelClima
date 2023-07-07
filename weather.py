'''EJEMPLO:    SIMPLEMENTE ESCRIBIR EL LUGAR
**************************************************************************
copacabana-ant (Si no se añade -ant nos lleva a rio de janeiro - Brasil)
bello
guarne
amaga
medellin
barranquilla
new york
berlin
pekin
kampala
canberra
**************************************************************************
             FUNCIONA EN TODO EL MUNDO
'''
import requests

def main():
    #dosctring
    '''
    🦉                                    🦉
    ESTA FUNCIÓN TOMA EL CLIMA DE UNA CIUDAD
    Y NOS DEVUELVE UNA ESPECIE DE GRÁFICA EN
    DONDE NOS ESPECIFICA LA INFORMACIÓN
    EN VISUAL STUDIO O EN EL MISMO AMBIENTE
    VIRTUAL SE VE MUY BIEN!
    🦉                                    🦉
    '''
    city = input("Escoge la ciudad: ")

    # SE CONSTRUYE LA URL DEL SERVICIO DE PRONÓSTICO DEL TIEMPO USANDO LA CIUDAD PROPORCIONADA.
    url = f'https://wttr.in/{city}'

    # SE REALIZA UNA PETICIÓN GET A LA URL PARA OBTENER EL PRONÓSTICO DEL TIEMPO.
    weather = requests.get(url).text
    print(weather)

if __name__ == '__main__':
    main()
