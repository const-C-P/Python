from db.session import SessionLocal

def get_db():
    db=SessionLocal()
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("db : ", db)
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    try:
        yield db # DB 연결 성공한 경우, DB 세션 시작
    finally:
        db.close()
        # DB 세션이 시작된 후, API 호출이 마무리되면 DB 세션을 닫아준다.