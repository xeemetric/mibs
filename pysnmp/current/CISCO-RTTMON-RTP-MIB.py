# PySNMP SMI module. Autogenerated from smidump -f python CISCO-RTTMON-RTP-MIB
# by libsmi2pysnmp-0.1.3 at Fri Aug 16 06:26:23 2013,
# Python version (2, 6, 6, 'final', 0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( rttMonCtrlAdminIndex, rttMonLatestOper, rttMonStats, ) = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex", "rttMonLatestOper", "rttMonStats")
( RttResponseSense, ) = mibBuilder.importSymbols("CISCO-RTTMON-TC-MIB", "RttResponseSense")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp")

# Objects

rttMonRtpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6))
if mibBuilder.loadTexts: rttMonRtpStatsTable.setDescription("The table is for RTP operation statistics. It contains \nsummarized information of the results for one RTP operation. \nA rolling accumulated history of this information \nis maintained in a series of hourly 'group(s)'. The operation \nof this table is same as that of rttMonStatsCaptureTable, \nexcept that this table will store 2 hours of data.\n\nIt is a rollover table.  When rttMonRtpStatsStartTimeIndex\ngroups exceeds the rttMonStatisticsAdminNumHourGroups value, the\noldest corresponding hourly group will be deleted and will be\nreplaced with the new rttMonRtpStatsStartTimeIndex hourly\ngroup.")
rttMonRtpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1)).setIndexNames((0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"), (0, "CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsStartTimeIndex"))
if mibBuilder.loadTexts: rttMonRtpStatsEntry.setDescription("A list of objects which accumulate the results of a\nseries of RTP operations over a 60 minute time period\nor a time period stored in rttMonScheduleAdminRttLife,\nwhichever is smaller.\n\nThis entry is created only if the rttMonCtrlAdminRttType\nis 'rtp'.")
rttMonRtpStatsStartTimeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 1), TimeStamp()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: rttMonRtpStatsStartTimeIndex.setDescription("The time when this row was created.")
rttMonRtpStatsRTTAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRTTAvg.setDescription("Average Round trip time.")
rttMonRtpStatsRTTMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRTTMin.setDescription("Minimum Round trip time.")
rttMonRtpStatsRTTMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRTTMax.setDescription("Maximum Round trip time.")
rttMonRtpStatsIAJitterDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterDSAvg.setDescription("Average of inter-arrival jitter at source.")
rttMonRtpStatsIAJitterDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterDSMin.setDescription("Minimum of inter-arrival jitter at source.")
rttMonRtpStatsIAJitterDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterDSMax.setDescription("Maximum of inter-arrival jitter at source.")
rttMonRtpStatsPacketLossDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossDSAvg.setDescription("Average number of packets lost from destination to source.")
rttMonRtpStatsPacketLossDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossDSMin.setDescription("Minimum number of packets lost from destination to source.")
rttMonRtpStatsPacketLossDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossDSMax.setDescription("Maximum number of packets lost from destination to source.")
rttMonRtpStatsPacketLateDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLateDSAvg.setDescription("Average number of late packets at source.")
rttMonRtpStatsPacketEarlyDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketEarlyDSAvg.setDescription("Average number of early packets at source.")
rttMonRtpStatsPacketOOSDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketOOSDSAvg.setDescription("Average number of out of sequence packets at source.")
rttMonRtpStatsFrameLossDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsFrameLossDSAvg.setDescription("Average Number of Codec Frame loss events at Source.")
rttMonRtpStatsFrameLossDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsFrameLossDSMin.setDescription("Minimum Number of Codec Frame loss events at Source.")
rttMonRtpStatsFrameLossDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsFrameLossDSMax.setDescription("Maximum number of Codec Frame loss events at Source.")
rttMonRtpStatsRFactorDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorDSAvg.setDescription("Average Computed value of R factor at Source.")
rttMonRtpStatsRFactorDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorDSMin.setDescription("Minimum Computed value of R factor at Source.")
rttMonRtpStatsRFactorDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorDSMax.setDescription("Maximum Computed value of R factor at Source.")
rttMonRtpStatsMOSCQDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQDSAvg.setDescription("Average Estimated Mean Opinion Score for conversational\nquality at Source.")
rttMonRtpStatsMOSCQDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQDSMin.setDescription("Minimum Estimated Mean Opinion Score for conversational\nquality at Source.")
rttMonRtpStatsMOSCQDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 22), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQDSMax.setDescription("Maximum Estimated Mean Opinion Score for conversational\nquality at Source.")
rttMonRtpStatsMOSLQDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSLQDSAvg.setDescription("Average Estimated Mean Opinion Score for listening\nquality at Source.")
rttMonRtpStatsMOSLQDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSLQDSMin.setDescription("Minimum Estimated Mean Opinion Score for listening\nquality at Source.")
rttMonRtpStatsMOSLQDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSLQDSMax.setDescription("Maximum Estimated Mean Opinion Score for listening\nquality at Source.")
rttMonRtpStatsIAJitterSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 26), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterSDAvg.setDescription("Average of inter-arrival jitter at destination.")
rttMonRtpStatsIAJitterSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 27), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterSDMin.setDescription("Minimum of inter-arrival jitter at destination.")
rttMonRtpStatsIAJitterSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 28), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsIAJitterSDMax.setDescription("Maximum of inter-arrival jitter at destination.")
rttMonRtpStatsPacketLossSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 29), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossSDAvg.setDescription("Average number of packets lost from source to destination.")
rttMonRtpStatsPacketLossSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 30), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossSDMin.setDescription("Minimum number of packets lost from source to destination.")
rttMonRtpStatsPacketLossSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 31), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketLossSDMax.setDescription("Maximum number of packets lost from source to destination.")
rttMonRtpStatsPacketsMIAAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 32), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsPacketsMIAAvg.setDescription("Average number of lost packets whose loss direction couldn't\nbe determined.")
rttMonRtpStatsRFactorSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 33), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorSDAvg.setDescription("Average estimated value of R-factor at destination.")
rttMonRtpStatsRFactorSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 34), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorSDMin.setDescription("Minimum estimated value of R-factor at destination.")
rttMonRtpStatsRFactorSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 35), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsRFactorSDMax.setDescription("Maximum estimated value of R-factor at destination.")
rttMonRtpStatsMOSCQSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 36), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQSDAvg.setDescription("Average estimated mean opinion score for conversational\nquality at destination.")
rttMonRtpStatsMOSCQSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 37), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQSDMin.setDescription("Minimum estimated mean opinion score for conversational\nquality at destination.")
rttMonRtpStatsMOSCQSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 39), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsMOSCQSDMax.setDescription("Maximum estimated mean opinion score for conversational\nquality at destination.")
rttMonRtpStatsOperAvgOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 40), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperAvgOWSD.setDescription("Average one way latency value from source to destination")
rttMonRtpStatsOperMinOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 41), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMinOWSD.setDescription("Minimum one way latency value from source to destination")
rttMonRtpStatsOperMaxOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 42), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMaxOWSD.setDescription("Maximum one way latency value from source to destination")
rttMonRtpStatsOperAvgOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 43), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperAvgOWDS.setDescription("Average one way latency value from destination to source")
rttMonRtpStatsOperMinOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 44), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMinOWDS.setDescription("Minimum one way latency value from destination to source")
rttMonRtpStatsOperMaxOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 45), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsOperMaxOWDS.setDescription("Maximum one way latency value from destination to source")
rttMonRtpStatsTotalPacketsSDAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 46), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsSDAvg.setDescription("Average number of packets sent from source to destination")
rttMonRtpStatsTotalPacketsSDMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 47), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsSDMin.setDescription("Minimum number of packets sent from source to destination")
rttMonRtpStatsTotalPacketsSDMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 48), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsSDMax.setDescription("Maximum number of packets sent from source to destination")
rttMonRtpStatsTotalPacketsDSAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 49), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsDSAvg.setDescription("Average number of packets sent from destination to source")
rttMonRtpStatsTotalPacketsDSMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 50), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsDSMax.setDescription("Maximum number of packets sent from destination to source")
rttMonRtpStatsTotalPacketsDSMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 51), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonRtpStatsTotalPacketsDSMin.setDescription("Minimum number of packets sent from destination to source")
rttMonLatestRtpOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3))
if mibBuilder.loadTexts: rttMonLatestRtpOperTable.setDescription("A table which contains the status of latest RTP\noperation. \n\nEach conceptual row corresponds to a RTP operation\ndefined in rttMonCtrlAdminTable and has same index as\nrttMonCtrlAdminTable. \n\nAn entry in this table is created only if the \nrttMonCtrlAdminRttType is 'rtp', the rttMonEchoAdminProtocol \nis 'rtpAppl' and the rttMonEchoAdminTargetAddress is \nappropriately configured. The entry will start to collect \ndata when the rttMonCtrlAdminStatus is moved into 'active' \nstate. The entry will be removed when the corresponding \nrttMonCtrlAdminStatus is in 'destroy' state.")
rttMonLatestRtpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1)).setIndexNames((0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"))
if mibBuilder.loadTexts: rttMonLatestRtpOperEntry.setDescription("An entry in RTP operation talbe. Each entry specifies the \nresults and statistics for the latest RTP operation.")
rttMonLatestRtpOperRTT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperRTT.setDescription("Round trip time for RTP packet.")
rttMonLatestRtpOperIAJitterDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperIAJitterDS.setDescription("Inter-arrival Jitter at source for the latest operation.")
rttMonLatestRtpOperPacketLossDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketLossDS.setDescription("Number of packets lost from destination to source for the\nlatest operation.")
rttMonLatestRtpOperPacketLateDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketLateDS.setDescription("Number of late packets at source for the latest operation.")
rttMonLatestRtpOperPacketEarlyDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketEarlyDS.setDescription("Number of early packets at source for the latest operation.")
rttMonLatestRtpOperPacketOOSDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketOOSDS.setDescription("Number of out of sequence packets at source for the\nlatest operation.")
rttMonLatestRtpOperFrameLossDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperFrameLossDS.setDescription("Number of CODEC frame loss events at source for\nlatest operation.")
rttMonLatestRtpOperRFactorDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperRFactorDS.setDescription("Computed value of R factor at source for latest operation.")
rttMonLatestRtpOperMOSCQDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMOSCQDS.setDescription("Estimated Mean Opinion Score for conversational\nquality at source for latest operation.")
rttMonLatestRtpOperMOSLQDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMOSLQDS.setDescription("Estimated Mean Opinion Score for listening quality at source\nfor latest operation.")
rttMonLatestRtpOperSense = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 11), RttResponseSense()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperSense.setDescription("An application specific sense code for the completion status\nof the latest operation.")
rttMonLatestRtpErrorSenseDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpErrorSenseDescription.setDescription("An sense description for the completion status\nof the latest RTP operation. ")
rttMonLatestRtpOperIAJitterSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperIAJitterSD.setDescription("Inter-arrival jitter at destination for latest operation.")
rttMonLatestRtpOperPacketLossSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketLossSD.setDescription("Number of packets lost from source to destination for latest\noperation.")
rttMonLatestRtpOperPacketsMIA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperPacketsMIA.setDescription("Number of packets missing in action while measuring \nstatistics in source to destination direction")
rttMonLatestRtpOperRFactorSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperRFactorSD.setDescription("Estimated value of R-factor at destination for latest \noperation.")
rttMonLatestRtpOperMOSCQSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMOSCQSD.setDescription("Estimated mean opinion score for conversational quality at \ndestination for latest operation.")
rttMonLatestRtpOperMinOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMinOWSD.setDescription("Minimum one way latency value in source to destination \ndirection.")
rttMonLatestRtpOperMaxOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMaxOWSD.setDescription("Maximum one way latency value in source to destination\ndirection.")
rttMonLatestRtpOperAvgOWSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperAvgOWSD.setDescription("Average one way latency value in source to destination\ndirection.")
rttMonLatestRtpOperMinOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMinOWDS.setDescription("Minimum one way latency value in destination to source\ndirection.")
rttMonLatestRtpOperMaxOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 22), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperMaxOWDS.setDescription("Maximum one way latency value in destination to source\ndirection.")
rttMonLatestRtpOperAvgOWDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperAvgOWDS.setDescription("Average one way latency value in destination to source\ndirection")
rttMonLatestRtpOperTotalPaksSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperTotalPaksSD.setDescription("Total number of packets sent in source to destination\ndirection")
rttMonLatestRtpOperTotalPaksDS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rttMonLatestRtpOperTotalPaksDS.setDescription("Total number of packets sent in destination to source\ndirection")
ciscoRttMonRtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 487)).setRevisions(("2005-08-09 00:00",))
if mibBuilder.loadTexts: ciscoRttMonRtpMIB.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: ciscoRttMonRtpMIB.setContactInfo("Cisco Systems, Inc.\nCustomer Service \n\nPostal: 170 W Tasman Drive\nSan Jose, CA 95134\n\nTel: +1 800 553 NETS\nEmail: cs-ipsla@cisco.com")
if mibBuilder.loadTexts: ciscoRttMonRtpMIB.setDescription("An extension to the CISCO-RTTMON-MIB for Cisco IP SLA \nRTP operation, Real-Time Transport Protocol(RFC 1889). This \noperation provides capability to measure voice quality metrics \nsuch as RTT (Round Trip Time), Jitter, MOS (Mean Opinion Score) \nscores by setting up RTP stream between two routers. In voice \ncommunications, particularly Internet telephony, MOS provides \na numerical measure of the quality of human speech at the \ndestination end of the circuit.")
ciscoRttMonRtpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 0))
ciscoRttMonRtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 1))
ciscoRttMonRtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 2))
ciscoRttMonRtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 1))
ciscoRttMonRtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2))

