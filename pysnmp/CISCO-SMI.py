#
# PySNMP MIB module CISCO-SMI (http://pysnmp.sf.net)
# ASN.1 source file:///opt/xee/dev/mibs/asn1/cisco/CISCO-SMI
# Produced by pysmi-0.0.6 at Mon Dec  7 15:51:14 2015
# On host ubuntu platform Linux version 3.19.0-31-generic by user dkor
# Using Python version 2.7.9 (default, Apr  2 2015, 15:33:21) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9)).setRevisions(("2012-08-29 00:00", "2009-02-03 00:00", "2002-03-21 00:00", "2001-05-22 00:00", "2000-11-01 22:46", "2000-01-11 00:00", "1997-04-09 00:00", "1995-05-16 00:00", "1994-04-26 20:00",))
ciscoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 1))
local = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 2))
temporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 3))
pakmon = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 4))
workgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 5))
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6))
ciscoSB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1))
ciscoSMB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 2))
ciscoAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 7))
ciscoConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 8))
ciscoMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9))
ciscoExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10))
ciscoAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11))
ciscoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 12))
lightstream = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 13))
ciscoworks = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 14))
newport = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 15))
ciscoPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 16))
ciscoPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17))
ciscoPIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17, 2))
ciscoPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18))
ciscoPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18, 2))
ciscoDomains = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19))
ciscoCIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20))
ciscoCibMmiGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 1))
ciscoCibProvGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 2))
ciscoPKI = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 21))
ciscoProxy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 1))
ciscoPartyProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 1))
ciscoContextProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 2))
ciscoRptrGroupObjectID = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2))
ciscoUnknownRptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 1))
cisco2505RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 2))
cisco2507RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 3))
cisco2516RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 4))
ciscoWsx5020RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 5))
ciscoChipSets = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3))
ciscoChipSetSaint1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 1))
ciscoChipSetSaint2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 2))
ciscoChipSetSaint3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 3))
ciscoChipSetSaint4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 4))
ciscoTDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 19, 99999))
ciscoTDomainUdpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 1))
ciscoTDomainUdpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 2))
ciscoTDomainTcpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 3))
ciscoTDomainTcpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 4))
ciscoTDomainLocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 5))
ciscoTDomainClns = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 6))
ciscoTDomainCons = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 7))
ciscoTDomainDdp = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 8))
ciscoTDomainIpx = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 9))
ciscoTDomainSctpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 10))
ciscoTDomainSctpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 11))
mibBuilder.exportSymbols("CISCO-SMI", workgroup=workgroup, ciscoContextProxy=ciscoContextProxy, ciscoExperiment=ciscoExperiment, ciscoTDomainIpx=ciscoTDomainIpx, lightstream=lightstream, ciscoPolicyAuto=ciscoPolicyAuto, ciscoTDomainTcpIpv4=ciscoTDomainTcpIpv4, ciscoTDomainSctpIpv6=ciscoTDomainSctpIpv6, ciscoChipSetSaint4=ciscoChipSetSaint4, ciscoDomains=ciscoDomains, ciscoPartnerProducts=ciscoPartnerProducts, ciscoChipSetSaint3=ciscoChipSetSaint3, ciscoProducts=ciscoProducts, cisco=cisco, cisco2505RptrGroup=cisco2505RptrGroup, ciscoTDomainDdp=ciscoTDomainDdp, local=local, cisco2516RptrGroup=cisco2516RptrGroup, ciscoMgmt=ciscoMgmt, ciscoPolicy=ciscoPolicy, ciscoChipSetSaint1=ciscoChipSetSaint1, otherEnterprises=otherEnterprises, ciscoCIB=ciscoCIB, newport=newport, ciscoModules=ciscoModules, ciscoAgentCapability=ciscoAgentCapability, ciscoWsx5020RptrGroup=ciscoWsx5020RptrGroup, ciscoUnknownRptrGroup=ciscoUnknownRptrGroup, ciscoCibProvGroup=ciscoCibProvGroup, ciscoTDomainSctpIpv4=ciscoTDomainSctpIpv4, ciscoTDomainClns=ciscoTDomainClns, ciscoPartyProxy=ciscoPartyProxy, ciscoRptrGroupObjectID=ciscoRptrGroupObjectID, ciscoTDomains=ciscoTDomains, ciscoTDomainUdpIpv4=ciscoTDomainUdpIpv4, ciscoSB=ciscoSB, ciscoCibMmiGroup=ciscoCibMmiGroup, PYSNMP_MODULE_ID=cisco, ciscoTDomainTcpIpv6=ciscoTDomainTcpIpv6, cisco2507RptrGroup=cisco2507RptrGroup, ciscoChipSetSaint2=ciscoChipSetSaint2, ciscoTDomainLocal=ciscoTDomainLocal, ciscoConfig=ciscoConfig, ciscoPibToMib=ciscoPibToMib, ciscoPIB=ciscoPIB, ciscoworks=ciscoworks, ciscoTDomainUdpIpv6=ciscoTDomainUdpIpv6, temporary=temporary, ciscoProxy=ciscoProxy, ciscoPKI=ciscoPKI, ciscoAdmin=ciscoAdmin, ciscoSMB=ciscoSMB, ciscoTDomainCons=ciscoTDomainCons, pakmon=pakmon, ciscoChipSets=ciscoChipSets)
