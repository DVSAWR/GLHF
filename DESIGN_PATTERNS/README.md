# Паттерны проектирования

Паттерны проектирования можно разделить на несколько основных групп в зависимости от их назначения и области применения. В классическом подходе, принятом в книге "Design Patterns: Elements of Reusable Object-Oriented Software" паттерны делятся на три основные категории:

- Порождающие паттерны (Creational Patterns)
- Структурные паттерны (Structural Patterns)
- Поведенческие паттерны (Behavioral Patterns)

| Порождающие паттерны (Creational Patterns)        | description                                                                 |
|-----------------|--------------------------------------------------------------------------|
| Singleton       | Обеспечивает наличие единственного экземпляра класса.                    |
| Factory Method  | Определяет интерфейс для создания объекта, но позволяет подклассам выбрать класс создаваемого объекта. |
| Abstract Factory| Предоставляет интерфейс для создания семейств взаимосвязанных или зависимых объектов без указания их конкретных классов. |
| Builder         | Разделяет процесс построения сложного объекта и его представление, позволяя использовать один и тот же процесс построения для создания различных представлений. |
| Prototype       | Создает объект путем клонирования прототипа вместо создания нового объекта с нуля. |

| Структурные паттерны (Structural Patterns)      | description                                                                 |
|-----------------|--------------------------------------------------------------------------|
| Adapter         | Преобразует интерфейс одного класса в другой, чтобы он мог быть использован в системе, ожидающей другой интерфейс. |
| Bridge          | Разделяет абстракцию и реализацию так, чтобы они могли изменяться независимо друг от друга. |
| Composite       | Позволяет работать с объектами, состоящими из других объектов, как с однородными структурами. |
| Decorator       | Динамически добавляет обязанности к объекту без изменения его структуры. |
| Facade          | Предоставляет унифицированный интерфейс для работы с несколькими классами или подсистемами. |
| Flyweight       | Минимизирует использование памяти за счет совместного использования общих частей объектов. |
| Proxy           | Представляет собой замену другого объекта, который может выполнять дополнительные действия перед или после делегирования вызова основному объекту. |

| Поведенческие паттерны (Behavioral Patterns)        | description     |
|-----------------------------|--------------------------------------------------------|
| Strategy        | Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми. |
| Observer        | Определяет зависимость типа "один ко многим" между объектами, так что при изменении состояния одного объекта все зависящие от него объекты уведомляются и обновляются автоматически. |
| Command         | Инкапсулирует запрос как объект, позволяя параметризировать методы клиентских объектов с запросами, задерживать выполнение запросов или хранить их в очереди. |
| State           | Позволяет объекту изменять свое поведение в зависимости от внутреннего состояния. |
| Chain of Responsibility | Передает запрос последовательно по цепочке обработчиков до тех пор, пока один из них не обработает запрос. |
| Interpreter     | Предоставляет способ определения грамматики для языка специфического домена, позволяя выражать операции над элементами этой грамматики. |
| Iterator | Обеспечивает способ последовательного доступа ко всем элементам агрегированного объекта без раскрытия его внутренней структуры. |
| Mediator        | Определяет объект, который управляет взаимодействием между набором объектов, чтобы они не ссылались напрямую друг на друга и тем самым не становились взаимосвязанными. |
| Memento         | Без нарушения инкапсуляции захватывает и сохраняет внутреннее состояние объекта, чтобы позднее восстановить его. |
| Visitor         | Позволяет добавлять новые операции к объектам без изменения их классов. |
| *Dependency Injection | Позволяет внедрять зависимости в классы, минимизируя их жесткую связь с другими классами. |

## Порождающие паттерны (Creational Patterns)

Эти паттерны касаются механизмов создания объектов, позволяя создавать объекты более гибким и контролируемым способом.

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

## Структурные паттерны (Structural Patterns)

Эти паттерны касаются композиции классов и объектов, помогая организовать структуру кода таким образом, чтобы он был эффективным и гибким.

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

### Мост (Bridge)

Разделяет абстракцию и реализацию таким образом, чтобы они могли изменяться независимо.

```python
class AbstractImplementation(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Implementation(AbstractImplementation):
    def operation(self) -> str:
        return self.__class__.__name__


class Abstraction:
    def __init__(self, implementation: AbstractImplementation):
        self.implementation = implementation

    def bridge(self) -> str:
        return f"Abstraction: bridge with {self.implementation.operation()}"


abstraction = Abstraction(Implementation())
print(abstraction.bridge())

# OUTPUT
# Abstraction: bridge with Implementation
```

**Преимущества** : \
Разделение абстракции и реализации. \
Возможность расширения обоих компонентов независимо.

