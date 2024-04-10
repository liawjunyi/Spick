from sqlalchemy.orm import Session
import models, schemas
from fastapi.encoders import jsonable_encoder

def get_reservations(db: Session):
    return db.query(models.Reservation).all()

def create_reservation(db: Session, reservation: schemas.Reservation):
    print(reservation.dict())
    db_reservation = models.Reservation(**reservation.dict())
    
    try: 
        db.add(db_reservation)
        db.commit()
        db.refresh(db_reservation)
    except Exception as e:
        return None
    return db_reservation

def get_reservation_by_id(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.reservation_id == reservation_id).first()

def delete_reservation_by_id(db: Session, reservation_id: int):
    db.query(models.Reservation).filter(models.Reservation.reservation_id == reservation_id).delete()
    db.commit()