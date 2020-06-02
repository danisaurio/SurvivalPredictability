import csv
from dataclasses import dataclass


@dataclass
class Patient:
    def __init__(self, sex, age, race, rhythm, rosc):
        self.sex = sex
        self.age = age
        self.race = race
        self.rhythm = rhythm
        self.rosc = rosc

def read_file(self):
    national_data = []
    with open('dummyData.csv', 'r') as dummyCSV:
        tab_reader = csv.DictReader(dummyCSV, delimiter=',')
        for row in tab_reader:
            patient = data_modification(self, row)
            national_data.append(patient)
    return national_data

def data_modification(self, row):
    sex_to_number = {
        'female':0,
        'male':1
    }
    race_to_number = {
        'caucasian':0,
        'native':1,
        'african':2,
        'asian':3,
        'islander':4,
    }
    rhythm_to_number  = {
        'vf':0,
        'pvt':1,
        'asystole':2,
        'pea':3,
    }
    rosc_to_number = {
        'yes':0,
        'no':1,
    }
    sex = sex_to_number[row['sex']]
    age = row['age'] #no need of modification
    race = race_to_number[row['race']]
    rhythm = rhythm_to_number[row['rhythm']]
    rosc = rosc_to_number[row['rosc']]
    return Patient(sex, age, race, rhythm, rosc)


def get_data(self):
    patient_info = [(patient.sex, patient.age, patient.race, patient.rhythm, patient.rosc) for patient in read_file(self)]
    print([list(patient) for patient in patient_info])

get_data(self=Patient)


