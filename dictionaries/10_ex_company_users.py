company_dict = {}

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' -> ')
    company_name = command[0]
    employee_id = command[1]

    if company_name not in company_dict:
        company_dict[company_name] = []

    if employee_id not in company_dict[company_name]:
        company_dict[company_name].append(employee_id)

for company, id in company_dict.items():
    print(f'{company}')
    for employee in id:
        print(f'-- {employee}')