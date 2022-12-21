import requests
import time
import datetime
from decimal import Decimal


# Получение JSON данных, возвращаемых при переходе по указанному url с headers, cookies
def get_json_with_headers_cookies(url, my_headers, my_cookies, url_referer):
    try:
        step = 1
        error_message = ''
        my_headers['referer'] = url_referer
        r = requests.get(url, headers = my_headers, cookies = my_cookies)
        step = 2
        max_try = 10 # Максимальное количество попыток соединения с сайтом
        cur_try = 0 # Номер текущей попытки соединения с сайтом
        # Статус код 429 - Слишком много запросов
        while r.status_code == 429 and cur_try < max_try:
            print(r.status_code)
            step = 3
            time.sleep(1)
            r = requests.get(url, headers = my_headers, cookies= my_cookies)
            step = 4
            cur_try += 1
        # Обработка ошибки, что не получен ответ от сайта за максимальное количество попыток или ответ пустой
        if cur_try >= max_try or r.status_code == 400:
            error_message = f'ошибка в get_json_with_headers_cookies на шаге {step}: Не удалось получить ответ от сайта {url} за {max_try} попыток (Статус: {r.status_code})'
            return 1, error_message
        data = r.json()
        step = 5
        time.sleep(0.5)
        return data, error_message
    except Exception as err:
        error_message = f'ошибка в get_json_with_headers_cookies на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message

# Получение JSON данных, возвращаемых при переходе по указанному url
def get_json(url):
    try:
        step = 1
        error_message = ''
        r = requests.get(url)
        step = 2
        max_try = 10 # Максимальное количество попыток соединения с сайтом
        cur_try = 0 # Номер текущей попытки соединения с сайтом
        while r.status_code != 200 and cur_try < max_try:
            step = 3
            time.sleep(1)
            r = requests.get(url)
            step = 4
            cur_try += 1
        # Обработка ошибки, что не получен ответ от сайта за максимальное количество попыток
        if cur_try >= max_try:
            error_message = f'ошибка в get_json на шаге {step}: Не удалось получить ответ от сайта {url} за {max_try} попыток'
            return 1, error_message
        data = r.json()
        step = 5
        return data, error_message
    except Exception as err:
        error_message = f'ошибка в get_json на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message

# Возвращает JSON словарь с данными, которые нужно добавить в MySQL
def get_missing_data_to_insert(connection, json_data, json_key_field, mysql_table_name, mysql_column_id_name):
    try:
        step = 1
        error_message = ''
        if len(json_data) > 0:
            get_data_string = ""
            for i in range(len(json_data)):
                step = 2
                get_data_string += f"{mysql_column_id_name} = '{json_data[i][json_key_field]}' or "
            get_data_string = get_data_string[0:-3]
            get_data_string += ";"
            step = 3
            with connection.cursor() as cursor:
                request = f"SELECT * FROM `{str(connection.db)[2:-1]}`.`{mysql_table_name}` WHERE " + \
                    get_data_string
                step = 4
                cursor.execute(request)
                data_by_odid = cursor.fetchall()
                step = 5
            data_to_insert = []
            for i in range(len(json_data)):
                step = 6
                data_exist_flag = False
                for j in range(len(data_by_odid)):
                    step = 7
                    if not data_exist_flag and json_data[i][json_key_field] == data_by_odid[j][json_key_field]:
                        data_exist_flag = True
                if data_exist_flag == False:
                    step = 8
                    data_to_insert.append(json_data[i])
                    step = 9
        return data_to_insert, error_message
    except Exception as err:
        error_message = f'ошибка в get_missing_data_to_insert на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message

# Меняет все значения указанного столбца на их id по данным из mySQL.
# Требуется указать имя таблицы в mysql, имя столбца с id, имя столбца с значениями
def replace_data_name_to_data_id(connection, json_data, json_column_name, mysql_table_name, mysql_column_id_name, mysql_column_name_name):
    try:
        error_message = ''
        step = 1
        with connection.cursor() as cursor:
            request = f"SELECT * FROM `{str(connection.db)[2:-1]}`.`{mysql_table_name}`"
            step = 2
            cursor.execute(request)
            work_data = cursor.fetchall()
            step = 3
            for i in range(len(work_data)):
                step = 4
                for j in range(len(json_data)):
                    step = 5
                    if json_data[j][json_column_name] == work_data[i][mysql_column_name_name]:
                        json_data[j][json_column_name] = work_data[i][mysql_column_id_name]
                        step = 6
        return json_data, error_message
    except Exception as err:
        error_message = f'ошибка в replace_data_name_to_data_id на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message
    
# Замена всех значений указанного столбца с True на 1, с False на 0
def replace_bool_to_int(data, column_name_json):
    try:
        step = 1
        error_message = ''
        for i in range(len(data)):
            if data[i][column_name_json] == True:
                data[i][column_name_json] = 1
                step = 2
            else:
                data[i][column_name_json] = 0
                step = 3
        return data, error_message
    except Exception as err:
        error_message = f'ошибка в replace_bool_to_int на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message
    
# Формирование списка со всеми данными из запроса JSON по указанному имени поля
def get_data_list_from_json(json_data, json_key):
    try:
        step = 1
        error_message = ''
        work_list = []
        for i in range(len(json_data)):
            step = 2
            try:
                work_list.append(json_data[i][json_key])
                step = 3
            except KeyError:
                pass
        return work_list, error_message
    except Exception as err:
        error_message = f'ошибка в get_data_list_from_json на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message
    
  
# Поиск данных, которые требуется обновить в MySQL
# Возвращает JSON словарь с данными, которые нужно добавить в MySQL
def get_data_to_update(connection, json_data, json_key_field, mysql_table_name, mysql_column_id_name):
    try:
        step = 1
        error_message = ''
        data_to_update = []
        get_data_string = ''
        update_counter = 0
        max_json_index = range(len(json_data))
        for i in max_json_index:
            step = 2
            get_data_string += f" ({mysql_column_id_name} = '{json_data[i][json_key_field]}' AND NOT lastChangeDate = '{json_data[i]['lastChangeDate'][0:19].replace('T', ' ')}') OR"
            update_counter += 1
            if update_counter >= 100 or i == max_json_index:
                step = 3
                get_data_string = get_data_string[0:-2]
                with connection.cursor() as cursor:
                    request = f"SELECT {mysql_column_id_name} FROM `{str(connection.db)[2:-1]}`.`{mysql_table_name}` WHERE" + get_data_string
                    step = 4
                    cursor.execute(request)
                    data_to_update_dict = cursor.fetchall()
                    step = 5
                    for j in range(len(data_to_update_dict)):
                        data_to_update.append(data_to_update_dict[j][json_key_field])
                        step = 6
                get_data_string = ''
                update_counter = 0
        data_to_update = list(set(data_to_update))
        return data_to_update, error_message
    except Exception as err:
        error_message = f'ошибка в get_data_to_update на шаге {step}: ' + str(err).replace("'", "")
        return 1, error_message
   
