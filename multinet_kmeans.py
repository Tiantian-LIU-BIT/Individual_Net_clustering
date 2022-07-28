# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 09:27:29 2020

@author: tiantian
"""

import numpy as np
import scipy.io as scio
from Bio.Cluster import kcluster
import os
from sklearn.metrics import silhouette_score
import h5py
list_name=[]
list_name.append(['attention'])
list_name.append(['dmn'])
list_name.append(['fpn'])
list_name.append(['limbic'])
list_name.append(['motor'])
list_name.append(['salient'])
list_name.append(['visual'])

list_name=['attention','dmn','fpn','limbic','motor','salient','visual']
tt=0
for info in os.listdir(r'E:\research\Aging_individual\myindividualwindow\pyimport'):
    domain=os.path.abspath(r'E:\research\Aging_individual\myindividualwindow\pyimport')
    info=os.path.join(domain,info)
    
    file=h5py.File(info, 'r')
    all_data=np.transpose(file['fc_all'])
    
    clusterid,error,nfound=kcluster(all_data,3,dist='b',npass=100)

    silhouette_avg = silhouette_score(all_data, clusterid, metric = 'manhattan')


    save_fn1 = str.format('E://research//Aging_individual//myindividualwindow//'+list_name[tt]+'_clusterid03.mat')
    scio.savemat(save_fn1, {'clusterid': clusterid})
    
    save_fn2 = str.format('E://research//Aging_individual//myindividualwindow//'+list_name[tt]+'_error03.mat')
    scio.savemat(save_fn2, {'error': error})
    
    save_fn3 = str.format('E://research//Aging_individual//myindividualwindow//'+list_name[tt]+'_nfound03.mat')
    scio.savemat(save_fn3, {'nfound': nfound})
    
    save_fn4 = str.format('E://research//Aging_individual//myindividualwindow//'+list_name[tt]+'_silhouette_avg03.mat')
    scio.savemat(save_fn4, {'silhouette_avg': silhouette_avg})
    
    tt=tt+1
    