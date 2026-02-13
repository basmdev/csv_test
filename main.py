import argparse
import csv

from prettytable import PrettyTable


def load_csv(files):
    """Load data from CSV files."""
    csv_data = []

    for file in files:
        try:
            with open(file, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    csv_data.append(row)
        except FileNotFoundError:
            print(f"The file {file} was not found.")

    return csv_data


def print_as_table(headers, rows):
    """Tabular output."""
    table = PrettyTable()
    table.field_names = headers
    for row in rows:
        table.add_row(row)

    if headers:
        table.align[headers[0]] = "l"
        for header in headers[1:]:
            table.align[header] = "r"

    print(table)


def calculate_average_gdp(data):
    """Calculation of average GDP."""
    stats = {}
    for row in data:
        country, gdp = row.get("country"), row.get("gdp")
        if country and gdp:
            if country not in stats:
                stats[country] = [0.0, 0]
            stats[country][0] += float(gdp)
            stats[country][1] += 1

    temp_list = []
    for country, values in stats.items():
        avg_value = values[0] / values[1]
        temp_list.append([avg_value, country])

    temp_list.sort(reverse=True)

    result_list = []
    for avg, country in temp_list:
        result_list.append([country, f"{avg:.2f}"])

    return ["Country", "GDP"], result_list


# Dictionary of available reports with their corresponding functions
REPORTS = {
    "average-gdp": calculate_average_gdp,
}


def main():
    parser = argparse.ArgumentParser(
        description="Script for processing macroeconomic data from CSV files"
    )
    parser.add_argument("-f", "--files", nargs="+", help="File names", required=True)
    parser.add_argument(
        "-r", "--report", help="Report name", choices=REPORTS.keys(), required=True
    )
    args = parser.parse_args()

    data = []

    if args.files:
        data = load_csv(args.files)

    if not data:
        print("Data has not been loaded.")
        return

    headers, rows = REPORTS[args.report](data)
    print_as_table(headers, rows)


if __name__ == "__main__":
    main()
