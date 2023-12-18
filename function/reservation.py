# 예약 함수
def make_reservation(name, room_number, check_in, check_out, connection):
    try:
        cursor = connection.cursor()

        # 고객 ID 조회 쿼리
        get_id_customer_query = """
        SELECT id_customer FROM customers WHERE name = %s
        """
        cursor.execute(get_id_customer_query, (name,))
        id_customer = cursor.fetchone()

        if not id_customer:
            print(f"{name} 님의 정보를 찾을 수 없습니다.")
            return

        # 예약 정보 삽입 쿼리
        insert_reservation_query = """
        INSERT INTO reservations (id_customer, room_number, check_in, check_out)
        VALUES (%s, %s, %s, %s)
        """
        reservation_data = (id_customer[0], room_number, check_in, check_out)

        cursor.execute(insert_reservation_query, reservation_data)
        connection.commit()

        print(f"{name} 님의 예약이 성공적으로 완료되었습니다.")

    except Exception as e:
        print(f"예약 오류: {e}")



#예약 취소 함수
def cancel_reservation(name, room_number, connection):
    try:
        cursor = connection.cursor()

        # 고객 ID 조회 쿼리
        get_id_customer_query = """
        SELECT id_customer FROM customers WHERE name = %s
        """
        cursor.execute(get_id_customer_query, (name,))
        id_customer = cursor.fetchone()

        if not id_customer:
            print(f"{name} 님의 정보를 찾을 수 없습니다.")
            return

        # 예약 취소 쿼리
        cancel_reservation_query = """
        DELETE FROM reservations
        WHERE id_customer = %s AND room_number = %s
        """
        cursor.execute(cancel_reservation_query, (id_customer[0], room_number))
        connection.commit()

        print(f"{name} 님의 예약이 성공적으로 취소되었습니다.")

    except Exception as e:
        print(f"예약 취소 오류: {e}")