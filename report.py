from flask import Flask, jsonify, request
import csv
import sys
def generate_report(json_file, target_month, target_department):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        birthdays = 0
        anniversaries = 0
        birthdays_by_department = {}
        anniversaries_by_department = {}

        for row in reader:
            if row['Month'].lower() == target_month.lower():
                birthdays += 1
                department = row['Department']
                birthdays_by_department[department] = birthdays_by_department.get(department, 0) + 1
            if row['Anniversary'].lower() == target_month.lower():
                anniversaries += 1
                department = row['Department']
                anniversaries_by_department[department] = anniversaries_by_department.get(department, 0) + 1

    print(f"Report for {target_month.capitalize()}&{target_departmnet.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {birthdays}")
    print("By department:")
    for department, count in birthdays_by_department.items():
        print(f"- {department}: {count}")

    print("--- Anniversaries ---")
    print(f"Total: {anniversaries}")
    print("By department:")
    for department, count in anniversaries_by_department.items():
        print(f"- {department}: {count}")


if len(sys.argv) != 3:
    print("Usage: python report.py <database_file.csv> <month>")
    sys.exit(1)

csv_file = sys.argv[1]
target_month = sys.argv[2]

generate_report(json_file, target_month, target_department )