# Augmentions

# Groups

ciscoRttMonRtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2, 1)).setObjects(*(("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketEarlyDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSLQDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperFrameLossDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLateDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketEarlyDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperSense"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLateDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRFactorDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLossDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperIAJitterDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketOOSDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSCQDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketOOSDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpErrorSenseDescription"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRTT"), ) )
if mibBuilder.loadTexts: ciscoRttMonRtpGroup.setDescription("A collection of objects related to the  \nstatistics for RTP operation.")
ciscoRttMonRtpGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2, 2)).setObjects(*(("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMaxOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperTotalPaksDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLossSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSCQSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMinOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRFactorSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketsMIA"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperAvgOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketsMIAAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperAvgOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMaxOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMinOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMaxOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperTotalPaksSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMaxOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperAvgOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperAvgOWDS"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMinOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMinOWSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDMin"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDAvg"), ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperIAJitterSD"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDMax"), ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDMin"), ) )
if mibBuilder.loadTexts: ciscoRttMonRtpGroupRev1.setDescription("A collection of objects related to the  \nSource to Destination statistics for RTP Operation.")

# Compliances

ciscoRttMonRtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 1, 1)).setObjects(*(("CISCO-RTTMON-RTP-MIB", "ciscoRttMonRtpGroup"), ("CISCO-RTTMON-RTP-MIB", "ciscoRttMonRtpGroupRev1"), ) )
if mibBuilder.loadTexts: ciscoRttMonRtpMIBCompliance.setDescription("The compliance statement for new MIB extensions for\n(1) Rtp  operation and statistics")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-RTTMON-RTP-MIB", PYSNMP_MODULE_ID=ciscoRttMonRtpMIB)

