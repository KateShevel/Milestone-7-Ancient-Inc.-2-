from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

# Define the path to the CSV file
csv_file_path = 'database.csv'

# Function to generate the report
def generate_report(target_month, target_department):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        birthdays = 0
        anniversaries = 0
        birthdays_by_department = {}
        anniversaries_by_department = []

        for row in reader:
            if row['Month'].lower() == target_month.lower() and row['Department'].lower() == target_department.lower():
                birthdays_by_department[row['ID']] = {
                    "name": row['Name'],
                    "birthday": row['Birthday']
                }
            if row['Anniversary'].lower() == target_month.lower() and row['Department'].lower() == target_department.lower():
                anniversaries_by_department.append({
                    "name": row['Name'],
                    "anniversary": row['Anniversary']
                })

    report = {
        "birthdays": {
            "total": len(birthdays_by_department),
            "employees": birthdays_by_department
        },
        "anniversaries": {
            "total": len(anniversaries_by_department),
            "employees": anniversaries_by_department
        }
    }
    return report

# Endpoint to retrieve birthdays report
@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    report = generate_report(month, department)['birthdays']
    return jsonify(report)


# Endpoint to retrieve anniversaries report
@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    report = generate_report(month, department)['anniversaries']
    return jsonify(report)

if __name__ == '__main__':
    app.run()
