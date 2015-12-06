# PySNMP SMI module. Autogenerated from smidump -f python CISCO-RTTMON-IP-EXT-MIB
# by libsmi2pysnmp-0.1.3 at Fri Aug 16 06:26:01 2013,
# Python version (2, 6, 6, 'final', 0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( rttMonCtrlAdminEntry, rttMonEchoAdminEntry, rttMonEchoPathAdminEntry, rttMonHistoryCollectionEntry, rttMonLpdGrpStatsEntry, rttMonStatsCollectEntry, ) = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonCtrlAdminEntry", "rttMonEchoAdminEntry", "rttMonEchoPathAdminEntry", "rttMonHistoryCollectionEntry", "rttMonLpdGrpStatsEntry", "rttMonStatsCollectEntry")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( DscpOrAny, ) = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "DscpOrAny")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( IPv6FlowLabelOrAny, ) = mibBuilder.importSymbols("IPV6-FLOW-LABEL-MIB", "IPv6FlowLabelOrAny")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

ciscoRttMonIPExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 572)).setRevisions(("2006-08-02 00:00",))
if mibBuilder.loadTexts: ciscoRttMonIPExtMIB.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: ciscoRttMonIPExtMIB.setContactInfo("Cisco Systems, Inc.\nCustomer Service\n\nPostal: 170 W Tasman Drive\nSan Jose, CA 95134\n\nTel: +1 800 553 NETS\nEmail: cs-ipsla@cisco.com")
if mibBuilder.loadTexts: ciscoRttMonIPExtMIB.setDescription("This MIB contains extensions to tables in CISCO-RTTMON-MIB\nto support IP-layer extensions, specifically IPv6 addresses \nand other information related to IPv6 and other IP information")
crttMonIPExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 572, 1))
crttMonIPEchoAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1))
if mibBuilder.loadTexts: crttMonIPEchoAdminTable.setDescription("An extension of the rttMonEchoAdminTable, defined in\nthe CISCO-RTTMON-MIB, which provides the additional\ncapability of recording the addresses as IPv6 addresses,\nplus other IPv6 and IP layer extension information")
crttMonIPEchoAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1))
if mibBuilder.loadTexts: crttMonIPEchoAdminEntry.setDescription("A list of additional objects needed for IPv6 addresses.")
crttMonIPEchoAdminTargetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminTargetAddrType.setDescription("An enumerated value which specifies the address type \nof the target. \nThis object must be used along with the\ncrttMonIPEchoAdminTargetAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPEchoAdminTargetAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonEchoAdminTargetAddress), this object contains\nthe value 'unknown'.")
crttMonIPEchoAdminTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 2), InetAddress().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminTargetAddress.setDescription("A string which specifies the address of the target. \nThis object, in conjunction with the\ncrttMonIPEchoAdminTargetAddrType object, \nmay be used to specify either an IPv6 or an IPv4 address and \nis an alternative to the rttMonEchoAdminTargetAddress object,\nwhich may only specify an IPv4 address. In case the target is\na V4  IP address then both crttMonIPEchoAdminTargetAddrType/\ncrttMonIPEchoAdminTargetAddress AND \nrttMonEchoAdminTargetAddress may be used to specify it so long \nas both try to specify the\nsame V4 IP address. Alternatively only one of \nrttMonEchoAdminTargetAddress\nOR crttMonIPEchoAdminTargetAddrType/\ncrttMonIPEchoAdminTargetAddress may be used to specify the \nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPEchoAdminTargetAddrType/\ncrttMonIPEchoAdminTargetAddress must be used and \nrttMonEchoAdminTargetAddress may not be instantiated or\nmay have a zero length string.")
crttMonIPEchoAdminSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminSourceAddrType.setDescription("An enumerated value which specifies the address type \nof the source.\nThis object must be used along with the\ncrttMonIPEchoAdminSourceAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPEchoAdminSourceAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonEchoAdminSourceAddress), this object contains\nthe value 'unknown'.")
crttMonIPEchoAdminSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 4), InetAddress().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminSourceAddress.setDescription("A string which specifies the address of the target. \nThis object, together with the \ncrttMonIPEchoAdminSourceAddrType object,\nmay be used to specify either an IPv6 or an IPv4 address and \nis an alternative to the rttMonEchoAdminSourceAddress\nobject, which\nmay only specify an IPv4 address. In case the target is a V4\nIP address then both crttMonIPEchoAdminSourceAddrType/\ncrttMonIPEchoAdminSourceAddress AND \nrttMonEchoAdminSourceAddress\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonEchoAdminSourceAddress\nOR crttMonIPEchoAdminSourceAddrType/\ncrttMonIPEchoAdminSourceAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPEchoAdminSourceAddrType/\ncrttMonIPEchoAdminSourceAddress must be used and\nrttMonEchoAdminSourceAddress may not be instantiated or\nmay have a zero length string.")
crttMonIPEchoAdminNameServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 5), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminNameServerAddrType.setDescription("An enumerated value which specifies the address type \nof the target.\nThis object must be used along with the\ncrttMonIPEchoAdminNameServerAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPEchoAdminNameServerAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonEchoAdminNameServer), this object contains\nthe value 'unknown'.")
crttMonIPEchoAdminNameServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 6), InetAddress().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminNameServerAddress.setDescription("A string which specifies the address of the target. This object,\ntogether with the crttMonIPEchoAdminNameServerAddrType object,\nmay be used to specify either an IPv6 or an IPv4 address and is\nan alternative to the rttMonEchoAdminNameServer object, which\ncan only specify an IPv4. In case the target is a V4\nIP address then both crttMonIPEchoAdminNameServerAddrType/\ncrttMonIPEchoAdminNameServerAddress AND \nrttMonEchoAdminNameServer\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonEchoAdminNameServer\nOR crttMonIPEchoAdminNameServerAddrType/\ncrttMonIPEchoAdminNameServerAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPEchoAdminNameServerAddrType/\ncrttMonIPEchoAdminNameServerAddress must be used and\nrttMonEchoAdminNameServer may not be instantiated or\nmay have a zero length string.")
crttMonIPEchoAdminLSPSelAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 7), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminLSPSelAddrType.setDescription("An enumerated value which specifies the address type \nof the target.\nThis object must be used along with the\ncrttMonIPEchoAdminLSPSelAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPEchoAdminLSPSelAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonEchoAdminLSPSelector), this object contains\nthe value 'unknown'.")
crttMonIPEchoAdminLSPSelAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 8), InetAddress().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminLSPSelAddress.setDescription("A string which specifies the address of the LSP Selector. \nThis object, in conjunction with the \ncrttMonIPEchoAdminLSPSelAddrType object,\nmay be used to specify either an IPv6 or an IPv4 address and is\nan alternative to the rttMonEchoAdminLSPSelector object, which\ncan only specify an IPv4 address.In case the target is a V4\nIP address then both crttMonIPEchoAdminLSPSelAddrType/\ncrttMonIPEchoAdminLSPSelAddress AND rttMonEchoAdminLSPSelector\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonEchoAdminLSPSelector\nOR crttMonIPEchoAdminLSPSelAddrType/\ncrttMonIPEchoAdminLSPSelAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPEchoAdminLSPSelAddrType/\ncrttMonIPEchoAdminLSPSelAddress must be used and\nrttMonEchoAdminLSPSelector may not be instantiated or\nmay have a zero length string.")
crttMonIPEchoAdminDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 9), DscpOrAny().clone('-1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminDscp.setDescription("The DSCP value (either an IPv4 TOS octet or an IPv6 Traffic\nClass octet) to be set in outgoing packets.")
crttMonIPEchoAdminFlowLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 10), IPv6FlowLabelOrAny()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoAdminFlowLabel.setDescription("The Flow Label in an IPv6 packet header.")
crttMonIPLatestRttOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2))
if mibBuilder.loadTexts: crttMonIPLatestRttOperTable.setDescription("An extension of the rttMonLatestRttOperTable, defined in\nthe CISCO-RTTMON-MIB, which provides the additional\ncapability of specifying IPv6 addresses.")
crttMonIPLatestRttOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1))
if mibBuilder.loadTexts: crttMonIPLatestRttOperEntry.setDescription("A list of objects required to support IPv6 addresses. ")
crttMonIPLatestRttOperAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crttMonIPLatestRttOperAddressType.setDescription("An enumerated value which specifies the address type \nof the target.\nThis object must be used along with the\ncrttMonIPLatestRttOperAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPLatestRttOperAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonLatestRttOperAddress), this object contains\nthe value 'unknown'.")
crttMonIPLatestRttOperAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1, 2), InetAddress().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crttMonIPLatestRttOperAddress.setDescription("A string which specifies the address of the target. This object,\ntogether with the crttMonIPLatestRttOperAddressType object,\nmay be used to specify either an IPv6 or an IPv4 address and is\nan alternative to the rttMonLatestRttOperAddress object, which\ncan only specify an IPv4 address. In case the target is a V4\nIP address then both crttMonIPLatestRttOperAddressType/\ncrttMonIPLatestRttOperAddress AND rttMonLatestRttOperAddress\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonLatestRttOperAddress\nOR crttMonIPLatestRttOperAddressType/\ncrttMonIPLatestRttOperAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPLatestRttOperAddressType/\ncrttMonIPLatestRttOperAddress must be used and\nrttMonLatestRttOperAddress may not be instantiated or\nmay have a zero length string.")
crttMonIPEchoPathAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3))
if mibBuilder.loadTexts: crttMonIPEchoPathAdminTable.setDescription("An extension of the rttMonEchoPathAdminTable, defined in\nthe CISCO-RTTMON-MIB, which provides the additional\ncapability of recording the hops as IPv6 addresses.")
crttMonIPEchoPathAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1))
if mibBuilder.loadTexts: crttMonIPEchoPathAdminEntry.setDescription("A list of additional objects needed for IPv6 addresses.")
crttMonIPEchoPathAdminHopAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoPathAdminHopAddrType.setDescription("An enumerated value which specifies the address type \nof the hop.\nThis object must be used along with the\ncrttMonIPEchoPathAdminHopAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPEchoPathAdminHopAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonEchoPathAdminHopAddress), this object contains\nthe value 'unknown'.")
crttMonIPEchoPathAdminHopAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1, 2), InetAddress().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crttMonIPEchoPathAdminHopAddress.setDescription("A string which specifies the address of the hop. This object,\ntogether with the crttMonIPEchoPathAdminHopAddrType object, \nmay be used to specify either an IPv6 or an IPv4 address and is \nan alternative to the \nrttMonEchoPathAdminHopAddress object, which\ncan only specify an IPv4 address. In case the target is a V4\nIP address then both crttMonIPEchoPathAdminHopAddrType/\ncrttMonIPEchoPathAdminHopAddress AND \nrttMonEchoPathAdminHopAddress\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonEchoPathAdminHopAddress\nOR crttMonIPEchoPathAdminHopAddrType/\ncrttMonIPEchoPathAdminHopAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPEchoPathAdminHopAddrType/\ncrttMonIPEchoPathAdminHopAddress must be used and\nrttMonEchoPathAdminHopAddress may not be instantiated or\nmay have a zero length string.")
crttMonIPStatsCollectTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4))
if mibBuilder.loadTexts: crttMonIPStatsCollectTable.setDescription("An extension of the rttMonStatsCollectTable, defined in\nthe CISCO-RTTMON-MIB, which provides the additional\ncapability of specifying the collection address as an\nIPv6 address.")
crttMonIPStatsCollectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1))
if mibBuilder.loadTexts: crttMonIPStatsCollectEntry.setDescription("A list of additional objects needed for IPv6 addresses.")
crttMonIPStatsCollectAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: crttMonIPStatsCollectAddressType.setDescription("An enumerated value which specifies the address type \nof the target.\nThis object must be used along with the\ncrttMonIPStatsCollectAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPStatsCollectAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonStatsCollectAddress), this object contains\nthe value 'unknown'.")
crttMonIPStatsCollectAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1, 2), InetAddress().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: crttMonIPStatsCollectAddress.setDescription("A string which specifies the address of the collection target. \nThis object, in conjunction with the \ncrttMonIPStatsCollectAddressType object,\nmay be used to specify either an IPv6 or an IPv4 address and is\nan alternative to the rttMonStatsCollectAddress object, which\ncan only specify an IPv4 address. In case the target is a V4\nIP address then both crttMonIPStatsCollectAddressType/\ncrttMonIPStatsCollectAddress AND rttMonStatsCollectAddress\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonStatsCollectAddress\nOR crttMonIPStatsCollectAddressType/\ncrttMonIPStatsCollectAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPStatsCollectAddressType/\ncrttMonIPStatsCollectAddress must be used and\nrttMonStatsCollectAddress may not be instantiated or\nmay have a zero length string.")
crttMonIPLpdGrpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5))
if mibBuilder.loadTexts: crttMonIPLpdGrpStatsTable.setDescription("An extension of the rttMonLpdGrpStatsTable, defined in\nthe CISCO-RTTMON-MIB, which provides the additional\ncapability of specifying the target PE address as an\nIPv6 address.")
crttMonIPLpdGrpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1))
if mibBuilder.loadTexts: crttMonIPLpdGrpStatsEntry.setDescription("A list of additional objects needed for IPv6 addresses.")
crttMonIPLpdGrpStatsTargetPEAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: crttMonIPLpdGrpStatsTargetPEAddrType.setDescription("An enumerated value which specifies the address type \nof the target.\nThis object must be used along with the\ncrttMonIPLpdGrpStatsTargetPEAddr\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPLpdGrpStatsTargetPEAddr is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonLpdGrpStatsTargetPE), this object contains\nthe value 'unknown'.")
crttMonIPLpdGrpStatsTargetPEAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1, 2), InetAddress().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: crttMonIPLpdGrpStatsTargetPEAddr.setDescription("A string which specifies the address of the target PE. \nThis object, in conjunction with the \ncrttMonIPLpdGrpStatsTargetPEAddrType object,\nmay be used to specify either an IPv6 or an IPv4 address and is\nan alternative to the rttMonLpdGrpStatsTargetPE object, which\ncan only specify an IPv4 address. In case the target is a V4\nIP address then both crttMonIPLpdGrpStatsTargetPEAddrType/\ncrttMonIPLpdGrpStatsTargetPEAddr AND rttMonLpdGrpStatsTargetPE\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonLpdGrpStatsTargetPE\nOR crttMonIPLpdGrpStatsTargetPEAddrType/\ncrttMonIPLpdGrpStatsTargetPEAddr may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPLpdGrpStatsTargetPEAddrType/\ncrttMonIPLpdGrpStatsTargetPEAddr must be used and\nrttMonLpdGrpStatsTargetPE may not be instantiated or\nmay have a zero length string.")
crttMonIPHistoryCollectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6))
if mibBuilder.loadTexts: crttMonIPHistoryCollectionTable.setDescription("An extension of the rttMonHistoryCollectionTable, defined in\nthe CISCO-RTTMON-MIB, which provides the additional\ncapability of specifying the target address as an\nIPv6 address.")
crttMonIPHistoryCollectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1))
if mibBuilder.loadTexts: crttMonIPHistoryCollectionEntry.setDescription("A list of additional objects needed for IPv6 addresses.")
crttMonIPHistoryCollectionAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: crttMonIPHistoryCollectionAddrType.setDescription("An enumerated value which specifies the address type \nof the target.\nThis object must be used along with the\ncrttMonIPHistoryCollectionAddress\nobject as it identifies the address family of the\naddress specified by that object. If the value\nof crttMonIPHistoryCollectionAddress is a zero-length\nstring (e.g., because an IPv4 address is specified by \nrttMonHistoryCollectionAddress), this object contains\nthe value 'unknown'.")
crttMonIPHistoryCollectionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1, 2), InetAddress().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: crttMonIPHistoryCollectionAddress.setDescription("A string which specifies the address of the target. \nThis object, in conjunction with the \ncrttMonIPHistoryCollectionAddrType object,\nmay be used to specify either an IPv6 or an IPv4 address and is\nan alternative to the \nrttMonHistoryCollectionAddress object, which\ncan only specify an IPv4 address. In case the target is a V4\nIP address then both crttMonIPHistoryCollectionAddrType/\ncrttMonIPHistoryCollectionAddress AND \nrttMonHistoryCollectionAddress\nmay be used to specify it so long as both try to specify the\nsame V4 IP address. Alternatively only one of\nrttMonHistoryCollectionAddress\nOR crttMonIPHistoryCollectionAddrType/\ncrttMonIPHistoryCollectionAddress may be used to specify the\nV4 IP address, in which case the other may either not be\ninstantiated or contain a zero length string.\nIn case the the target is a V6 IP address\nthen only crttMonIPHistoryCollectionAddrType/\ncrttMonIPHistoryCollectionAddress must be used and\nrttMonHistoryCollectionAddress may not be instantiated or\nmay have a zero length string.")
ciscoRttMonIPExtMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 572, 2))
ciscoRttMonIPExtMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1))
ciscoRttMonIPExtMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2))

