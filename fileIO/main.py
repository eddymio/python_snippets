import argparse

from BulkFileModification import BulkFileModification


def main(path, extension, content):
    bulk = BulkFileModification(path, extension)
    print('Operating on the following files : ', bulk.file_paths)
    bulk.bulk_head_insert(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Indicate the absolute path of the files to browse.', default='.')
    parser.add_argument('--ext', help='Provide the extension to filter with.', default='html')
    parser.add_argument('content', help='Content to include (ex : "<script>...</script>").')
    args = parser.parse_args()

    # execute only if run as a script
    main(args.path, args.ext, args.content)
