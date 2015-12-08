#
# PySNMP MIB module CISCO-TC (http://pysnmp.sf.net)
# ASN.1 source file:///opt/xee/dev/mibs/asn1/cisco/CISCO-TC
# Produced by pysmi-0.0.6 at Mon Dec  7 15:53:32 2015
# On host ubuntu platform Linux version 3.19.0-31-generic by user dkor
# Using Python version 2.7.9 (default, Apr  2 2015, 15:33:21) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ciscoModules, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 1)).setRevisions(("2011-11-11 00:00", "2011-06-17 00:00", "2010-02-24 00:00", "2009-06-18 00:00", "2009-03-10 00:00", "2009-02-26 00:00", "2008-04-02 00:00", "2007-02-15 00:00", "2006-07-06 00:00", "2006-04-13 00:00", "2005-06-24 00:00", "2005-06-16 00:00", "2004-10-11 00:00", "2004-06-08 00:00", "2004-04-14 00:00", "2002-12-18 00:00", "2002-12-12 16:00", "2002-12-02 00:00", "2002-09-22 00:00", "2002-09-17 00:00", "2002-04-16 00:00", "2001-07-07 00:00", "2001-01-18 00:00", "2000-11-21 00:00", "1998-10-28 00:00", "1997-03-13 00:00", "1996-08-14 00:00", "1996-07-08 00:00", "1996-02-22 00:00", "1995-06-07 00:00",))
class Layer2Cos(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,7)

class CiscoNetworkProtocol(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65535,)
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("ipv6", 20), ("cdm", 21), ("nbf", 22), ("bpxIgx", 23), ("clnsPfx", 24), ("http", 25), ("unknown", 65535),)

class CiscoNetworkAddress(OctetString, TextualConvention):
    pass

class Unsigned64(Counter64, TextualConvention):
    pass

class InterfaceIndexOrZero(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

class SAPType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,254)

class CountryCode(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,2),)
class CountryCodeITU(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,255)

class EntPhysicalIndexOrZero(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

class CiscoRowOperStatus(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4),)

class CiscoPort(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,65535)

class CiscoIpProtocol(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,255)

class CiscoLocationClass(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8,)
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8),)

class CiscoLocationSpecifier(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class CiscoInetAddressMask(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,128)

class CiscoAbsZeroBasedCounter32(Gauge32, TextualConvention):
    pass

class CiscoSnapShotAbsCounter32(Unsigned32, TextualConvention):
    pass

class CiscoAlarmSeverity(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7),)

class PerfHighIntervalCount(Counter64, TextualConvention):
    pass

