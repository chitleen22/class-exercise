import logging

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
    pass


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
    pass


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    logger.debug("Before dropping missing rows: %d rows", df.shape[0])
    df = df.dropna()
    logger.debug("After dropping missing rows: %d rows", df.shape[0])
    return df
