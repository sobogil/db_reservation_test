import mysql.connector
from mysql.connector import Error
#연결 함수
def create_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1qaz2wsx!QAZ@WSX",
            database = "work"
        )
        if connection.is_connected():
            print("호텔 예약 서비스에 오신걸 환영합니다.")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
#연결 종료 함수
def close_database_connection(connection, cursor=None):
    try:
        if connection.is_connected():
            if cursor:
                cursor.close()
            connection.close()
            print("호텔 예약 서비스 연결이 종료되었습니다.")

    except Exception as e:
        print(f"연결 종료 오류: {e}")