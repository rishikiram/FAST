from struct import unpack
from time import time
from obspy import read
from obspy import Stream
from obspy import UTCDateTime
from obspy.clients.fdsn import Client 
from obspy.clients.fdsn.header import FDSNException
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys
import os
import json
import glob
import collections

EQ = collections.namedtuple("EQ", ["det_start_ind", "diff_ind", "nevents","peaksum", "tot_vol"])

# Inputs - UtahFORGE
in_mseed_dir = '../SeisDetection/data/'
in_FINAL_Detection_List = './data/network_detection/1sta_1stathresh_FORK_GHZ_events.txt'
out_dir = './data/event_clips'
init_time = UTCDateTime('2024-04-02T00:00:04.150000') # global start time for all channels
dt_fp = 4 * 0.15

# wtime_before is the number of seconds before the event 
# time (first column in FINAL_Detection_List_HectorMine_7sta_2stathresh.txt).  
# wtime_after is the number of seconds after the event time.  
# these parameters specify the window length (total of 180 seconds, for the default parameters)

wtime_before = 60 # time window before origin time (s)
wtime_after = 120 # time window after origin time (s)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

[det_start_ind, diff_ind, nevents, peaksum, tot_vol] = np.loadtxt(in_FINAL_Detection_List, usecols=(0,1,2,3,4), unpack=True, skiprows=1, delimiter=',')

det_times = dt_fp * det_start_ind
diff_times = dt_fp * diff_ind

EQ_detections = []

for i in range(len(det_start_ind)):
    EQ_detection = EQ(det_start_ind[i], diff_ind[i], nevents[i], peaksum[i], tot_vol[i])
    EQ_detections.append(EQ_detection)

# Cut event files from original unfiltered data (NOT decimated filtered data) for further phase picking
st = read(in_mseed_dir+'Deci500.2024*', format='MSEED')
print(st.__str__(extended=True))
print(len(st))

print("\n ------------------- OUTPUT CUT EVENT FILES --------------------------\n")

i_load = 0

for kk in range(len(EQ_detections)):
    ev_time = init_time + det_times[kk]
    start_time = ev_time - wtime_before
    end_time = ev_time + wtime_after
    print(kk, start_time, end_time)

    i_load += 1
    
    st_slice = st.slice(start_time, end_time)

    for tr in st_slice:
        timestamp = str(ev_time.year).zfill(2) + str(ev_time.month).zfill(2) + str(ev_time.day).zfill(2) + str(ev_time.hour).zfill(2) + str(ev_time.minute).zfill(2) + str(ev_time.second).zfill(2)

        output_file_name = out_dir + "/" + kk +'_'+ timestamp + '_' + str(det_times[kk]) + '_' + tr.stats.station + '_' + tr.stats.channel + '.sac'
        tr.write(output_file_name, format='SAC')

print ("Number of event waveforms loaded =", i_load) 
