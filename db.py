'''Module to interact with localhost database expanded using Singlestore Studio'''
import csv
import pymysql


def connect(db_name, host='localhost', user='root', password='root'):
    '''Setting up the connection with SingleStore database'''

    connection = pymysql.connect(host=host, user=user, password=password, db=db_name)
    cursor = connection.cursor()

    return connection, cursor

def main():
    '''Main function'''
    connection, cursor = connect('adtech')

    query = "SELECT * FROM events"
    cursor.execute(query)

    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])  # write headers
        writer.writerows(cursor)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()
