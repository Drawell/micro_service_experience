import argparse
from os import path
from time import sleep

STORAGE_NAME = "storage"

def write(filename, payload):
    with open(path.join(STORAGE_NAME, filename), 'a') as f:
        f.writelines(payload)


def read(filename):
    with open(path.join(STORAGE_NAME, filename), 'r') as f:
        content = f.read()
    
    return content



def main():
    parser = argparse.ArgumentParser(prog='File Storage',
                                     description='Store some information in files')
    parser.add_argument('filename')
    parser.add_argument('-w', '--write', action='store_true')
    parser.add_argument('-r', '--read', action='store_true')
    parser.add_argument('-c', '--content')
    parser.add_argument('-p', '--pause', type=int)
    args = parser.parse_args()

    if args.write:
        write(args.filename, args.content)
    elif args.read:
        print(read(args.filename))
    else:
        print("unkonwn operation")

    if args.pause:
        sleep(args.pause)




if __name__ == '__main__':
    main()