## Objetivo
Familiarizarse con la carga de un grafo a partir de una ontología predefinida, usando spacy para identificar los conceptos necesarios para crear nodos y relaciones

## Varios
La clase SimpleMatcher es una abstracción del matcher de spacy. 
Permite agregar patrones con el formato que definimos en el último encuentro. El método get_matches devuelve un diccionario en donde la llave es el nombre del patrón con el que matcheó, y una lista de matches para ese patrón 

La clase OntologyWrapper es una abstracción de rdflib. Permite agregar instancias de clases con label (solamente) y relaciones entre objetos o entre un objeto y un literal (nada más por ahora).

---
ontoreq.ttl es la definición de la ontología. O sea: clases y relaciones

output.ttl es el resultado de cargar las instancias por código sobre esa ontología. 

_Ambos archivos pueden abrirse y mirarse con protege_

## Pasos
- Abrir la terminal en la carpeta donde se trabajará (cmd)
- Clonarse este repo (```git clone git@github.com:tanevitch/AprendiendoMatcher.git && cd AprendiendoMatcher```)
- Crear el ambiente virtual (```python -m venv .env```)
- Activar el ambiente virtual (```.env\Scripts\activate```)
- Instalar las dependencias (```pip install -r requirements.txt```)
- Instalar protege (https://protege.stanford.edu/)  
- Crear un archivo .json (a mano), donde definan:
    - Requerimiento
    - Persona que lo llevará a cabo
    - Elementos necesarios para que la persona lleve a cabo el requerimiento
- En principio, cargar a mano algunos individuos como está en el main.py. Luego, se usará el archivo del punto anterior para ese fin.

## Fuentes para matcher
✨ https://spacy.io/api/matcher 

✨ https://spacy.io/usage/rule-based-matching

✨ https://explosion.ai/demos/matcher 

✨ https://universaldependencies.org/docs/en/pos/

✨ https://universaldependencies.org/docs/en/dep/

## Fuentes para grafo

✨ https://programmerclick.com/article/725852296/ (explicacion protege. esto ya está hecho, no es necesario tocar nada. esto es lo que permitió generar el ontoreq.ttl)
✨ https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html (docu rdflib. esto es lo que está hecho en la clase ontologywrapper)