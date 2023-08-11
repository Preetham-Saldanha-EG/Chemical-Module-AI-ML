import os
import csv

unique_chems = set()
columns = ["Composition/information on ingredients", "Hazards Identification", "First Aid Measures","Accidental Release Measures", "Handling and Storage",
                "Exposure Controls/Personal Protection", "Physical/Chemical Properties",
                "Stability and Reactivity Data","Disposal Considerations","Fire Fighting Measures",
                "Toxicological information","Ecological information","Disposal considerations",
                "Transport information","Regulatory information","Other information"
                ]
records = []



def checkIfLineIsHeading(line):
    for column in columns:
        print( columns.index(column))
        if column in line:
            return columns.index(column)
    return -1

def extract_sections(data):

    curr_index=0

    product_id = None
    current_section = None
    section_data = {section: "" for section in columns}
    # print(section_data)
    

    lines = data
    for line in lines:
        line = line.strip()
        # index= checkIfLineIsHeading(line)
        if line.startswith("Product ID:"):
           
            product_id = line[len("Product ID:"):].strip()
        
        elif checkIfLineIsHeading(line) !=-1:
         
            current_section= columns[checkIfLineIsHeading(line)]
        
        elif current_section and line:
            section_data[current_section] += line + ' '
            print(current_section, curr_index)
    # print(records,section_data)

    return [product_id] + [section_data[section] for section in columns]     
    # print(records)
    # return records

def write_to_csv(records):
    with open('chems_data_626.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        header = ["Product ID","Composition/information on ingredients", "Hazards Identification", "First Aid Measures","Accidental Release Measures", "Handling and Storage",
                "Exposure Controls/Personal Protection", "Physical/Chemical Properties",
                "Stability and Reactivity Data","Disposal Considerations","Fire Fighting Measures",
                "Toxicological information","Ecological information","Disposal considerations",
                "Transport information","Regulatory information","Other information"]
        csvwriter.writerow(header)
        csvwriter.writerows(records)
# Load Chemicals List
with open('chemicalNames.txt', 'r') as chem_file:
    chemicals = set(line.strip().lower() for line in chem_file)

# Process Dataset Folder
dataset_folder = 'f2'
output_file = 'foundTheseChemicalsInMSDS.txt'
folders_to_process = 627  # Change this value to limit processing to the first 30 folders

with open(output_file, 'w') as found_file:
    
    processed_folders = 0
    for root, _, files in os.walk(dataset_folder):
        print("reaches here")
        if processed_folders >= folders_to_process:
            
            break

        for file in files:
            
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
              
                with open(file_path, 'r') as txt_file:
                    lines = txt_file.read().split('\n')
                    
                    if len(lines) >= 3:
                        # print(lines[2])
                        product_id_line = lines[2].strip()
                        if product_id_line.startswith("Product ID:"):
                            product_id = product_id_line[len("Product ID:"):].strip()
                            if product_id.lower() in chemicals:
                                if product_id.lower() not in  unique_chems:
                                  unique_chems.add(product_id.lower())
                                  found_file.write(f"{product_id}, {file}\n")
                                  records.append(extract_sections(lines))
        
        processed_folders += 1


write_to_csv(records)
print("end of script")