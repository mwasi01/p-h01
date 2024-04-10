class Patient:  

  def __init__(self, name, age, gender):
       self.name = name   
       self.age = age   
       self.gender = gender  
       self.vital_signs = []       
       self.notes = []


def add_vital_signs(self, vital_sign, time_taken):  
    self.vital_signs.append((vital_sign, time_taken))  

def add_note(self, note):     
  self.notes.append(note) 

def display_details(self):  
    print("Patient Details:")     
    print("Name:", self.name)        
    print("Age:", self.age)         
    print("Gender:", self.gender)        
    print("Vital Signs:")      

for vital_sign, time_taken in self.vital_signs:  
    print("- Vital Sign:", vital_sign)            
    print("  Time Taken:", time_taken)        
    print("Notes:")       

for note in self.notes:            
    print("- Note:", note)         
    print() 

# Function to input patient details

def input_patient_details():     
     name = input("Enter patient's name: ")    
    age = input("Enter patient's age: ")    
    gender = input("Enter patient's gender: ")    
      return name, age, gender  

# Function to input vital signs
 def input_vital_signs():  
     vital_sign = input("Enter vital sign: ") 
     time_taken = input("Enter time taken (e.g., 10:30 AM): ")   
      return vital_sign, time_taken 

# Function to input patient notes  
 def input_patient_notes():     
     note = input("Enter patient's note: ")   
      return note 

# Main function
 def main():     patients = [] 
          while True:         print("Options:")  
print("1. Add Patient Details")    
print("2. Add Vital Signs")        
print("3. Add Patient Notes")       

print("4. Display Patient Details") 
print("5. Exit")        

choice = input("Enter choice (1/2/3/4/5): ")     
if choice == '1':            
name, age, gender = input_patient_details()             
patient = Patient(name, age, gender)             
patients.append(patient)             
print("Patient details added successfully.\n")        
     elif choice == '2':           
         if not patients:                
            print("No patients added yet. Please add patient details first.\n")                
 

continue             for i, patient in enumerate(patients, start=1):        print(f"{i}. {patient.name}")        
patient_choice = int(input("Enter patient number: "))             if 1 <= patient_choice <= len(patients):            
patient = patients[patient_choice - 1]                 vital_sign, time_taken = input_vital_signs()           
patient.add_vital_signs(vital_sign, time_taken)                 print("Vital signs added successfully.\n")    
else:                 print("Invalid patient number. Please try again.\n")         elif choice == '3':        
if not patients:                 print("No patients added yet. Please add patient details first.\n")          
continue             for i, patient in enumerate(patients, start=1):                 print(f"{i}. {patient.name}")    
patient_choice = int(input("Enter patient number: "))             if 1 <= patient_choice <= len(patients):            
patient = patients[patient_choice - 1]                 note = input_patient_notes()                 patient.add_note(note)      
print("Note added successfully.\n")             else:                 print("Invalid patient number. Please try again.\n")      

elif choice == '4':             if not patients:                 print("No patients added yet.\n")                 continue     
for i, patient in enumerate(patients, start=1):                 print(f"{i}. {patient.name}")             patient_choice = int(input("Enter patient number: "))    
if 1 <= patient_choice <= len(patients):                 patient = patients[patient_choice - 1]                 patient.display_details()             else:        
print("Invalid patient number. Please try again.\n")      
elif choice == '5':             print("Exiting program...")        
break         else:             print("Invalid choice. Please try again.\n") 
if __name__ == "__main__":     main()
