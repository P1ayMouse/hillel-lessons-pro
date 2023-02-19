import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()

    print(args.output)


if __name__ == '__main__':
    main()
