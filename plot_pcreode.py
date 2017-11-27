file_path ='./myeloid_w_ids/'


#pdb.set_trace()
#out_graph, out_ids = pcreode.pCreode( data=pca_reduced_data, density=density_1, noise=noise, 
#                                      target=target, file_path=file_path, num_runs=10)

#pcreode.pCreode_Scoring( data=pca_reduced_data, file_path=file_path, num_graphs=10)

seed = 123
gid = 9

#Plot graph
pcreode.plot_save_graph( seed=seed, file_path=file_path, graph_id=gid, data=pca_reduced_data, 
                         overlay= data_raw.ELANE, density=density_1, file_out='Elane', upper_range=1.5)