**Недостатки** : \
Может усложнить структуру проекта. \
Требуется тщательное планирование и проектирование.

### Компоновщик (Composite)

Позволяет работать с группой объектов как с одним объектом.

```python
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Gear(Component):
    def operation(self) -> str:
        return self.__class__.__name__


class Composite(Component):
    def __init__(self):
        self._children: list[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def operation(self) -> str:
        result = []
        for child in self._children:
            result.append(child.operation())
        return " ".join(result)


composite = Composite()
composite.add(Gear())
composite.add(Gear())
print(composite.operation())

# OUTPUT
# Gear Gear
```

**Преимущества** : \
Упрощает работу с древовидными структурами. \
Позволяет применять одни и те же операции к различным типам объектов.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует тщательного управления иерархией объектов.

### Декоратор (Decorator)

Динамически добавляет обязанности к объекту без изменения его структуры.

```python
class AbstractComponent(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Component(AbstractComponent):
    def operation(self) -> str:
        return self.__class__.__name__


class AbstractDecorator(AbstractComponent):
    def __init__(self, component: AbstractComponent):
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


class Decorator(AbstractDecorator):
    def operation(self) -> str:
        return f"Decorator({self._component.operation()})"


decorated_component = Decorator(Component())
print(decorated_component.operation())

# OUTPUT
# Decorator(Component)
```

**Преимущества** : \
Позволяет динамически добавлять функциональность. \
Избегает изменения исходного кода классов.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует внимательного управления иерархией декораторов.

### Фасад (Facade)

Предоставляет единый интерфейс для группы интерфейсов в подсистеме.

```python
class Subsystem:
    def operation(self) -> str:
        return f"{self.__class__.__name__}: Ready"


class SubsystemA(Subsystem):
    pass


class SubsystemB(Subsystem):
    pass


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self) -> str:
        result = [
            self._subsystem_a.operation(),
            self._subsystem_b.operation(),
        ]
        return "\n".join(result)


facade = Facade()
print(facade.operation())

# OUTPUT
# SubsystemA: Ready
# SubsystemB: Ready
```

**Преимущества** : \
Упрощает взаимодействие с комплексными системами. \
Изолирует клиентский код от сложностей подсистемы.

**Недостатки** : \
Может ограничивать гибкость использования подсистемы. \
Требует тщательного проектирования.

### Легковес (Flyweight)

Поддерживает эффективное использование памяти путем совместного использования данных между многими похожими объектами.

```python
class Flyweight:
    def __init__(self, shared_state: str):
        self._shared_state = shared_state

    def operation(self, unique_state: str):
        s = self._shared_state
        u = unique_state
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.")


class FlyweightFactory:
    _flyweights = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print(f"FlyweightFactory: Can't find a flyweight '{key}', creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f"FlyweightFactory: Reusing existing flyweight '{key}'.")
        return self._flyweights[key]


factory = FlyweightFactory([])
flyweight1 = factory.get_flyweight(["q"])
flyweight1.operation("qwe")
flyweight2 = factory.get_flyweight(["q"])
flyweight2.operation("asd")

# OUTPUT
# FlyweightFactory: Can't find a flyweight 'q', creating new one.
# Flyweight: Displaying shared (['q']) and unique (qwe) state.
# FlyweightFactory: Reusing existing flyweight 'q'.
# Flyweight: Displaying shared (['q']) and unique (asd) state.
```

**Преимущества** : \
Эффективное использование памяти. \
Позволяет работать с большим количеством объектов.

**Недостатки** : \
Может усложнить управление состоянием объектов. \
Требует тщательного разделения общего и уникального состояния.

### Заместитель (Proxy)

Представляет собой объект, который контролирует доступ к другому объекту.

```python
class AbstractSubject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class Subject(AbstractSubject):
    def request(self) -> None:
        print(f"{self.__class__.__name__}: call request")


class Proxy(AbstractSubject):
    def __init__(self, subject: Subject):
        self._real_subject = subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print(f"{self.__class__.__name__}: Checking access...")
        return True

    def log_access(self) -> None:
        print(f"{self.__class__.__name__}: Logging...")


subject = Subject()
proxy = Proxy(subject)
proxy.request()

# OUTPUT
# Proxy: Checking access...
# Subject: call request
# Proxy: Logging...
```

**Преимущества** : \
Контроль доступа к объектам. \
Возможность добавления дополнительной логики перед и после вызова основного объекта.

**Недостатки** : \
Может замедлить выполнение операций. \
Требует внимательного управления зависимостями.

## Поведенческие паттерны (Behavioral Patterns)

