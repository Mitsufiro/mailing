<div id="badges" align='center'>
    <a>
        <img src="https://img.shields.io/badge/Python-3.10-green?logo=Python">
    </a>
    <a>
        <img src="https://img.shields.io/badge/FastAPI-0.73.0-green?logo=fastapi&logoColor=black?style=plastic"/>
    </a>
    <a>
        <img src="https://img.shields.io/badge/alembic-1.9.0-green?logo=alembic&logoColor=black?style=plastic">
    </a>
    <a>
        <img src="https://img.shields.io/badge/postgresql-14.6-blue?logo=postgresql&logoColor=white">
    </a>
    <a>
        <img src="https://img.shields.io/badge/SQLalchemy-1.4.45-blue?logo=SQLalchemy">
    </a>
    <a>
        <img src="https://img.shields.io/badge/RabbitMQ-3.9.11-red?logo=RabbitMQ&logoColor=red">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Celery-5.2.7-green?logo=Celery&logoColor=green">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Flower-1.0.0-yellow?logo=Flower">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Docker-20.10.16-green?logo=Docker&logoColor=black?style=plastic">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Traefik-blue?logo=traefik&logoColor=black?style=plastic">
    </a>
</div>

# Cервис управления рассылками API администрирования и получения статистики.

• Реализованы методы создания рассылок, просмотра созданных и получения статистики по выполненным рассылкам.

• Реализован сам сервис отправки уведомлений на почту пользователей.

• Реализован ролевой доступ к API-методам в зависимости от уровня прав пользователя.

• Настроена валидация данных.

• Подготовлен docker-контейнер с сервисами.

• Настроен Traefik.

• Сервис находится по адресу: [https://encryptedmailing.online/docs#/](https://encryptedmailing.online/docs#/)

**Спроектированы и реализованы API для:**

• Добавления нового клиента в справочник со всеми его атрибутами

• Обновления данных атрибутов клиента

• Удаления клиента из справочника

• Добавления новой рассылки со всеми её атрибутами

• Получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам

• Получения детальной статистики отправленных сообщений по конкретной рассылке

• Обновления атрибутов рассылки

• Удаления рассылки

• Обработки активных рассылок и отправки сообщений клиентам

**Логика рассылки:**

• После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - должны быть выбраны из справочника все клиенты, которые подходят под значения фильтра, указанного в этой рассылке и запущена отправка для всех этих клиентов.

• Если создаётся рассылка с временем старта в будущем - отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.

• По ходу отправки сообщений собирается статистика по каждому сообщению для последующего формирования отчётов.

• Клонируем репозиторий:

    git clone https://github.com/Mitsufiro/fastapi_celery

• Разворачиваем контейнер:

    docker-compose up
• Создаем миграцию:

    docker exec fastapi_celery_web_1 alembic revision --autogenerate -m "New Migration"
____________________________
    docker exec fastapi_celery_web_1 alembic upgrade head

• Создайте админ-пользователя:

![alt text](screens/create_user.png)

• Определите своему пользователю права администатора id: 1 role: admin

![alt text](screens/admin_role.png)

• Авторизуйтесь

![alt text](screens/auth_1.png)
![alt text](screens/auth_2.png)

• Создайте клиентов введя номер телефона, произвольный тег и существующую почту чтобы убедиться что рассылка работает.

![alt text](screens/create_client.png)

• Метод внесения изменений клиенту.

![alt text](screens/change_client.png)

• Теперь можно создать рассылку.

![alt text](screens/create_mailing.png)

![alt text](screens/mailing_done.png)

• Проверяем почту.

![alt text](screens/Chek.png)

