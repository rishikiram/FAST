# 0.11 Calipatria, June 2021  

![calipatria_maps](img/calipatria_maps.png)  

Get stations and waveform data in directory: `/app/data/20210605_Calipatria_data/  `

```
(eq_fast) root@6006660926e5:/app# cd parameters/preprocess/Calipatria/
```  

Get station data in directory: /app/data/20210605_Calipatria_data/stations/  

```
(eq_fast) root@6006660926e5:/app/parameters/preprocess/Calipatria# python get_station_list_Calipatria.py
```  

For these stations, download waveform data in directory: `/app/data/20210605_Calipatria_data/waveforms/`  

Try the mass downloader first. Then try the get_waveforms function from client directly to get any data missed from mass downloader. You may need to run waveform download scripts multiple times to get all data.  

```
(eq_fast) root@6006660926e5:/app/parameters/preprocess/Calipatria# python get_waveforms_mdl_Calipatria.py
(eq_fast) root@6006660926e5:/app/parameters/preprocess/Calipatria# python get_station_list_Calipatria.py
```  

Not all stations from the original station list will have downloadable waveform data. Clean up the station list so that only stations with downloaded waveform data are included.  

```
(eq_fast) root@6006660926e5:/app/parameters/preprocess/Calipatria# python clean_station_list_Calipatria.py
```  

Need to manually arrange downloaded MSEED data into directories, with one directory per station named as:
`/app/data/20210605_Calipatria_data/waveforms${STATION_NAME}/`  

### **Preprocess**  
apply 4-12 Hz bandpass filter to all MSEED data, decimate to 25 Hz (factor of 4 for 100-sps data; factor of 8 for 200-sps data). This script will output MSEED data named with “Deci..” to be used in FAST.  

```
(eq_fast) root@6006660926e5:/app/parameters/preprocess/Calipatria# cd ../../../utils/preprocess/
(eq_fast) root@6006660926e5:/app/utils/preprocess# ../../parameters/preprocess/Calipatria/bandpass_filter_decimate_Calipatria.sh
```  

### **Fingerprint**  

43 stations, 113 channels  

```
(eq_fast) root@6006660926e5:/app/utils/preprocess# cd ../../fingerprint/
(eq_fast) root@6006660926e5:/app/fingerprint# ../parameters/fingerprint/Calipatria/run_fp_Calipatria.sh
```  

### **Similarity Search**  
Ended up not using 6 PB stations (18 channels). Now 37 stations, 95 channels  

```
(eq_fast) root@6006660926e5:/app/fingerprint# cd ../simsearch/
(eq_fast) root@6006660926e5:/app/simsearch# ../parameters/simsearch/Calipatria/run_simsearch_calipatria.sh
```  

### **Postprocessing**  

```  
(eq_fast) root@6006660926e5:/app/simsearch# cd ../postprocessing/
(eq_fast) root@6006660926e5:/app/postprocessing# ../parameters/postprocess/Calipatria/output_calipatria_pairs.sh
(eq_fast) root@6006660926e5:/app/postprocessing# ../parameters/postprocess/Calipatria/combine_calipatria_pairs.sh
```  

### **Network detection**  
If list index out of range in partition, fails to keep running -> try 1 partition  

```
(eq_fast) root@6006660926e5:/app/postprocessing# python scr_run_network_det.py ../parameters/postprocess/Calipatria/37sta_3stathresh_network_params.json
```  

### **Postprocess: Clean Network Detection Results**

```
(eq_fast) root@6006660926e5:/app/postprocessing# cd ../utils/network/
(eq_fast) root@6006660926e5:/app/utils/network# python arrange_network_detection_results.py
```  
  
Input parameter changes made to `arrange_network_detection_results.py` (from Hector Mine -> Calipatria)  

``` py linenums="4"
det_dir = ‘../../data/20210605_Calipatria_Data/network_detection/’
network_file = ‘37sta_3stathresh_detlist_rank_by_peaksum.txt’
nsta = 37
```

```
(eq_fast) root@6006660926e5:/app/utils/network# ./remove_duplicates_after_network.sh
```  
  

Input parameter changes made to `remove_duplicates_after_network.sh` (from Hector Mine -> Calipatria)  

