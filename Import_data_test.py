import os 

cmd = "curl http://github.com/ksu-hmi/Patient_Treatment_Prescreening_Tool/raw/main/Python_Project_Data_Diagnosis.csv -o Python_Project_Data_Diagnosis.csv"

os.system(cmd)

diagonsis_file = open('Python_Project_Data_Diagnosis.csv', 'r')
diagnosis = diagonsis_file.readlines()

print (diagnosis)



