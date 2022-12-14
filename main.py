import numpy as np

import utils as utils
import os

############# SET PATHS OF VARIABLES OF INTEREST ########################################

# Paths of variables of interest, e.g. from prior generation.
# (In most cases, as in this example, these variables are saved as .npy files, grouped together in .npz).
# (Some other variables are saved as .txt files. In utils.py there are functions to deal with .txt format).
path_layer1_d = 'venv/data/results/train/postprior/layer1/d.npz'
path_layer2_d = 'venv/data/results/train/postprior/layer2/d.npz'
path_x = 'venv/data/results/train/postprior/output/x.npz'

############# CHOOSE SPECIFIC SEQUENCES FROM EACH VARIABLE OF INTEREST ##################
# (For instance, .npz files from prior generation contain several sequences).
layer1_d_seq0 = 'd_0.npy'
layer2_d_seq0 = 'd_0.npy'
x_seq = 'x_0.npy'
# Specify their paths
path_layer1_d_seq0 = os.path.join(os.path.dirname(path_layer1_d), layer1_d_seq0)   
path_layer2_d_seq0 = os.path.join(os.path.dirname(path_layer2_d), layer2_d_seq0)
path_x_seq = os.path.join(os.path.dirname(path_x), x_seq)

############# FOR EACH VARIABLE, SELECT SOME SPECIFIC UNITS #############################
# (Indexes for the units are specified in the form of lists).
# Save it all in a dictionary.
dict = {path_layer1_d_seq0: [0,1,2,3], path_layer2_d_seq0: [0,1,2,3], path_x_seq: list(np.arange(14))}





if __name__ == "__main__":

    ############# CREATE .CSV FILE IF REQUIRED FOR FURTHER ANALYSIS #########################

    #First, unzip the .npz files
    utils.unzip(path_layer1_d, layer1_d_seq0)
    utils.unzip(path_layer2_d, layer2_d_seq0)
    utils.unzip(path_x, x_seq)

    filename = 'venv/data/priorgen_file.csv'
    utils.csv_maker(dict, filename)

    ############# PLOT PRIMITIVES ###########################################################

    #Make a list with the variables to print
    var_d1 = utils.npy_to_array(path_layer1_d_seq0)[:,0:4]
    var_d2 = utils.npy_to_array(path_layer2_d_seq0)[:,0:4]
    var_x = utils.npy_to_array(path_x_seq)
    vars_lst = [var_d1, var_d2, var_x]

    #Set distance between vertical bars in the plotting (usually, primitive or chunk length).
    len_prim = 140

    #Plot
    utils.prim_plotter(vars_lst, len_prim, 'Layer_2 d', 'Layer_1 d', 'Output')













