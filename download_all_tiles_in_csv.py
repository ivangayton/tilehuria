#!/bin/python
"""Download necessary tiles for creation of an MBTile dataset.

Arguments:
    [1] A CSV file or URL created by create_csv.py containing tile URLs

Usage:
    
Output:
    Pile 'o' tiles from a tileserver

Example:
    python3 download_all_tiles_in_csv.py mylist.csv  
"""
import sys
import os
import threading
import csv
import time
import urllib.request

def check_dir(path):
    if not os.path.exists(path):
        outdir = os.makedirs(path)

def managechunk(chunk, outdirpath):
    """Downloads all tiles contained in a chunk (list of tile rows)"""
    for item in chunk:
        row = item[0].split(';')
        url = (row[4])
        (z, x, y) = (str(row[3]), str(row[1]), str(row[2]))
        check_dir('{}{}/{}'.format(outdirpath, z, x))
        outfilename = ('{}/{}/{}/{}.png'.format(outdirpath, z, x, y))
        try:
            rawdata = urllib.request.urlopen(url, timeout=10).read()
        except:
            print('Thread {} timed out on {}'
                  .format(threading.get_ident(),outfilename))
        # print('Thread {} Writing {}'
        #      .format(threading.get_ident(),outfilename))
        # if the file is less than 116 bytes, there's no tile at this level
        if(len(rawdata) > 116):
            with open(outfilename, 'wb') as outfile:
                outfile.write(rawdata)

def task(inlist, num_threads, outdirpath):
    header_row = inlist.pop(0)
    # Break the list into chunks of approximately equal size
    chunks = [inlist[i::num_threads] for i in range(num_threads)]

    threads = []
    for chunk in chunks:

        thread = threading.Thread(target=managechunk, args=(chunk, outdirpath))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def main(infile):
    """Eat CSV of tile urls, spit out folder full of tiles"""
    (infilename, extension) = os.path.splitext(infile)
    outdirpath = '{}/'.format(infilename)
    check_dir(outdirpath)
    threads_to_use=50
    
    start = time.time()
    with open(infile) as csvfile:
        reader = csv.reader(csvfile)
        tile_rows = list(reader)
        if(len(tile_rows)) < 100:
           threads_to_use = int(len(tile_rows)/2)
        task(tile_rows, threads_to_use, outdirpath)

    end = time.time() - start
    print('Finished. Downloading took {} seconds'.format(end))

if __name__ == "__main__":

    if len( sys.argv ) != 2:
        print("[ ERROR ] you must supply 1 argument: ")
        print("1) a CSV file")

        sys.exit(1)

    main(sys.argv[1])
