import openpyxl
import csv
import os

def convert_excel_to_csv(excel_path, csv_path):
    """
    Converts an Excel file to a CSV file.

    Args:
        excel_path (str): The path to the input Excel file.
        csv_path (str): The path to the output CSV file.
    """
    print(f"Starting conversion of {excel_path} to {csv_path}...")

    try:
        workbook = openpyxl.load_workbook(excel_path)
    except FileNotFoundError:
        print(f"Error: The file {excel_path} was not found.")
        return

    sheet = workbook.active

    with open(csv_path, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        for row in sheet.iter_rows():
            writer.writerow([cell.value for cell in row])

    print("Conversion completed successfully.")

if __name__ == "__main__":
    # Define the file paths
    excel_file = "sample.xlsx"  # Replace with your Excel file name
    csv_file = "output.csv"      # Replace with your desired CSV file name

    # Get the absolute paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(current_dir, excel_file)
    csv_path = os.path.join(current_dir, csv_file)

    # Run the conversion
    convert_excel_to_csv(excel_path, csv_path)
