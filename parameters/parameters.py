import os

file_name = 'energydata_complete.csv'
data_folder = 'data'

main_path = os.getcwd()

file_path = os.path.join(os.path.join(main_path, data_folder), file_name)