import string
import random
import pandas as pd
from datetime import date


class Insurance:
    def __init__(self) -> None:
        self.ID = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=8))
        self.validity = 12
        self.type = None
        self.vendor = None
        self.creation_date = date.today().strftime("%B %d, %Y")
        self.maturation_date = (date.today() + pd.DateOffset(
            months=self.validity)).strftime("%B %d, %Y")

    def recalcMaturation(self) -> None:
        self.maturation_date = (date.today() + pd.DateOffset(
            months=self.validity)).strftime("%B %d, %Y")

    def updateValidity(self, n) -> None:
        self.validity += n
        self.recalcMaturation()

    def __str__(self) -> str:
        return(f"""\n
        Insurance ID: {self.ID}\n
        Insurance Validity: {self.validity} months from creation\n
        Insurance Type: {self.type}\n
        Insurance Vendor: {self.vendor}\n
        Insurance Created On: {self.creation_date}\n
        Insurance Expiring On: {self.maturation_date} (Maturation Date, can be extended)\n
        """)

    def toDict(self):
        return({
            'ID': self.ID,
            'Validity': self.validity,
            'Type': self.type,
            'Vendor': self.vendor,
            'Created On': self.creation_date,
            'Expiring On': self.maturation_date,
        })

    def fromDict(self, dict_obj):
        self.ID = dict_obj['ID']
        self.validity = dict_obj['Validity']
        self.type = dict_obj['Type']
        self.vendor = dict_obj['Vendor']
        self.creation_date = dict_obj['Created On']
        self.maturation_date = dict_obj['Expiring On']
