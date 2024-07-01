# DOCKER

## DOCKERFILE

Dockerfile - это скрипт, который содержит инструкции для создания образа Docker. Он определяет базовый образ для создания вашего собственного, устанавливает переменные среды, программное обеспечение и настраивает контейнер для конкретьного приложения или сервиса

### DOCKERFILE SYNTAX

#### FROM

Указывает базовый образ для образа Docker

```docker
FROM image_name: tag
#Example
FROM ubuntu:20.04
```

#### WORKDIR

Устанавливает рабочую директорию (папку) для последующих инструкций.

```docker
WORKDIR /path/to/directory
#Example
WORKDIR /app
```

#### COPY

Копирует файлы или католги из контекста сборки образа в контейнер. Из OC, где лежит Dockerfile, на OC образа, который собирает этот Dockerfile.

```docker
COPY host_source_path container_destination_path
#Example
COPY ..
```

#### RUN

Выполняет консольные команды на OC образа.

```docker
RUN command1 && comand2
#Example
RUN apt-get update && apt-get install -y curl
```

#### ENV

Устанавливает переменные окружения в образе

```docker
ENV KEY=VALUE
#Example
ENV NODE_VERSION=14
```

#### EXPOSE

Сообщает Docker, что контейнер слушает указанные сетевые порты во время выполнения.

```docker
EXPOSE port
#Example
EXPOSE port 8080
```

#### CMD

Представляет консольные команды или параметры для запуска по умолчанию для выполняемого контейнера

```docker
CMD ["executable","param1","param2"]
#Example
CMD ["nmp","start"]
```

```docker
CMD executable param1 param2
#Example
CMD npm run dev
```

#### ARG

Определяет перменные который пользователи могу передать на этапе сборки билдеру с помоцью команды docker build

```docker
ARG VARIABLE_NAME=default_value
#Example
ARG VERSION=latest
```

#### ENTRYPOINT

Настроить контейнер для выполнения как испоняемого файла. Устанавливает перменные окружения в образе.

```docker
ENTRYPOIN ["executable", "param1", "param2"]
#Example
ENTRYPOINT ["node", "app.js"]
```

```docker
ENTRYPOINT executable param1 param2
#Example
ENTRYPOINT node app.js
```

#### VOLUME

Создает точку размещения внешних volumes или других контейнеров

```docker
VOLUME /path/to/volume
#Example
VOLUME /data
```

#### LABEL

Добавляет метаданные к образу в виде пар ключ-значение

```docker
LABEL key="value"
#Example
LABEL version="1.0" maintainer="Adrian"
```

#### USER

Указывает имя пользователя или UID для использования при запуске образа

```docker
USER user_name
#Example
USER app
```

#### ADD

Копирует файлы или директории и может извлекать архивы в процессе сборки

```docker
ADD source_path destination_path
#Example
ADD ./app.tar.gz /app
```

Похоже на `COPY`, но с дополнительными возможностями, напрмер, извлечение архивов.

### DOCKERFILE EXAMPLE

```docker
# Использовать официальный образ Node.js в качестве базового
FROM node:20-alpine

# Установить рабочую директорию в /app
WORKDIR /app

# Копировать package.json и package-lock.json в рабочую директорию
COPY package*.json ./

# Копировать содержимое текущей директории в контейнер в /app
COPY . .

# Открыть порт 8080 для внешнего мира
EXPOSE 8080

# Определить переменную среды
ENV NODE_ENV=production

# Запустить app.js при старте контейнера
CMD node app.js
```

## DOCKER COMPOSE

Docker Compose - это YAML файл, который определяет многоконтейнерное приложение Docker. Он указывает сервисы, сети и volumes для придложения, а также любые дополнительные опции конфигурации


### DOCKER COMPOSE SYNTAX

#### version

Укзаывает версию формата файла Docker Compose

```docker
version: '3.8'
```

#### services

Определяет сервисы/контейнеры, которые составляют приложение

```docker
networks:
    my_network:
        driver: bridge
```

#### command
Переопределяет команду запуска по умолчанию, указанную в образе Docker

```docker
command: ["npm", "start"]
```

