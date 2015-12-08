#
# PySNMP MIB module RFC1315-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///opt/xee/dev/mibs/asn1/ietf/RFC1315-MIB
# Produced by pysmi-0.0.6 at Mon Dec  7 15:53:32 2015
# On host ubuntu platform Linux version 3.19.0-31-generic by user dkor
# Using Python version 2.7.9 (default, Apr  2 2015, 15:33:21) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, transmission, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, NotificationType, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "transmission", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
frame_relay = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 32)).setLabel("frame-relay")
class Index(Integer32):
    pass

class DLCI(Integer32):
    pass

frDlcmiTable = MibTable((1, 3, 6, 1, 2, 1, 10, 32, 1), )
frDlcmiEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 32, 1, 1), ).setIndexNames((0, "RFC1315-MIB", "frDlcmiIfIndex"))
frDlcmiIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 1), Index()).setMaxAccess("readonly")
frDlcmiState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("noLmiConfigured", 1), ("lmiRev1", 2), ("ansiT1-617-D", 3), ("ansiT1-617-B", 4),))).setMaxAccess("readwrite")
frDlcmiAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("q921", 1), ("q922March90", 2), ("q922November90", 3), ("q922", 4),))).setMaxAccess("readwrite")
frDlcmiAddressLen = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(2, 3, 4,)).clone(namedValues=NamedValues(("two-octets", 2), ("three-octets", 3), ("four-octets", 4),))).setMaxAccess("readwrite")
frDlcmiPollingInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5,30)).clone(10)).setMaxAccess("readwrite")
frDlcmiFullEnquiryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,255)).clone(6)).setMaxAccess("readwrite")
frDlcmiErrorThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,10)).clone(3)).setMaxAccess("readwrite")
frDlcmiMonitoredEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,10)).clone(4)).setMaxAccess("readwrite")
frDlcmiMaxSupportedVCs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
frDlcmiMulticast = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 10), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("nonBroadcast", 1), ("broadcast", 2),))).setMaxAccess("readwrite")
frCircuitTable = MibTable((1, 3, 6, 1, 2, 1, 10, 32, 2), )
frCircuitEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 32, 2, 1), ).setIndexNames((0, "RFC1315-MIB", "frCircuitIfIndex"), (0, "RFC1315-MIB", "frCircuitDlci"))
frCircuitIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 1), Index()).setMaxAccess("readonly")
frCircuitDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 2), DLCI()).setMaxAccess("readonly")
frCircuitState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("invalid", 1), ("active", 2), ("inactive", 3),)).clone('active')).setMaxAccess("readwrite")
frCircuitReceivedFECNs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 4), Counter32()).setMaxAccess("readonly")
frCircuitReceivedBECNs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 5), Counter32()).setMaxAccess("readonly")
frCircuitSentFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 6), Counter32()).setMaxAccess("readonly")
frCircuitSentOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 7), Counter32()).setMaxAccess("readonly")
frCircuitReceivedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 8), Counter32()).setMaxAccess("readonly")
frCircuitReceivedOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 9), Counter32()).setMaxAccess("readonly")
frCircuitCreationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
frCircuitLastTimeChange = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 11), TimeTicks()).setMaxAccess("readonly")
frCircuitCommittedBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
frCircuitExcessBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
frCircuitThroughput = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 14), Integer32()).setMaxAccess("readwrite")
frErrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 32, 3), )
frErrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 32, 3, 1), ).setIndexNames((0, "RFC1315-MIB", "frErrIfIndex"))
frErrIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 1), Index()).setMaxAccess("readonly")
frErrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)).clone(namedValues=NamedValues(("unknownError", 1), ("receiveShort", 2), ("receiveLong", 3), ("illegalDLCI", 4), ("unknownDLCI", 5), ("dlcmiProtoErr", 6), ("dlcmiUnknownIE", 7), ("dlcmiSequenceErr", 8), ("dlcmiUnknownRpt", 9), ("noErrorSinceReset", 10),))).setMaxAccess("readonly")
frErrData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 3), OctetString()).setMaxAccess("readonly")
frErrTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
frame_relay_globals = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 32, 4)).setLabel("frame-relay-globals")
frTrapState = MibScalar((1, 3, 6, 1, 2, 1, 10, 32, 4, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2),)).clone('disabled')).setMaxAccess("readwrite")
frDLCIStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 10, 32) + (0,1)).setObjects(*(("RFC1315-MIB", "frCircuitIfIndex"), ("RFC1315-MIB", "frCircuitDlci"), ("RFC1315-MIB", "frCircuitState"),))
mibBuilder.exportSymbols("RFC1315-MIB", frDlcmiFullEnquiryInterval=frDlcmiFullEnquiryInterval, frDlcmiAddress=frDlcmiAddress, frCircuitIfIndex=frCircuitIfIndex, Index=Index, frDlcmiMonitoredEvents=frDlcmiMonitoredEvents, frDLCIStatusChange=frDLCIStatusChange, frCircuitReceivedBECNs=frCircuitReceivedBECNs, frErrTime=frErrTime, frDlcmiTable=frDlcmiTable, frErrIfIndex=frErrIfIndex, frDlcmiState=frDlcmiState, frDlcmiEntry=frDlcmiEntry, frCircuitLastTimeChange=frCircuitLastTimeChange, frErrType=frErrType, frDlcmiMulticast=frDlcmiMulticast, DLCI=DLCI, frCircuitSentFrames=frCircuitSentFrames, frCircuitState=frCircuitState, frDlcmiMaxSupportedVCs=frDlcmiMaxSupportedVCs, frTrapState=frTrapState, frCircuitExcessBurst=frCircuitExcessBurst, frame_relay=frame_relay, frCircuitEntry=frCircuitEntry, frCircuitCommittedBurst=frCircuitCommittedBurst, frCircuitDlci=frCircuitDlci, frCircuitReceivedOctets=frCircuitReceivedOctets, frame_relay_globals=frame_relay_globals, frCircuitCreationTime=frCircuitCreationTime, frDlcmiErrorThreshold=frDlcmiErrorThreshold, frCircuitTable=frCircuitTable, frCircuitReceivedFECNs=frCircuitReceivedFECNs, frCircuitSentOctets=frCircuitSentOctets, frDlcmiAddressLen=frDlcmiAddressLen, frErrTable=frErrTable, frDlcmiIfIndex=frDlcmiIfIndex, frCircuitThroughput=frCircuitThroughput, frErrData=frErrData, frCircuitReceivedFrames=frCircuitReceivedFrames, frErrEntry=frErrEntry, frDlcmiPollingInterval=frDlcmiPollingInterval)
