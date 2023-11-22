# Продуктовый помощник Foodgram - дипломный проект студента 63 когорты Яндекс.Практикум Сухарева Н.Р.

## Описание проекта Foodgram

«Продуктовый помощник»: приложение, на котором пользователи публикуют рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в свое избранное.
Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд согласно рецепта/ов.
Сайт доступен по адресу: seritofood.hopto.org

## Запуск с использованием CI/CD и Docker

```bash
# В Settings - Secrets and variables создаем переменный с вашими данными
# Это необходимо для работы с CI/CD, DockerHub, GitHub
ALLOWED_HOSTS
DB_ENGINE
DB_HOST
DB_PORT
HOST
MY_LOGIN
MY_PASS
PASSPHRASE
POSTGRES_DB
POSTGRES_PASSWORD
POSTGRES_USER
SECRET_KEY
SSH_KEY
USER
```

Все действия будем выполнять в Docker, docker compose как на локальной машине так и на сервере ВМ Yandex.Cloud.
Предварительно установим на ВМ в облаке необходимые компоненты для работы:

```bash
# username - ваш логин, ip - ip ВМ под управлением Linux Дистрибутива с пакетной базой deb.
ssh username@ip
```

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
```

```bash
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
```

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker compose
```

```bash
sudo chmod +x /usr/local/bin/docker compose
```

```bash
sudo systemctl start docker.service && sudo systemctl enable docker.service
```

Всё, что нам нужно, установлено, далее, создаем папку /infra в домашней директории /home/username/:

```bash
cd ~
```

```bash
mkdir infra
```

Предварительно из папки /backend и /frontend загрузим актуальные данные на DockerHub (на вашем ПК) (seritothemaid - ваш логин на DH):

```bash
docker login -u seritothemaid
```

```bash
cd backend
```

```bash
docker build -t seritothemaid/foodgram_backend:latest .
```

```bash
docker push seritothemaid/foodgram_backend:latest
```

```bash
cd ..
```

```bash
cd frontend
```

Готовим фронт для приложения, это заготовка для отправки на DH (где seritothemaid ваш логин на DH):
```bash
docker build -t seritothemaid/foodgram_frontend:latest .
```

Отправляем на DG:
```bash
docker push seritothemaid/foodgram_frontend:latest
```

Перенести файлы docker-compose.yml и default.conf на сервер, из папки infra в текущем репозитории (на вашем ПК).

```bash
cd infra
```

```bash
scp docker-compose.yml username@server_ip:/home/username/
```

```bash
scp default.conf username@server_ip:/home/username/
```

Так же, создаем файл .env в директории infra на ВМ:

```bash
touch .env
```

Заполнить в настройках репозитория секреты .env, необходимы для работы postgres в docker

```python
DB_ENGINE='django.db.backends.postgresql'
POSTGRES_DB='foodgram' # Задаем имя для БД.
POSTGRES_USER='foodgram_u' # Задаем пользователя для БД.
POSTGRES_PASSWORD='foodgram_u_pass' # Задаем пароль для БД.
DB_HOST='db'
DB_PORT='5432'
SECRET_KEY='secret'  # Задаем секрет.
ALLOWED_HOSTS='127.0.0.1, backend' # Вставляем свой IP сервера.
DEBUG = False
```

На этом настройка закончена, далее в папке infra выполняем команду:

```bash
docker compose up -d --build
```

Проект запустится на ВМ и будет доступен по указанному вами адресу либо IP. Завершение настройки на ВМ:

В папке infra выполняем команду, что бы собрать контейнеры:

Остановить: 

```bash
docker compose stop
```

Удалить вместе с volumes:

```bash
# Все данные удалятся!
docker compose down -v
``` 

Для доступа к контейнеру backend и сборки финальной части выполняем следующие команды:

```bash
docker compose exec backend python manage.py makemigrations
```

```bash
docker compose exec backend python manage.py migrate --noinput
```

```bash
docker compose exec backend python manage.py createsuperuser
```

```bash
docker compose exec backend python manage.py collectstatic --no-input
```

Дополнительно можно наполнить DB ингредиентами и тэгами:

```bash
docker compose exec backend python manage.py import_csv
```

```bash
docker compose exec backend python manage.py import_tags
```

На этом всё, продуктовый помощник запущен, можно наполнять его рецептами и делится с друзьями!
Автор: Сухарев Н.Р.
