import argparse
import logging
import sys

from class5_file_utils import inspect_file, inspect_extension

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a text file"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to a .txt file"
    )
    args = parser.parse_args()

    # TODO 1: Call inspect_file() inside a try block.
    try:
        file_info = inspect_file(args.input)
    except FileNotFoundError:
        logger.error("File not found: %s", args.input)
        sys.exit(1)

    # TODO 2: Catch FileNotFoundError.
    #         Log an ERROR message (e.g. file not found), and
    #         exit with sys.exit(1).
    try:
        file_info = inspect_extension(file_info)
    except ValueError:
        logger.error("Unsupported file format: %s", file_info["extension"])
        sys.exit(1)
    logger.info("File inspected successfully: %s", file_info["name"])
    logger.info("File extension: %s", file_info["extension"])

    # TODO 3: Call inspect_extension() inside a separate try block.

    # TODO 4: Catch ValueError.
    #         Log an ERROR message (e.g. unsupported format), and
    #         exit with sys.exit(1).

    # TODO 5: Log an INFO message containing the
    #         file name and extension.


if __name__ == "__main__":
    main()