Эти паттерны касаются распределения обязанностей между объектами и управления взаимодействием между ними.

### Цепочка обязанностей (Chain of Responsibility)

Передает запросы последовательно через цепочку обработчиков до тех пор, пока один из них не обработает запрос.

```python
class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class Handler(AbstractHandler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class HandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return f"{self.__class__.__name__}: handle {request}"
        else:
            return super().handle(request)


class HandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return f"{self.__class__.__name__}: handle {request}"
        else:
            return super().handle(request)


handler_a = HandlerA()
handler_b = HandlerB()
handler_a.set_next(handler=handler_b)

print(handler_a.handle("A"))
print(handler_a.handle("B"))
print(handler_a.handle("C"))

# OUTPUT
# HandlerA: handle A
# HandlerB: handle B
# None
```

**Преимущества** : \
Упрощает добавление новых обработчиков. \
Разделение ответственности между различными компонентами.

**Недостатки** : \
Может усложнить отладку и диагностику. \
Требует тщательного управления порядком обработчиков.

### Интерпретатор (Interpreter)

Определяет представление грамматики для заданного языка и интерпретатор выражений в этой грамматике.

```python
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: str) -> bool:
        pass


class TerminalExpression(Expression):
    def __init__(self, data: str):
        self._data = data

    def interpret(self, context) -> bool:
        return self._data in context


class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context: str) -> bool:
        return self._expr1.interpret(context) or self._expr2.interpret(context)


class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context: str) -> bool:
        return self._expr1.interpret(context) and self._expr2.interpret(context)


is_qwe = OrExpression(TerminalExpression("qwe"), TerminalExpression("QWE"))
is_asd_and_qwe = AndExpression(TerminalExpression("asd"), is_qwe)
print(is_qwe.interpret("qwe"))
print(is_asd_and_qwe.interpret("asd QWE"))

# OUTPUT
# True
# True
```

**Преимущества** : \
Возможность легко добавлять новые правила. \
Четкое разделение между грамматикой и ее интерпретацией.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует тщательного проектирования грамматики.

### Итератор (Iterator)

Обеспечивает способ последовательного доступа ко всем элементам агрегированного объекта без раскрытия его внутренней структуры.

```python
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


class Iterable(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class ConcreteIterable(Iterable):
    def __init__(self):
        self._items = []

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self)

    def add_item(self, item):
        self._items.append(item)


class ConcreteIterator(Iterator):
    def __init__(self, iterable: ConcreteIterable):
        self._iterable = iterable
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._iterable._items)

    def next(self):
        if self.has_next():
            item = self._iterable._items[self._index]
            self._index += 1
            return item
        raise Exception("No more items in iterator")


iterable = ConcreteIterable()
iterable.add_item("item A")
iterable.add_item("item B")
iterable.add_item("item C")

iterator = iterable.create_iterator()
while iterator.has_next():
    print(iterator.next())

# OUTPUT
# item A
# item B
# item C
```

**Преимущества** : \
Скрывает внутреннюю структуру коллекции. \
Позволяет легко перебирать элементы коллекции.

**Недостатки** : \
Может усложнить код для сложных коллекций. \
Требует внимательного управления состоянием итератора.

### Состояние (State)

Позволяет объекту изменять свое поведение при изменении внутреннего состояния.

```python
class State(ABC):
    @abstractmethod
    def handle(self):
        pass


class Context:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def request(self):
        self._state.handle()


class StateA(State):
    def handle(self):
        print(f"{self.__class__.__name__} handle request")


class StateB(State):
    def handle(self):
        print(f"{self.__class__.__name__} handle request")


context = Context(StateA())
context.request()
context.set_state(StateB())
context.request()

# OUTPUT
# StateA handle request
# StateB handle request
```

**Преимущества** : \
Разделение различных состояний и их поведения. \
Легкость добавления новых состояний.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует внимательного управления переходами между состояниями.

### Посетитель (Visitor)

Позволяет добавлять новые операции к объектам без изменения их классов.

```python
class Element(ABC):
    @abstractmethod
    def accept_visitor(self, visitor):
        pass


class ElementA(Element):
    def accept_visitor(self, visitor):
        visitor.visit_concrete_element_a(self)


class ElementB(Element):
    def accept_visitor(self, visitor):
        visitor.visit_concrete_element_b(self)


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass


class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{self.__class__.__name__}: visit {element}")

    def visit_concrete_element_b(self, element):
        print(f"{self.__class__.__name__}: visit {element}")


element_a = ElementA()
element_b = ElementB()
visitor = ConcreteVisitor()

element_a.accept_visitor(visitor)
element_b.accept_visitor(visitor)

# OUTPUT
# ConcreteVisitor: visit <__main__.ElementA object at 0x7f6a424ab6b0>
# ConcreteVisitor: visit <__main__.ElementB object at 0x7f6a422c3890>
```

