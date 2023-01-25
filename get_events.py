import requests
from bs4 import BeautifulSoup


def get_html(html: str) -> str:

    """Функция принимает на вход строку с url и
    возвращает html-страницу.
    Если по каким-то причинам функции не удалось получить ответ от
    запрашиваемого адреса, то функция вернёт ответ "Сетевая ошибка".
    """

    try:
        result = requests.get(html)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_python_events(html):

    """Функция парсит html, по заданным параметрам,
    полученный из функции get_html() и возвращает
    запрашиваемый фрагмент в текстовом формате, без html тэгов.
    """

    soup = BeautifulSoup(html, 'html.parser')
    news_list = soup.find('ul', class_="list-recent-events menu")
    return news_list.get_text()


def text_format(text: str) -> str:

    """Функция форматирует текст полученный из
    функции get_python_events() и выводит в консоль
    информацию о предстоящих ивентах с сайта python.org
    """

    prepare = text.strip().split('\n\n\n\n')
    for row in prepare:
        print(row.strip().replace('\n', ' '), '\n')


if __name__ == "__main__":
    html = get_html("https://www.python.org/events/")
    text = get_python_events(html)
    text_format(text)
