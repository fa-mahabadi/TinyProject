import argparse

parser = argparse.ArgumentParser(description="calculate average of numbers")
parser.add_argument(
    "-g", "--grade", type=float, nargs="+", help="integer number that user input"
)
parser.add_argument(
    "-f",
    "--format",
    default=2,
    type=int,
    help="Number of decimal places to round(default is 2)",
)
parser.add_argument(
    dest="total", const=sum, action="store_const", help="sum of integer numbers"
)
args = parser.parse_args()
avg = args.total(args.grade) / len(args.grade)
print(f"average is: {avg:.{args.format}f}")
