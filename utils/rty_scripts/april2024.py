import obspy
import obspy.clients.iris
import tqdm
import os.path
DATA_DIR = "/home/rootrish/FORK"


client = obspy.clients.iris.Client()
# Testing
# dt_start = obspy.UTCDateTime("2024-05-04T00:00:00")
# dt_end = dt_start + 100
# st1 = client.timeseries("UU", "FORK", "01", "GHZ", dt_start, dt_end,
#     filter=["decimate=500.0","bp=15,60"])
# st2 = client.timeseries("UU", "FORK", "01", "GHZ", dt_end, dt_end + 100,
#     filter=["decimate=500.0","bp=15,60"])
# print(len(st1[0].data), len(st2[0].data))  

#start of first stimulation: 2024-04-03 04:09:14-06
#end of last stimulation: 2024-04-17 07:29:04-06

# TODO if you pull data again, you should add demean and detrend("linear")
for d in tqdm.tqdm(range(2,19)):
    this_filename = os.path.join(DATA_DIR, "Deci100.2024.0."+f"{d:02}")
    
    dt_start = obspy.UTCDateTime(2024,4,d,0,0,0)
    dt_mid = dt_start + 3600*12
    dt_end = dt_start + 3600*24

    my_filters = ["decimate=100.0","bp=15,60", "demean"]
    
    if os.path.isfile(this_filename+"_00-00-00.UU.FORK.01.GHZ.mseed"):
        print("skipping "+this_filename+"_00-00-00.UU.FORK.01.GHZ.mseed")
    else:
        st = client.timeseries("UU", "FORK", "01", "GHZ", dt_start, dt_mid, filter=my_filters, filename= this_filename+"_00-00-00.UU.FORK.01.GHZ.mseed", output = "miniseed")
    
    if os.path.isfile(this_filename+"_12-00-00.UU.FORK.01.GHZ.mseed"):
        print("skipping "+this_filename+"_12-00-00.UU.FORK.01.GHZ.mseed")
    else:
        st = client.timeseries("UU", "FORK", "01", "GHZ", dt_mid, dt_end, filter=my_filters, filename= this_filename+"_12-00-00.UU.FORK.01.GHZ.mseed", output = "miniseed")
    