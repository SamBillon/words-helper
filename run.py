import sys

from bin.main import Entry

def main():
    entry = Entry()
    return entry.run()


if __name__ == '__main__':
    sys.exit(main())