import numpy as np
import os
from pulmonary.utils.io_files import getFinalNumber

def export_bin_results(filename, num_bins):
    #path = "/home/ydon868/Desktop/VentilationStudy/lung030/GTV/"#input("Please enter the terminal exnode file path:? ")
    #filename = path + "terminal.exnode"
    #num_bins = 20
    # print(filename)
    #dt = {'names':['Node','X','Y','Z','V','C','Pp','TV'], 'formats':[np.int,np.float,np.float,np.float,np.float,np.float,np.float,np.float]}
    ventarray = [[] for i in range(8)]
    filename = os.path.dirname(filename) + '/terminal.exnode'
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if 'Node' in lines[i]:
                nodenumber = getFinalNumber(lines[i], 'int')
                ventarray[0].append(int(nodenumber))
                for j in range(1,8):
                    if '************' in lines[i+j]:
                        lines[i+j]='3000.0'
                    ventarray[j].append(float(lines[i+j]))
    ventdata = np.array(ventarray)
    #ventdata['Node']=ventarray[0];ventdata['X']=ventarray[1];ventdata['Y']=ventarray[2];ventdata['Z']=ventarray[3];
    #ventdata['V']=ventarray[4];ventdata['C']=ventarray[5];ventdata['Pp']=ventarray[6];ventdata['TV']=ventarray[7];
    # print(ventdata)
    ventdata = ventdata.transpose()
    lung_height = max(ventdata[:,2])-min(ventdata[:,2])
    bin_interval = lung_height/num_bins
    # normalized by mean
    for i in range(4):
        col_mean = np.mean(ventdata[:,i+4])
        ventdata[:,i+4]=ventdata[:,i+4]/col_mean
    try:
        os.remove(os.path.dirname(filename) + '/binResult.txt')
    except OSError:
        pass
    for i in range(num_bins):
        bin_min = min(ventdata[:,2]) + bin_interval*i
        bin_max = min(ventdata[:,2]) + bin_interval*(i+1)
        height_percent = ((100/num_bins)*(i+1))-2.5
        if i != (num_bins-1):
            bin_array = ventdata[np.where((ventdata[:,2] >= bin_min) & (ventdata[:,2] < bin_max))]
        else:
            bin_array = ventdata[np.where((ventdata[:, 2] >= bin_min) & (ventdata[:, 2] <= bin_max))]
        flow_bin_mean = np.mean(bin_array[:, 4])
        comp_bin_mean = np.mean(bin_array[:, 5])
        pp_bin_mean = np.mean(bin_array[:, 6])
        tv_bin_mean = np.mean(bin_array[:, 7])
        flow_bin_std = np.std(bin_array[:, 4])
        comp_bin_std = np.std(bin_array[:, 5])
        pp_bin_std = np.std(bin_array[:, 6])
        tv_bin_std = np.std(bin_array[:, 7])
        flow_bin_sum = np.sum(bin_array[:,4])/1000
        bin_list = [height_percent, flow_bin_sum, flow_bin_mean, flow_bin_std, comp_bin_mean, comp_bin_std, pp_bin_mean, pp_bin_std, tv_bin_mean, tv_bin_std]
        path = os.path.dirname(filename)
        with open(path + '/binResult.txt', 'a') as f:
            for item in bin_list:
                f.write(str(item)+"\t")
            f.write("\n")