from function.connect import *
from function.customer import *
from function.reservation import *
from function.pay import *

def mainui():
    try:
        db_connection = create_connection()
        if db_connection:
            while True:
                print("\n1. 예약하기\n2. 예약 취소하기\n3. 결제하기\n4. 개인정보 추가\n5. 종료")
                choice = input("선택: ")

                if choice == "1":
                    name = input("고객 이름: ")
                    room_number = int(input("객실 번호: "))
                    check_in_date = input("체크인 날짜 (YYYY-MM-DD): ")
                    check_out_date = input("체크아웃 날짜 (YYYY-MM-DD): ")
                    make_reservation(name, room_number, check_in_date, check_out_date, db_connection)

                elif choice == "2":
                    name = input("고객 이름: ")
                    room_number = int(input("객실 번호: "))
                    cancel_reservation(name, room_number, db_connection)

                elif choice == "3":
                    name = input("고객 이름: ")
                    room_number = int(input("객실 번호: "))
                    payment_method= input("결제 방법 1.신용카드 2.무통장 입금: ")
                    make_payment(name, room_number, payment_method, db_connection)

                elif choice == "4":
                    name = input("고객 이름: ")
                    phone_number = int(input("핸드폰 번호: "))
                    email = input("이메일: ")
                    add_customer(name, phone_number, email, db_connection)

                elif choice == "5":
                    break
                else:
                    print("올바른 선택을 입력하세요.")

    finally:
        # 연결 종료 함수 호출 (예외 발생 여부와 상관없이 호출)
        close_database_connection(db_connection)