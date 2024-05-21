# SQL

[habr.com](https://habr.com/ru/articles/564390/#%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-sql) \
[SQL Trainer SQL ACADEMY](https://sql-academy.org/ru/trainer) \
[SQL Trainer ITResume](https://itresume.ru/problems)

<a name="DATA TYPES">qweqwe</a> 

## DATABASE STRUCTURE

| DB OBJECTS  | DESCRIPTION                                                                                                                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TABLE`     | таблицы содержат данные, которые хранятся в БД. Это основной объект.                                                                                                                                                    |
| `INDEX`     | индексы используются для увеличения производительности в операциях поиска и выборки данных.  [INFO](https://postgrespro.ru/docs/postgresql/13/indexes)                                                                  |
| `SEQUENCE`  | объект БД, предназначенный для генерации значений, которые используются в качестве значений полей в записях таблицы. [INFO](https://postgrespro.ru/docs/postgresql/13/functions-sequence)                               |
| Constraints | ограничение - объект БД, предназначенный для проверки значений полей таблиц при их создании и изменении. [INFO](https://postgrespro.ru/docs/postgresql/13/ddl-constraints)                                              |
| `PROCEDURE` | позволяют программировать на уровне самой БД (формально — на уровне СУБД), то есть БД содержат средства компиляции программного кода. Поэтому можно часть алгоритмов вынести на уровень БД                              |
| `TRIGGER`   | объект БД, представляющий собой механизм вызова некоторой процедуры при наступлении некоторого события. Событием может быть создание, удаление или изменение записи таблицы. Триггеры применяются к конкретной таблице. |
| `VIEW`      | это виртуальная таблица, которая обычно содержит связанные данные из нескольких таблиц и используется для удобства запросов данных.                                                                                     |

## DATA TYPES

| DATA TYPE          | DESCRIPTION                                                              |
|--------------------|--------------------------------------------------------------------------|
| `BIGINT`           | -9,223,372,036,854,775,808 ... 9,223,372,036,854,775,807                 |
| `INT`              | -2,147,483,648 ... 2,147,483,647                                         |
| `SMALLINT`         | 	-32,768 ... 32,767                                                      |
| `TINYINT`          | 0 ... 255                                                                |
| `BIT`              | 0 ... 1                                                                  |
| `DECIMAL`          | -10^38 +1 ... 10^38 -1                                                   |
| `NUMERIC`          | -10^38 +1 ... 10^38 -1                                                   |
| `MONEY`            | -922,337,203,685,477.5808 ... +922,337,203,685,477.5807                  |
| `SMALLMONEY`       | -214,748.3648 ... +214,748.3647                                          |
| `FLOAT`            | -1.79E + 308 ... 1.79E + 308                                             |
| `REAL`             | -3.40E + 38 ... 3.40E + 38                                               |
| `DATETIME`         | Jan 1, 1753 ... Dec 31, 9999                                             |
| `SMALLDATETIME`    | Jan 1, 1900 ... Jun 6, 2079                                              |
| `DATE`             | Дата сохраняется в виде June 30, 1991                                    |
| `TIME`             | Время сохраняется в виде 12:30 P.M.                                      |
| `CHAR`             | Строка длиной до 8,000 символов (не-юникод символы, фиксированной длины) |
| `VARCHAR`          | Строка длиной до 8,000 символов (не-юникод символы, переменной длины)    |
| `TEXT`             | Не-юникод данные переменной длины, длиной до 2,147,483,647 символов      |
| `NCHAR`            | Строка длиной до 4,000 символов (юникод символы, фиксированной длины)    |
| `NVARCHAR`         | Строка длиной до 4,000 символов (юникод символы, переменной длины)       |
| `NTEXT`            | Юникод данные переменной длины, длиной до 1,073,741,823 символов         |
| `BINARY`           | Данные размером до 8,000 байт (фиксированной длины)                      |
| `VARBINARY`        | Данные размером до 8,000 байт (переменной длины)                         |
| `IMAGE`            | Данные размером до 2,147,483,647 байт (переменной длины)                 |
| `TIMESTAMP`        | Уникальные числа, обновляющиеся при каждом изменении строки              |
| `UNIQUEIDENTIFIER` | Глобально-уникальный идентификатор (GUID)                                |
| `CURSOR`           | Объект курсора                                                           |
| `TABLE`            | Промежуточный результат, предназначенный для дальнейшей обработки        |

### PRIMARY KEY / FOREIGN KEY

```sql
CREATE TABLE matches(
    id INT NOT NULL PRIMARY KEY,
    home_team_api_id INT NOT NULL FOREIGN KEY REFERENCES teams(api_id),
    away_team_api_id INT NOT NULL FOREIGN KEY REFERENCES teams(api_id)
    );
```

## REQUEST STRUCTURE

| CMD        | DESCRIPTION                                                                                       |
|------------|---------------------------------------------------------------------------------------------------|
| `SELECT`   | определяет данные для извлечения                                                                  |
| `FROM`     | определяет таблицу для извлечения данных                                                          |
| `WHERE`    | определяет фильтрацию до агрегирования данных                                                     |                                                    
| `GROUP BY` | используется для определения групп выходных строк, к которым могут применяться агрегатные функции |
| `HAVING`   | определяет фильтрацию уже агрегированных данных                                                   |
| `ORDER BY` | определяет порядок вывода строк в запросе                                                         |

### SELECT

```sql
SELECT -- / SELECT DISTINCT
    director,
    movie_title,
    10 - rating AS difference
FROM sql.kinopoisk
```

### FROM

```sql
SELECT *
FROM
    sql.teams,
    sql.matches
```

### WHERE

```sql
SELECT *
FROM sql.kinopoisk
WHERE (rating BETWEEN 8 AND 8.5 OR year < 1990)
    AND overview IS NOT NULL
    AND movie_title NOT LIKE 'Т%'
    AND movie_title LIKE '____________'
```

### GROUP BY

```sql
SELECT
   type1 primary_type,
   count(DISTINCT type2) additional_types_count,
   AVG(hp) avg_hp,
   SUM(attack) attack_sum
FROM sql.pokemon
GROUP BY primary_type
ORDER BY additional_types_count DESC, primary_type
```

### HAVING

```sql
SELECT
    type1, 
    COUNT(*)
FROM sql.pokemon
WHERE attack BETWEEN 50 AND 100 OR defense BETWEEN 50 AND 100
GROUP BY type1
HAVING MAX(hp) <= 125
ORDER BY COUNT(*) DESC
LIMIT 1 OFFSET 4
```

### ORDER BY

```sql
SELECT
    director,
    movie_title
FROM sql.kinopoisk
ORDER BY year, rating DESC -- / ASC
OFFSET 3 LIMIT 1
```

### LIMIT

```sql
SELECT *
FROM sql.kinopoisk
OFFSET 3 LIMIT 5
```

## FUNCTIONS

| FUNCTION [INFO](https://postgrespro.ru/docs/postgrespro/11/functions-aggregate) | DESCRIPTION                                                                   |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `AVG`                                                                           | вычисляет среднее значение                                                    |
| `SUM`                                                                           | вычисляет сумму значений                                                      |
| `MIN`                                                                           | вычисляет наименьшее значение                                                 |
| `MAX`                                                                           | вычисляет наибольшее значение                                                 |
| `COUNT`                                                                         | вычисляет количество записей в таблице                                        |
| `CONCAT`                                                                        | объединение строк                                                             |
| `LENGTH`                                                                        | возвращает количество символов в строке                                       |
| `TRIM`                                                                          | удаляет пробелы в начале и конце строки                                       |
| `SUBSTRING`                                                                     | извлекает подстроку из строки                                                 |
| `REPLACE`                                                                       | заменяет подстроку в строке                                                   |
| `LOWER`                                                                         | переводит символы строки в нижний регистр                                     |
| `UPPER`                                                                         | переводит символы строки в верхний регистр и т.д.                             |
| `ROUND`                                                                         | округляет число                                                               |
| `TRUNCATE`                                                                      | обрезает дробное число до указанного количества знаков после запятой          |
| `CEILING`                                                                       | возвращает наименьшее целое число, которое больше или равно текущему значению |
| `FLOOR`                                                                         | возвращает наибольшее целое число, которое меньше или равно текущему значению |
| `POWER`                                                                         | возводит число в указанную степень                                            |
| `SQRT`                                                                          | возвращает квадратный корень числа                                            |
| `RAND`                                                                          | генерирует случайное число с плавающей точкой в диапазоне от 0 до 1           |
| `CURDATE` `CURRENT_DATE`                                                        | возвращает текущую дату                                                       |
| `CURTIME` `CURRENT_TIME`                                                        | возвращает текущее время                                                      |
| `DAYOFMONTH(date)`                                                              | возвращает день месяца в виде числа                                           |
| `DAYOFWEEK(date)`                                                               | возвращает день недели в виде числа                                           |
| `DAYOFYEAR(date)`                                                               | возвращает номер дня в году                                                   |
| `MONTH(date)`                                                                   | возвращает месяц                                                              |
| `YEAR(date)`                                                                    | возвращает год                                                                |
| `LAST_DAY(date)`                                                                | возвращает последний день месяца в виде даты                                  |
| `HOUR(time)`                                                                    | возвращает час                                                                |
| `MINUTE(time)`                                                                  | возвращает минуты                                                             |
| `SECOND(time)`                                                                  | возвращает секунды                                                            |
| `DATE_ADD(date, interval)`                                                      | выполняет сложение даты и определенного временного интервала                  |
| `DATE_SUB(date, interval)`                                                      | выполняет вычитание из даты определенного временного интервала                |
| `DATEDIFF(date1, date2)`                                                        | возвращает разницу в днях между двумя датами                                  |
| `TO_DAYES(date)`                                                                | возвращает количество дней с 0-го дня года                                    |
| `TIME_TO_SEC(time)`                                                             | возвращает количество секунд с полуночи                                       |
| `DATE_FORMAT(date, format)`                                                     | форматирования даты                                                           |
| `TIME_FORMAT(date, format)`                                                     | форматирования времени                                                        |

#### COUNT / SUM / AVG / MIN / MAX

```sql
SELECT
    COUNT(*) pokemon_count,
    AVG(speed) avg_speed,
    MAX(hp) max_hp,
    MIN(hp) min_hp
FROM sql.pokemon
WHERE type1 = 'Electric'
    AND type2 IS NOT NULL
    AND (attack > 50 OR defense > 50)
```

## OPERATORS

| Operator  | Description                                                                                                                                                                                                                                                                                                                        |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `+`       | Сложение                                                                                                                                                                                                                                                                                                                           |
| `-`       | Вычитание                                                                                                                                                                                                                                                                                                                          |
| `*`       | Умножение                                                                                                                                                                                                                                                                                                                          |
| `/`       | Деление                                                                                                                                                                                                                                                                                                                            |
| `%`       | Деление с остатком                                                                                                                                                                                                                                                                                                                 |
| `=`       | Определяет равенство                                                                                                                                                                                                                                                                                                               |
| `!=`      | Определяет неравенство                                                                                                                                                                                                                                                                                                             |
| `<>`      | Определяет неравенство                                                                                                                                                                                                                                                                                                             |
| `>`       | Больше                                                                                                                                                                                                                                                                                                                             |
| `<`       | Меньше                                                                                                                                                                                                                                                                                                                             |
| `>=`      | Больше или равно                                                                                                                                                                                                                                                                                                                   |
| `<=`      | Меньше или равно                                                                                                                                                                                                                                                                                                                   |
| `!<`      | Не меньше                                                                                                                                                                                                                                                                                                                          |
| `!>`      | Не больше                                                                                                                                                                                                                                                                                                                          |
| `ALL`     | Сравнивает все значения                                                                                                                                                                                                                                                                                                            |
| `AND`     | Объединяет условия                                                                                                                                                                                                                                                                                                                 |
| `ANY`     | Сравнивает одно значение с другим, если последнее совпадает с условием                                                                                                                                                                                                                                                             |
| `BETWEEN` | Проверяет вхождение значения в диапазон от минимального до максимального                                                                                                                                                                                                                                                           |
| `EXISTS`  | Определяет наличие строки, соответствующей определенному критерию                                                                                                                                                                                                                                                                  |
| `IN`      | Выполняет поиск значения в списке значений                                                                                                                                                                                                                                                                                         |
| `NOT`     | Инвертирует (меняет на противоположное) смысл других логических операторов                                                                                                                                                                                                                                                         |
| `OR`      | Комбинирует условия (одно из условий должно совпадать)                                                                                                                                                                                                                                                                             |
| `IS NULL` | Определяет, является ли значение нулевым                                                                                                                                                                                                                                                                                           |
| `UNIQUE`  | Определяет уникальность строки                                                                                                                                                                                                                                                                                                     |
| `LIKE`    | Сравнение значений с помощью операторов с подстановочными знаками. Существует два вида таких операторов: проценты (%) нижнее подчеркивание (_) % означает 0, 1 или более символов. _ означает точно 1 символ.                                                                                                                      |
| `REGEX`   | Определить регулярное выражение, которому должна соответствовать запись. В регулярное выражении могут использоваться следующие специальные символы: `^` — начало строки `$` — конец строки `.` — любой символ `[symbol]` — любой из указанных в скобках символов `[start-end]` — любой символ из диапазона `I` — разделяет шаблоны |

## JOIN OPERATIONS

| JOIN TYPE      | DESCRIPTION                                                                                                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `JOIN`         | оператор SQL, который позволяет соединять таблицы по условию                                                                                                                                                                                                                                                               |
| `INNER JOIN`   | присоединяются только те строки таблиц, которые удовлетворяют условию соединения. Если в любой из соединяемых таблиц находятся такие строки, которые не удовлетворяют заявленному условию, — они отбрасываются.                                                                                                            |
| `LEFT JOIN`    | из левой (относительно оператора) таблицы сохраняются все строки, а из правой добавляются только те, которые соответствуют условию соединения. Если в правой таблице не находится соответствия, то значения строк второй таблицы будут иметь значение `NULL`.                                                              |
| `RIGHT JOIN`   | При использовании `RIGHT JOIN` сохраняется та же логика, что и для `LEFT JOIN`, только за основу берётся правая таблица                                                                                                                                                                                                    |
| `FULL JOIN`    | `FULL OUTER JOIN` объединяет в себе `LEFT JOIN` и `RIGHT JOIN` и позволяет сохранить кортежи обеих таблиц. Даже если не будет соответствий, мы сохраним все записи из обеих таблиц. <br> `FULL OUTER JOIN` может быть полезен в ситуациях, когда схема данных недостаточно нормализована и не хватает таблиц-справочников. |
| `CROSS JOIN`   | `CROSS JOIN` соединяет таблицы так, что каждая запись в первой таблице присоединяется к каждой записи во второй таблице, иначе говоря, даёт декартово произведение.                                                                                                                                                        |
| `NATURAL JOIN` | ключевое слово `NATURAL` в начале оператора `JOIN` позволяет не указывать условие соединения таблиц — для соединения будут использованы столбцы с одинаковым названием из этих таблиц                                                                                                                                      |
| `SELF JOIN`    | сравнения записей внутри одной и той же таблицы                                                                                                                                                                                                                                                                            |

### INNER JOIN

![](inner_.png)

```sql
SELECT
    m.id,
    t1.short_name home_short,
    t2.short_name away_short
FROM
    sql.matches m
    JOIN sql.teams t1 ON m.home_team_api_id = t1.api_id
    JOIN sql.teams t2 ON m.away_team_api_id = t2.api_id
ORDER BY 1
```

### LEFT JOIN

![](left_.png)

```sql
SELECT
    DISTINCT t.long_name
FROM
    sql.teams t
    LEFT JOIN sql.matches m ON t.api_id = m.home_team_api_id or t.api_id = m.away_team_api_id
WHERE 
    m.id is not null
ORDER BY 1
```

### RIGHT JOIN

![](right_.png)

```sql
SELECT
    DISTINCT t.long_name
FROM
    sql.matches m 
    RIGHT JOIN sql.teams t ON t.api_id = m.home_team_api_id or t.api_id = m.away_team_api_id
WHERE 
    m.id is not null
ORDER BY 1
```

### FULL JOIN

![](full_.PNG)

```sql
SELECT
    t.long_name,
    m.id
FROM
    sql.teams t
    FULL JOIN sql.matches m on t.api_id = m.home_team_api_id
ORDER BY
    m.id DESC
```

### CROSS JOIN

![](cross_.PNG)

```sql
SELECT
    DISTINCT
    t1.short_name home_team,
    t2.short_name away_team
FROM
    sql.teams as t1
    CROSS JOIN sql.teams as t2
WHERE 
    t1.id != t2.id
ORDER BY 
    1, 2
```

### NATURAL JOIN

```sql
SELECT
    t1.short_name home_team,
    t2.short_name away_team
FROM
    sql.teams as t1
    NATURAL JOIN sql.teams as t2
```

### SELF JOIN

```sql
SELECT
    t1.short_name home_team,
    t2.short_name away_team
FROM
    sql.teams as t1
    JOIN sql.teams as t2 on t1.id = t2.id
```

## TYPIFICATION

```sql
SELECT
    s.ship_date::TEXT date_period,
    COUNT(s.ship_id) cnt_shipment
FROM sql.shipment s
GROUP BY s.ship_date
UNION ALL
SELECT
    'total_shipments',
    COUNT(s.ship_id)
FROM sql.shipment s
ORDER BY cnt_shipment DESC
```

## UNION

| UNION TYPE  | DESCRIPTION                                                                                                                                                                                                                                                                                  |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UNION`     | присоединяет любой результат запроса к другому «снизу» при условии, что у них одинаковая структура, а именно: <br> 1. одинаковый тип данных; <br> 2. одинаковое количество столбцов; <br> 3. одинаковый порядок столбцов согласно типу данных. <br> `UNION` выводит только уникальные записи |
| `UNION ALL` | `UNION ALL` присоединяет все строки последующих таблиц к предыдущим, без ограничений по уникальности                                                                                                                                                                                         |

```sql
SELECT c.city_name object_name, 'city' object_type
FROM sql.city 
UNION
SELECT c.state, 'state'
FROM sql.city c
UNION
SELECT d.first_name, 'driver'
FROM sql.driver d
UNION
SELECT t.make, 'truck'
FROM sql.truck t
ORDER BY object_name, object_type
```

```sql
SELECT
    c.city_name,
    c.state,
    'доставка осуществлялась' shipping_status
FROM 
    sql.city c
    LEFT JOIN sql.shipment s on c.city_id = s.city_id
WHERE s.city_id IS NOT NULL
UNION
SELECT
    c.city_name,
    c.state,
    'доставка не осуществлялась' shipping_status
FROM sql.city c
    LEFT JOIN sql.shipment s on c.city_id = s.city_id
WHERE s.city_id IS NULL
ORDER BY city_name, state, shipping_status
```

```sql
SELECT
    c.city_name AS city_name,
    COUNT(s.ship_id) shippings_fake
FROM
    sql.city c
    JOIN sql.shipment s ON c.city_id=s.city_id
GROUP BY
    c.city_name
HAVING
     COUNT(s.ship_id) > 10
UNION
SELECT
    c.city_name AS city_name,
    COUNT(s.ship_id)+5 shippings_fake
FROM
    sql.city c
    JOIN sql.shipment s ON c.city_id=s.city_id
GROUP BY
    c.city_name
HAVING
     COUNT(s.ship_id) <= 10
ORDER BY
    shippings_fake desc,
    city_name asc
```

```sql
SELECT 1000000 column
UNION 
SELECT 541 column
UNION
SELECT -500 column
UNION 
SELECT 100 column
ORDER BY 1 DESC
LIMIT 1
```

## EXCEPT

## INTERSECT