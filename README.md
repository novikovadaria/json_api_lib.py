# Модуль для работы с json 

## Получение JSON данных, возвращаемых при переходе по указанному url с headers, cookies
get_json_with_headers_cookies(url, my_headers, my_cookies, url_referer)

url - основная ссылка для запроса, my_headers - headers, my_cookies - куки, url_referer - референтная ссылка

## Получение JSON данных, возвращаемых при переходе по указанному url
get_json(url)

url - основная ссылка для запроса

## Возвращает JSON словарь с данными, которые нужно добавить в MySQL
get_missing_data_to_insert(connection, json_data, json_key_field, mysql_table_name, mysql_column_id_name)

connection - соединение с бд, json_data - словарь json, json_key_field - название ключей в json, mysql_column_id_name - название столбцов в mysql 

## Меняет все значения указанного столбца на их id по данным из mySQL.Требуется указать имя таблицы в mysql, имя столбца с id, имя столбца с значениями
replace_data_name_to_data_id(connection, json_data, json_column_name, mysql_table_name, mysql_column_id_name, mysql_column_name_name)

connection - соединение с бд, json_data - словарь json, json_column_name - название ключей в json, mysql_table_name - название таблицы, mysql_column_id_name - название столбцов в mysql с id,  mysql_column_name_name - название столбцов в mysql

## Замена всех значений указанного столбца с True на 1, с False на 0
replace_bool_to_int(data, column_name_json)

data - словарь json, column_name_json - название ключей в json, к-ые надо заменить

## Формирование списка со всеми данными из запроса JSON по указанному имени поля
get_data_list_from_json(json_data, json_key)

json_data - словарь json, json_key - название ключей в json

## Поиск данных, которые требуется обновить в MySQLВозвращает JSON словарь с данными, которые нужно добавить в MySQL
get_data_to_update(connection, json_data, json_key_field, mysql_table_name, mysql_column_id_name)

connection - соединение с бд, json_data - словарь json, json_key_field - название ключей в json, mysql_column_id_name - название столбцов в mysql 
_________________________________________________________________________________________________________________________________________________________
# Module for working with json

## Getting JSON data returned when clicking on the specified url with headers, cookies
get_json_with_headers_cookies(url, my_headers, my_cookies, url_referer)

url - the main link for the request, my_headers - headers, my_cookies - cookies, url_referer - reference link

## Getting JSON data returned when clicking on the specified url
get_json(url)

url - the main link for the request

## Returns a JSON dictionary with data to be added to MySQL
get_missing_data_to_insert(connection, json_data, json_key_field, mysql_table_name, mysql_column_id_name)

connection - db connection, json_data - json dictionary, json_key_field - key names in json, mysql_column_id_name - column names in mysql

## Changes all values of the specified column to their id according to data from MySQL.You need to specify the table name in mysql, the column name with id, the column name with the values
replace_data_name_to_data_id(connection, json_data, json_column_name, mysql_table_name, mysql_column_id_name, mysql_column_name_name)

connection - database connection, json_data - json dictionary, json_column_name - name of keys in json, mysql_table_name - table name, mysql_column_id_name - name of columns in mysql with id, mysql_column_name_name - name of columns in mysql

## Replacing all values of the specified column from True to 1, from False to 0
replace_bool_to_int(data, column_name_json)

data is a json dictionary, column_name_json is the name of the keys in json, the keys need to be replaced

## Generating a list with all the data from the JSON request by the specified field name
get_data_list_from_json(json_data, json_key)

json_data is a json dictionary, json_key is the name of the keys in json

## Searching for data that needs to be updated in MySQL returns a JSON dictionary with data that needs to be added to MySQL
get_data_to_update(connection, json_data, json_key_field, mysql_table_name, mysql_column_id_name)

connection - db connection, json_data - json dictionary, json_key_field - name of keys in json, mysql_column_id_name - name of columns in mysql
