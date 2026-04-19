import re
from openpyxl import Workbook

COLUMN_MARKERS = ["A", "B", "C", "F"]
COLUMN_NAMES = ["Date", "Time"] + COLUMN_MARKERS

def parse_input_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().strip()

    # Split entries by blank lines
    raw_entries = re.split(r'\n\s*\n', content)

    parsed_entries = []

    for i in range(len(raw_entries)):
        entry = raw_entries[i]
        lines = entry.strip().split("\n")
        if len(lines) < 2:
            continue

        # Date and time are strings, the rest are lists
        data = {COLUMN_NAMES[0]: "", COLUMN_NAMES[1]: ""}
        for col_name in COLUMN_NAMES[2:]:
            data[col_name] = []

        column_markers_as_regex_string = ""
        for str in COLUMN_MARKERS:
            column_markers_as_regex_string += str

        # First 2 lines are optional, for date and time
        for j in range(2):
            match = re.match(f'^\\(([{column_markers_as_regex_string}])\\)\\s*(.*)', lines[j].strip())
            if not match:
                data[COLUMN_NAMES[j]] = lines[j].strip()
        marker_index = 0
        line_index = 2
        while line_index < len(lines):
            line = lines[line_index]
            match = re.match(f'\\(([{COLUMN_MARKERS[marker_index]}])\\)\\s*(.*)', line.strip())
            if match:
                key, text = match.groups()
                data[key].append(text.strip())
                line_index += 1
            else:
                data[COLUMN_MARKERS[marker_index]].append("")
            marker_index = (marker_index + 1) % len(COLUMN_MARKERS)

        parsed_entries.append(data)

    return parsed_entries


def expand_rows(parsed_entries):
    rows = []

    for data in parsed_entries:
        max_count = max(
            [len(data[k]) for k in COLUMN_MARKERS] + [1]
        )

        for i in range(max_count):
            row = []

            # Date and time are set only for the first row of an entry
            row.append(data[COLUMN_NAMES[0]] if i == 0 else "")
            row.append(data[COLUMN_NAMES[1]] if i == 0 else "")

            # Append the data from the column markers
            row += [data[column_name][i] if i < len(data[column_name]) else "" for column_name in COLUMN_MARKERS]

            rows.append(row)

    return rows


def write_to_excel(rows, output_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    # Header
    ws.append(COLUMN_NAMES)

    # Data rows
    for row in rows:
        ws.append(row)

    wb.save(output_file)


def main():
    input_file = "input.txt"
    output_file = "output.xlsx"

    parsed_entries = parse_input_file(input_file)
    rows = expand_rows(parsed_entries)
    write_to_excel(rows, output_file)

    print(f"Excel file '{output_file}' generated successfully.")


if __name__ == "__main__":
    main()