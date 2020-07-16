import argparse

from fileIO.BulkFileModification import BulkFileModification


def main(path, extension):
    bulk = BulkFileModification(path, extension)
    bulk.bulk_head_insert('<script>')
    print('Operating on the following files : ', bulk.file_paths)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Indicate the absolute path of the files to browse.', default='.')
    parser.add_argument('--ext', help='Provide the extension to filter with.', default='html')
    args = parser.parse_args()

    # execute only if run as a script
    main(args.path, args.ext)
