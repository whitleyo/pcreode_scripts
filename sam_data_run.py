# imports the pcreode package
import pcreode
# matplotlib is a commonly used package for plotting
import matplotlib.pyplot as plt
# pandas is a package used for making the handling of large data sets easier
import pandas as pd
# numpy is very common package for handling arrays and matrices
import numpy as np

import pdb

fName = './normData.txt'
normData_array = np.loadtxt(fname = fName, dtype = 'string', delimiter = '\t')

var_genes = np.loadtxt(fname = 'varGenes.txt', dtype = 'string')
col0 = normData_array[:,0]
row_keep = (np.in1d(col0,var_genes) | (col0 == ''))
normData_subset = normData_array[row_keep,:]

normData_t = normData_subset.T
dim_normData_t = np.shape(normData_t)




my_data = normData_t[1:dim_normData_t[0] + 1, 1:dim_normData_t[1] + 1].astype('float')
my_index = normData_t[1:dim_normData_t[0] + 1, 0]
my_cols = normData_t[0,1:dim_normData_t[1] + 1]

df = pd.DataFrame(data = my_data, index = my_index, columns = my_cols)

data_pca = pcreode.PCA( df)
data_pca.get_pca()

data_pca.pca_plot_explained_var( xlim=(0,20))
exp_var_fname = 'sam_data_pca_exp_var'
plt.savefig(fname = exp_var_fname)

pca_test_data = data_pca.pca_set_components( 20)



fig = plt.figure( figsize=(12,12))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
cc = 'r'

#commented out are the plots used to make pca_plot 1
#ax1.scatter( pca_test_data[:,0], pca_test_data[:,1], alpha=0.5, s=25, c=cc)
#ax2.scatter( pca_test_data[:,2], pca_test_data[:,1], alpha=0.5, s=25, c=cc)
#ax3.scatter( pca_test_data[:,2], pca_test_data[:,3], alpha=0.5, s=25, c=cc)
#ax4.scatter( pca_test_data[:,4], pca_test_data[:,3], alpha=0.5, s=25, c=cc)
#ax1.set_xlabel("PC1", fontsize=15), ax1.set_ylabel("PC2", fontsize=15)
#ax2.set_xlabel("PC3", fontsize=15), ax2.set_ylabel("PC2", fontsize=15)
#ax3.set_xlabel("PC3", fontsize=15), ax3.set_ylabel("PC4", fontsize=15)
#ax4.set_xlabel("PC5", fontsize=15), ax4.set_ylabel("PC4", fontsize=15)

ax1.scatter( pca_test_data[:,4], pca_test_data[:,5], alpha=0.5, s=25, c=cc)
ax2.scatter( pca_test_data[:,6], pca_test_data[:,5], alpha=0.5, s=25, c=cc)
ax3.scatter( pca_test_data[:,8], pca_test_data[:,7], alpha=0.5, s=25, c=cc)
ax4.scatter( pca_test_data[:,9], pca_test_data[:,8], alpha=0.5, s=25, c=cc)

ax1.set_xlabel("PC5", fontsize=15), ax1.set_ylabel("PC6", fontsize=15)
ax2.set_xlabel("PC7", fontsize=15), ax2.set_ylabel("PC6", fontsize=15)
ax3.set_xlabel("PC9", fontsize=15), ax3.set_ylabel("PC8", fontsize=15)
ax4.set_xlabel("PC10", fontsize=15), ax4.set_ylabel("PC9", fontsize=15)
#fig_name = './pca_plots'
fig_name = './pca_plots2'

#select top 11 PCs based upon brendan's PCA analysis
pca_reduced_data = data_pca.pca_set_components( 11)

#select top 3 pcs
#pca_reduced_data = data_pca.pca_set_components()


plt.savefig(fname = fig_name)

# determine appropriate density

dens = pcreode.Density( pca_reduced_data)
dens.nearest_neighbor_hist( )
nn_hist_fname = './sam_data_nn_hist'
plt.savefig(fname = nn_hist_fname)

density_8 = dens.get_density( radius=5.0)
dens.density_hist( n_bins=50)
fnam_dens_hist_8 = 'sam_data_dens_hist_5'
plt.savefig(fname = fnam_dens_hist_8)

# Plot density onto cells plotted in PCA space, with density for radius 5
fig = plt.figure( figsize=(16,8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
cc = density_8
ax1.scatter( pca_reduced_data[:,0], pca_reduced_data[:,1], alpha=0.5, s=25, c=cc)
ax2.scatter( pca_reduced_data[:,2], pca_reduced_data[:,1], alpha=0.5, s=25, c=cc)
ax1.set_xlabel("PC1", fontsize=15), ax1.set_ylabel("PC2", fontsize=15)
ax2.set_xlabel("PC3", fontsize=15), ax2.set_ylabel("PC2", fontsize=15)
fname_dens_rad_8 = 'sam_data_dens_rad_5'
plt.savefig(fname = fname_dens_rad_8)

#repeat procedure for radius 7

density_20 = dens.get_density( radius=7.0)
dens.density_hist( n_bins=100)
fnam_dens_hist_20 = 'sam_data_dens_hist_7'
plt.savefig(fname = fnam_dens_hist_20)

fig = plt.figure( figsize=(16,8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
cc = density_20
ax1.scatter( pca_reduced_data[:,0], pca_reduced_data[:,1], alpha=0.5, s=25, c=cc)
ax2.scatter( pca_reduced_data[:,2], pca_reduced_data[:,1], alpha=0.5, s=25, c=cc)
ax1.set_xlabel("PC1", fontsize=15), ax1.set_ylabel("PC2", fontsize=15)
ax2.set_xlabel("PC3", fontsize=15), ax2.set_ylabel("PC2", fontsize=15)
fnam_dens_rad_20 = 'sam_data_dens_rad_7'
plt.savefig(fname = fnam_dens_rad_20)

#repeat procedure for radius 6

density_14 = dens.get_density( radius=6.0)
dens.density_hist( n_bins=100)
fnam_dens_hist_14 = 'sam_data_dens_hist_6'
plt.savefig(fname = fnam_dens_hist_14)

fig = plt.figure( figsize=(16,8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
cc = density_14
ax1.scatter( pca_reduced_data[:,0], pca_reduced_data[:,1], alpha=0.5, s=25, c=cc)
ax2.scatter( pca_reduced_data[:,2], pca_reduced_data[:,1], alpha=0.5, s=25, c=cc)
ax1.set_xlabel("PC1", fontsize=15), ax1.set_ylabel("PC2", fontsize=15)
ax2.set_xlabel("PC3", fontsize=15), ax2.set_ylabel("PC2", fontsize=15)
fnam_dens_rad_14 = 'sam_data_dens_rad_6'
plt.savefig(fnam_dens_rad_14)
