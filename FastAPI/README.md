# FASTAPI

[INFO](https://fastapi.tiangolo.com/tutorial/first-steps/)

- **GET** - для получения данных.
- **POST** - для создания новых данных.
- **PUT** - для полного обновления существующих данных.
- **PATCH** - для частичного обновления.
- **DELETE** - для удаления данных.

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

`main.py`

```python
class User(BaseModel):
    username: str
    age: int


@app.put('/items/{item_id}')
async def update_item(
    *,
    item_id: int = Path(ge=0, le=150),
    q: str | None = Query(alias='Q-W-E'),
    user: User,
    one_more_body: int = Body(embed=True)
    # When `embed` is `True`, the parameter will be expected in a JSON body
    # as a key instead of being the JSON body itself.
    # This happens automatically when more than one `Body` parameter is declared.
):
    response = {'item_id': item_id}
    if q:
        response.update({'q': q})
    if user:
        response.update({'user': user})
    if one_more_body:
        response.update({'one_more_body': one_more_body})

    return response
```

`http://127.0.0.1:8000/items/50?Q-W-E=yes`

Request body

```json
{
  "user": {
    "username": "string",
    "age": 0
  },
  "one_more_body": 6
}
```

Response body

```json
{
  "item_id": 50,
  "q": "yes",
  "user": {
    "username": "string",
    "age": 0
  },
  "one_more_body": 6
}
```

## `Body` NESTED MODELS

With FastAPI, you can define, validate, document, and use arbitrarily deeply nested models

`main.py`

```python
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class DescUrl(BaseModel):
    url: HttpUrl


class Pokemon(BaseModel):
    name: str
    hp: int
    atk: int
    strong_against: set[str] = []
    description: DescUrl



@app.put('/pokemons/{id}')
async def update_pokemon(id: int, pokemon: Pokemon):
    response = {'id': id, 'pokemon': pokemon}

    return response
```

Request body

```json
{
  "name": "string",
  "hp": 0,
  "atk": 0,
  "strong_against": [],
  "description": {
    "url": "https://example.com/"
  }
}
```

Response body

```json
{
  "id": 1,
  "pokemon": {
    "name": "string",
    "hp": 0,
    "atk": 0,
    "strong_against": [],
    "description": {
      "url": "https://example.com/"
    }
  }
}
```

## DECLARE REQUEST EXAMPLE DATA

You can declare examples of the data your app can receive.

### EXAMPLE WITH EXTRA `JSON` SCHEMA IN `pydantic` MODELS

`main.py`

```python
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Pokemon(BaseModel):
    name: str
    hp: int | None = None
    weight: float

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'name': 'Rattata',
                    'hp': 30,
                    'weight': 3.5
                }
            ]
        }
    }


@app.put('/pokemons/{id}')
async def update_pokemon(id: int, pokemon: Pokemon):
    response = {'id': id, 'pokemon': pokemon}
    return response
```

`http://127.0.0.1:8000/pokemons/1`

```json
{
  "id": 1,
  "pokemon": {
    "name": "Rattata",
    "hp": 30,
    "weight": 3.5
  }
}
```

### EXAMPLE WITH `Field` ADDITIONAL ARGUMENTS

`main.py`

```python
class Pokemon(BaseModel):
    name: str = Field(examples=['Rattata'])
    hp: int | None = Field(None, examples=[30])
    weight: float = Field(examples=[3.5])


@app.put('/pokemons/{id}')
async def update_pokemon(id: int, pokemon: Pokemon):
    response = {'id': id, 'pokemon': pokemon}
    return response
```

Response body

```json
{
  "id": 1,
  "pokemon": {
    "name": "Rattata",
    "hp": 30,
    "weight": 3.5
  }
}
```

### EXAMPLE WITH `Body`

`main.py`

```python
@app.put('/pokemons/{id}')
async def update_pokemon(
    id: int,
    pokemon: Pokemon = Body(
        examples={
            'normal': {
                'summary': 'Default example',
                'description': 'Default description',
                'value': {
                    'name': 'Rattata',
                    'hp': 30,
                    'weight': 3.5
                }
            }
        }
    )
):
    response = {'id': id, 'pokemon': pokemon}
    return response
```

## EXTRA DATA TYPES

Some of the additional data types:

`UUID`
`datetime.datetime`
`datetime.date`
`datetime.time`
`datetime.timedelta`
`frozenset`
`bytes`
`Decimal`
[Pydantic data types](https://docs.pydantic.dev/latest/concepts/types/)

### EXAMPLE WITH `UUID`, `datetime`

`main.py`

```python
import datetime
from uuid import UUID


@app.put('items/{item}')
async def read_items(
    item: UUID,
    start_date: datetime.datetime | None = Body(None),
    end_date: datetime.datetime | None = Body(None)
):
    response = {
        'item': item,
        'start_date': start_date,
        'end_date': end_date
    }

    return response
```

## `Cookie` AND `Header` PARAMETERS

`main.py`

```python
from fastapi import Cookie, Header


@app.get('/users')
async def read_users(
    cookie_id: str | None = Cookie(None),
    accept: str | None = Header(None),
    host: str | None = Header(None),
    referer: str | None = Header(None),

):
    return {
        'cookie_id': cookie_id,
        'accept': accept,
        'host': host,
        'referer': referer,
    }
```

```json
{
  "cookie_id": null,
  "accept": "application/json",
  "host": "127.0.0.1:8000",
  "referer": "http://127.0.0.1:8000/docs"
}
```

## RESPONSE MODEL

You can declare the type used for the response by annotating the path operation function return type.

You can use type annotations the same way you would for input data in function parameters, you can use Pydantic models, lists, dictionaries, scalar values like integers, booleans, etc

### EXAMPLE WITH INPUT AND OUTPUT MODELS

`main.py`

```python
class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
```

Request body

```json
{
  "username": "qwe",
  "password": "123"
}
```

Response body

```json
{
  "username": "qwe"
}
```

### RESPONSE MODEL ENCODING PARAMETERS WITH `response_model_exclude_unset`

`main.py`

```python
class Pokemon(BaseModel):
    name: str
    hp: int = 0
    weight: float | None = None
    types: set[str] = set()
    status: bool = False


pokemons = {
    1:  {
        'name': 'Bulbasaur',
        'hp': 45,
        'weight': 6.9,
        'types': ['GRASS', 'POISON'],
        'status': True,
    },
    2: {
        'name': 'Сharmander',
        'weight': 8.5,
    }
}


@app.post(
    '/pokemons/{id}',
    response_model=Pokemon,
    response_model_exclude_unset=True,
)
async def create_pokemon(id: int):
    return pokemons[id]
```

`http://127.0.0.1:8000/pokemons/1`

```json
{
  "name": "Bulbasaur",
  "hp": 45,
  "weight": 6.9,
  "types": [
    "POISON",
    "GRASS"
  ],
  "status": true
}
```

`http://127.0.0.1:8000/pokemons/2`

```json
{
  "name": "Сharmander",
  "weight": 8.5
}
```

## EXTRA MODELS

This is especially the case for user models, because:
1. The input model needs to be able to have a password.
2. The output model should not have a password.
3. The database model would probably need to have a hashed password.

### EXAMPLE WITH MULTIPLE MODELS

`main.py`

```python
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def password_hasher(password: str):
    return "supersecret" + password


def save_user(user_in: UserIn):
    hashed_password = password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)

    print("def save_user done")
    return user_in_db


@app.post("/user/", response_model=UserInDB)  # resoonse_model=UserOut
async def create_user(user_in: UserIn):
    user_saved = save_user(user_in)
    return user_saved
```

Request body

```json
{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}
```

Response body

```json
{
  "username": "string",
  "email": "user@example.com",
  "hashed_password": "supersecretstring"
}
```

## RESPONSE STATUS CODE

The same way you can specify a response model, you can also declare the HTTP status code used for the response with the parameter `status_code` in any of the `Path` operations.

In short:

- `100` and above are for "Information". You rarely use them directly. Responses with these status codes cannot have a body.
- `200` and above are for "Successful" responses. These are the ones you would use the most. `200` is the default status code, which means everything was "OK".
- `300` and above are for "Redirection". Responses with these status codes may or may not have a body.
- `400` and above are for "Client error" responses. These are the second type you would probably use the most.
- `500` and above are for server errors. You almost never use them directly. When something goes wrong at some part in your application code, or server, it will automatically return one of these status codes.

### EXAMPLE WITH `status_code`

`main.py`

```python
from fastapi import status


# @app.post('/items/', status_code=200)
@app.post('/items/', status_code=status.HTTP_202_ACCEPTED)
async def create_item(name: str):
    return {'name': name}
```

## `Form` FIELDS

When you need to receive form fields instead of JSON, you can use `Form`

`main.py`

```python
from fastapi import Form


class User(BaseModel):
    username: str
    passwornd: str


@app.post('/login/')
async def login(
    username: str = Form(),
    passsword: str = Form()
):
    print('passsword:', passsword)
    return {'username': username}
```

## REQUEST `Files`

`UploadFile` has the following attributes:

- `filename`: A str with the original file name that was uploaded (e.g. myimage.jpg).
- `content_type`: A str with the content type (MIME type / media type) (e.g. image/jpeg).
- `file`: A SpooledTemporaryFile (a file-like object). This is the actual Python file that you can pass directly to other functions or libraries that expect a "file-like" object.

`UploadFile` has the following async methods. They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

- `write(data)`: Writes data (str or bytes) to the file.
- `read(size)`: Reads size (int) bytes/characters of the file.
- `seek(offset)`: Goes to the byte position offset (int) in the file. E.g., `await myfile.seek(0)` would go to the start of the file. This is especially useful if you run `await myfile.read()` once and then need to read the contents again.
- `close()`: Closes the file.

### NAME

`main.py`

```python
from fastapi import File, UploadFile

@app.post('/files/')
async def create_file(file: bytes = File()):
    return {'file': len(file)}


@app.post('/uploadfile')
async def upload_file(file: UploadFile):
    return {'filename': file.filename}
```

### MULTIPLE FILE UPLOADS

`main.py`

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
```

## REQUEST `Forms` AND `Files`

`main.py`

```python
@app.post('/files/')
async def create_file(
    file: bytes = File(),
    second_file: UploadFile = File(),
    token: str = Form(),
):
    return {
        'file_size': len(file),
        'token': token,
        'fileb_content_type': second_file.content_type,
    }
```

Response body

```json
{
  "file_size": 693,
  "token": "QWE-123",
  "fileb_content_type": "application/rtf"
}
```

## HANDLING ERRORS

### EXAMPLE WITH `HTTPException`

```python
from fastapi import HTTPException


items = {'QWE': 'Quality, Warranty, and Efficiency'}


@app.get('/items/{item}')
async def read_item(item: str):
    if item not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return {'item': items[item]}
```

`http://127.0.0.1:8000/items/QWE`

Response body

```json
{
  "item": "Quality, Warranty, and Efficiency"
}
```

### CUSTOM EXEPTION HANDLERS

`main.py`

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
```

## `JSON` ENCODER

There are some cases where you might need to convert a data type (Pydantic models) to something compatible with `JSON` (dict, list, etc). For example, if you need to store it in a database.

`main.py`

```python
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
```

## DEPENDENCIES



### DATABASE DEPENDENCIES WITH `yield`


`main.py`

```python
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

## AUTHORIZATION

### `oauth2_scheme`

`main.py`

```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
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

```json
RESPONSE
```
-->
