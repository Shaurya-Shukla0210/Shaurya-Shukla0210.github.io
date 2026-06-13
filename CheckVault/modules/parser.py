import re

def parse_salary_slip(text):

    data = {}

    # Employee name
    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "employee" in line.lower():
            if i + 1 < len(lines):
                data["employee"] = lines[i + 1].strip()

    # Find all money-like values
    amounts = re.findall(r'\d+[,\.]\d+', text)

    if len(amounts) >= 3:
        data["gross_salary"] = amounts[-3]
        data["tax"] = amounts[-2]
        data["net_salary"] = amounts[-1]

    return data