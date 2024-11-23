from obspy import read
from obspy import UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib import rcParams

rcParams['pdf.fonttype'] = 42
# print(rcParams['pdf.fonttype'])


if len(sys.argv) != 3:
   print("Usage: python PARTIALplot_detected_waveforms_UtahFORGE.py <start_ind> <end_ind>")
   sys.exit(1)

IND_FIRST = int(sys.argv[1])
IND_LAST = int(sys.argv[2])
print("PROCESSING:", IND_FIRST, IND_LAST)
   

# Inputs
times_dir = './data/network_detection/'
event_file = "1sta_1stathresh_FORK_GHZ_events.txt"
[det_start_ind, diff_ind, nevents, peaksum, tot_vol] = np.loadtxt(times_dir+event_file, usecols=(0,1,2,3,4), unpack=True, skiprows=1, delimiter=',')
out_dir = times_dir+'UU.FORK.GHZ_WaveformPlots/'
if not os.path.exists(out_dir):
   os.makedirs(out_dir)

# Times
dt_fp = 4 * 0.15 # 0.005 from UU.FORK.GHZ.fingerprint.json
det_times = dt_fp * det_start_ind
diff_times = dt_fp * diff_ind
print(len(det_times))

# Window length (seconds) for event plot
init_time = UTCDateTime('2024-04-02T00:00:04.150000') # global start time for all channels
wtime_before = 30
wtime_after = 30

# Plot dimensions
out_width = 400
out_height = 800

# Read in data and plot
# Use filtered data for plotting
ts_dir = '../SeisDetection/data/'
st = read(ts_dir+'Deci500.*', format='MSEED')
print(len(st))
print(st.__str__(extended=True))

for kk in range(IND_FIRST, IND_LAST):
   # if diff_times[kk]
   ev_time = init_time + det_times[kk]
   start_time = ev_time - wtime_before
   end_time = ev_time + diff_times[kk] + wtime_after
   # end_time = ev_time + wtime_after
   # if (diff_times[kk] > wtime_after): # special case: unusually long delay between start and end times
   #    end_time = ev_time + diff_times[kk] + wtime_after

   st_slice = st.slice(start_time, end_time)

   out_file = out_dir+'event_rank'+format(kk,'05d')+'_peaksum'+str(int(peaksum[kk]))+'_ind'+str(int(det_start_ind[kk]))+'_time'+str(det_times[kk])+'_'+ev_time.strftime('%Y-%m-%dT%H:%M:%S.%f')+'_30pad.png'
   st_slice.plot(equal_scale=False, size=(out_width,out_height), outfile=out_file)
