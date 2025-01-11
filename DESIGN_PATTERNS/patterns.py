from abc import ABC, abstractmethod
import copy

# Абстрактная фабрика (Abstract Factory)
print("\nIMPLEMENTATION Abstract Factory:")


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

# Строитель (Builder)
print("\nIMPLEMENTATION Builder:")


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

# Фабричный метод (Factory Method)
print("\nIMPLEMENTATION Factory Method:")


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


# Прототип (Prototype)
print("\nIMPLEMENTATION Prototype:")


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

# Одиночка (Singleton)
print("\nIMPLEMENTATION Singleton:")


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

# Адаптер (Adapter)
print("\nIMPLEMENTATION Adapter:")


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
