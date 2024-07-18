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
{ "message": "hola worldr" }
```

## `URL`

`https://example.com:8080/path/to/resource?query=param#fragment`

`https://` - `example.com` - `:8080` - `/path/to/resource` - `?query=param` - `#fragment`

| | | |
| --- | --- | --- |
| `https://` | `Scheme` (схема) | указывает протокол, который используется для доступа к ресурсу (например, HTTP или HTTPS). |
|`example.com` | `Host` (хост) | доменное имя или IP-адрес сервера, на котором находится ресурс. |
|`:8080` | `Port` (порт) | номер порта, через который осуществляется соединение с сервером. Если порт не указан, используется порт по умолчанию для данного протокола (80 для HTTP и 443 для HTTPS). |
|`/path/to/resource` | `Path` (путь) | путь к ресурсу на сервере. Он может состоять из нескольких сегментов, разделенных слешами ( `/` ). |
|`?query=param` | `Query` (запрос) | строка запроса, содержащая параметры в формате ключ=значение. Параметры разделяются амперсандом ( `&` ). |
|`#fragment`| `Fragment` (фрагмент) | якорь, указывающий на определенную часть ресурса. Обычно используется для перехода к определенному разделу на веб-странице. |

## `Path` PARAMETERS

`Path` (путь): `/path/to/resource` - путь к ресурсу на сервере. Он может состоять из нескольких сегментов, разделенных слешами (`/`).

### EXAMPLE

`main.py`

```python
@app.get('/get-item/{item}')
async def get_item(item: int):
    return {'item': item}
```

`http://127.0.0.1:8000/get-item/123`

```json
{ "item": 123 }
```

### EXAMPLE WITH `Enum`

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

## `Query` PARAMETERS

`Query` (запрос): `?query=param` - строка запроса, содержащая параметры в формате ключ=значение. Параметры разделяются амперсандом (`&`).

### EXAMPLE `get_list_items`

`main.py`

```python
items_db = [{'item': '1'}, {'item': '2'}, {'item': '3'}]


@app.get('/items')
async def get_list_items(start: int = 1, end: int = 1):
    return items_db[start:start + end]
```

`http://127.0.0.1:8000/items`

```json
[ { "item": "2" } ]
```

`http://127.0.0.1:8000/items?skip=0&limit=3`

```json
[ { "item": "1" }, { "item": "2" }, { "item": "3" } ]
```

### EXAMPLE `get_item`

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

### EXAMPLE `get_item` WITH `.update()`

`main.py`

```python
@app.get('/items/item')
async def get_item(item: str, q: str | None = None, desc: bool = False):
    item = {'item': item}
    if q:
        return {'item': item, 'q': q}
    if desc:
        item.update(
            {
                "description": "DESCRIPTION"
            }
        )
    return item
```

`http://127.0.0.1:8000/items/item?item=qwe`

```json
{ "item": "QWE" }
```

`http://127.0.0.1:8000/items/item?item=QWE&desc=true`

|`&desc=true`|`&desc=false`|
|-----|------|
| true | false |
| True | False |
| 1 | 0 |
| yes | no |
|on | off |

```json
{ "item": "QWE", "description": "DESCRIPTION" }
```

## REQUEST BODY

### EXAMPLE `create_user` WITH `pydantic`

`main.py`

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    surname: str | None = None  # AFTER 3.10
    patronymic: Optional[str] = None  # BEFOR 3.10
    status: bool

@app.post('/users')
async def create_user(user: User) -> User:
    return user
```

Request body

```json
{
  "id": 0,
  "name": "string",
  "status": true
}
```

Response body

```json
{
  "id": 0,
  "name": "string",
  "surname": null,
  "patronymic": null,
  "status": true
}
```

### EXAMPLE `create_user` WITH `.model_dump()`

`main.py`

```python
@app.post('/users')
async def create_user(user: User):
    user_dict = user.model_dump()
    if not user.surname:
        user_dict.update(
            {
                'status': False,
                'fine': 100.0
            }
        )
    return user_dict
