#!/usr/bin/env python3
from argparse import ArgumentParser
import os
from datetime import datetime
import subprocess


def copy_folders(folder, target):
    print('Start copy:\t%s' % folder)
    subprocess.check_call(['cp', '-r', folder, target])


def main():
    parser = ArgumentParser()
    parser.add_argument('--src', required=True)
    parser.add_argument('--target', required=True)
    parser.add_argument('--even', required=False, default=False, action='store_true')
    args = parser.parse_args()
    for fn in os.listdir(args.src):
        file_path = os.path.join(args.src, fn)
        if not os.path.isdir(file_path):
            continue
        try:
            when = datetime.strptime(fn, '%Y-%m-%d')
            if args.even and when.day % 2 == 0:
                copy_folders(file_path, args.target)
            elif not args.even and when.day % 2 == 1:
                copy_folders(file_path, args.target)
        except ValueError:
            pass


if __name__ == '__main__':
    main()
