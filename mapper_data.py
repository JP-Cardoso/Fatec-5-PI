class MapperData:
    @staticmethod
    def mapper(dados) -> dict:
        data = {
            # "creditability": dados["Creditability"],
            "balance": dados["AccountBalance"],
            "duration": dados["DurationofCredit"],
            "paymentStatus": dados["PaymentStatusofPreviousCredit"],
            "purpose": dados["Purpose"],
            "amount": dados["CreditAmount"],
            "savings": dados["ValueSavings"],
            "currentEmployment": dados["Lengthofcurrentemployment"],
            "instalment": dados["Instalmentpercent"],
            "marital": dados["Sex&MaritalStatus"],
            "guarantors": dados["Guarantors"],
            "durationAddress": dados["DurationinCurrentaddress"],
            "asset": dados["Mostvaluableavailableasset"],
            "age": dados["Age"],
            "concurrentCredits": dados["ConcurrentCredits"],
            "typeApartment": dados["Typeofapartment"],
            "numberofCredits": dados["NoofCreditsatthisBank"],
            "occupation": dados["Occupation"],
            "dependents": dados["Noofdependents"],
            "telephone": dados["Telephone"],
            "worker": dados["ForeignWorker"],
        }
        return data