```

Request body

```json
{
  "id": 0,
  "name": "string",
  "status": true
}
```

Response body

```json
{
  "id": 0,
  "name": "string",
  "surname": null,
  "patronymic": null,
  "status": false,
  "fine": 100
}
```

### EXAMPLE `create_user_with_put`

`main.py`

```python
@app.put('/users/{age}')
async def create_user_with_put(age: int, user: User):
    return {'age': age, **user.model_dump()}
```

Request URL

`http://127.0.0.1:8000/users/100`

Request body

```json
{
  "id": 0,
  "name": "string",
  "status": true
}
```

Response body

```json
{
  "age": 100,
  "id": 0,
  "name": "string",
  "surname": null,
  "patronymic": null,
  "status": true
}
```

## `Query` PARAMETERS AND STRING VALIDATION

| | |
| --- | --- |
| `min_length` | минимальная длинна |
| `max_length` | максимальная длинна |
| `pattern` | регулярное выражение, которому должен соответствовать параметр |
| `default` | значение по умолчанию |
| `list` | множественное значение по умолчанию |
| `title` | название параметра запроса |
| `description` | описание параметра запроса |
| `alias` | псевданим запроса |
| `deprecated` | устаревший параметр |
| `include_in_schema=False` | исключить query-параметр из генерируемой OpenAPI схемы  |

### EXAMPLE `get_pokemons` WITH `Query(max_length=3)`

`main.py`

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Pokemon(BaseModel):
    id: int
    name: str
    weight: str | None = None


@app.get('/pokemons')
async def get_pokemons(q: str | None = Query(None, max_length=3)):
    result = {
        'pokemons': [
            {
                'name': 'Bulbasaur'
            },
            {
                'name': 'Charmander'
            },
        ]
    }
    if q:
        result.update({'q': q})
    return result
```

`http://127.0.0.1:8000/pokemons?q=QWE`

```json
{"pokemons":[{"name":"Bulbasaur"},{"name":"Charmander"}],"q":"QWE"}
```

`http://127.0.0.1:8000/pokemons?q=QWEE`

```json
{"detail":[{"type":"string_too_long","loc":["query","q"],"msg":"String should have at most 3 characters","input":"QWEE","ctx":{"max_length":3}}]}
```

### EXMAPLE `multidefault` WITH `Annotated`

`main.py`

```python
from typing import Annotated


@app.get("/multidefault")
async def read_items(q: Annotated[list[str], Query()] = ["qwe", "asd"]):
    result = {"q": q}
    return result
```

`http://127.0.0.1:8000/multidefault`

```json
{
  "q": [
    "qwe",
    "asd"
  ]
}
```

## `Path` PARAMETERS AND NUMERIC VALIDATION

| | |
| -- | -- |
|`gt`| greater than|
|`ge`| greater than or equal|
|`lt`| less than|
|`le`| less than or equal|

### EXAMPLE WITH `Path`


`main.py`

```python
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


@app.get('/validation/{item}')
async def read_items_validation(
    item: Annotated[int, Path(description='Path allways required!')],
    first: str | None = Query(None, alias='first-query'),
    second: Annotated[str | None, Query(alias='second-query')] = None
):
    result = {'item': item}
    if first:
        result.update({'first query': first})
    if second:
        result.update({'second query': second})

    return result
```

`http://127.0.0.1:8000/validation/1?first-query=qwe&second-query=asd`

```json
{
  "item": 1,
  "first query": "qwe",
  "second query": "asd"
}
```

### EXAMPLE WITH `ge`, `le` IN `Path`, `Query`

`main.py`

```python
@app.get('/{num}')
async def read_num_validation(
    num: Annotated[
        int,
        Path(ge=2, le=9),
    ],
    size: Annotated[
        float,
        Query(ge=0, le=7.75),
    ],
):
    result = {'num': num, 'size': size}
    if size:
        result.update({'size': size})
    return result
```

`http://127.0.0.1:8000/3?size=3`

```json
{
  "num": 3,
  "size": 3
}
```

## `Body` MULTIPLE PARAMETERS



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
