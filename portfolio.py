import pandas as pd
import insurance_manager
import os


def main():
    portfolio = insurance_manager.InsuranceManager()
    history = None
    if 'portfolio.csv' in os.listdir():
        history = pd.read_csv('portfolio.csv')
    if history is not None:    
        portfolio.importHistory(history.to_dict('records'))
    n = int(input('Enter number of new insurances : '))
    for i in range(n):
        portfolio.newInsurance()
    df = pd.DataFrame.from_records(portfolio.getInsurancesDicts())
    df = pd.concat([history, df])
    if df.shape[0] > 0:    
        df.to_csv('portfolio.csv', index=False)
    portfolio.showInsurances()


if __name__ == '__main__':
    main()
