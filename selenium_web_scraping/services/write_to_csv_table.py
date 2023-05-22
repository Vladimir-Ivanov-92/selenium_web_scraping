import csv


def create_column_headers_in_csv_table(bs4_object, path_to_result_csv_file) -> None:
    data_title = bs4_object.find("div", class_="Cells").find_all("p")

    article = "Артикул"
    name_description = data_title[0].text
    amount = data_title[1].text
    price = data_title[2].text

    with open(path_to_result_csv_file, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                article,
                name_description,
                amount,
                price
            )
        )


def write_data_in_csv_table(bs4_object, path_to_result_csv_file):
    # Получение количества строк(кол-ва объектов для записи):
    data_len = bs4_object.find_all("div", class_="Item-title")

    # Получение данных
    data_products_name_description = bs4_object.find_all("div", class_="Item-title")
    data_products_amount = bs4_object.find_all("div", class_="Item-center")
    data_products_price = bs4_object.find_all("div", class_="Item-price")

    # Запись в файл данных по объектам
    for i in range(len(data_len)):
        article_value = data_products_name_description[i].text.split(" ")[0]
        name_description_value = " ".join(
            data_products_name_description[i].text.split(" ")[1:])
        amount_value = data_products_amount[i].text
        price_value = data_products_price[i].text
        with open(path_to_result_csv_file, "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    article_value,
                    name_description_value,
                    amount_value,
                    price_value
                )
            )
