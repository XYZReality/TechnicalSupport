import pandas as pd
from datetime import datetime

file_path = 'progressElements_1406.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path, low_memory=False)




def has_multiple_lines(cell_value):
    if isinstance(cell_value, str):
        # Split the cell value into lines
        lines = cell_value.split("\n")
        # Check if there are more than one line
        return len(lines) > 1
    else:
        return False


mask = df["elementName"].apply(has_multiple_lines)

rows_with_multiple_lines = df[mask]

if rows_with_multiple_lines.empty:
    print("No rows with multiple lines in the 'elementName' column found.")
else:
    # Extract the modelId column
    model_ids = rows_with_multiple_lines["modelId"]
    print(model_ids)

    # Generate a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"model_ids_with_multiple_lines_{timestamp}.csv"
    
    # Save the modelId series to a CSV file
    model_ids.to_csv(output_filename, index=False)
    print(f"Model IDs saved to {output_filename}")

