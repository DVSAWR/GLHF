# Патерны проектирования

## Порождающие паттерны

### Абстрактная фабрика (Abstract Factory)

Паттерн предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов.

```python
class AbstractProductA(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ProductA1(AbstractProductA):
    def operation(self) -> str:
        return self.__class__.__name__


class ProductA2(AbstractProductA):
    def operation(self) -> str:
        return self.__class__.__name__


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass


class Factory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()


class Factory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()


def code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    print(product_a.operation())


code(Factory1())
code(Factory2())

# OUTPUT
# ProductA1
# ProductA2
```

**Преимущества** : \
Изолирует конкретные классы. \
Упрощает добавление новых вариантов продуктов. \
Обеспечивает согласованность между продуктами.

**Недостатки** : \
Может усложнить код из-за множества дополнительных классов. \
Необходимость изменения кода при добавлении новых продуктов.

### Строитель (Builder)

Разделяет процесс построения сложного объекта от его представления так, что один и тот же процесс построения может создавать различные представления.

```python
class CompositProduct:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def join_parts(self):
        print(f"Product parts: {', '.join(self.parts)}")


class Builder:
    def __init__(self):
        self.product = CompositProduct()

    def build_part_a(self):
        self.product.add("part A")

    def build_part_b(self):
        self.product.add("part B")

    def get_result(self) -> CompositProduct:
        return self.product


builder = Builder()
builder.build_part_a()
builder.build_part_b()
result = builder.get_result()
result.join_parts()

# OUTPUT
# Product parts: part A, part B
```

**Преимущества** : \
Позволяет изменять внутреннее представление продукта. \
Изолирует код, создающий объект, от кода, использующего объект. \
Поддерживает разные варианты представления продукта.

**Недостатки** : \
Увеличивает количество классов. \
Может быть избыточным для простых объектов.

### Фабричный метод (Factory Method)

Определяет интерфейс для создания объекта, но позволяет подклассам выбрать класс создаваемого экземпляра.

```python
class AbstractProduct(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Product(AbstractProduct):
    def operation(self):
        return self.__class__.__name__


class AbstractFactory(ABC):
    @abstractmethod
    def factory_method(self) -> AbstractProduct:
        pass

    def operation(self) -> str:
        product = self.factory_method()
        return f"AbstractFactory operation worked with {product.operation()} in {self.__class__.__name__}"


class Factory(AbstractFactory):
    def factory_method(self):
        return Product()


factory = Factory()
print(factory.operation())

# OUTPUT
# AbstractFactory operation worked with Product in Factory
```

**Преимущества** : \
Легко добавлять новые продукты без изменения существующего кода. \
Позволяет делегировать создание объектов подклассам.

**Недостатки** : \
Может привести к увеличению числа классов. \
Может усложнить структуру проекта.

### Прототип (Prototype)

Создает объекты, используя клонирование существующих объектов-прототипов.

```python
class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"value: {self.value}"


prototype = ConcretePrototype(20)
cloned_prototype = prototype.clone()
print(f"{prototype} id: {id(prototype)} {type(prototype)}")
print(f"{cloned_prototype} id: {id(cloned_prototype)} {type(cloned_prototype)}")

# OUTPUT
# value: 20 id: 140508344013344 <class '__main__.ConcretePrototype'>
# value: 20 id: 140508344013536 <class '__main__.ConcretePrototype'>
```

**Преимущества** : \
Избегает дублирования кода создания объектов. \
Позволяет создавать новые объекты с минимальными затратами ресурсов.

**Недостатки** : \
Требует корректной реализации методов. \
Может быть сложно управлять глубокими копиями объектов.

### Одиночка (Singleton)

Гарантирует, что у класса есть только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.

```python
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# @singleton
# class Singleton:
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1.value, singleton2.value)
print(singleton1 is singleton2)

# OUTPUT
# 10 10
# True
```

**Преимущества** : \
Гарантирует единственность ресурса. \
Предоставляет глобальную точку доступа.

**Недостатки** : \
Может привести к скрытым зависимостям и трудностям в тестировании. \
Нарушает принцип единственной ответственности.

## Структурные паттерны

### Адаптер (Adapter)

Преобразует интерфейс одного класса в другой интерфейс, который ожидается клиентом.

```python
class Target:
    def request(self) -> str:
        return "Target: The default request"


class Adaptee:
    def specific_request(self) -> str:
        return "tseuqer cificeps ehT :eetpadA"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter -> {self.specific_request()[::-1]}"


target = Adapter()
print(target.request())

# OUTPUT
# Adapter -> Adaptee: The specific request
```

**Преимущества** : \
Позволяет совместно использовать несовместимые классы. \
Улучшает повторное использование кода.

**Недостатки** : \
Может усложнить код за счет дополнительных уровней абстракции. \
Может быть сложно понять и поддерживать.

