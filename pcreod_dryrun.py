

# imports the pcreode package
import pcreode
# matplotlib is a commonly used package for plotting
import matplotlib.pyplot as plt
# pandas is a package used for making the handling of large data sets easier 
import pandas as pd
# numpy is very common package for handling arrays and matrices
import numpy as np

import pdb

file_nm = "./Myeloid_with_IDs.csv"

data_raw = pd.read_csv( file_nm)
data_raw.head()
data_pca = pcreode.PCA( data_raw)
data_pca.get_pca()

pca_test_data = data_pca.pca_set_components( 5)
pca_reduced_data = data_pca.pca_set_components( 3)



dens = pcreode.Density( pca_reduced_data)
density_1 = dens.get_density( radius=1.0)
noise = 8.0
target = 50.0
file_path ='./myeloid_w_ids/'


#pdb.set_trace()
out_graph, out_ids = pcreode.pCreode( data=pca_reduced_data, density=density_1, noise=noise, 
                                      target=target, file_path=file_path, num_runs=10)

pcreode.pCreode_Scoring( data=pca_reduced_data, file_path=file_path, num_graphs=10)

seed = 123
gid = 9

#Plot graph
pcreode.plot_save_graph( seed=seed, file_path=file_path, graph_id=gid, data=pca_reduced_data, 
                         overlay= data_raw.ELANE, density=density_1, file_out='Elane', upper_range=1.5)


