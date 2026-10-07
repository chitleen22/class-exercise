import logging

logger = logging.getLogger(__name__)


def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    # If any are missing, log an ERROR and raise ValueError.
    # Log an INFO.
    # Return the DataFrame.
    if missing:
        logger.error("missing required columns: %s", missing)
        raise ValueError(f"Missing required columnds: {missing}")
    logger.info("All required columna present: %s", required_columns)
    return df
