import argparse
from typing import List

from src.utils.add_common_args import add_common_args


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fix some common problems that your files have. Add missing date metadata when need or other missing tags",
        add_help=True,
        exit_on_error=True,
    )

    parser.add_argument(
        "--dates_from",
        nargs="*",
        type=List[str],
        default=["fileexif", "filename"],
        help="Sources to obtain the capture date of the asset, in order of preference. Options can include 'fileexif' (from file's EXIF data), 'filename' (from the filename) or 'filedate' (from the OS date of the file)",
    )

    parser.add_argument(
        "--overwrite_dates",
        action="store_true",
        default=False,
        help="Overwrite some date tags even if they are defined, based on the 'date_from' argument",
    )

    parser.add_argument(
        "--gps_fix",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Fix the 'QuickTime:GPSCoordinates' tag of the file metadata",
    )

    parser.add_argument(
        "--os_dates",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Modify the file creation and modification time based on his exif",
    )

    add_common_args(parser)

    return parser.parse_args()
