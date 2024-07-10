# CI/CD

### Создание и регистрация docker runner

```cmd
docker volume create gitlab-runner-config
```

```cmd
docker run -d --name shift-gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

```cmd
docker exec -it shift-gitlab-runner gitlab-runner register
```

### Настройка gitlab-ci.yml

```yml
image: python:3.12

stages:
  - lint
  - test

before_script:
  - pip install poetry
  - poetry config virtualenvs.create true
  - poetry config virtualenvs.in-project true
  - poetry install --all-extras --compile --no-root

Flake8:
  stage: lint
  script:
    - poetry run flake8 src/app
  only:
    - merge_requests

Mypy:
  stage: lint
  script:
    - poetry run mypy src/app
  only:
    - merge_requests

Pytest:
  stage: test
  script:
    - export PYTHONPATH=$PYTHONPATH:/.../.../.../.../.../.../src
    - poetry run pytest
  only:
    - merge_requests
```
