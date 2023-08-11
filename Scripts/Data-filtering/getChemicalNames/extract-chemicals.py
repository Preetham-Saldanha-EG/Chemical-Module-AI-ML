import csv
import re
def get_third_column(csv_file, txt_file):
  """Retrieves values from the third column of a CSV file and stores them in a text file in separate lines.

  Args:
    csv_file: The path to the CSV file.
    txt_file: The path to the text file to store the third column values.
  """

  with open(csv_file, 'r') as csv_file_obj:
    reader = csv.reader(csv_file_obj, delimiter=',')
    with open(txt_file, 'w') as txt_file_obj:
      for row in reader:
        third_column_value = row[3]
        for chemical in third_column_value.split(','):
            if chemical.endswith("(PROVISIONAL)"):
            #   chemical=chemical.strip()
              txt_file_obj.write(chemical[:-13] + '\n')
              continue
            txt_file_obj.write(chemical + '\n')

def sort_strings(txt_file):
  """Sorts the order of strings in multiple lines in a text file.

  Args:
    txt_file: The path to the text file to sort.
  """

  with open(txt_file, 'r') as txt_file_obj:
    lines = txt_file_obj.readlines()

    strings = []
    for line in lines:
      match = re.match('^(.*)$', line)
      if match:
        strings.append(match.group(1))

    strings.sort()

    with open(txt_file, 'w') as txt_file_obj:
      for string in strings:
        txt_file_obj.write(string + '\n')

def remove_duplicate_lines(txt_file):
  """Removes duplicate lines from a text file.

  Args:
    txt_file: The path to the text file to remove duplicates from.
  """

  with open(txt_file, 'r') as txt_file_obj:
    lines = txt_file_obj.readlines()

    seen_lines = set()
    new_lines = []

    for line in lines:
      line = line.strip()
      if line not in seen_lines:
        seen_lines.add(line)
        new_lines.append(line)

  with open(txt_file, 'w') as txt_file_obj:
    for line in new_lines:
      txt_file_obj.write(line + '\n')


def remove_lines_containing_and(txt_file):
  with open(txt_file, 'r') as txt_file_obj:
    lines = txt_file_obj.readlines()

    strings = []
    for line in lines:
       if " and " not in line:
            strings.append(line)
       


    with open(txt_file, 'w') as txt_file_obj:
      for string in strings:
        txt_file_obj.write(string + '\n')

def remove_empty_lines(txt_file):
  """Removes empty lines from a text file.

  Args:
    txt_file: The path to the text file to remove empty lines from.
  """

  with open(txt_file, 'r') as txt_file_obj:
    lines = txt_file_obj.readlines()

    new_lines = [line for line in lines if line.strip()]

  with open(txt_file, 'w') as txt_file_obj:
    for line in new_lines:
      txt_file_obj.write(line)

if __name__ == '__main__':
  csv_file = 'CAS.csv'
  txt_file = 'chemicalNames.txt'
#   get_third_column(csv_file, txt_file)
#   sort_strings(txt_file)
# remove_duplicate_lines(txt_file)
# remove_lines_containing_and(txt_file)
  remove_empty_lines(txt_file)
