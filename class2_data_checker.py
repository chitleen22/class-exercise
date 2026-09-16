import argparse
import csv
import logging
import sys
from pathlib import Path


def check_data(filename):
    """Read the CSV file and check for missing values."""
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]
    missing_rows = []

    for row_number, row in enumerate(data, start=2):
        if any(value == "" for value in row):
            missing_rows.append(row_number)

    return header, data, missing_rows


# TODO 1: Create an ArgumentParser
parser = argparse.ArgumentParser(
    description="Check the quality of a CSV file.")

# TODO 2: Add a named argument (required):
parser.add_argument("-i", "--input", required=True, help="CSV file to check")

# TODO 3: Add an named argument (optional):
parser.add_argument("-o", "--output", default="data_quality.txt",
                    help="Output report filename")

# TODO 4: Add a boolean flag:
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show detailed DEBUG messages")

# TODO 5: Parse the command-line arguments
args = parser.parse_args()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if args.verbose else logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# Check if the file exists
p = Path(args.input)
if not p.is_file():
    logger.error(f"File not found: '{args.input}'")
    sys.exit(1)

logger.info(f"File validated: '{args.input}'")

# Check the data
header, data, missing_rows = check_data(args.input)
logger.info(f"Loaded {len(data)} rows")

for row_number in missing_rows:
    logger.warning(f"Row {row_number} has missing values")

# Save the report
with open(args.output, "w") as f:
    f.write(f"Number of rows: {len(data)}\n")
    f.write(f"Number of columns: {len(header)}\n")
    f.write(f"Number of rows with missing values: {len(missing_rows)}\n")

logger.info(f"Report saved to {args.output}")