# Objects
mibBuilder.exportSymbols("CISCO-RTTMON-RTP-MIB", rttMonRtpStatsTable=rttMonRtpStatsTable, rttMonRtpStatsEntry=rttMonRtpStatsEntry, rttMonRtpStatsStartTimeIndex=rttMonRtpStatsStartTimeIndex, rttMonRtpStatsRTTAvg=rttMonRtpStatsRTTAvg, rttMonRtpStatsRTTMin=rttMonRtpStatsRTTMin, rttMonRtpStatsRTTMax=rttMonRtpStatsRTTMax, rttMonRtpStatsIAJitterDSAvg=rttMonRtpStatsIAJitterDSAvg, rttMonRtpStatsIAJitterDSMin=rttMonRtpStatsIAJitterDSMin, rttMonRtpStatsIAJitterDSMax=rttMonRtpStatsIAJitterDSMax, rttMonRtpStatsPacketLossDSAvg=rttMonRtpStatsPacketLossDSAvg, rttMonRtpStatsPacketLossDSMin=rttMonRtpStatsPacketLossDSMin, rttMonRtpStatsPacketLossDSMax=rttMonRtpStatsPacketLossDSMax, rttMonRtpStatsPacketLateDSAvg=rttMonRtpStatsPacketLateDSAvg, rttMonRtpStatsPacketEarlyDSAvg=rttMonRtpStatsPacketEarlyDSAvg, rttMonRtpStatsPacketOOSDSAvg=rttMonRtpStatsPacketOOSDSAvg, rttMonRtpStatsFrameLossDSAvg=rttMonRtpStatsFrameLossDSAvg, rttMonRtpStatsFrameLossDSMin=rttMonRtpStatsFrameLossDSMin, rttMonRtpStatsFrameLossDSMax=rttMonRtpStatsFrameLossDSMax, rttMonRtpStatsRFactorDSAvg=rttMonRtpStatsRFactorDSAvg, rttMonRtpStatsRFactorDSMin=rttMonRtpStatsRFactorDSMin, rttMonRtpStatsRFactorDSMax=rttMonRtpStatsRFactorDSMax, rttMonRtpStatsMOSCQDSAvg=rttMonRtpStatsMOSCQDSAvg, rttMonRtpStatsMOSCQDSMin=rttMonRtpStatsMOSCQDSMin, rttMonRtpStatsMOSCQDSMax=rttMonRtpStatsMOSCQDSMax, rttMonRtpStatsMOSLQDSAvg=rttMonRtpStatsMOSLQDSAvg, rttMonRtpStatsMOSLQDSMin=rttMonRtpStatsMOSLQDSMin, rttMonRtpStatsMOSLQDSMax=rttMonRtpStatsMOSLQDSMax, rttMonRtpStatsIAJitterSDAvg=rttMonRtpStatsIAJitterSDAvg, rttMonRtpStatsIAJitterSDMin=rttMonRtpStatsIAJitterSDMin, rttMonRtpStatsIAJitterSDMax=rttMonRtpStatsIAJitterSDMax, rttMonRtpStatsPacketLossSDAvg=rttMonRtpStatsPacketLossSDAvg, rttMonRtpStatsPacketLossSDMin=rttMonRtpStatsPacketLossSDMin, rttMonRtpStatsPacketLossSDMax=rttMonRtpStatsPacketLossSDMax, rttMonRtpStatsPacketsMIAAvg=rttMonRtpStatsPacketsMIAAvg, rttMonRtpStatsRFactorSDAvg=rttMonRtpStatsRFactorSDAvg, rttMonRtpStatsRFactorSDMin=rttMonRtpStatsRFactorSDMin, rttMonRtpStatsRFactorSDMax=rttMonRtpStatsRFactorSDMax, rttMonRtpStatsMOSCQSDAvg=rttMonRtpStatsMOSCQSDAvg, rttMonRtpStatsMOSCQSDMin=rttMonRtpStatsMOSCQSDMin, rttMonRtpStatsMOSCQSDMax=rttMonRtpStatsMOSCQSDMax, rttMonRtpStatsOperAvgOWSD=rttMonRtpStatsOperAvgOWSD, rttMonRtpStatsOperMinOWSD=rttMonRtpStatsOperMinOWSD, rttMonRtpStatsOperMaxOWSD=rttMonRtpStatsOperMaxOWSD, rttMonRtpStatsOperAvgOWDS=rttMonRtpStatsOperAvgOWDS, rttMonRtpStatsOperMinOWDS=rttMonRtpStatsOperMinOWDS, rttMonRtpStatsOperMaxOWDS=rttMonRtpStatsOperMaxOWDS, rttMonRtpStatsTotalPacketsSDAvg=rttMonRtpStatsTotalPacketsSDAvg, rttMonRtpStatsTotalPacketsSDMin=rttMonRtpStatsTotalPacketsSDMin, rttMonRtpStatsTotalPacketsSDMax=rttMonRtpStatsTotalPacketsSDMax, rttMonRtpStatsTotalPacketsDSAvg=rttMonRtpStatsTotalPacketsDSAvg, rttMonRtpStatsTotalPacketsDSMax=rttMonRtpStatsTotalPacketsDSMax, rttMonRtpStatsTotalPacketsDSMin=rttMonRtpStatsTotalPacketsDSMin, rttMonLatestRtpOperTable=rttMonLatestRtpOperTable, rttMonLatestRtpOperEntry=rttMonLatestRtpOperEntry, rttMonLatestRtpOperRTT=rttMonLatestRtpOperRTT, rttMonLatestRtpOperIAJitterDS=rttMonLatestRtpOperIAJitterDS, rttMonLatestRtpOperPacketLossDS=rttMonLatestRtpOperPacketLossDS, rttMonLatestRtpOperPacketLateDS=rttMonLatestRtpOperPacketLateDS, rttMonLatestRtpOperPacketEarlyDS=rttMonLatestRtpOperPacketEarlyDS, rttMonLatestRtpOperPacketOOSDS=rttMonLatestRtpOperPacketOOSDS, rttMonLatestRtpOperFrameLossDS=rttMonLatestRtpOperFrameLossDS, rttMonLatestRtpOperRFactorDS=rttMonLatestRtpOperRFactorDS, rttMonLatestRtpOperMOSCQDS=rttMonLatestRtpOperMOSCQDS, rttMonLatestRtpOperMOSLQDS=rttMonLatestRtpOperMOSLQDS, rttMonLatestRtpOperSense=rttMonLatestRtpOperSense, rttMonLatestRtpErrorSenseDescription=rttMonLatestRtpErrorSenseDescription, rttMonLatestRtpOperIAJitterSD=rttMonLatestRtpOperIAJitterSD, rttMonLatestRtpOperPacketLossSD=rttMonLatestRtpOperPacketLossSD, rttMonLatestRtpOperPacketsMIA=rttMonLatestRtpOperPacketsMIA, rttMonLatestRtpOperRFactorSD=rttMonLatestRtpOperRFactorSD, rttMonLatestRtpOperMOSCQSD=rttMonLatestRtpOperMOSCQSD, rttMonLatestRtpOperMinOWSD=rttMonLatestRtpOperMinOWSD, rttMonLatestRtpOperMaxOWSD=rttMonLatestRtpOperMaxOWSD, rttMonLatestRtpOperAvgOWSD=rttMonLatestRtpOperAvgOWSD, rttMonLatestRtpOperMinOWDS=rttMonLatestRtpOperMinOWDS, rttMonLatestRtpOperMaxOWDS=rttMonLatestRtpOperMaxOWDS, rttMonLatestRtpOperAvgOWDS=rttMonLatestRtpOperAvgOWDS, rttMonLatestRtpOperTotalPaksSD=rttMonLatestRtpOperTotalPaksSD, rttMonLatestRtpOperTotalPaksDS=rttMonLatestRtpOperTotalPaksDS, ciscoRttMonRtpMIB=ciscoRttMonRtpMIB, ciscoRttMonRtpMIBNotifs=ciscoRttMonRtpMIBNotifs, ciscoRttMonRtpMIBObjects=ciscoRttMonRtpMIBObjects, ciscoRttMonRtpMIBConformance=ciscoRttMonRtpMIBConformance, ciscoRttMonRtpMIBCompliances=ciscoRttMonRtpMIBCompliances, ciscoRttMonRtpMIBGroups=ciscoRttMonRtpMIBGroups)

# Groups
mibBuilder.exportSymbols("CISCO-RTTMON-RTP-MIB", ciscoRttMonRtpGroup=ciscoRttMonRtpGroup, ciscoRttMonRtpGroupRev1=ciscoRttMonRtpGroupRev1)

# Compliances
mibBuilder.exportSymbols("CISCO-RTTMON-RTP-MIB", ciscoRttMonRtpMIBCompliance=ciscoRttMonRtpMIBCompliance)