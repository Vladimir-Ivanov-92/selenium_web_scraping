from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    executable_path: str
    url_for_parsing: str
    path_to_save_html_file: str
    path_to_result_csv_file: str

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        # (относительно текущей рабочей директории)
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'


# При импорте файла сразу создастся и провалидируется объект конфига,
# который можно далее импортировать
config = Settings()
