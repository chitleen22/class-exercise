import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    clean_text,
    drop_missing_rows,
    remove_duplicates,
    remove_iqr_outliers,
    show_overview,
)


logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    input_path = Path(args.input)
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        logger.error("File not found: %s", input_path)
        sys.exit(1)
    logger.info("Loaded %d rows from %s", df.shape[0], input_path)
    show_overview(df)
    df = remove_duplicates(df)
    logger.info("Removed duplicates. Remaining rows: %d", df.shape[0])
    df = drop_missing_rows(df)
    logger.info("Dropped missing rows. Remaining rows: %d", df.shape[0])
    show_overview(df)
    logger.info("Final overview of the cleaned DataFrame:")
    show_overview(df)
    logger.info("Cleaning process completed.")
    return df

    # TODO 3:
    # Inside a try block, remove runtime_minutes outliers
    # using remove_iqr_outliers() with a threshold of 1.5.
    # Catch ValueError and exit with sys.exit(1).# Log an INFO message. 
    try:
        df = remove_iqr_outliers(df, "runtime_minutes", 1.5)
    except ValueError as e:
        logger.error("Error removing outliers: %s", e)
        sys.exit(1)
    logger.info(
        "Removed runtime_minutes outliers. Remaining rows: %d", df.shape[0])
    show_overview(df)
    logger.info("Overview after removing runtime_minutes outliers:")
    show_overview(df)

    # TODO 4:
    # Apply clean_text() to title, type, and country.
    # Log an INFO message.
    df["title"] = df["title"].apply(clean_text)
    df["type"] = df["type"].apply(clean_text)
    df["country"] = df["country"].apply(clean_text)
    logger.info("Applied clean_text() to title, type, and country.")
    show_overview(df)
    logger.info("Applied clean_text() to title, type, and country.")
    logger.info(
        "overview after appplying clean_text() to title, type and country.")
    show_overview(df)
    logger.info("Cleaning process completed.")

    # TODO 5:
    # Create a report (dictionary) containing rows_before, rows_after, rows_removed, and columns.
    # Log an INFO message reporting: rows_before, rows_after, rows_removed, and columns.
    report = {
        "rows_before": 1000,  # Replace with the actual number of rows before cleaning
        "rows_after": df.shape[0],
        # Replace with the actual number of rows removed
        "rows_removed": 1000 - df.shape[0],
        "columns": df.columns.tolist()
    }
    logger.info(
        "Cleaning report: rows_before=%d, rows_after=%d, rows_removed=%d, columns=%s",
        report["rows_before"],
        report["rows_after"],
        report["rows_removed"],
        report["columns"]
    )
    return report


if __name__ == "__main__":
    main()
