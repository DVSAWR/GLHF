# PyTest

## Test type

### Unit tests

Тестирование фрагмента кода

```py
def test_purchase_succeds_when_enough_inventory():
    # ARRANGE
    store = Store()
    store.add_inventory(Product.SHAMPOO, 10)
    customer = Customer()

    # ACT
    sucess = customer.purchase(store, Product.SHAMPOO, 5)

    # ASSERT
    assert success == True
    assert store.get_inventory(Product.SHAMPOO) == 5
```

### Integration tests

Проверка внедомменого функционала

#### End to end tests

Часть интеграционных тестов проводящих наиболее полный набор часте приложения

## mock, monkeypatch

