from obspy import read
from obspy import UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib import rcParams

rcParams['pdf.fonttype'] = 42
print(rcParams['pdf.fonttype'])


if len(sys.argv) != 3:
   print("Usage: python PARTIALplot_detected_waveforms_UtahFORGE.py <start_ind> <end_ind>")
   sys.exit(1)

IND_FIRST = int(sys.argv[1])
IND_LAST = int(sys.argv[2])
print("PROCESSING:", IND_FIRST, IND_LAST)
   

# Inputs
times_dir = '../../data/network_detection/'
[det_start_ind, det_end_ind, dL, nevents, nsta, tot_ndets, max_ndets, tot_vol, max_vol, peaksum, num_sta, diff_ind] = np.loadtxt(times_dir+'sort_nsta_peaksum_TODO_FinalUniqueNetworkDetectionTimes.txt', usecols=(0,1,2,3,4,5,6,7,8,9,10,11), unpack=True)
out_dir = times_dir+'TODO_NetworkWaveformPlots/'
#[det_start_ind, det_end_ind, dL, nevents, nsta, tot_ndets, max_ndets, tot_vol, max_vol, peaksum, num_sta] = np.loadtxt(times_dir+'FINAL_7sta_Hector_events.txt', unpack=True)
#out_dir = times_dir+'Earthquakes_7sta_2stathresh_NetworkWaveformPlots/'
if not os.path.exists(out_dir):
   os.makedirs(out_dir)

# Times
dt_fp = 1.0
det_times = dt_fp * det_start_ind
diff_times = dt_fp * diff_ind
dL_dt = dt_fp * dL
print(len(det_times))

# Window length (seconds) for event plot
init_time = UTCDateTime('2024-04-0200:00:00.000000') # global start time for all channels
wtime_before = 10
wtime_after = 40

# Plot dimensions
out_width = 400
out_height = 800

# Read in data and plot
# Use filtered data for plotting
ts_dir = '../../data/'
st = read(ts_dir+'waveforms*/Deci500.*', format='MSEED')
print(len(st))
print(st.__str__(extended=True))

for kk in range(IND_FIRST, IND_LAST):
   ev_time = init_time + det_times[kk]
   start_time = ev_time - wtime_before
   end_time = ev_time + wtime_after
   if (diff_times[kk] > wtime_after): # special case: unusually long delay between start and end times
      end_time = ev_time + diff_times[kk] + wtime_after

   st_slice = st.slice(start_time, end_time)

   out_file = out_dir+'event_rank'+format(kk,'05d')+'_nsta'+str(int(num_sta[kk]))+'_peaksum'+str(int(peaksum[kk]))+'_ind'+str(int(det_start_ind[kk]))+'_time'+str(det_times[kk])+'_'+ev_time.strftime('%Y-%m-%dT%H:%M:%S.%f')+'.png'
   st_slice.plot(equal_scale=False, size=(out_width,out_height), outfile=out_file)
