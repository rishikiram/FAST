import obspy

# single_channel = obspy.core.read("/Users/rishi/envitrace repos/SeisDetection/data/timeseries_2024-04-2_am.mseed")
# single_channel.plot()
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,2,2,30),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,2,3,0))
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,2,6,22),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,2,6,25))

# single_channel = obspy.core.read("/Users/rishi/envitrace repos/SeisDetection/data/timeseries_2024-04-4_am.mseed")
# single_channel.plot()
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,4,2,30),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,4,3,0))
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,4,6,22),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,4,6,25))

# single_channel = obspy.core.read("/Users/rishi/envitrace repos/SeisDetection/data/timeseries_2024-04-7_am.mseed")
# single_channel.plot()
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,7,2,30),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,7,3,0))
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,7,7,20),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,7,7,30))

# single_channel = obspy.core.read("/Users/rishi/envitrace repos/SeisDetection/data/timeseries_2024-04-15_am.mseed")
# single_channel.plot()
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,15,1,30),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,15,2,0))
# single_channel.plot(starttime = obspy.core.utcdatetime.UTCDateTime(2024,4,15,9,20),endtime = obspy.core.utcdatetime.UTCDateTime(2024,4,15,9,30))

single_channel = obspy.core.read("/Users/rishi/envitrace repos/SeisDetection/data/timeseries_2024-04-18_pm.mseed")
single_channel.plot()
single_channel.detrend(type='demean')
single_channel.plot()
single_channel.detrend(type='linear')
single_channel.plot()