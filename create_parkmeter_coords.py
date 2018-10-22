import pandas as pd
import numpy as np

data_case_storage="C://Users//Antoine//Documents//Oliver Wymann//stored_data_case.h5"

def list_HDF_file(file_name):
    with pd.HDFStore(file_name, complevel=9, complib='blosc') as store:
        result = store.keys()   
    return result

def read_HDF_file(file_name, table):
    with pd.HDFStore(file_name, complevel=9, complib='blosc') as store:
        return store[table]

print(list_HDF_file(data_case_storage))

# Extracting the parkmeter coordinates and deleting the duplicates
df=read_HDF_file(data_case_storage,"/transaction_and_locations")
parkmeter_coordinates = df['parkmeter_coordinates'].drop_duplicates()


# Printing stuff
print(type(parkmeter_coordinates))
print(parkmeter_coordinates.shape)

print(parkmeter_coordinates.head(10))
print(parkmeter_coordinates[44])
print(type(parkmeter_coordinates[44]))
float_coords = np.array(parkmeter_coordinates[44], dtype=np.float64)

# Storing the coordinates
parkmeter_coordinates.to_hdf('parkmeter_coords.h5', key='parkmeter_coordinates')
