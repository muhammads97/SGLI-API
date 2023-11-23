"""
Author: Muhammad Salah
Email: msalah.29.10@gmail.com
"""
from src import *

if __name__ == "__main__":
    if args.search:
        if args.csv: search_csv(args)
        else:        search(args)
    elif args.download:
        if args.csv: download_csv(args)
        else:        download(args)
    elif args.extract:
        if args.csv: extract_csv(args)
        else:        extract(args)
    empty_temp()
