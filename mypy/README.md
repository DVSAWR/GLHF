# MYPY

`mypy main.py`

## Стандартные типы

### К стандартным скалярным (не коллекциям) типам относятся следующие

- `int` – целочисленная переменная любой длины. Например: 42, -10, 0;
- `float` – число с плавающей точкой. Например: 0.13, 5.0, math.pi;
- `bool` – булево значение, True или False;
- `str` – строка. Например: “Hello, world!”;
- `bytes` – последовательность байт. Например: b”Hello”;
- `bytearray` – изменяемый массив байт. Например: bytearray(b”Hello”);
- `None` – аналог void типа в Си. Имеет None как единственное значение.

### К стандартным дженерик типам относятся следующие

- `List[T]` – список, элементы которого имеют тип T;
- `Tuple[T1, T2, …, TN]` – кортеж, первый элемент которого имеет тип T1, второго – T2 и так далее;
- `Dict[K, V]` – словарь, ключи которого имеют тип K, а значения – тип V;
- `Optional[T, V]` – тип T или None, аналогично Union[T, None];
- `Any` – любой тип;
- `Union[T1, T2, …, TN]` – любой тип из T1, T2, …, TN;
- `Callable[[T1, …], TResult]` – функция, которая принимает аргументы типов T1, … и возвращает TResult.

## EXAMPLES

```python
@dataclass
class User:
    username: str
    password: str
    token: Optional[str] = None
```

```python
def jwt_token_create(self, payload: Dict[str, Any], secret_key: str) -> str:
```

```python
def jwt_toke_decode(self, jwt_token: str, secret_key: str) -> Union[Dict[str, Any], Literal['ERROR']]:
```