class ConfigIterator(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

class BulkConfigResult(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class ListIndex(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,2147483647)

class ListIndexOrZero(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

class TimeIntervalSec(Unsigned32, TextualConvention):
    pass

class TimeIntervalMin(Unsigned32, TextualConvention):
    pass

class CiscoMilliSeconds(Unsigned32, TextualConvention):
    pass

class MicroSeconds(Unsigned32, TextualConvention):
    pass

class CiscoPortList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)

class CiscoPortListRange(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8,)
    namedValues = NamedValues(("oneto2k", 1), ("twoKto4K", 2), ("fourKto6K", 3), ("sixKto8K", 4), ("eightKto10K", 5), ("tenKto12K", 6), ("twelveKto14K", 7), ("fourteenKto16K", 8),)

class IfOperStatusReason(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255,), SingleValueConstraint(256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268,))
    namedValues = NamedValues(("other", 1), ("none", 2), ("hwFailure", 3), ("loopbackDiagFailure", 4), ("errorDisabled", 5), ("swFailure", 6), ("linkFailure", 7), ("offline", 8), ("nonParticipating", 9), ("initializing", 10), ("vsanInactive", 11), ("adminDown", 12), ("channelAdminDown", 13), ("channelOperSuspended", 14), ("channelConfigurationInProgress", 15), ("rcfInProgress", 16), ("elpFailureIsolation", 17), ("escFailureIsolation", 18), ("domainOverlapIsolation", 19), ("domainAddrAssignFailureIsolation", 20), ("domainOtherSideEportIsolation", 21), ("domainInvalidRcfReceived", 22), ("domainManagerDisabled", 23), ("zoneMergeFailureIsolation", 24), ("vsanMismatchIsolation", 25), ("parentDown", 26), ("srcPortNotBound", 27), ("interfaceRemoved", 28), ("fcotNotPresent", 29), ("fcotVendorNotSupported", 30), ("incompatibleAdminMode", 31), ("incompatibleAdminSpeed", 32), ("suspendedByMode", 33), ("suspendedBySpeed", 34), ("suspendedByWWN", 35), ("domainMaxReTxFailure", 36), ("eppFailure", 37), ("portVsanMismatchIsolation", 38), ("loopbackIsolation", 39), ("upgradeInProgress", 40), ("incompatibleAdminRxBbCredit", 41), ("incompatibleAdminRxBufferSize", 42), ("portChannelMembersDown", 43), ("zoneRemoteNoRespIsolation", 44), ("firstPortUpAsEport", 45), ("firstPortNotUp", 46), ("peerFCIPPortClosedConnection", 47), ("peerFCIPPortResetConnection", 48), ("fcipPortMaxReTx", 49), ("fcipPortKeepAliveTimerExpire", 50), ("fcipPortPersistTimerExpire", 51), ("fcipPortSrcLinkDown", 52), ("fcipPortSrcAdminDown", 53), ("fcipPortAdminCfgChange", 54), ("fcipSrcPortRemoved", 55), ("fcipSrcModuleNotOnline", 56), ("invalidConfig", 57), ("portBindFailure", 58), ("portFabricBindFailure", 59), ("noCommonVsanIsolation", 60), ("ficonVsanDown", 61), ("invalidAttachment", 62), ("portBlocked", 63), ("incomAdminRxBbCreditPerBuf", 64), ("tooManyInvalidFlogis", 65), ("deniedDueToPortBinding", 66), ("elpFailureRevMismatch", 67), ("elpFailureClassFParamErr", 68), ("elpFailureClassNParamErr", 69), ("elpFailureUnknownFlowCtlCode", 70), ("elpFailureInvalidFlowCtlParam", 71), ("elpFailureInvalidPortName", 72), ("elpFailureInvalidSwitchName", 73), ("elpFailureRatovEdtovMismatch", 74), ("elpFailureLoopbackDetected", 75), ("elpFailureInvalidTxBbCredit", 76), ("elpFailureInvalidPayloadSize", 77), ("bundleMisCfg", 78), ("bitErrRuntimeThreshExceeded", 79), ("linkFailLinkReset", 80), ("linkFailPortInitFail", 81), ("linkFailPortUnusable", 82), ("linkFailLossOfSignal", 83), ("linkFailLossOfSync", 84), ("linkFailNosRcvd", 85), ("linkFailOLSRcvd", 86), ("linkFailDebounceTimeout", 87), ("linkFailLrRcvd", 88), ("linkFailCreditLoss", 89), ("linkFailRxQOverflow", 90), ("linkFailTooManyInterrupts", 91), ("linkFailLipRcvdBb", 92), ("linkFailBbCreditLoss", 93), ("linkFailOpenPrimSignalTimeout", 94), ("linkFailOpenPrimSignalReturned", 95), ("linkFailLipF8Rcvd", 96), ("linkFailLineCardPortShutdown", 97), ("fcspAuthenfailure", 98), ("fcotChecksumError", 99), ("ohmsExtLoopbackTest", 100), ("invalidFabricBindExchange", 101), ("tovMismatch", 102), ("ficonNotEnabled", 103), ("ficonNoPortNumber", 104), ("ficonBeingEnabled", 105), ("ePortProhibited", 106), ("portGracefulShutdown", 107), ("trunkNotFullyActive", 108), ("fabricBindingSwitchWwnNotFound", 109), ("fabricBindingDomainInvalid", 110), ("fabricBindingDbMismatch", 111), ("fabricBindingNoRspFromPeer", 112), ("dpvmVsanSuspended", 113), ("dpvmVsanNotFound", 114), ("trackedPortDown", 115), ("ecSuspendedOnLoop", 116), ("isolateBundleMisCfg", 117), ("noPeerBundleSupport", 118), ("portBringupIsolation", 119), ("domainNotAllowedIsolated", 120), ("virtualIvrDomainOverlapIsolation", 121), ("outOfService", 122), ("portAuthFailed", 123), ("bundleStandby", 124), ("portConnectorTypeErr", 125), ("errorDisabledReInitLmtReached", 126), ("ficonDupPortNum", 127), ("localRcf", 128), ("twoSwitchesWithSameWWN", 129), ("invalidOtherSidePrincEFPReqRecd", 130), ("domainOther", 131), ("elpFailureAllZeroPeerWWNRcvd", 132), ("preferredPathIsolation", 133), ("fcRedirectIsolation", 134), ("portActLicenseNotAvailable", 135), ("sdmIsolation", 136), ("fcidAllocationFailed", 137), ("externallyDisabled", 138), ("unavailableNPVUpstreamPort", 139), ("unavailableNPVPrefUpstreamPort", 140), ("sfpReadError", 141), ("stickyDownOnLinkFailure", 142), ("tooManyLinkFlapsErr", 143), ("unidirectionalUDLD", 144), ("txRxLoopUDLD", 145), ("neighborMismatchUDLD", 146), ("authzPending", 147), ("hotStdbyInBundle", 148), ("incompleteConfig", 149), ("incompleteTunnelCfg", 150), ("hwProgrammingFailed", 151), ("tunnelDstUnreachable", 152), ("suspendByMtu", 153), ("sfpInvalid", 154), ("sfpAbsent", 155), ("portCapabilitiesUnknown", 156), ("channelErrDisabled", 157), ("vrfMismatch", 158), ("vrfForwardReferencing", 159), ("dupTunnelConfigDetected", 160), ("primaryVLANDown", 161), ("vrfUnusable", 162), ("errDisableHandShkFailure", 163), ("errDisabledBPDUGuard", 164), ("dot1xSecViolationErrDisabled", 165), ("emptyEchoUDLD", 166), ("vfTaggingCapErr", 167), ("portDisabled", 168), ("tunnelModeNotConfigured", 169), ("tunnelSrcNotConfigured", 170), ("tunnelDstNotConfigured", 171), ("tunnelUnableToResolveSrcIP", 172), ("tunnelUnableToResolveDstIP", 173), ("tunnelVrfDown", 174), ("sifAdminDown", 175), ("phyIntfDown", 176), ("ifSifLimitExceeded", 177), ("sifHoldDown", 178), ("noFcoe", 179), ("dcxCompatMismatch", 180), ("isolateBundleLimitExceeded", 181), ("sifNotBound", 182), ("errDisabledLacpMiscfg", 183), ("satFabricIfDown", 184), ("invalidSatFabricIf", 185), ("noRemoteChassis", 186), ("vicEnableNotReceived", 187), ("vicDisableReceived", 188), ("vlanVsanMappingNotEnabled", 189), ("stpNotFwdingInFcoeMappedVlan", 190), ("moduleOffline", 191), ("udldAggModeLinkFailure", 192), ("stpInconsVpcPeerDisabled", 193), ("setPortStateFailed", 194), ("suspendedByVpc", 195), ("vpcCfgInProgress", 196), ("vpcPeerLinkDown", 197), ("vpcNoRspFromPeer", 198), ("protoPortSuspend", 199), ("tunnelSrcDown", 200), ("cdpInfoUnavailable", 201), ("fexSfpInvalid", 202), ("errDisabledIpConflict", 203), ("fcotClkRateMismatch", 204), ("portGuardTrustSecViolation", 205), ("sdpTimeout", 206), ("satIncompatTopo", 207), ("waitForFlogi", 208), ("satNotConfigured", 209), ("npivNotEnabledInUpstream", 210), ("vsanMismatchWithUpstreamSwPort", 211), ("portGuardBitErrRate", 212), ("portGuardSigLoss", 213), ("portGuardSyncLoss", 214), ("portGuardLinkReset", 215), ("portGuardCreditLoss", 216), ("ipQosMgrPolicyAppFailure", 217), ("pauseRateLimitErrDisabled", 218), ("lstGrpUplinkDown", 219), ("stickyDnLinkFailure", 220), ("routerMacFailure", 221), ("dcxMultipleMsapIds", 222), ("dcxHundredPdusRcvdNoAck", 223), ("enmSatIncompatibleUplink", 224), ("enmLoopDetected", 225), ("nonStickyExternallyDisabled", 226), ("subGroupIdNotAssigned", 227), ("vemUnlicensed", 228), ("profileNotFound", 229), ("nonExistentVlan", 230), ("vlanInvalidType", 231), ("vlanDown", 232), ("vpcPeerUpgrade", 233), ("ipQosDcbxpCompatFailure", 234), ("nonCiscoHbaVfTag", 235), ("domainIdConfigMismatch", 236), ("sfpSpeedMismatch", 237), ("xcvrInitializing", 238), ("xcvrAbsent", 239), ("xcvrInvalid", 240), ("vfcBindingInvalid", 241), ("vlanNotFcoeEnabled", 242), ("pvlanNativeVlanErr", 243), ("ethL2VlanDown", 244), ("ethIntfInvalidBinding", 245), ("pmonFailure", 246), ("l3NotReady", 247), ("speedMismatch", 248), ("flowControlMismatch", 249), ("vdcMode", 250), ("suspendedDueToMinLinks", 251), ("enmPinFailLinkDown", 252), ("inactiveM1PortFpathActiveVlan", 253), ("parentPortDown", 254), ("moduleRemoved", 255),) + NamedValues(("corePortMct", 256), ("nonCorePortMct", 257), ("ficonInorderNotActive", 258), ("invalidEncapsulation", 259), ("modemLineDeasserted", 260), ("ipSecHndshkInProgress", 261), ("sfpEthCompliantErr", 262), ("cellularModemUnattached", 263), ("outOfGlblRxBuffers", 264), ("sfpFcCompliantErr", 265), ("ethIntfNotLicensed", 266), ("domainIdsInvalid", 267), ("fabricNameInvalid", 268),)

class EntLogicalIndexOrZero(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)

class CiscoURLString(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)

class CiscoURLStringOrEmpty(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class CiscoHTTPResponseStatusCode(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(100,599)

class CvE164Address(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,128)

class CiscoVlanList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,128)

class CiscoCosList(Bits, TextualConvention):
    namedValues = NamedValues(("cos0", 0), ("cos1", 1), ("cos2", 2), ("cos3", 3), ("cos4", 4), ("cos5", 5), ("cos6", 6), ("cos7", 7),)

class CiscoPbbServiceIdentifier(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,16777216)

class CiscoBridgeDomain(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,65535)

class Cisco2KVlanList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)

class CiscoInterfaceIndexList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)

