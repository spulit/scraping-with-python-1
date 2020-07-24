from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Equipos

equiposFromPage = soup.find_all('span', class_='nombre-equipo')

equipos = list()

for equipo in equiposFromPage:
    if (not equipos.__contains__(equipo.text)):
        equipos.append(equipo.text)

print(equipos)
print(equipos.__len__())

# Puntuación

puntuacionFromPage = soup.find_all('td', class_='destacado')

puntuaciones = list()

contador = 0
for puntuacion in puntuacionFromPage:

    if (not puntuaciones.__contains__(puntuacion.text)) & (contador < 20):
        puntuaciones.append(puntuacion.text)
        contador += 1

print(puntuaciones)
print(puntuaciones.__len__())

datos = pd.DataFrame({'Nombre': equipos, 'Puntos': puntuaciones})
datos.to_csv('Clasificacion.csv', index=False)
print(datos)

