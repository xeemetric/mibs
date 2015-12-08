#
# PySNMP MIB module CISCO-RTTMON-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///opt/xee/dev/mibs/asn1/cisco/CISCO-RTTMON-TC-MIB
# Produced by pysmi-0.0.6 at Mon Dec  7 15:51:48 2015
# On host ubuntu platform Linux version 3.19.0-31-generic by user dkor
# Using Python version 2.7.9 (default, Apr  2 2015, 15:33:21) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRttMonTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 485)).setRevisions(("2012-05-25 00:00", "2011-09-15 00:00", "2010-04-26 00:00", "2006-08-11 00:00", "2006-07-17 00:00", "2006-03-02 00:00", "2005-08-09 00:00",))
class RttReset(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("ready", 1), ("reset", 2),)

class RttMonOperation(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("notApplicable", 0), ("httpGet", 1), ("httpRaw", 2), ("ftpGet", 3), ("ftpPassive", 4), ("ftpActive", 5), ("voipDTAlertRinging", 6), ("voipDTConnectOK", 7),)

class RttResponseSense(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,)
    namedValues = NamedValues(("other", 0), ("ok", 1), ("disconnected", 2), ("overThreshold", 3), ("timeout", 4), ("busy", 5), ("notConnected", 6), ("dropped", 7), ("sequenceError", 8), ("verifyError", 9), ("applicationSpecific", 10), ("dnsServerTimeout", 11), ("tcpConnectTimeout", 12), ("httpTransactionTimeout", 13), ("dnsQueryError", 14), ("httpError", 15), ("error", 16), ("mplsLspEchoTxError", 17), ("mplsLspUnreachable", 18), ("mplsLspMalformedReq", 19), ("mplsLspReachButNotFEC", 20), ("enableOk", 21), ("enableNoConnect", 22), ("enableVersionFail", 23), ("enableInternalError", 24), ("enableAbort", 25), ("enableFail", 26), ("enableAuthFail", 27), ("enableFormatError", 28), ("enablePortInUse", 29), ("statsRetrieveOk", 30), ("statsRetrieveNoConnect", 31), ("statsRetrieveVersionFail", 32), ("statsRetrieveInternalError", 33), ("statsRetrieveAbort", 34), ("statsRetrieveFail", 35), ("statsRetrieveAuthFail", 36), ("statsRetrieveFormatError", 37), ("statsRetrievePortInUse", 38),)

class RttMonRttType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,)
    namedValues = NamedValues(("echo", 1), ("pathEcho", 2), ("fileIO", 3), ("script", 4), ("udpEcho", 5), ("tcpConnect", 6), ("http", 7), ("dns", 8), ("jitter", 9), ("dlsw", 10), ("dhcp", 11), ("ftp", 12), ("voip", 13), ("rtp", 14), ("lspGroup", 15), ("icmpjitter", 16), ("lspPing", 17), ("lspTrace", 18), ("ethernetPing", 19), ("ethernetJitter", 20), ("lspPingPseudowire", 21), ("video", 22), ("y1731Delay", 23), ("y1731Loss", 24), ("mcastJitter", 25),)

class RttMplsVpnMonRttType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("jitter", 1), ("echo", 2), ("pathEcho", 3),)

class RttMplsVpnMonLpdFailureSense(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("unknown", 1), ("noPath", 2), ("allPathsBroken", 3), ("allPathsUnexplorable", 4), ("allPathsBrokenOrUnexplorable", 5), ("timeout", 6), ("error", 7),)

class RttMplsVpnMonLpdGrpStatus(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("unknown", 1), ("up", 2), ("partial", 3), ("down", 4),)

class RttMonProtocol(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,)
    namedValues = NamedValues(("notApplicable", 1), ("ipIcmpEcho", 2), ("ipUdpEchoAppl", 3), ("snaRUEcho", 4), ("snaLU0EchoAppl", 5), ("snaLU2EchoAppl", 6), ("snaLU62Echo", 7), ("snaLU62EchoAppl", 8), ("appleTalkEcho", 9), ("appleTalkEchoAppl", 10), ("decNetEcho", 11), ("decNetEchoAppl", 12), ("ipxEcho", 13), ("ipxEchoAppl", 14), ("isoClnsEcho", 15), ("isoClnsEchoAppl", 16), ("vinesEcho", 17), ("vinesEchoAppl", 18), ("xnsEcho", 19), ("xnsEchoAppl", 20), ("apolloEcho", 21), ("apolloEchoAppl", 22), ("netbiosEchoAppl", 23), ("ipTcpConn", 24), ("httpAppl", 25), ("dnsAppl", 26), ("jitterAppl", 27), ("dlswAppl", 28), ("dhcpAppl", 29), ("ftpAppl", 30), ("mplsLspPingAppl", 31), ("voipAppl", 32), ("rtpAppl", 33), ("icmpJitterAppl", 34), ("ethernetPingAppl", 35), ("ethernetJitterAppl", 36), ("videoAppl", 37), ("y1731dmm", 38), ("y17311dm", 39), ("y1731lmm", 40), ("mcastJitterAppl", 41), ("y1731slm", 42),)

class RttMonCodecType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3,)
    namedValues = NamedValues(("notApplicable", 0), ("g711ulaw", 1), ("g711alaw", 2), ("g729a", 3),)

class RttMonLSPPingReplyMode(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("replyIpv4Udp", 1), ("replyIpv4UdpRA", 2),)

class RttMonTargetAddress(OctetString, TextualConvention):
    pass

class RttMonReactVar(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,)
    namedValues = NamedValues(("rtt", 1), ("jitterSDAvg", 2), ("jitterDSAvg", 3), ("packetLossSD", 4), ("packetLossDS", 5), ("mos", 6), ("timeout", 7), ("connectionLoss", 8), ("verifyError", 9), ("jitterAvg", 10), ("icpif", 11), ("packetMIA", 12), ("packetLateArrival", 13), ("packetOutOfSequence", 14), ("maxOfPositiveSD", 15), ("maxOfNegativeSD", 16), ("maxOfPositiveDS", 17), ("maxOfNegativeDS", 18), ("iaJitterDS", 19), ("frameLossDS", 20), ("mosLQDS", 21), ("mosCQDS", 22), ("rFactorDS", 23), ("successivePacketLoss", 24), ("maxOfLatencyDS", 25), ("maxOfLatencySD", 26), ("latencyDSAvg", 27), ("latencySDAvg", 28), ("packetLoss", 29), ("iaJitterSD", 30), ("mosCQSD", 31), ("rFactorSD", 32),)

class RttMonIdLst(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class RttMonCtrlIndex(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,2147483647)

mibBuilder.exportSymbols("CISCO-RTTMON-TC-MIB", RttMonLSPPingReplyMode=RttMonLSPPingReplyMode, RttMonRttType=RttMonRttType, ciscoRttMonTCMIB=ciscoRttMonTCMIB, RttMonProtocol=RttMonProtocol, RttMonCodecType=RttMonCodecType, RttMplsVpnMonLpdGrpStatus=RttMplsVpnMonLpdGrpStatus, RttMonReactVar=RttMonReactVar, RttMplsVpnMonLpdFailureSense=RttMplsVpnMonLpdFailureSense, RttReset=RttReset, RttMonIdLst=RttMonIdLst, RttMonOperation=RttMonOperation, RttMonCtrlIndex=RttMonCtrlIndex, PYSNMP_MODULE_ID=ciscoRttMonTCMIB, RttMplsVpnMonRttType=RttMplsVpnMonRttType, RttMonTargetAddress=RttMonTargetAddress, RttResponseSense=RttResponseSense)