# Augmentions
rttMonCtrlAdminEntry, = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonCtrlAdminEntry")
rttMonCtrlAdminEntry.registerAugmentions(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperEntry"))
crttMonIPLatestRttOperEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonLpdGrpStatsEntry, = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsEntry")
rttMonLpdGrpStatsEntry.registerAugmentions(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsEntry"))
crttMonIPLpdGrpStatsEntry.setIndexNames(*rttMonLpdGrpStatsEntry.getIndexNames())
rttMonEchoAdminEntry, = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonEchoAdminEntry")
rttMonEchoAdminEntry.registerAugmentions(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminEntry"))
crttMonIPEchoAdminEntry.setIndexNames(*rttMonEchoAdminEntry.getIndexNames())
rttMonHistoryCollectionEntry, = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonHistoryCollectionEntry")
rttMonHistoryCollectionEntry.registerAugmentions(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionEntry"))
crttMonIPHistoryCollectionEntry.setIndexNames(*rttMonHistoryCollectionEntry.getIndexNames())
rttMonEchoPathAdminEntry, = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonEchoPathAdminEntry")
rttMonEchoPathAdminEntry.registerAugmentions(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminEntry"))
crttMonIPEchoPathAdminEntry.setIndexNames(*rttMonEchoPathAdminEntry.getIndexNames())
rttMonStatsCollectEntry, = mibBuilder.importSymbols("CISCO-RTTMON-MIB", "rttMonStatsCollectEntry")
rttMonStatsCollectEntry.registerAugmentions(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectEntry"))
crttMonIPStatsCollectEntry.setIndexNames(*rttMonStatsCollectEntry.getIndexNames())

# Groups

ciscoIPExtCtrlGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2, 1)).setObjects(*(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminHopAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminNameServerAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminLSPSelAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminFlowLabel"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminTargetAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminDscp"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsTargetPEAddr"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminSourceAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsTargetPEAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperAddressType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminHopAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminLSPSelAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectAddressType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminSourceAddress"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminTargetAddrType"), ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminNameServerAddress"), ) )
if mibBuilder.loadTexts: ciscoIPExtCtrlGroupRev1.setDescription("A collection of objects that were added to enhance the\nfunctionality of the RTT application to support other\nIP layer extensions like IPv6,\nspecifically IPv6 addresses and other information.")

# Compliances

ciscoRttMonIPExtMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1, 1)).setObjects(*(("CISCO-RTTMON-IP-EXT-MIB", "ciscoIPExtCtrlGroupRev1"), ) )
if mibBuilder.loadTexts: ciscoRttMonIPExtMibComplianceRev1.setDescription("The compliance statement for new MIB extensions for\nsupporting IPv6 addresses and other IP-layer extensions")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-RTTMON-IP-EXT-MIB", PYSNMP_MODULE_ID=ciscoRttMonIPExtMIB)

# Objects
mibBuilder.exportSymbols("CISCO-RTTMON-IP-EXT-MIB", ciscoRttMonIPExtMIB=ciscoRttMonIPExtMIB, crttMonIPExtObjects=crttMonIPExtObjects, crttMonIPEchoAdminTable=crttMonIPEchoAdminTable, crttMonIPEchoAdminEntry=crttMonIPEchoAdminEntry, crttMonIPEchoAdminTargetAddrType=crttMonIPEchoAdminTargetAddrType, crttMonIPEchoAdminTargetAddress=crttMonIPEchoAdminTargetAddress, crttMonIPEchoAdminSourceAddrType=crttMonIPEchoAdminSourceAddrType, crttMonIPEchoAdminSourceAddress=crttMonIPEchoAdminSourceAddress, crttMonIPEchoAdminNameServerAddrType=crttMonIPEchoAdminNameServerAddrType, crttMonIPEchoAdminNameServerAddress=crttMonIPEchoAdminNameServerAddress, crttMonIPEchoAdminLSPSelAddrType=crttMonIPEchoAdminLSPSelAddrType, crttMonIPEchoAdminLSPSelAddress=crttMonIPEchoAdminLSPSelAddress, crttMonIPEchoAdminDscp=crttMonIPEchoAdminDscp, crttMonIPEchoAdminFlowLabel=crttMonIPEchoAdminFlowLabel, crttMonIPLatestRttOperTable=crttMonIPLatestRttOperTable, crttMonIPLatestRttOperEntry=crttMonIPLatestRttOperEntry, crttMonIPLatestRttOperAddressType=crttMonIPLatestRttOperAddressType, crttMonIPLatestRttOperAddress=crttMonIPLatestRttOperAddress, crttMonIPEchoPathAdminTable=crttMonIPEchoPathAdminTable, crttMonIPEchoPathAdminEntry=crttMonIPEchoPathAdminEntry, crttMonIPEchoPathAdminHopAddrType=crttMonIPEchoPathAdminHopAddrType, crttMonIPEchoPathAdminHopAddress=crttMonIPEchoPathAdminHopAddress, crttMonIPStatsCollectTable=crttMonIPStatsCollectTable, crttMonIPStatsCollectEntry=crttMonIPStatsCollectEntry, crttMonIPStatsCollectAddressType=crttMonIPStatsCollectAddressType, crttMonIPStatsCollectAddress=crttMonIPStatsCollectAddress, crttMonIPLpdGrpStatsTable=crttMonIPLpdGrpStatsTable, crttMonIPLpdGrpStatsEntry=crttMonIPLpdGrpStatsEntry, crttMonIPLpdGrpStatsTargetPEAddrType=crttMonIPLpdGrpStatsTargetPEAddrType, crttMonIPLpdGrpStatsTargetPEAddr=crttMonIPLpdGrpStatsTargetPEAddr, crttMonIPHistoryCollectionTable=crttMonIPHistoryCollectionTable, crttMonIPHistoryCollectionEntry=crttMonIPHistoryCollectionEntry, crttMonIPHistoryCollectionAddrType=crttMonIPHistoryCollectionAddrType, crttMonIPHistoryCollectionAddress=crttMonIPHistoryCollectionAddress, ciscoRttMonIPExtMibConformance=ciscoRttMonIPExtMibConformance, ciscoRttMonIPExtMibCompliances=ciscoRttMonIPExtMibCompliances, ciscoRttMonIPExtMibGroups=ciscoRttMonIPExtMibGroups)

# Groups
mibBuilder.exportSymbols("CISCO-RTTMON-IP-EXT-MIB", ciscoIPExtCtrlGroupRev1=ciscoIPExtCtrlGroupRev1)

# Compliances
mibBuilder.exportSymbols("CISCO-RTTMON-IP-EXT-MIB", ciscoRttMonIPExtMibComplianceRev1=ciscoRttMonIPExtMibComplianceRev1)