class CiscoVrfName(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,32)

class CiscoEntityIndexList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)

mibBuilder.exportSymbols("CISCO-TC", CiscoNetworkAddress=CiscoNetworkAddress, CiscoInterfaceIndexList=CiscoInterfaceIndexList, CountryCodeITU=CountryCodeITU, CiscoLocationSpecifier=CiscoLocationSpecifier, CiscoNetworkProtocol=CiscoNetworkProtocol, ciscoTextualConventions=ciscoTextualConventions, ConfigIterator=ConfigIterator, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, EntLogicalIndexOrZero=EntLogicalIndexOrZero, CountryCode=CountryCode, CiscoRowOperStatus=CiscoRowOperStatus, CiscoLocationClass=CiscoLocationClass, CiscoIpProtocol=CiscoIpProtocol, ListIndex=ListIndex, CiscoEntityIndexList=CiscoEntityIndexList, CiscoURLString=CiscoURLString, InterfaceIndexOrZero=InterfaceIndexOrZero, CvE164Address=CvE164Address, CiscoVrfName=CiscoVrfName, IfOperStatusReason=IfOperStatusReason, Layer2Cos=Layer2Cos, CiscoInetAddressMask=CiscoInetAddressMask, PerfHighIntervalCount=PerfHighIntervalCount, CiscoURLStringOrEmpty=CiscoURLStringOrEmpty, CiscoMilliSeconds=CiscoMilliSeconds, CiscoAbsZeroBasedCounter32=CiscoAbsZeroBasedCounter32, SAPType=SAPType, CiscoPortListRange=CiscoPortListRange, CiscoPortList=CiscoPortList, CiscoVlanList=CiscoVlanList, CiscoHTTPResponseStatusCode=CiscoHTTPResponseStatusCode, CiscoCosList=CiscoCosList, BulkConfigResult=BulkConfigResult, CiscoPbbServiceIdentifier=CiscoPbbServiceIdentifier, MicroSeconds=MicroSeconds, Cisco2KVlanList=Cisco2KVlanList, CiscoSnapShotAbsCounter32=CiscoSnapShotAbsCounter32, CiscoBridgeDomain=CiscoBridgeDomain, ListIndexOrZero=ListIndexOrZero, Unsigned64=Unsigned64, TimeIntervalMin=TimeIntervalMin, PYSNMP_MODULE_ID=ciscoTextualConventions, CiscoAlarmSeverity=CiscoAlarmSeverity, CiscoPort=CiscoPort, TimeIntervalSec=TimeIntervalSec)