``` py linenums="4"
cd ../../data/20210605_Calipatria_Data/network_detection/
NETWORK_FILE=NetworkDetectionTimes_37sta_3stathresh_detlist_rank_by_peaksum.txt
```

```
(eq_fast) root@6006660926e5:/app/utils/network# python delete_overlap_network_detections.py
```  
  
Input parameter changes made to `delete_overlap_network_detections.py` (from Hector Mine -> Calipatria)  

``` py linenums="4"
input_dir = ‘../../data/20210605_Calipatria_Data/network_detection/’
allfile_name = input_dir+‘uniquestart_sorted_no_duplicates.txt’
outfile_name = input_dir+‘37sta_3stathresh_FinalUniqueNetworkDetectionTimes.txt’
n_sta = 37
```

```
(eq_fast) root@6006660926e5:/app/utils/network# ./final_network_sort_nsta_peaksum.sh
```  

  
Input parameter changes made to `final_network_sort_nsta_peaksum.sh` (from Hector Mine -> Calipatria)  

``` py linenums="4"
cd ../../data/20210605_Calipatria_Data/network_detection/
NETWORK_FILE=37sta_3stathresh_FinalUniqueNetworkDetectionTimes.txt
```

#### **Visualize the FAST output (739 events)**  

```
(eq_fast) root@6006660926e5:/app/utils/network# cat ../../data/20210605_Calipatria_Data/network_detection/sort_nsta_peaksum_37sta_3stathresh_FinalUniqueNetworkDetectionTimes.txt
```  

#### **Display FAST detection waveforms, descending order of peaksum-similarity**  

```
(eq_fast) root@6006660926e5:/app/utils/network# cd ../events/
(eq_fast) root@6006660926e5:/app/utils/events# python PARTIALplot_detected_waveforms_Calipatria.py 0 739
```  

Input parameter changes made to `PARTIALplot_detected_waveforms_Calipatria.py` (from Hector Mine -> Calipatria)  

``` py linenums="23"
times_dir = ‘../../data/20210605_Calipatria_Data/network_detection/’
```  

``` py linenums="25"
out_dir = times_dir+‘37sta_3stathresh_NetworkWaveformPlots/’
```  

``` py linenums="30"
dt_fp = 1.2
```  

``` py linenums="37"
init_time = UTCDateTime(‘2021-06-05T00:00:06.840000’)
```  

``` py linenums="47"
ts_dir = ‘../../data/20210605_Calipatria_Data/’
st = read(ts_dir+‘waveforms*/Deci*Z__20210605T000000Z__20210606T000000Z.mseed’) # Plot only vertical component
```  

#### **Set detection threshold - keep all events with at least 3 stations**  

```
(eq_fast) root@6006660926e5:/app/utils/events# cd ../../data/20210605_Calipatria_Data/network_detection/
(eq_fast) root@6006660926e5:/app/data/20210605_Calipatria_Data/network_detection# head -739 sort_nsta_peaksum_37sta_3stathresh_FinalUniqueNetworkDetectionTimes.txt > EQ_sort_nsta_peaksum_37sta_3stathresh_FinalUniqueNetworkDetectionTimes.txt
```  

#### **Output final FAST detected event list**  

```
(eq_fast) root@6006660926e5:/app/data/20210605_Calipatria_Data/network_detection# cd ../../../utils/events/
(eq_fast) root@6006660926e5:/app/utils/events# python output_final_detection_list.py
```  

Input parameter changes made to `output_final_detection_list.py` (from Hector Mine -> Calipatria)  

``` py linenums="9"
times_dir = ‘../../data/20210605_Calipatria_Data/network_detection/’
infile_name = ‘EQ_sort_nsta_peaksum_37sta_3stathresh_FinalUniqueNetworkDetectionTimes.txt’
outfile_name = times_dir+‘FINAL_Detection_List_Calipatria_37sta_3stathresh.txt’
init_time = UTCDateTime(‘2021-06-05T00:00:06.840000’) # global start time for all channels
dt_fp = 1.2
```

```
(eq_fast) root@6006660926e5:/app/utils/events# cat ../../data/20210605_Calipatria_Data/network_detection/FINAL_Detection_List_Calipatria_37sta_3stathresh.txt
```   

### **Cut event SAC files for phase picking**  

```
(eq_fast) root@6006660926e5:/app/utils/events# python cut_event_files.py
```  

