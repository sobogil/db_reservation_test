#손님 정보 추가
def add_customer(name, phone_number, email, connection):
    try:
        cursor = connection.cursor()

        # 고객 정보 삽입 쿼리
        insert_customer_query = """
        INSERT INTO customers (name, phone_number, email)
        VALUES (%s, %s, %s)
        """
        customer_data = (name, phone_number, email)

        cursor.execute(insert_customer_query, customer_data)
        connection.commit()

        print(f"{name} 님의 정보가 성공적으로 입력되었습니다.")

    except Exception as e:
        print(f"고객 정보 입력 오류: {e}")
