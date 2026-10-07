import logging
import re

import pandas as pd


logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    logger.debug("DataFrame shape: %s", df.shape)
    print("Shape:", df.shape)
    print("First five rows:")
    print(df.head())
    print("Column names:", df.columns.tolist())
    print("Data types:")
    print(df.dtypes)
    logger.debug("First five rows:\n%s", df.head())
    logger.debug("Column names: %s", df.columns.tolist())
    logger.debug("Data types:\n%s", df.dtypes)
    logger.debug("DataFrame shape: %s", df.shape)
    logger.debug("Overview of the DataFrame completed.")

    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    logger.debug("Before removing duplicates: %d rows", df.shape[0])
    df = df.drop_duplicates()
    logger.debug("After removing duplicates: %d rows", df.shape[0])
    return df
    return df
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    logger.debug("Before dropping missing rows: %d rows", df.shape[0])
    df = df.dropna()
    logger.debug("After dropping missing rows: %d rows", df.shape[0])
    return df


def clean_text(value):
    """Normalize one text value."""
    # TODO 1:
    # Strip surrounding whitespace.
    # Convert text to lowercase.
    # Collapse repeated whitespace.
    value = value.strip().lower()
    value = re.sub(r'\s+', ' ', value)
    return value
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    # TODO 2:
    # If column does not exist:
    # Log an ERROR message and raise ValueError.
    # Calculate Q1, Q3, and IQR.
    # Use threshold to calculate lower and upper bounds.
    # Keep rows inside the bounds.
    # Log a DEBUG message containing the bounds and the number of rows removed.
    # Return the resulting DataFrame.
    if column not in df.columns:
        logger.error("Column '%s' does not exist in the DataFrame.", column)
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    logger.debug(
        "Removing IQR outliers from column '%s': lower_bound=%f, upper_bound=%f",
        column, lower_bound, upper_bound
    )
    before_rows = df.shape[0]
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    after_rows = df.shape[0]
    logger.debug(
        "Removed %d IQR outliers from column '%s'. Remaining rows: %d",
        before_rows - after_rows, column, after_rows
    )
    return df
