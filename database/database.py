import sqlite3
from bank.costumer import costumer
from bank.bankTransaction import bankTransaction


def open_connection():
    connection = sqlite3.connect("transactions.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def create_costumer_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS costumer(
                    costumer_id PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    last_name TEXT,
                    personal_code FLOAT)
                    """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def create_bankTransaction_table():
    try:
        connection, cursor = open_connection()
        query = """CTREATE TABLE IF NOT EXISTS bankTransaction(
                    transaction_id PRIMARY KEY AUTOINCREMENT,
                    date DOUBLE,
                    account_number TEXT UNIQUE,
                    transfer TEXT UNIQUE
                    )
                    """


        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)


    finally:
        close_connection(connection, cursor)


create_costumer_table()
create_bankTransaction_table()


def query_database(query, params=None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query, params)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)

    except sqlite3.DataError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def create_costumer(costumer):
    query = "INSERT INTO costumer VALUE (?, ?, ?, ?)"
    params = (costumer.costumer_id, costumer.name, costumer.last_name, costumer.personal_code)
    query_database(query, params)


costumer1 = costumer(None, "John", "Banks", 39411252321)
costumer2 = costumer(None, "Jack", "Jones", 39210112322)


create_costumer(costumer1)


def get_costumer(costumer):
    query = "SELECT * FROM costumer WHERE costumer_id = (?) OR name = (?) OR last_name = (?) OR personal_code = (?)"
    params = (costumer.costumer_id, costumer.name, costumer.last_name, costumer.personal_code)
    query_database(query, params)


get_costumer(costumer1)


def ipdate_costumer(costumer):
    query = "UPDATE costumer SET name = 'Johnny' WHERE name = (?)"
    params = (costumer.name)
    query_database(query, params)


update_costumer(costumer1)


def delete_costumer(costumer):
    query = "DELETE FROM costumer WHERE name = (?) OR costumer_id = (?) OR last_name = (?) OR personal_code = (?)"
    params = (costumer.name, costumer.costumer_id, costumer.last_name, costumer.personal_code)
    query_database(query, params)


delete_costumer(costumer2)

def create_bankTransaction(bankTransaction):
    query = "INSERT INTO bankTransaction VALUES(?, ?, ?, ?)"
    params = (bankTransaction.transaction_id, bankTransaction.date, bankTransaction.account_number, bankTransaction.transfer)
    query_database(query, params)


bankTransaction1 = bankTransaction(None, '2019/12/13', 'LT-4531468453516', '500$')

def get_bankTransaction(bankTransaction):
    query = "SELECT * FROM bankTransaction WHERE transaction_id = (?), OR date = (?) OR account_number = (?) OR transfer = (?)"
    params = (bankTransaction.transaction_id, bankTransaction.date, bankTransaction.account_number, bankTransaction.transfer)
    query_database(query, params)


get_bankTransaction(bankTransaction1)


def update_bankTransaction(bankTransaction):
    query = "UPDATE bankTransaction SET transfer = '600$' WHERE transaction_id = (?)"
    params = (bankTransaction.transfer)
    query_database(query, params)


update_bankTransaction(bankTransaction1)


def delete_bankTransaction(bankTransaction):
    query = "DELETE FROM bankTransaction WHERE transaction_id = (?) OR date = (?) OR account_number = (?) OR transfer = (?)"
    params = (bankTransaction.transaction_id, bankTransaction.date, bankTransaction.account_number, bankTransaction.transfer)
    query_database(query, params)


delete_bankTransaction(bankTransaction2)

