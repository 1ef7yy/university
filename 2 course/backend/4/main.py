import requests
from PIL import Image
from io import BytesIO


def get_articles_titles():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()
        for article in articles[:5]:
            print(article["title"])
    else:
        print(f"Ошибка: {response.status_code}")


def check_site_availability():
    url = input("Введите URL сайта: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Сайт доступен")
        else:
            print(f"Сайт недоступен. Код состояния: {response.status_code}")
    except requests.exceptions.RequestException:
        print("Ошибка подключения")


def print_http_headers():
    url = input("Введите URL: ")
    response = requests.get(url)
    print("Заголовки ответа:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")


def download_random_image():
    url = "https://picsum.photos/200/300"
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save("random_image.jpg")
        print("Изображение сохранено как random_image.jpg")
    else:
        print(f"Ошибка: {response.status_code}")


def send_post_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=data)
    print(f"Ответ сервера: {response.json()}")


def register_user():
    url = "https://jsonplaceholder.typicode.com/users"
    user_data = {
        "name": input("Введите имя: "),
        "username": input("Введите имя пользователя: "),
        "email": input("Введите email: ")
    }
    response = requests.post(url, json=user_data)
    if response.status_code == 201:
        print("Пользователь успешно зарегистрирован")
    else:
        print(f"Ошибка регистрации: {response.status_code}")


def send_user_input():
    url = "https://jsonplaceholder.typicode.com/posts"
    title = input("Введите заголовок: ")
    body = input("Введите текст: ")
    data = {"title": title, "body": body, "userId": 1}
    response = requests.post(url, json=data)
    print(f"Ответ сервера: {response.json()}")


def get_weather():
    api_key = "9a0e4ffe23b84856975e1e4a72d739bb"
    city = input("Введите город: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Температура: {weather_data['main']['temp']}°C")
    else:
        print(f"Ошибка: {response.status_code}")


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        price_data = response.json()
        print(f"Текущий курс Bitcoin: ${price_data['bitcoin']['usd']}")
    else:
        print(f"Ошибка: {response.status_code}")


def get_github_repos():
    username = input("Введите имя пользователя GitHub: ")
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        print(f"Репозитории пользователя {username}:")
        for repo in repos:
            print(repo["name"])
    else:
        print(f"Ошибка: {response.status_code}")


def check_404_error():
    url = input("Введите URL для проверки: ")
    response = requests.get(url)
    if response.status_code == 404:
        print("Страница не найдена")
    else:
        print(f"Страница существует. Код состояния: {response.status_code}")


def check_redirect():
    url = input("Введите URL для проверки редиректа: ")
    response = requests.get(url, allow_redirects=False)
    if 300 <= response.status_code < 400:
        print(f"Редирект на: {response.headers['Location']}")
    else:
        print("Редирект не обнаружен")


def main():
    while True:
        print("\n1. Работа с GET-запросами")
        print("2. Работа с POST-запросами")
        print("3. Работа с публичными API")
        print("4. Обработка ошибок и редиректов")
        print("5. Выход")

        choice = input("Выберите раздел: ")

        if choice == "1":
            print("\n1. Получение данных с сайта")
            print("2. Проверка доступности сайта")
            print("3. Вывод HTTP-заголовков")
            print("4. Получение случайного изображения")
            print("5. Назад")

            sub_choice = input("Выберите программу: ")

            if sub_choice == "1":
                get_articles_titles()
            elif sub_choice == "2":
                check_site_availability()
            elif sub_choice == "3":
                print_http_headers()
            elif sub_choice == "4":
                download_random_image()
            elif sub_choice == "5":
                continue

        elif choice == "2":
            print("\n1. Отправка данных на сервер")
            print("2. Регистрация пользователя")
            print("3. Чтение введённых данных")
            print("4. Назад")

            sub_choice = input("Выберите программу: ")

            if sub_choice == "1":
                send_post_data()
            elif sub_choice == "2":
                register_user()
            elif sub_choice == "3":
                send_user_input()
            elif sub_choice == "4":
                continue

        elif choice == "3":
            print("\n1. Получение прогноза погоды")
            print("2. Получение данных о криптовалюте")
            print("3. Получение списка репозиториев GitHub")
            print("4. Назад")

            sub_choice = input("Выберите программу: ")

            if sub_choice == "1":
                get_weather()
            elif sub_choice == "2":
                get_bitcoin_price()
            elif sub_choice == "3":
                get_github_repos()
            elif sub_choice == "4":
                continue

        elif choice == "4":
            print("\n1. Обработка 404 ошибки")
            print("2. Проверка редиректа")
            print("3. Назад")

            sub_choice = input("Выберите программу: ")

            if sub_choice == "1":
                check_404_error()
            elif sub_choice == "2":
                check_redirect()
            elif sub_choice == "3":
                continue

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
