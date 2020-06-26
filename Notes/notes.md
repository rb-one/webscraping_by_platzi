# Curso de Web Scraping: Extracción de Datos en la Web

## [Contenido](#contenido)

- [Curso de Web Scraping: Extracción de Datos en la Web](#curso-de-web-scraping-extracción-de-datos-en-la-web)
  - [Contenido](#contenido)
  - [Modulo 1 Introducción, definiciones y ética](#modulo-1-introducción-definiciones-y-ética)
    - [Clase 1 Introducción y definiciones](#clase-1-introducción-y-definiciones)
    - [Clase 2 Ética y Legalidad](#clase-2-ética-y-legalidad)
    - [Clase 3 Configuración del entorno de trabajo con Jupyter](#clase-3-configuración-del-entorno-de-trabajo-con-jupyter)
  - [Modulo 2 HTML: Requests y BeautifulSoup](#modulo-2-html-requests-y-beautifulsoup)
    - [Clase 4 Descargando una página web](#clase-4-descargando-una-página-web)
    - [Clase 5 Parseando HTML con BeautifulSoup](#clase-5-parseando-html-con-beautifulsoup)
    - [Clase 6 Extrayendo información](#clase-6-extrayendo-información)
    - [Clase 7 Manejo de errores](#clase-7-manejo-de-errores)
    - [Clase 8 Descargando Contenido](#clase-8-descargando-contenido)
    - [Clase 9 Descargando Multimedia](#clase-9-descargando-multimedia)
    - [Clase 10 Unificando el scraper](#clase-10-unificando-el-scraper)
  - [Modulo 3 Scraping JavaScript con Selenium](#modulo-3-scraping-javascript-con-selenium)
    - [Clase 11 Instalación y configuración de Selenium](#clase-11-instalación-y-configuración-de-selenium)
    - [Clase 12 Sitios dinámicos y Selenium](#clase-12-sitios-dinámicos-y-selenium)
    - [Clase 13 Selección de elementos](#clase-13-selección-de-elementos)
    - [Clase 14 Interactuando con los elementos](#clase-14-interactuando-con-los-elementos)
    - [Clase 15 Scrapeando escalas y tarifas](#clase-15-scrapeando-escalas-y-tarifas)
    - [Clase 16 Construyendo Funciones](#clase-16-construyendo-funciones)
    - [Clase 17 Construyendo la función para unificar el scraper](#clase-17-construyendo-la-función-para-unificar-el-scraper)
    - [Clase 18 Demoras dinámicas](#clase-18-demoras-dinámicas)
    - [Clase 19 Comentarios Finales](#clase-19-comentarios-finales)
  - [Modulo 4 APIs](#modulo-4-apis)
    - [Clase 20 Introducción a APIs](#clase-20-introducción-a-apis)
      - [Que es una API](#que-es-una-api)
      - [REST](#rest)
      - [Documentacion](#documentacion)
      - [JSON](#json)
    - [Clase 21 Utilizando APIs: construir una url](#clase-21-utilizando-apis-construir-una-url)
    - [Clase 22 Utilizando APIs: Tokens y Búsqueda](#clase-22-utilizando-apis-tokens-y-búsqueda)
    - [Clase 23 Obteniendo la Discografia](#clase-23-obteniendo-la-discografia)
    - [Clase 24 Obteniendo los albums](#clase-24-obteniendo-los-albums)
    - [Clase 25 Final del proyecto + bonus](#clase-25-final-del-proyecto--bonus)
  - [Modulo 5 Scrapy, Tesseract y Proxies](#modulo-5-scrapy-tesseract-y-proxies)
    - [Clase 26 Scrapy](#clase-26-scrapy)
    - [Clase 27 Ejecutando el scraper con scrapy](#clase-27-ejecutando-el-scraper-con-scrapy)
    - [Clase 28 Proxies](#clase-28-proxies)
    - [Clase 29 Tesseract](#clase-29-tesseract)
    - [Clase 30 Conclusion y cierre del curso](#clase-30-conclusion-y-cierre-del-curso)

## Modulo 1 Introducción, definiciones y ética

### Clase 1 Introducción y definiciones

**Web Scrapping** es el proceso de extracción de datos almacenados en la web.

**Web Crawling** es para mapear e indexar páginas web para conocer su contenido, así como hace Google y varios buscadores.

### Clase 2 Ética y Legalidad

- Estoy violando alguna reglamentación local?
- Estoy violando los "Términos y condiciones" del sitio.
- Estoy accediendo a lugares no autorizados?
- Es legal el uso que le voy a dar a los datos?

Tenemos estos articulos

<https://www.forbes.com/sites/emmawoollacott/2019/09/10/linkedin-data-scraping-ruled-legal/#66d703ba1b54>

<https://nubela.co/blog/is-linkedin-scraping-legal/>

Casi todas las paginas tienen un archivo robots.txt para darnos  las buenas practicas de obtención de esas paginas, pero no es vinculante y no hay nada que no nos permita escrapear todo el sitio. Se responsable.

### Clase 3 Configuración del entorno de trabajo con Jupyter

Introducción
La Distribución Anaconda es un paquete de software que cuenta con todo lo necesario para empezar a trabajar en Data Science utilizando Python (o R). Incluye la instalación del intérprete de Python con los módulos externos más usados en Data Science y diversos entornos de desarrollo entre los que se encuentra Jupyter, el que usaremos durante el curso.

También cuenta con un administrador de paquetes y entornos llamado conda,que nos permitirá crear entornos de trabajo aislados y descargar e instalar librerías de código externas que iremos viendo durante el curso.

Otra de las ventajas de Anaconda es que es multi-plataforma y cuenta con instaladores para Windows, MacOs y Linux. En este documento te enseñaré a instalar Anaconda en Windows.

Para más información sobre el proceso de instalación de Anaconda e instructivos sobre cómo instalarlo en otros sistemas operativos, te recomiendo que visites la página oficial: <https://docs.anaconda.com/anaconda/install/>.

## Modulo 2 HTML: Requests y BeautifulSoup

### Clase 4 Descargando una página web

Instalamos las librerías:

- jupyter
- requests
- bs4

![requests_1](src/requests_1.png)
![requests_2](src/requests_2.png)
![requests_3](src/requests_3.png)

### Clase 5 Parseando HTML con BeautifulSoup

![bs4_1](src/bs4_1.png)
![bs4_2](src/bs4_2.png)

### Clase 6 Extrayendo información

![bs4_3](src/bs4_3.png)
![bs4_4](src/bs4_4.png)
![bs4_5](src/bs4_5.png)

### Clase 7 Manejo de errores

La importancia de la programación defensiva, y solución al reto anterior

![manejo_de_errores](src/manejo_de_errores.png)

### Clase 8 Descargando Contenido

![descargando_contenido_1](src/descargando_contenido_1.png)

### Clase 9 Descargando Multimedia

![descargando_contenido_multimedia_1](src/descargando_contenido_multimedia_1.png)
![descargando_contenido_multimedia_2](src/descargando_contenido_multimedia_2.png)

### Clase 10 Unificando el scraper

```py
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
```

## Modulo 3 Scraping JavaScript con Selenium

### Clase 11 Instalación y configuración de Selenium

Para poder utilizar Selenium con Python hay que seguir una serie de pasos que están detallados a continuación.

De todas formas, siempre es recomendable leer la documentación oficial de las herramientas.

Instalar los bindings de Selenium para Python. Éstos nos permitirán controlar un navegador desde el código.
Ejecutar:

pip install selenium

O si estás utilizando Anaconda, puedes instalarlo con:

conda install -c conda-forge selenium

Selenium necesita un driver para poder generar una interfaz con el navegador. Dependiendo el navegador que uses, deberás descargar un driver distinto. Acá te dejo un listado de los links de descarga para los distintos navegadores. Asegurate de descargar el que corresponda con la versión de tu navegador:
Chrome: <https://sites.google.com/a/chromium.org/chromedriver/downloads>

Edge: <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>

Firefox: <https://github.com/mozilla/geckodriver/releases>

Safari: <https://webkit.org/blog/6900/webdriver-support-in-safari-10/>

Es importante que el archivo descargado esté en una carpeta accesible desde la Jupyter Notebook, ya que necesitaremos referenciarlo desde el código para poder utilizarlo.

### Clase 12 Sitios dinámicos y Selenium

Cuando hice este curso era imposible por el covid usar este sitio, lo mejor es hacerlo por cuenta propia con otras paginas, guardo capturas para guia.

![Selenium_example](src/Selenium_example.png)
![Selenium_example_1](src/Selenium_example_1.png)
![Selenium_example_2](src/Selenium_example_2.png)

### Clase 13 Selección de elementos

Vamos a utilizar x-path es decir la ruta xml.

// indica que tiene que buscar en todos los elementos del arbol.

![selenium_seleccion_elementos_1](src/selenium_seleccion_elementos_1.png)
![selenium_seleccion_elementos_2](src/selenium_seleccion_elementos_2.png)

### Clase 14 Interactuando con los elementos

![selenium_interactuando_con_elementos_1.png](src/selenium_interactuando_con_elementos_1.png)

### Clase 15 Scrapeando escalas y tarifas

![escalas_y_tarifas_1.png](src/escalas_y_tarifas_1.png)
![escalas_y_tarifas_2.png](src/escalas_y_tarifas_2.png)

### Clase 16 Construyendo Funciones

![construyendo_funciones_1](src/construyendo_funciones_1.png)
![construyendo_funciones_2](src/construyendo_funciones_2.png)

### Clase 17 Construyendo la función para unificar el scraper

![unificar_funciones_1.png](src/unificar_funciones_1.png)

### Clase 18 Demoras dinámicas

la manera mas sencilla es usar una espera estatica

```py
import time
time.sleep(10)
```

Lo mejor es usar las demoras dinamicas de selenium.

![demoras_dinamicas](src/demoras_dinamicas.png)

### Clase 19 Comentarios Finales

Dado que selenium esmuy tardado, usalo como alternativa final, prefiere request y bs4 o apis antes de.

## Modulo 4 APIs

### Clase 20 Introducción a APIs

En este módulo utilizaremos APIs para obtener información sobre artistas, discos y tracks disponibles en Spotify.

#### Que es una API

Por sus siglas en inglés, una API es una interfaz para programar aplicaciones (Application Programming Interface). Es decir que es un conjunto de funciones, métodos, reglas y definiciones que nos permitirán desarrollar aplicaciones (en este caso un scraper) que se comuniquen con los servidores de Spotify. Las APIs son diseñadas y desarrolladas por las empresas que tienen interés en que se desarrollen aplicaciones (públicas o privadas) que utilicen sus servicios. Spotify tiene APIs públicas y bien documentadas que estaremos usando en el desarrollo de este proyecto.

#### REST

Un término se seguramente te vas a encontrar cuando estés buscando información en internet es REST o RESTful. Significa representational state transfer y si una API es REST o RESTful, implica que respeta unos determinados principios de arquitectura, como por ejemplo un protocolo de comunicación cliente/servidor (que será HTTP) y (entre otras cosas) un conjunto de operaciones definidas que conocemos como métodos. Ya veníamos usando el método GET para hacer solicitudes a servidores web.

#### Documentacion

Como mencioné antes, las APIs son diseñadas por las mismas empresas que tienen interés en que se desarrollen aplicaciones (públicas o privadas) que consuman sus servicios o información. Es por eso que la forma de utilizar las APIs variará dependiendo del servicio que querramos consumir. No es lo mismo utilizar las APIs de Spotify que las APIs de Twitter. Por esta razón es de suma importancia leer la documentación disponible, generalmente en la sección de desarrolladores de cada sitio. Te dejo el link a la de [Spotify](https://developer.spotify.com/documentation/)

#### JSON

Json significa JavaScript Object Notation y es un formato para describir objetos que ganó tanta popularidad en su uso que ahora se lo considera independiente del lenguaje. De hecho, lo utilizaremos en este proyecto por más que estemos trabajando en Python, porque es la forma en la que obtendremos las respuestas a las solicitudes que realicemos utilizando las APIs. Para nosotros, no será ni más ni menos que un diccionario con algunas particularidades que iremos viendo a lo largo del curso.

### Clase 21 Utilizando APIs: construir una url

![Api_1](src/Api_1.png)

### Clase 22 Utilizando APIs: Tokens y Búsqueda

Spotify te requiere registrar tu aplicacion para poder utilizar la api, sigue la documentacion para ello.

Registrate <https://developer.spotify.com/dashboard/tos-accept>

Crea un una app en el  dashboard
![Api_2](src/Api_2.png)

Obtenemos los id para conexion

![Api_3](src/Api_3.png)

Implementamos el jupyter

![Api_4](src/Api_4.png)
![Api_5](src/Api_5.png)
![Api_6](src/Api_6.png)
![Api_7](src/Api_7.png)
![Api_8](src/Api_8.png)

### Clase 23 Obteniendo la Discografia

Creamos una funcion para obtener el token,y obtenemos la discografia a partir del id

![Api_9](src/Api_9.png)

### Clase 24 Obteniendo los albums

Obtenermos los albums implementando la funcion obtener_discografia.

![Api_10](src/Api_10.png)

![Api_11](src/Api_11.png)

### Clase 25 Final del proyecto + bonus

![Api_12](src/Api_12.png)

## Modulo 5 Scrapy, Tesseract y Proxies

### Clase 26 Scrapy

Scrapy es un framework que permite usar funciones asincronas y usar x-path, settear demoras y limitar los dominios, Scrappy funciona mediante clases.

![Scrapy_1](src/Scrapy_1.png)

### Clase 27 Ejecutando el scraper con scrapy

Realizamos este mismo  scrapper en el jupyter,

```py
import scrapy
from scrapy.crawler import CrawlerProcess


class Spider12(scrapy.Spider):
    name = 'spider12'
    allowed_domains = ['pagina12.com.ar']
    custom_settings = {'FEED_FORMAT': 'json',
                       'FEED_URI': 'resultados.json',
                       'DEPTH_LIMIT': 2}

    start_urls = ['https://www.pagina12.com.ar/secciones/el-pais',
                  'https://www.pagina12.com.ar/secciones/economia',
                  'https://www.pagina12.com.ar/secciones/sociedad',
                  'https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos',
                  'https://www.pagina12.com.ar/secciones/ciencia',
                  'https://www.pagina12.com.ar/secciones/el-mundo',
                  'https://www.pagina12.com.ar/secciones/deportes',
                  'https://www.pagina12.com.ar/secciones/contratapa']

    def parse(self, response):
        #Articulo promocionado
        nota_promocionada = response.xpath(
            '//div[@class="featured-article__container"]/h2/a/@href').get()
        if nota_promocionada is not None:
            yield response.follow(nota_promocionada, callback=self.parse_nota)

         #Listado de notas
        notas = response.xpath(
            '//ul[@class="article-list"]//li//a/@href').getall()
        for nota in notas:
            yield response.follow(nota, callback=self.parse_nota)

        # link a la siguiente pagina
        next_page = response.xpath('//a[@class="pagination-btn-next"]/@href')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_nota(self, response):
        #Parseo la nota
        titulo = response.xpath('//div[@class="article-title"]/text()').get()
        cuerpo = ''.join(response.xpath(
            '//div[@class="article-text"]/p/text()').getall())
        yield {'url': response.url,
               'titulo': titulo,
               'cuerpo': cuerpo}


process = CrawlerProcess()
process.crawl(Spider12)
process.start()
```

Para mas informacion ve a la  documentacion oficial de [scrapy](https://scrapy.org/)

### Clase 28 Proxies

Un Proxie es un intermediario entre el servidor web y nuestro scrapper.

Ubicamos nuestra ip publica

![Proxy_1](src/Proxy_1.png)
![Proxy_2](src/Proxy_2.png)

### Clase 29 Tesseract

**Tesseract** creada originalmente por Hp y actualmente mantenida por google es un OCR de reconocimiento de imagenes a texto.

Si usas ubuntu/wsl debes previamente instalar las dependencias adicionales

```bash
sudo apt-getupdate
```

Después instala tesseract OCR con:

```bash
sudo apt-get install tesseract-ocr -y
```

Instala los modelos del idioma español con:

```bash
sudo apt-get install tesseract-ocr-spa -y
```

Deberas instalar las dependencias adicionales del notebook

![Tesseract_1](src/Tesseract_1.png)
![Tesseract_2](src/Tesseract_2.png)
![Tesseract_3](src/Tesseract_3.png)
![Tesseract_4](src/Tesseract_4.png)

### Clase 30 Conclusion y cierre del curso

Usa este conocimiento sabiamente, lee los terminos y condiciones antes de hacer un scrapper.
