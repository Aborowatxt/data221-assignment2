import requests
from bs4 import BeautifulSoup
import csv

wikipedia_link = "https://en.wikipedia.org/wiki/Machine_learning"

#Storing the webpage HTML into a variable
machine_learning_page = requests.get(wikipedia_link, headers={"User-Agent": "Mozilla/5.0"}).text

#Parsing the webpage HTML using beautifulsoup
machine_learning_page = BeautifulSoup(machine_learning_page, "html.parser")

# Find the main article content
content_div = machine_learning_page.find("div", id="mw-content-text")

#Find the first table inside the main content area that contains at least 3 data rows
target_table = None
tables = content_div.find_all("table")

for table in tables:
    table_rows = table.find_all("tr")

    # Count rows that contain at least one <td>
    data_row_count = 0
    for row in table_rows:
        if row.find("td") is not None:
            data_row_count += 1

    if data_row_count >= 3:
        target_table = table
        break

if target_table is None:
    print("No valid table found.")
else:
    # Extract table data rows
    table_data_rows = []
    all_rows = target_table.find_all("tr")

    for row in all_rows:
        data_cells = row.find_all("td")
        if len(data_cells) == 0:
            continue

        row_values = [cell.get_text(strip=True) for cell in data_cells]
        table_data_rows.append(row_values)

    # Find the maximum number of columns
    max_number_of_columns = 0
    for row_values in table_data_rows:
        if len(row_values) > max_number_of_columns:
            max_number_of_columns = len(row_values)

    # Extract headers from <th> if present
    header_row = None
    for row in all_rows:
        header_cells = row.find_all("th")
        if len(header_cells) > 0:
            header_row = [th.get_text(strip=True) for th in header_cells]
            break

        # Create default headers if none exist
        if header_row is None:
            column_headers = [f"col{i}" for i in range(1, max_number_of_columns + 1)]
        else:
            column_headers = header_row

            # Adjust header count to match data columns
            if len(column_headers) < max_number_of_columns:
                while len(column_headers) < max_number_of_columns:
                    column_headers.append(f"col{len(column_headers) + 1}")
            elif len(column_headers) > max_number_of_columns:
                column_headers = column_headers[:max_number_of_columns]

        # Pad rows with missing values
        for row_values in table_data_rows:
            while len(row_values) < max_number_of_columns:
                row_values.append("")


# Save the table to a CSV file
        output_file = open("wiki_table.csv", "w", newline="", encoding="utf-8")
        csv_writer = csv.writer(output_file)

        csv_writer.writerow(column_headers)
        csv_writer.writerows(table_data_rows)

        output_file.close()

        print("Saved table to wiki_table.csv")
        print("Rows saved:", len(table_data_rows))
        print("Columns:", max_number_of_columns)