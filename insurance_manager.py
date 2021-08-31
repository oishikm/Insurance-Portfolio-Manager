import insurance


class InsuranceManager:
    def __init__(self) -> None:
        self.insurances = []

    def importHistory(self, list_hist):
        if len(list_hist) > 0:
            for obj in list_hist:
                insurance_obj = insurance.Insurance()
                insurance_obj.fromDict(obj)
                self.insurances.append(insurance_obj)

    def addInsurance(self, insurance_obj):
        self.insurances.append(insurance_obj)

    def showInsurances(self):
        if len(self.insurances) > 0:
            print('\nInsurances in portfolio : \n')
            ctr = 0
            for insurance_obj in self.insurances:
                ctr += 1
                print(f'[{ctr}]\n{insurance_obj}')
        else:
            print('\nNo Insurances in portfolio.\n')

    def newInsurance(self):
        insurance_obj = insurance.Insurance()
        insurance_obj.type = input('Enter Insurance Type : ')
        insurance_obj.vendor = input('Enter Insurance Vendor : ')
        self.addInsurance(insurance_obj)

    def getInsurancesDicts(self):
        record = []
        for insurance_obj in self.insurances:
            record.append(insurance_obj.toDict())
        return record
