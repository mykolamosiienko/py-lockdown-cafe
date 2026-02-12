import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Person is not vaccinated")
        elif visitor["vaccine"].get("expiration_date") < today_date:
            raise OutdatedVaccineError("Vaccine has expired")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Person is not wearing a mask")
        return f"Welcome to {self.name}"
