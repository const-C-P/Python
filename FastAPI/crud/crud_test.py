from sqlalchemy.orm import Session
from db.models.test_model import Test


def get_itemsAll(db: Session):
    return db.query(Test).all()
