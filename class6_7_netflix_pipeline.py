import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    drop_missing_rows,
    remove_duplicates,
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

    # Create a Path object from args.input.
    # Inside a try block, load that path using pd.read_csv().
    # Catch FileNotFoundError, log an ERROR message,
    # and exit with sys.exit(1).
    # Log an INFO message.

    # TODO 5:

    # Call show_overview().
    # Log an INFO message.

    # TODO 6:
    f"Dropped missing rows. Remaining rows: {df.shape[0]}"
    f"Removed duplicates. Remaining rows: {df.shape[0]}"
    logger.info("Removed duplicates. Remaining rows: %d", df.shape[0])
    logger.info("Dropped missing rows. Remaining rows: %d", df.shape[0])
    logger.info("Final overview of the cleaned DataFrame:")
    show_overview(df)
    logger.info("Cleaning process completed.")
    return df

    # Call remove_duplicates().
    # Call drop_missing_rows().
    # Log an INFO message after each step that
    # includes the number of rows removed.


if __name__ == "__main__":
    main()
