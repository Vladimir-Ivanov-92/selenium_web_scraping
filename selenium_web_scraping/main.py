import time

from bs4 import BeautifulSoup
from selenium import webdriver
from services.write_to_csv_table import (create_column_headers_in_csv_table,
                                         write_data_in_csv_table)

from settings import config


# Выгрузка страницы сайта в отдельный HTML файл:
def get_html_page_selenium(url_for_parsing, path_to_save_html_file) -> None:
    options = webdriver.FirefoxOptions()
    options.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    options.headless = True

    try:
        driver = webdriver.Firefox(
            executable_path=config.executable_path,
            options=options
        )
        driver.get(url=url_for_parsing)
        time.sleep(5)
        # Запись данных в файл:
        with open(path_to_save_html_file, "w") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# Парсинг HTML страницы из файла и запись в csv файл:
def record_data_in_csv_file(path_to_save_html_file, path_to_result_csv_file) -> None:
    # Открытие сохраненой копии страницы сайта с необходимыми данными:
    with open(path_to_save_html_file, "r") as file:
        src = file.read()

    # Создание экземпляра объекта bs4:
    soup = BeautifulSoup(src, "lxml")

    # Создание заголовков столбцов в csv таблице:
    create_column_headers_in_csv_table(soup, path_to_result_csv_file)

    # Запись данных в csv файл:
    write_data_in_csv_table(soup, path_to_result_csv_file)


def get_data_to_csv_from_url(url_for_parsing, path_to_save_html_file,
                             path_to_result_csv_file) -> None:
    get_html_page_selenium(url_for_parsing, path_to_save_html_file)
    record_data_in_csv_file(path_to_save_html_file, path_to_result_csv_file)


if __name__ == '__main__':
    get_data_to_csv_from_url(config.url_for_parsing, config.path_to_save_html_file,
                             config.path_to_result_csv_file)