**Преимущества** : \
Позволяет добавлять новые операции без изменения классов элементов. \
Упрощает добавление новых операций.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует внимательного управления иерархией классов.

### Стратегия (Strategy)

Определяет набор алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.

```python
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_something_with_array(self, data):
        result = self._strategy.do_algorithm(data)
        print(f"{self.__class__.__name__} result: {list(result)}")


class StrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class StrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


array = [3, 1, 2, 4]
context = Context(StrategyA())
context.do_something_with_array(array)
context.set_strategy(StrategyB())
context.do_something_with_array(array)

# OUTPUT
# Context result: [1, 2, 3, 4]
# Context result: [4, 3, 2, 1]
```

**Преимущества** : \
Позволяет легко менять алгоритмы. \
Изолирует алгоритмы от других частей кода.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует внимательного управления стратегиями.

### Шаблонный метод (Template Method)

Определяет скелет алгоритма в базовом классе, но позволяет подклассам переопределять некоторые шаги этого алгоритма.

```python
class AbstractClass(ABC):
    def template_method(self):
        self.start_operation_a()
        self.required_operation_a()
        self.end_operation_a()
        self.start_operation_b()
        self.required_operation_b()
        self.end_operation_b()

    def start_operation_a(self):
        print(f"{self.__class__.__name__} -> AbstractClass: operation_a ")

    def start_operation_b(self):
        print(f"{self.__class__.__name__} -> AbstractClass: operation_b")

    @abstractmethod
    def required_operation_a(self):
        pass

    @abstractmethod
    def required_operation_b(self):
        pass

    def end_operation_a(self):
        pass

    def end_operation_b(self):
        pass


class ConcreteClassA(AbstractClass):

    def required_operation_a(self):
        print(f"{self.__class__.__name__}: required_operation_a")

    def required_operation_b(self):
        print(f"{self.__class__.__name__}: required_operation_b")


class ConcreteClassB(AbstractClass):

    def required_operation_a(self):
        print(f"{self.__class__.__name__}: required_operation_a")

    def required_operation_b(self):
        print(f"{self.__class__.__name__}: required_operation_b")

    def end_operation_a(self):
        print(f"{self.__class__.__name__}: end_operation_a")


concrete_class_a = ConcreteClassA()
concrete_class_a.template_method()
print("")
concrete_class_b = ConcreteClassB()
concrete_class_b.template_method()

# OUTPUT
# ConcreteClassA -> AbstractClass: operation_a
# ConcreteClassA: required_operation_a
# ConcreteClassA -> AbstractClass: operation_b
# ConcreteClassA: required_operation_b

# ConcreteClassB -> AbstractClass: operation_a
# ConcreteClassB: required_operation_a
# ConcreteClassB: end_operation_a
# ConcreteClassB -> AbstractClass: operation_b
# ConcreteClassB: required_operation_b
```

**Преимущества** : \
Позволяет переопределять части алгоритма без изменения его структуры. \
Изолирует стандартные части алгоритма от специфических.

**Недостатки** : \
Может усложнить структуру проекта. \
Требует внимательного управления подклассами.

### Хранитель (Memento)

Без нарушения инкапсуляции захватывает и сохраняет внутреннее состояние объекта, чтобы позднее восстановить его.

```python
class Originator:
    def __init__(self, state):
        self._state = state

    def save_to_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()

    def __str__(self):
        return f"{self.__class__.__name__} current state: {self._state}"


class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


originator = Originator("initial commit")
memento = originator.save_to_memento()
print(originator)

originator._state = "add some bugs"
print(originator)

originator.restore_from_memento(memento)
print(originator)

# OUTPUT
# Originator current state: initial commit
# Originator current state: add some bugs
# Originator current state: initial commit
```

**Преимущества** : \
Сохраняет состояние объекта без нарушения инкапсуляции. \
Позволяет легко восстанавливать предыдущее состояние.

**Недостатки** : \
Может усложнить управление состояниями. \
Требует внимательного управления хранением мементо.

### Наблюдатель (Observer)

Определяет зависимость типа "один ко многим" между объектами, так что при изменении состояния одного объекта все зависящие от него объекты уведомляются и обновляются автоматически.

