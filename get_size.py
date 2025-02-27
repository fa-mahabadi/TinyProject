import argparse
import os


def directory_size(dir):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return f"size of {args.directory } : {total_size/1024:.2f} KB"


def file_size(file):
    return f"size of {args.file } :{os.path.getsize(file)/1024:.2f} KB"


def size_of_file_with_specify_extension(dir, extension):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(f".{extension}"):
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
    return f"size of {args.directory } with .{extension} : {total_size/1024:.2f} KB"


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
parser.add_argument(
    "-F", "--file_extension", help="display size of file with specify extenstion"
)
group.add_argument("-d", "--directory", help="display size of directory")
group.add_argument("-f", "--file", help="display size of file")
args = parser.parse_args()


if args.directory and args.file_extension:
    print(size_of_file_with_specify_extension(args.directory, args.file_extension))
elif args.file and args.file_extension:
    print("Have not result")
elif args.directory:
    print(directory_size(args.directory))
elif args.file:
    print(file_size(args.file))
else:
    print("Please enter correct format, for more information use 'get_size.py -h'")
