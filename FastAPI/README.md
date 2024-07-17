# FASTAPI

## CREATE APP WITH `FastAPI`

`main.py`

```python
from fastapi import FastAPI

app = FastAPI()


@app.get('/', description='Your first route.', deprecated=True)
async def root():
    return {'message': 'hola worldr'}

# uvicorn src.main:app --reload
```

`http://127.0.0.1:8000/`

```json
{
  'message': 'hola worldr'
}
```

## `URL` PARAMETERS

`https://example.com:8080/path/to/resource?query=param#fragment`

`https://` `example.com` `:8080` `/path/to/resource` `?query=param` `#fragment`

- `Scheme` (схема): `https` - указывает протокол, который используется для доступа к ресурсу (например, HTTP или HTTPS).

- `Host` (хост): `example.com` - доменное имя или IP-адрес сервера, на котором находится ресурс.

- `Port` (порт): `8080` - номер порта, через который осуществляется соединение с сервером. Если порт не указан, используется порт по умолчанию для данного протокола (80 для HTTP и 443 для HTTPS).

- `Path` (путь): `/path/to/resource` - путь к ресурсу на сервере. Он может состоять из нескольких сегментов, разделенных слешами (/).

- `Query` (запрос): `?query=param` - строка запроса, содержащая параметры в формате ключ=значение. Параметры разделяются амперсандом (&).

- `Fragment` (фрагмент): `#fragment` - якорь, указывающий на определенную часть ресурса. Обычно используется для перехода к определенному разделу на веб-странице.

### `Path` PARAMETERS

`main.py`

```python
@app.get('/get-item/{item}')
async def get_item(item: int):
    return {'item': item}
```

`http://127.0.0.1:8000/get-item/123`

```json
{
  'item': 123
}
```

#### EXAMPLE WITH `Enum`

`main.py`

```python
from enum import Enum

class PokemonEnum(str, Enum):
    bulbasaur = 'bulbasaur'
    charmander = 'charmander'
    squirtle = 'squirtle'

@app.get('/pokemons/{name}')
async def get_pokemon(name: PokemonEnum):
    if name == PokemonEnum.bulbasaur:
        return {
            'name': name, 
            'message': 'Bulba, bulbasaur.'
        }

    if name.value == 'charmander':
        return {
            'name': name, 
            'message': 'Char, charmander.'
        }
    
    return {
        'name': name, 
        'message': 'Squirtle!'        
    }
```

`http://127.0.0.1:8000/pokemons/bulbasaur`

```json
{
  "name": "bulbasaur",
  "message": "Bulba, bulbasaur."
}
```

`http://127.0.0.1:8000/pokemons/charmander`

```json
{
  "name": "charmander",
  "message": "Char, charmander."
}
```

`http://127.0.0.1:8000/pokemons/squirtle`

```json
{
  "name": "squirtle",
  "message": "Squirtle!"
}
```

### `Query` PARAMETERS

`main.py`

```python
items_db = [{'item': '1'}, {'item': '2'}, {'item': '3'}]


@app.get('/items')
async def list_items(skip: int = 1, limit: int = 1):
    return items_db[skip:skip + limit]
```

`http://127.0.0.1:8000/items`

```json
[ { "item": "2" } ]
```

`http://127.0.0.1:8000/items?skip=0&limit=3`

```json
[ { "item": "1" }, { "item": "2" }, { "item": "3" } ]
```

#### OPTIONAL EXAMPLE

`main.py`

```python
@app.get('/items/item')
async def get_item(item: str, q: str | None = None):
    if q:
        return {'item': item, 'q': q}
    return {'item': item}
```

`http://127.0.0.1:8000/items/item?item=QWE`

```json
{ "item": "QWE" }
```

`http://127.0.0.1:8000/items/item?item=QWE&q=ASD`

```json
{ "item": "QWE", "q": "ASD" }
```



<!-- 
### NAME

`main.py`

```python
PYTHONFASTAPI
```

`URL`

```json
RESPONSE
``` 
-->
