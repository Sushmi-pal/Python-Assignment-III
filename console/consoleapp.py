import csv
from csv import writer
import pandas
df = pandas.read_csv('student_info.csv')
l = len(df)
sn = l + 1


class Academy:
    def __init__(self):
        with open('courses.csv') as f:
            r = csv.reader(f, delimiter='.')
            for i in r:
                self.courses = i

    def inquiry_course(self):
        print("Courses are: ")
        with open('courses.csv') as f:
            r = csv.reader(f, delimiter='.')
            for i in r:
                self.courses = i
                print(self.courses)

    def register_student(self, list_of_elem):
        with open('student_info.csv', 'a+', newline='') as write_obj:
            fieldnames = ['ID', 'Name', 'Amount', 'Amount Remaining']
            writer = csv.DictWriter(write_obj, fieldnames=fieldnames, delimiter='|')
            writer.writeheader()
            writer.writerow({'ID': list_of_elem[0], 'Name': list_of_elem[1], 'Amount': list_of_elem[2],
                             'Amount Remaining': list_of_elem[3]})

    def display_student(self):
        with open('student_info.csv') as read_obj:
            csv_reader = csv.DictReader(read_obj)
            for row in csv_reader:
                print(f'\t{row["Name"]} {row["Amount"]}  {row["Amount Remaining"]}.')

    def remove_student(self, ID):
        self.id = ID
        with open('student_info.csv', mode='r') as file1:
            reader = csv.DictReader(file1)
            new_list = []
            for row in reader:
                new_list.append(row)
            print(new_list)
            file1.close()

        with open('employee_file2.csv', 'w') as file2:
            fieldnames = ['ID', 'Name', 'Amount', 'Amount Remaining']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            for row in new_list:
                if row['ID'] != self.id:
                    writer.writerow(row)
            file2.close()

    def update_amount(self, ID, amount):
        self.id = ID
        self.amount = amount
        with open('student_info.csv', mode='r') as file1:
            reader = csv.DictReader(file1)
            new_list = []
            for row in reader:
                new_list.append(row)
            print(new_list)
            file1.close()

        with open('employee_file2.csv', 'w') as file2:
            fieldnames = ['ID', 'Name', 'Amount', 'Amount Remaining']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            for row in new_list:
                if row['ID'] == self.id:
                    row['Amount'] += self.amount
                print(row)
                writer.writerow(row)

    def update_name(self, name, ID):
        self.id = ID
        self.name = name
        with open('student_info.csv', mode='r') as file1:
            reader = csv.DictReader(file1)
            new_list = []
            for row in reader:
                new_list.append(row)
            print(new_list)
            file1.close()

        with open('employee_file2.csv', 'w') as file2:
            fieldnames = ['ID', 'Name', 'Amount', 'Amount Remaining']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            for row in new_list:
                if row['Name'] == self.name and row['ID'] == self.id:
                    row['Name'] = self.name
                print(row)
                writer.writerow(row)


a = Academy()
print("Select what you want to do: \n1) Inquire Coueses \n2) Registeer \n3) Display payment information \n4) "
      "Update information \n5) Leave program ")
choice = int(input("Enter your choice: "))
if (choice == 1):
    a.inquiry_course()
    input()
elif (choice == 2):

    name = input('Enter your name')
    amount = int(input('How much amount do you pay now?'))
    amount_remaining = 20000 - amount
    row_contents = [sn, name, amount, amount_remaining]
    a.register_student(row_contents)
elif (choice == 3):
    print(a.display_student)

elif (choice == 4):
    print("Choose update option: \n1) Update Name \n2) Pay left Fees")
    update_choice = int(input("Enter your Choice: "))
    if update_choice == 1:
        new_name = input("Enter your new name: ")
        id = int(input("Enter your id"))
        a.update_name(new_name, id)
    elif update_choice == 2:
        amount = int(input('Enter the payment amount'))
        id = int(input("Enter your id"))
        if a.update_amount(amount, id):
            print('Your account has been updated')
elif (choice == 5):
    id = int(input('Enter the id number provided by the academy'))
    a.remove_student(id)

