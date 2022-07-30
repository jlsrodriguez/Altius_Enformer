# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:16:51 2021

@author: jarod
"""

from Bio import SeqIO
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'

import kipoiseq
from kipoiseq import Interval
import pandas as pd
import numpy as np



def fasta_extractor(fasta):
    #TODO: Navigate to folder containing fasta and navigate back: oschdir
    
    sequences = []
    seq_names = []
    
    with open(fasta, 'r') as file:
        for Seq_record in SeqIO.parse(file, 'fasta'):
            format_string = "%s" % Seq_record.seq
            handle = Seq_record.id
            sequences.append(format_string)
            seq_names.append(handle)
            
    return sequences, seq_names

#One-hot encoder made for fasta files, subs an N in for errors   
def one_hot_encoder(sequences):
    
    temp_base = []
    
    pattern = 'ACGTN'
    
    full_seq_dict = {}
    single_seq_dict = {}
    
    char_to_int = dict((c,i) for i, c in enumerate(pattern))
    int_to_char = dict((i,c) for i, c in enumerate(pattern))
    n = 0
    
    for seq in sequences:
        
        int_seq = [char_to_int[char] for char in seq]
        
        one_hot_seq = list()
        
        for base in int_seq:
            
           
           if base == 4:
               
               temp_base = [0,0,0,0]
               one_hot_seq.append(temp_base)
               
           else:
            
               temp_base = [0 for _ in range(len(pattern)-1)]
               temp_base[base] = 1
               one_hot_seq.append(temp_base)
             
        one_hot_seq = np.array(one_hot_seq)
        
        single_seq_dict = {n:one_hot_seq}
        
        full_seq_dict[n] = single_seq_dict[n]
        
        n = n + 1
    for x in range(len(sequences)):
        
        full_seq_dict[x] = full_seq_dict[x][np.newaxis,:,:]    
        
    return full_seq_dict
