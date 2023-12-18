from datetime import datetime
# 결제 함수
def make_payment(name, room_number, payment_method, connection):
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

        # 객실 가격 조회 쿼리
        get_room_price_query = """
        SELECT price FROM rooms WHERE room_number = %s
        """
        cursor.execute(get_room_price_query, (room_number,))
        room_price = cursor.fetchone()

        if not room_price:
            print(f"{room_number} 번 객실의 정보를 찾을 수 없습니다.")
            return
        
        # id_reservation찾기
        get_id_reservaion_query = """
        SELECT id_reservation FROM reservations WHERE id_customer = %s
        """
        cursor.execute(get_id_reservaion_query, (id_customer[0],))
        id_reservation = cursor.fetchone()

        if not id_reservation:
            print(f"{name} 님의 예약 정보를 찾을 수 없습니다.")
            return
        
        # 결제 정보 삽입 쿼리
        insert_payment_query = """
        INSERT INTO payment (id_reservation, payment_date, payment_price, payment_method)
        VALUES (%s, %s, %s, %s)
        """
        payment_data = (id_reservation[0], datetime.now(), room_price[0], payment_method)

        cursor.execute(insert_payment_query, payment_data)
        connection.commit()

        print(f"{name} 님의 결제 정보가 성공적으로 입력되었습니다.\n")
        print("현재 예약하신 룸의 가격은 "+str(room_price[0])+"이며 결제 방법은 "+ payment_method+" 입니다")
        if payment_method=="무통장 입금":
            print("3일 이내에 해당 계좌번호에 입금해주시길 바랍니다.\n소보길 국민은행 9xxx-xxx-xx-xxxxx")

    except Exception as e:
        print(f"결제 오류: {e}")

