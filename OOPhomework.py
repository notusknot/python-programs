class Vaccine:
    def __init__(self, name, rate, company):
        self.name = name
        self.rate = rate
        self.company = company
moderna = Vaccine('moderna', 90, 'Moderna')
johnson = Vaccine('johnson', 87, 'Johnson&Johnson')
pfeizer = Vaccine('pfeizer', 92, 'Pfeizer')
vaccineList = [moderna, johnson, pfeizer]
print(vaccineList)

ans = input('What vaccine would you like to know about?')
for loop in vaccineList:
    if ans == loop:
        print('ok')
        print(loop)
    else:
        print('This vaccine is not in our database.')
