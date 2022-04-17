## Objetivo
Aprender a usar el Matcher de Spacy. Para eso, se proveen tests de unidad que deben pasar exitosamente. La tarea es implementar el matcher que haga que los tests pasen.
## Pasos
- Abrir la terminal en la carpeta donde se trabajará (cmd)
- Clonarse este repo (```git clone git@github.com:tanevitch/AprendiendoMatcher.git && cd AprenderMatcher```)
- Crear el ambiente virtual (```python -m venv .env```)
- Activar el ambiente virtual (```.env\Scripts\activate```)
- Instalar las dependencias:
    - ```pip install spacy```
    - ```python -m spacy download en_core_web_trf```
- Crear el archivo requirements.txt. Luego enviar las librerías instaladas en el entorno virtual a ese archivo: ```pip freeze > requirements.txt```. De esta manera, no tenemos que estar diciéndole a todo el mundo qué instalar. Todo está ahí, todas las personas instalarán las dependencias necesarias con ```pip install -r requirements.txt``` (pero yo no lo hice así para que uds aprendan.)
- Completar el código hasta que los test pasen. Para correr los test: ```python -m unittest matchertest.py```

## Fuentes
✨ https://spacy.io/api/matcher 

✨ https://spacy.io/usage/rule-based-matching

✨ https://explosion.ai/demos/matcher 