Input parameter changes made to `cut_event_files.py` (from Hector Mine -> Calipatria)  

``` py linenums="20"
stations = [“USGCB”, “BC3", “BOM”, “CLI2", “COA”, “COK2", “CRR”,
    “CTC”, “CTW”, “DRE”, “ERR”, “FRK”, “IMP”, “NSS2",
    “OCP”, “RXH”, “SAL”, “SLB”, “SLV”, “SNR”, “SWP”,
    “SWS”, “THM”, “WMD”, “WWF”, “286", “5056”, “5058",
    “5062”, “5271", “5274”, “5444",
    “WLA”, “WLA01", “WLA03”, “WLA04", “WLA06”]
in_mseed_dir = ‘../../data/20210605_Calipatria_Data/’
in_FINAL_Detection_List = ‘../../data/20210605_Calipatria_Data/network_detection/FINAL_Detection_List_Calipatria_37sta_3stathresh.txt’
out_dir = ‘../../data/20210605_Calipatria_Data/event_ids’
init_time = UTCDateTime(‘2021-06-05T00:00:06.840000’, precision=2) # global start time for all channels
dt_fp = 1.2
```  

``` py linenums="80"
st = read(‘../../data/20210605_Calipatria_Data/waveforms*/[!Deci]*.mseed’)
```  

### **Pick phases with SeisBench**  

```
(eq_fast) root@6006660926e5:/app/utils/events# cd ../picking/
(eq_fast) root@6006660926e5:/app/utils/picking# python run_seisbench.py
```  

Input parameter changes made to `run_seisbench.py` (from Hector Mine -> Calipatria)  

``` py linenums="16"
base_dir = ‘../../data/20210605_Calipatria_Data/’
```  

``` py linenums="18"
stations = [‘CLI2’, ‘COK2’, ‘OCP’, ‘SAL’, ‘WWF’, ‘5062’, ‘5271’, ‘5444’]
```  

### **Earthquake location with HYPOINVERSE**  

```
(eq_fast) root@6006660926e5:/app/utils/picking# cd ../location/
(eq_fast) root@6006660926e5:/app/utils/location# python SeisBench2hypoinverse.py
```  

Input parameter changes made to `SeisBench2hypoinverse.py` (from Hector Mine -> Calipatria)  

``` py linenums="25"
base_dir = ‘../../data/20210605_Calipatria_Data/’
start_lat = 33.1
start_lon = -115.6
start_depth = 5
```

```
(eq_fast) root@6006660926e5:/app/utils/location# python output_station_file.py
```  

Input parameter changes made to `output_station_file.py` (from Hector Mine -> Calipatria)  

``` py linenums="113"
base_dir = ‘../../data/20210605_Calipatria_Data/’
```

```
(eq_fast) root@6006660926e5:/app/utils/location# cd ../../data/20210605_Calipatria_Data/location_hypoinverse/
(eq_fast) root@6006660926e5:/app/data/20210605_Calipatria_Data/location_hypoinverse/# ../../../utils/location/hyp1.40/source/hyp1.40
COMMAND? @locate_events.hyp
(eq_fast) root@6006660926e5:/app/data/20210605_Calipatria_Data/location_hypoinverse/# cd ../../../utils/location/
(eq_fast) root@6006660926e5:/app/utils/location# python output_hypoinverse_as_text.py
```  

Input parameter changes made to `output_hypoinverse_as_text.py` (from Hector Mine -> Calipatria)  

``` py linenums="12"
catalog_start_time = UTCDateTime(‘2021-06-05T00:00:06.840000’)
loc_dir = ‘../../data/20210605_Calipatria_Data/location_hypoinverse/’ 
```  

### **Mapping earthquake locations with PyGMT**  

```
(eq_fast) root@6006660926e5:/app/utils/location# cd ../mapping/
(eq_fast) root@6006660926e5:/app/utils/mapping# conda deactivate
root@6006660926e5:/app/utils/mapping# conda activate pygmt
(pygmt) root@6006660926e5:/app/utils/mapping# python hypoinverse_to_pygmt_Calipatria.py
```  

![calipatria_FAST_maps](img/calipatria_FAST_maps.png)  
<figcaption>Plots of detected earthquakes from FAST output</figcaption>  