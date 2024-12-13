from psycopg2 import Error
import psycopg2.extras

try:
    connection = psycopg2.connect(user="postgres",
                                  password="g,adfgi9hm",
                                  host="localhost",
                                  port="5432",
                                  database="washing_machine")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print("You are connected to base")

except (Exception, Error) as error:
    raise TypeError("Error while connecting to PostgreSQL", error)

washing_machines = [
    ('WASH123', 'LG', 35000, 8, 2022),
    ('WM-145', 'Samsung', 40000, 9, 2023),
    ('EcoBubble 7kg', 'Samsung', 30000, 7, 2021),
    ('F4V5VY1W', 'LG', 45000, 10, 2023),
    ('WT-80', 'Bosch', 38000, 8, 2022),
    ('AWE 6516', 'Ariston', 25000, 6, 2020),
    ('WAT24360BY', 'Bosch', 32000, 7, 2021),
    ('DWD-FD1200', 'Daewoo', 27000, 6, 2020),
    ('WM-60', 'Whirlpool', 29000, 7, 2021),
    ('XQG60-9188', 'Haier', 36000, 8, 2022),
    ('WASH-200', 'LG', 25000, 7, 2021),
    ('WM-123', 'Samsung', 22000, 6, 2020),
    ('EcoWash 6kg', 'Samsung', 18000, 6, 2021),
    ('F4J6VY1W', 'LG', 27000, 8, 2022),
    ('WT-70', 'Bosch', 23000, 7, 2021),
    ('AWE 6515', 'Ariston', 19000, 6, 2020),
    ('WAT24350BY', 'Bosch', 21000, 7, 2021),
    ('DWD-FD1100', 'Daewoo', 16000, 6, 2020),
    ('WM-50', 'Whirlpool', 20000, 7, 2021),
    ('XQG60-9180', 'Haier', 24000, 8, 2022),
    ('WASH-300', 'LG', 28000, 9, 2023),
    ('WM-200', 'Samsung', 25000, 8, 2022),
    ('EcoWash 7kg', 'Samsung', 23000, 7, 2021),
    ('F4J5VY1W', 'LG', 29000, 9, 2023),
    ('WT-90', 'Bosch', 27000, 8, 2022),
    ('AWE 6514', 'Ariston', 21000, 6, 2020),
    ('WAT24340BY', 'Bosch', 22000, 7, 2021),
    ('DWD-FD1000', 'Daewoo', 17000, 6, 2020),
    ('WM-70', 'Whirlpool', 18000, 7, 2021),
    ('XQG60-9170', 'Haier', 26000, 8, 2022),
    ('WASH-400', 'LG', 29000, 9, 2023),
    ('WM-300', 'Samsung', 24000, 8, 2022),
    ('EcoWash 8kg', 'Samsung', 25000, 8, 2021),
    ('F4J4VY1W', 'LG', 30000, 10, 2023),
    ('WT-100', 'Bosch', 28000, 9, 2022),
    ('AWE 6513', 'Ariston', 22000, 6, 2020),
    ('WAT24330BY', 'Bosch', 23000, 7, 2021),
    ('DWD-FD900', 'Daewoo', 19000, 6, 2020),
]


try:
    connection = psycopg2.connect()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main (
            id SERIAL PRIMARY KEY,
            model VARCHAR(50),
            brand VARCHAR(50),
            price INTEGER,
            volume INTEGER,
            year INTEGER
        )
    ''')
    insert_query = '''
            INSERT INTO main (model, brand, price, volume, year)
            VALUES (%s, %s, %s, %s, %s)
        '''
    cursor.executemany(insert_query, washing_machines)

    connection.commit()
    print(f"{cursor.rowcount} записей добавлено в таблицу.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