```python
class ConcreteSubject(Subject):
    _observers = []
    _state: int = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(f"Subject state changed to {self._state}")

    def set_state(self, state: int):
        self._state = state
        self.notify()


class ObserverA(Observer):
    def update(self, message: str):
        print(f"{self.__class__.__name__}: {message}")


class ObserverB(Observer):
    def update(self, message: str):
        print(f"{self.__class__.__name__}: {message}")


subject = ConcreteSubject()

observer_a = ObserverA()
observer_b = ObserverB()

subject.attach(observer_a)
subject.attach(observer_b)
subject.set_state(0)

subject.detach(observer_a)
subject.set_state(55)

# OUTPUT
# ObserverA: Subject state changed to 0
# ObserverB: Subject state changed to 0
# ObserverB: Subject state changed to 55
```

**Преимущества** : \
Наблюдатели и субъекты не зависят друг от друга напрямую. \
Легко добавлять или удалять наблюдателей без изменения кода субъекта.

**Недостатки** : \
При большом количестве наблюдателей может возникнуть проблема производительности из-за множественных вызовов. \
Сложно контролировать порядок выполнения и потенциальные циклические зависимости.

### Команда (Command)

Инкапсулирует запрос как объект, позволяя параметризировать методы клиентских объектов с запросами, задерживать выполнение запросов или хранить их в очереди.

```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SwitchOnCommand(Command):
    def __init__(self, switch: "Switch"):
        self._switch = switch

    def execute(self):
        self._switch.on()


class SwitchOffCommand(Command):
    def __init__(self, switch: "Switch"):
        self._switch = switch

    def execute(self):
        self._switch.off()


class Switch:
    def on(self):
        print(f"{self.__class__.__name__}: ON")

    def off(self):
        print(f"{self.__class__.__name__}: OFF")


class RemoteControler:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def run_command(self):
        if self._command:
            self._command.execute()


switch = Switch()
switch_on = SwitchOnCommand(switch)
switch_off = SwitchOffCommand(switch)
remote = RemoteControler()

remote.set_command(switch_on)
remote.run_command()
remote.set_command(switch_off)
remote.run_command()

# OUTPUT
# Switch: ON
# Switch: OFF
```

**Преимущества** : \
Команды инкапсулируют действия, что делает код более модульным и легким для тестирования. \
Легко реализовать функциональность отмены и повтора операций.

**Недостатки** : \
Увеличение числа классов и объектов может усложнить код. \
Дополнительные слои абстракции могут повлиять на производительность.

### Посредник (Mediator)

Определяет объект, который управляет взаимодействием между набором объектов, чтобы они не ссылались напрямую друг на друга и тем самым не становились взаимосвязанными.

```python
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component2 = component2

    def notify(self, sender: object, event: str):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

c1.mediator = mediator
c2.mediator = mediator

c1.do_a()
print("")
c2.do_d()

# OUTPUT
# Component 1 does A.
# Mediator reacts on A and triggers following operations:
# Component 2 does C.

# Component 2 does D.
# Mediator reacts on D and triggers following operations:
# Component 1 does B.
# Component 2 does C.
```

**Преимущества** : \
Компоненты не зависят друг от друга напрямую, что упрощает их модификацию и расширение. \
Все взаимодействия между компонентами проходят через посредника, что упрощает управление и поддержку.

**Недостатки** : \
Посредник может стать слишком сложным и трудным для поддержки, если он управляет большим количеством компонентов. \
Если посредник выходит из строя, это может повлиять на всю систему.

### Внедрение зависимостей (Dependency Injection)

Позволяет внедрять зависимости в классы, минимизируя их жесткую связь с другими классами

```python
class RepositoryInterface(ABC):
    @abstractmethod
    def get_data(self) -> str:
        pass


class DatabaseRepository(RepositoryInterface):
    def get_data(self) -> str:
        return "Data from database"


class FileRepository(RepositoryInterface):
    def get_data(self) -> str:
        return "Data from file"


class Service:
    def __init__(self, repository: RepositoryInterface):
        self._repository = repository

    def action(self) -> str:
        return f"Service action with {self._repository.get_data()}"


db_repo = DatabaseRepository()
service = Service(db_repo)
print(service.action())

file_repo = FileRepository()
service = Service(file_repo)
print(service.action())

# OUTPUT
# Service action with Data from database
# Service action with Data from file
```

**Преимущества** : \
Легко заменять реальные зависимости на моки или заглушки при тестировании. \
Возможность динамически менять зависимости без изменения кода класса.

**Недостатки** : \
Внедрение зависимостей может усложнить конфигурацию приложения, особенно если зависимостей много. \
Необходимо управлять жизненным циклом зависимостей, что может привести к ошибкам, если не сделать это правильно.
