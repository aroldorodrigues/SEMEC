import pandas as pd
import folium
import webbrowser
from escolas_conectadas_app import limites_girau
from escolas_conectadas_app import geoescolas

def mapa ():
    var = geoescolas.dados
    lim = limites_girau.limites_girau
    # Coordenadas do centro de Girau do Ponciano
    centro_girau = [-9.796336411128157, -36.83646846282193]

    # Criando o mapa com o centro em Girau do Ponciano
    mapa = folium.Map(location=centro_girau, zoom_start=11)

    # Adicionando polígono para os limites de Girau do Ponciano
    folium.Polygon(
        locations=lim,
        color='green',
        fill=True,
        fill_color='yellow',
        fill_opacity=0.1
    ).add_to(mapa)

    # Adicionando marcadores para os locais
    for index, local in pd.DataFrame(var).iterrows():
        folium.Marker(
         icon=folium.Icon(color='green'),
         location=[local['Latitude'], local['Longitude']],
        popup=local['Nome']
     ).add_to(mapa)

    # Salvando o mapa como um arquivo HTML
    mapa.save('mapa_girau_do_ponciano_com_limites.html')

    # Abrindo automaticamente o mapa no navegador padrão
    webbrowser.open('mapa_girau_do_ponciano_com_limites.html')