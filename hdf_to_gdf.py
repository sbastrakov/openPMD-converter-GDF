
from __future__ import division
import os
import sys
def hdf_to_gdf(hdf_file_directory, gdf_file_directory):

    print('Converting .gdf to .hdf file')
    if os.path.exists(gdf_file_directory):
        os.remove(gdf_file_directory)

    hdf_file = h5py.File(hdf_file_directory, 'a')
    with open(gdf_file_directory, 'wb') as gdf_file:
        gdf_file_to_hdf_file(gdf_file, hdf_file)

    gdf_file.close()
    hdf_file.close()
    print('Converting .gdf to .hdf file... Complete.')
class Constants:
    GDFID = 94325877
    GDFNAMELEN = 16


def files_from_args(file_names):
    gdf_file = ''
    hdf_file = ''
    for arg in file_names:
        if arg[-4:] == '.gdf':
            gdf_file = arg
        elif arg[-3:] == '.h5':

            hdf_file = arg
    return gdf_file, hdf_file


def converter(hdf_file, gdf_file):
    if hdf_file != '':
        if os.path.exists(hdf_file):
            if gdf_file == '':
                gdf_file = hdf_file[:-4] + '.gdf'
                print('Destination .gdf directory not specified. Defaulting to ' + gdf_file)
            else:
                gdf_file = gdf_file[:-4] + '.gdf'

            hdf_to_gdf(hdf_file, gdf_file)
        else:
            print('The .hdf file does not exist to convert to .gdf')


def main(file_names):
    gdf_path, hdf_path = files_from_args(file_names)
    converter(hdf_path, gdf_path)


if __name__ == "__main__":
    file_names = sys.argv
    main(file_names)
