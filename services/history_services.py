from models.calculation import Calculation
from database import SessionLocal


def add_calculation(calculation_data):

    db = SessionLocal()

    calculation = Calculation(
        a=calculation_data["a"],
        b=calculation_data["b"],
        operation=calculation_data["operation"],
        result=calculation_data["result"],
        created_at=calculation_data["created_at"]
    )

    db.add(calculation)
    db.commit()
    db.refresh(calculation)
    db.close()

    return calculation


def get_all_calculations():

    db = SessionLocal()

    calculations = db.query(Calculation).all()

    db.close()

    return calculations


def get_calculation_by_id(calc_id):

    db = SessionLocal()

    calculation = (
        db.query(Calculation)
        .filter(Calculation.id == calc_id)
        .first()
    )

    db.close()

    return calculation


def delete_calculation(calc_id):

    db = SessionLocal()

    calculation = (
        db.query(Calculation)
        .filter(Calculation.id == calc_id)
        .first()
    )

    if calculation is None:
        db.close()
        return False

    db.delete(calculation)
    db.commit()
    db.close()

    return True


def clear_history():

    db = SessionLocal()

    db.query(Calculation).delete()

    db.commit()
    db.close()