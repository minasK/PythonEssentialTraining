from argparse import \
    ArgumentParser  # the argumentParser class allows you to keep track of all the arguments the program accepts

parser = ArgumentParser()
parser.add_argument('--output', required=True, help='destination of the file')

args = parser.parse_args()

print(args.output)

def minas(n):
    n = n
    print(n)

minas(5)
