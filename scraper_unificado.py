import requests
from bs4 import BeautifulSoup
import pandas as pd


def  main(url):
    links_secciones = _obtener_secciones(url)
    notas = _obtener_notas(links_secciones)
    data = _obtener_data(notas)
    _save_data(data)

def _obtener_secciones(url):
    request = requests.get(url)
    
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        secciones = soup.find('ul', attrs={'class': 'hot-sections'}).find_all('li')
        links_secciones = [seccion.a.get('href') for seccion in secciones]

    return links_secciones


def _obtener_notas(links_secciones):
    notas = []
    for link in links_secciones:
        try:
            r = requests.get(link)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                notas.extend(__obtener_urls_notas(soup))
            else:
                print('No se pudo obtener la seccion', link)
        except:
            print('No se pudo obtener la seccion', link)

    return notas


def __obtener_urls_notas(soup):
    '''
    Funcion que recibe un objeto de BeautifulSoup de una pagina 
    de una seccion y devuelve una lista de urls a las notas de esa seccion.
    '''
    lista_notas = []

    # Obtengo el articulo promocionado
    featured_article = soup.find(
        'div', attrs={'class': 'featured-article__container'})
    if featured_article:
        lista_notas.append(featured_article.a.get('href'))

    # Obtengo el listado de los articulos
    article_list = soup.find('ul', attrs={'class': 'article-list'})

    for article in article_list.find_all('li'):

        if article.a:
            lista_notas.append(article.a.get('href'))

    return list(set(lista_notas))


def _obtener_data(notas):
    data = []

    for i, nota in enumerate(notas):
        print(f'Scrapeando nota {i}/{len(notas)}')
        data.append(__scrape_nota(nota))
    return data


def __scrape_nota(url):
    try:
        nota = requests.get(url)
    except Excepton as e:
        print(f'Error scrapeando ULR {url}')
        print(e)
        return None

    if nota.status_code != 200:
        print('fError obteniendo nota {url}')
        print(f'Status code = {nota.status_code}')
        return None

    s_nota = BeautifulSoup(nota.text, 'html.parser')

    ret_dict = __obtener_info(s_nota)
    ret_dict['url'] = url

    return ret_dict


def __obtener_info(s_nota):
    # Creamos un diccionario vacio para probarlo con la informacion
    ret_dict = {}

    # Extraemos la fecha
    fecha = s_nota.find('span', attrs={'pubdate': 'pubdate'})
    if fecha:
        ret_dict['fecha'] = fecha.get('datetime')
    else:
        ret_dict['fecha'] = None

    # Extraemos el titulo
    titulo = s_nota.find('h1', attrs={'class': 'article-title'})
    if titulo:
        ret_dict['titulo'] = titulo.text
    else:
        ret_dict['titulo'] = None

    # Extraer la volanda
    volanta = s_nota.find('h2', attrs={'class': 'article-prefix'})
    if volanta:
        ret_dict['volanta'] = volanta.get_text()
    else:
        ret_dict['volanta'] = None

    # Extraer copete
    copete = s_nota.find('div', attrs={'class': 'article-summary'})
    if copete:
        ret_dict['copete'] = copete.get_text()
    else:
        ret_dict['copete'] = None

    # Extraer autor
    autor = s_nota.find('div', attrs={'class': 'article-author'})
    if autor:
        ret_dict['autor'] = autor.get_text()
    else:
        ret_dict['autor'] = None

    # Extraer imagen
    media = s_nota.find('div', attrs={'class': 'article-main-media'})
    if media:
        imagenes = media.find_all('img')
        if len(imagenes) == 0:
            print('no se encontraron imagenes')
        else:
            imagen = imagenes[-1]
            img_src = imagen.get('data-src')
            try:
                img_req = requests.get(img_src)
                if img_req.status_code == 200:
                    ret_dict['imagen'] = img_req.content
                else:
                    ret_dict['imagen'] = None
            except:
                print('No se pudo obtener la imagen')
    else:
        print('No se encontro media')

    # Extraerel  cuerpo
    cuerpo = s_nota.find('div', attrs={'class': 'article-text'})
    if cuerpo:
        ret_dict['cuerpo'] = cuerpo.get_text()
    else:
        ret_dict['cuerpo'] = None

    return ret_dict


def _save_data(data):
    df = pd.DataFrame(data)
    df.to_csv('Notas_pagina12.csv')
        
    return df


if __name__ == "__main__":
    url = 'https://www.pagina12.com.ar/'
    main(url)


