import csv

ages = []
sexes = []
bmis = []
num_children = []
smokers = []
regions = []
insurance_charges = []

def list_data(lst, csv_file, column):
    with open(csv_file) as csv_data:
        csv_dict = csv.DictReader(csv_data)
        for row in csv_dict:
            lst.append(row[column])
        return lst
    
list_data(ages, 'insurance.csv', 'age')
list_data(sexes, 'insurance.csv', 'sex')
list_data(bmis, 'insurance.csv', 'bmi')
list_data(num_children, 'insurance.csv', 'children')
list_data(smokers, 'insurance.csv', 'smoker')
list_data(regions, 'insurance.csv', 'region')
list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientInfo:
    def __init__(self, patient_age, patient_sex, patient_bmi, patient_children, patient_smoker, patient_region, patient_charge):
        self.patient_age = patient_age
        self.patient_sex = patient_sex
        self.patient_bmi = patient_bmi
        self.patient_children = patient_children
        self.patient_smoker = patient_smoker
        self.patient_region = patient_region
        self.patient_charge = patient_charge
    
    def analyze_age(self):
        total_age = 0
        for age in self.patient_age:
            total_age += int(age)
        return ("Average patient age: " + str(round(total_age / len(self.patient_age), 2)) + " years.")

    def analyze_sex(self):
        males = 0
        females = 0
        for sex in self.patient_sex:
            if sex == 'male':
                males += 1
            elif sex == 'female':
                females += 1
        print('Males: ' + str(males))
        print('Females: ' + str(females))

    def analyze_bmi(self):
        total_bmi = 0
        for bmi in self.patient_bmi:
            total_bmi += float(bmi)
        return ("Average patient BMI: " + str(round(total_bmi / len(self.patient_bmi), 2)))

    def analyze_children(self):
        total_children = 0
        for child in self.patient_children:
            total_children += int(child)
        return('Average # of children per household: ' + str(round(total_children /len(self.patient_children))))
    
    def analyze_smoker(self):
        yes_smokers = 0
        non_smokers = 0
        for smoke in self.patient_smoker:
            if smoke == 'yes':
                yes_smokers += 1
            elif smoke == 'no':
                non_smokers += 1
        print('Smokers: ' + str(yes_smokers))
        print('Non-smokers: ' + str(non_smokers))
    
    def analyze_regions(self):
        unique_regions = []
        for region in self.patient_region:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions
    
    def analyze_charges(self):
        total_charges = 0
        for charge in self.patient_charge:
            total_charges += float(charge)
        return ('Average annual medical insurance charges per household: ' + str(round(total_charges / len(self.patient_charge), 2)) + ' dollars.')
    
    def create_dict(self):
        self.patient_dict = {}
        self.patient_dict['age'] = [int(age) for age in self.patient_age]
        self.patient_dict['sex'] = self.patient_sex
        self.patient_dict['bmi'] = self.patient_bmi
        self.patient_dict['children'] = self.patient_children
        self.patient_dict['smoker'] = self.patient_smoker
        self.patient_dict['region'] = self.patient_region
        self.patient_dict['charges'] = self.patient_charge
        return self.patient_dict
    
patient_info = PatientInfo(ages, sexes, bmis, num_children, smokers, regions, insurance_charges)
patient_info.analyze_age()
patient_info.analyze_sex()
patient_info.analyze_bmi()
patient_info.analyze_smoker()
patient_info.analyze_children()
patient_info.analyze_regions()
patient_info.analyze_charges()
