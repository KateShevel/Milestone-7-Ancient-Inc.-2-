import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


def generate_employee():
    name = fake.name()

    # Generate random hiring date within the past 5 years
    hiring_date = fake.date_time_between(start_date='-5y', end_date='now')

    # Randomly choose department
    department = random.choice(['HR', 'Finance', 'IT', 'Marketing', 'R&D'])

    # Generate random birthday within age range of 20 to 65
    birthday = fake.date_of_birth(minimum_age=20, maximum_age=65)

    # Get verbal form of hiring month
    hiring_month_verbal = hiring_date.strftime('%B')  # Full month name

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    month_name = month_names[birthday.month - 1]

    return {'Name': name, 'Hiring Date': hiring_date, 'Department': department, 'Birthday': birthday,
            'Month': month_name, 'Anniversary': hiring_month_verbal}


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'ID', 'Hiring Date', 'Department', 'Birthday', 'Month',
                      'Anniversary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    employee_data = []
    for _ in range(100):
        employee_info = generate_employee()
        employee_data.append(employee_info)
    write_to_csv('database.csv', employee_data)


if __name__ == "__main__":
    main()

    import csv


    def print_csv_file(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


    if __name__ == "__main__":
        print_csv_file('database.csv')