import argparse
import os

import cv2

#from table_ocr.extract_tables import find_tables

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+")


def main(files):
    results = []
    for f in files:
        directory, filename = os.path.split(f)
        image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        tables = find_tables(image)
        files = []
        filename_sans_extension = os.path.splitext(filename)[0]
        if tables:
            os.makedirs(os.path.join(directory, filename_sans_extension), exist_ok=True)
        for i, table in enumerate(tables):
            table_filename = "bank_stmt.png".format(i)
            table_filepath = os.path.join(
                directory, filename_sans_extension, table_filename
            )
            files.append(table_filepath)
            cv2.imwrite(table_filepath, table)
        if tables:
            results.append((f, files))

    for image_filename, table_filenames in results:
        print("\n".join(table_filenames))


if __name__ == "__main__":
    args = parser.parse_args()
    files = args.files
    main(files)
