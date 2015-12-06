# PySNMP SMI module. Autogenerated from smidump -f python CISCO-ETHER-CFM-MIB
# by libsmi2pysnmp-0.1.3 at Fri Aug 16 02:54:39 2013,
# Python version (2, 6, 6, 'final', 0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( VlanId, ) = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Gauge32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( MacAddress, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TimeStamp")

# Types

class CfmMepid(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,8191)
    

# Objects

ciscoEtherCfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 461)).setRevisions(("2004-12-28 00:00",))
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setContactInfo("            Cisco Systems\nCustomer Service\nPostal: 170 W Tasman Drive\nSan Jose, CA 95134\nUSA\nTel: +1 800 553-NETS\nE-mail:  cs-ethermibs@cisco.com")
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setDescription("This MIB module defines the managed objects \nand notifications for Ethernet Connectivity \nFault Management (CFM).\n\nCFM is an end-to-end per service instance Ethernet layer \nOperations, Administration and Management (OAM) protocol. \n\nCFM events include: \n\n- Maintenance End-Point (MEP) coming up: establishing \n  connectivity\n\n- Maintenance End-Point going down: losing connectivity\n\n- Maintenance End-Point unknown: unexpected\n\n- Maintenance End-Point missing: expected but not reachable\n\n- Continuity Check Configuration Error: collision in MEP IDs\n\n- Continuity Check Loop: forwarding loop in network\n\n- Continuity Check Cross-connect: cross-connected \n  forwarding path.\n\nThe following acronyms are used in this module:\n\n- MEP: Maintenance End Point\n\n- MEPID: Maintenance End Point Identifier\n\n- CC: Continuity Check\n\n- CCDB: Continuity Check Database\n\n- SVLAN: Service Provider Virtual Local Area Network\n\n- VLAN: Virtual Local Area Network\n\n- CLI: Command Line Interface.\n\n- OAM: Operations Administration and Management.")
ciscoEtherCfmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 0))
ciscoEtherCfmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0))
ciscoEtherCfmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 1))
cecCfmEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1))
cEtherCfmMaxEventIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmMaxEventIndex.setDescription("This object specifies the maximum upper value supported \nfor the cEtherCfmEventIndex index by this agent.")
cEtherCfmEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2))
if mibBuilder.loadTexts: cEtherCfmEventTable.setDescription("This table contains a collection of Ethernet CFM notifications\ngenerated by the device. The notifications correspond to events\nrecognized by the device and fall into the following classes:\n\n- MEP-Up\n\n- MEP-Down\n\n- Configuration Error\n\n- Forwarding Loop\n\n- Cross-connected Ethernet Connection\n\n- Crosscheck Missing MEP\n\n- Crosscheck Unknown MEP\n\n- Crosscheck Service Up\n\nA conceptual row is created in this table whenever the device \nencounters one of the events listed above. Rows can only be\ncreated by the agent, and not at the request of the management\nstation.\n\nRows are deleted at the request of a management station by \nsetting the cEtherCfmEventDeleteRow object to 'delete'.\nAnother way of deleting rows is through the CLI.\n\nAlthough this table may be indexed uniquely by the \ncEtherCfmEventIndex index, the first two indices \n(cEtherCfmEventDomainIndex and cEtherCfmEventSvlan) are used\nto speed-up queries per maintenance domain and per customer\nservice instance. Furthermore, these two indices will help\nin defining the MIB views easily in order to restrict access\nto the MIB to particular entities (be it a service provider,\nor operator, or customer).")
cEtherCfmEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1)).setIndexNames((0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainIndex"), (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventSvlan"), (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventIndex"))
if mibBuilder.loadTexts: cEtherCfmEventEntry.setDescription("An entry in this table is created for every event reported\nby Ethernet CFM.")
cEtherCfmEventDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cEtherCfmEventDomainIndex.setDescription("This object represents the ID which uniquely identifies \na CFM maintenance domain on the device. Every domain can\nbe uniquely identified by its user-defined \nname (cEtherCfmEventDomainName) or device-assigned ID (this\nobject).")
cEtherCfmEventSvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 2), VlanId()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cEtherCfmEventSvlan.setDescription("The service VLAN identifier of the customer service \ninstance to which the event belongs.")
cEtherCfmEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cEtherCfmEventIndex.setDescription("A monotonically increasing integer for the sole purpose of\nindexing CFM events.  When it reaches the maximum value \nsupported by the agent, as defined in the \ncEtherCfmMaxEventIndex object, the agent wraps the value\nback to 1 and may flush existing entries.")
cEtherCfmEventDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventDomainName.setDescription("The name of the CFM maintenance domain.")
cEtherCfmEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,7,2,5,6,4,8,)).subtype(namedValues=NamedValues(("mepUp", 1), ("mepDown", 2), ("xconnect", 3), ("loop", 4), ("config", 5), ("xcheckMissing", 6), ("xcheckUnknown", 7), ("xcheckServiceUp", 8), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventType.setDescription("This object informs the management station of how to interpret\nthe rest of the objects within a row, as summarized in the \nfollowing table:\n\nLegend I: Ignored Object \n       V: Valid Object\n\nObject                                 cEtherCfmEventType\n                               | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8\n================================================================\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventDomainIndex      | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventSvlan            | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventIndex            | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventLastChange       | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventServiceId        | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventDomainName       | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventLclMepid         | I | I | I | V | V | I | I | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventLclMacAddress    | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventLclMepCount      | V | V | I | I | I | I | I | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventLclIfCount       | V | V | I | I | I | I | I | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventRmtMepid         | V | V | V | I | I | V | V | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventRmtMacAddress    | V | V | V | I | V | V | V | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventRmtPortState     | V | I | I | I | I | I | I | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventRmtServiceId     | I | I | V | I | I | I | I | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventCode             | V | V | I | I | I | I | I | I\n                               |   |   |   |   |   |   |   |\ncEtherCfmEventDeleteRow        | V | V | V | V | V | V | V | V\n                               |   |   |   |   |   |   |   |\n\nNote: When reading any ignored object, a value of 0 will \nbe returned by the agent.")
cEtherCfmEventLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLastChange.setDescription("The value of sysUpTime at the time when this row was created.")
cEtherCfmEventServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventServiceId.setDescription("The customer service instance to which the event belongs.")
cEtherCfmEventLclMepid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 8), CfmMepid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMepid.setDescription("The identifier of the local MEP impacted by the event.")
cEtherCfmEventLclMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMacAddress.setDescription("The MAC address of the device reporting the event.")
cEtherCfmEventLclMepCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMepCount.setDescription("The number of local MEPs affected by the event.")
cEtherCfmEventLclIfCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclIfCount.setDescription("The number of local interfaces affected by the event.")
cEtherCfmEventRmtMepid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 12), CfmMepid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtMepid.setDescription("The maintenance end-point identifier of the remote \nMEP causing the event entry to be logged.")
cEtherCfmEventRmtMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtMacAddress.setDescription("The MAC address of the remote maintenance point for which\nthe event entry is being logged.")
cEtherCfmEventRmtPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(2,4,6,3,7,5,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("adminDown", 3), ("test", 4), ("remoteExcessiveErrors", 5), ("localExcessiveErrors", 6), ("localNoData", 7), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtPortState.setDescription("The operational state of the port on which the \nremote MEP is configured. This information is \nderived from the port-state as indicated in the \nCC message. The possible values are:\n\n'up'                    - The port is operationally up.\n\n'down'                  - The port is operationally (but not\n                          administratively) down.\n\n'adminDown'             - The port is administratively down.\n\n'test'                  - The port is in test mode (perhaps \n                          due to an IEEE Standard 802.3ah OAM\n                          intrusive loopback operation).\n\n'remoteExcessiveErrors' - 802.3ah OAM reports that the other \n                          end of the link is receiving an \n                          excessive number of invalid frames.\n\n'localExcessiveErrors'  - 802.3ah OAM reports that this end of\n                          the link is receiving an excessive \n                          number of invalid frames.\n\n'localNoData'           - No data and no CFM messages have been\n                          received for an excessive length of \n                          time.")
cEtherCfmEventRmtServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 15), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtServiceId.setDescription("The ID that the remote device has configured for the \ncustomer service instance (VLAN).")
cEtherCfmEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 16), Integer().subtype(subtypeSpec=SingleValueConstraint(4,5,8,1,2,7,3,6,9,)).subtype(namedValues=NamedValues(("new", 1), ("returning", 2), ("portState", 3), ("lastGasp", 4), ("timeout", 5), ("configClear", 6), ("loopClear", 7), ("xconnectClear", 8), ("unknownClear", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventCode.setDescription("This object is used in decoding 'mepUp' and 'mepDown' events. \n\n** For 'mepUp', the following codes are relevant:\n\n    'new'           - This is the very first time the device \n                      receives a CC message from the remote MEP.\n\n    'returning'     - The device received a CC message from a \n                      remote MEP for which it had an expired \n                      CCDB entry.\n\n    'portState'     - The device received a CC message from a \n                      remote MEP for which it has a valid CCDB \n                      entry, and the message indicates a port \n                      status change.\n\n** For 'mepDown', the following codes are relevant:\n\n    'lastGasp'      - The device received a CC message from a\n                      remote MEP with zero lifetime.\n\n    'timeout'       - The local CCDB entry for the remote MEP \n                      expired.\n\n    'configClear'   - A previous CC message from a MEP that\n                      triggered a configuration error event\n                      is cleared.\n    \n    'loopClear'     - A previous CC message from a MEP that\n                      triggered a loop error event is cleared.\n\n    'xconnectClear' - A previous CC message from a MEP that\n                      triggered a crossconnect error event \n                      is cleared.\n\n    'unknownClear'  - A previous CC message from a MEP that\n                      triggered an unknown MEP event is \n                      cleared.")
cEtherCfmEventDeleteRow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 17), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("noop", 1), ("delete", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cEtherCfmEventDeleteRow.setDescription("This object allows the management station to \ndelete a row in the cEtherCfmEventTable in order\nto free system resources.\n\nWhen reading this object the value of 'noop' will be \nreturned. This object can only be set to 'delete'. \n\nWhen this object is set to 'delete', the conceptual\nrow corresponding to this object will be deleted to\nfree system resources. This is equivalent to clearing\nthe event log. Should the trigger that caused the event\nto be logged reoccur, the event will be re-asserted but\nin a different conceptual row.")
ciscoEtherCfmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2))
ciscoEtherCfmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1))
ciscoEtherCfmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2))

# Augmentions

# Notifications

cEtherCfmCcMepUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 1)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ) )
if mibBuilder.loadTexts: cEtherCfmCcMepUp.setDescription("This notification is generated in the following cases:\n\n- when a remote MEP first comes up, that is when we receive \na CC message from that MEP for the first time.\n\n- when the device receives a CC message from a MEP for which \nit has an expired CCDB entry.\n\n- when a CC message is received for a remote MEP for which\nthe device already has a CCDB entry and the port-state in\nthe received CC message is different from the cached \nprevious state.")
cEtherCfmCcMepDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 2)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ) )
if mibBuilder.loadTexts: cEtherCfmCcMepDown.setDescription("This notification is generated when a remote MEP goes down; \ni.e. the entry in CCDB corresponding to this MEP times out \nor the device receives a CC message with zero hold-time.")
cEtherCfmCcCrossconnect = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 3)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ) )
if mibBuilder.loadTexts: cEtherCfmCcCrossconnect.setDescription("This notification is generated when a device receives a CC\nmessage with the service ID not matching the one locally \nconfigured for the VLAN in question.")
cEtherCfmCcLoop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 4)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ) )
if mibBuilder.loadTexts: cEtherCfmCcLoop.setDescription("This notification is generated when a device receives a CC\nmessage with the same MEPID and MAC address as those of\nthe device itself, indicating that there is a forwarding\nloop and that the device is receiving its own CC messages.")
cEtherCfmCcConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 5)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ) )
if mibBuilder.loadTexts: cEtherCfmCcConfigError.setDescription("This notification is generated when a device receives a CC\nmessage with the same MEPID but different MAC address as \nthose of the device itself, indicating that there is a  \nmis-configuration in the network where a remote device\nhas the same MEPID configured.")
cEtherCfmXCheckMissing = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 6)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ) )
if mibBuilder.loadTexts: cEtherCfmXCheckMissing.setDescription("This notification is generated when an expected \n(configured) MEP does not come up during the cross-check\nstart timeout interval.")
cEtherCfmXCheckUnknown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 7)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ) )
if mibBuilder.loadTexts: cEtherCfmXCheckUnknown.setDescription("This notification is generated when an unexpected MEP\ncomes up.")
cEtherCfmXCheckServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 8)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ) )
if mibBuilder.loadTexts: cEtherCfmXCheckServiceUp.setDescription("This notification is generated when all the MEPs belonging\nto a customer service instance come up before the expiration of\nthe cross-check start timeout interval.")

# Groups

ciscoEtherCfmMIBEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 1)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDeleteRow"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainName"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLastChange"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmMaxEventIndex"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventType"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ) )
if mibBuilder.loadTexts: ciscoEtherCfmMIBEventGroup.setDescription("Set of objects needed for CFM events.")
ciscoEtherCfmMIBNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 2)).setObjects(*(("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckMissing"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcConfigError"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcLoop"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepUp"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckServiceUp"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcCrossconnect"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckUnknown"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepDown"), ) )
if mibBuilder.loadTexts: ciscoEtherCfmMIBNotifGroup.setDescription("Set of notifications implemented in this module.")

# Compliances

ciscoEtherCfmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1, 1)).setObjects(*(("CISCO-ETHER-CFM-MIB", "ciscoEtherCfmMIBEventGroup"), ("CISCO-ETHER-CFM-MIB", "ciscoEtherCfmMIBNotifGroup"), ) )
if mibBuilder.loadTexts: ciscoEtherCfmMIBCompliance.setDescription("Compliance statement for agents that support the Ethernet\nCFM MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", PYSNMP_MODULE_ID=ciscoEtherCfmMIB)

# Types
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", CfmMepid=CfmMepid)

# Objects
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", ciscoEtherCfmMIB=ciscoEtherCfmMIB, ciscoEtherCfmMIBNotifs=ciscoEtherCfmMIBNotifs, ciscoEtherCfmNotificationPrefix=ciscoEtherCfmNotificationPrefix, ciscoEtherCfmMIBObjects=ciscoEtherCfmMIBObjects, cecCfmEvents=cecCfmEvents, cEtherCfmMaxEventIndex=cEtherCfmMaxEventIndex, cEtherCfmEventTable=cEtherCfmEventTable, cEtherCfmEventEntry=cEtherCfmEventEntry, cEtherCfmEventDomainIndex=cEtherCfmEventDomainIndex, cEtherCfmEventSvlan=cEtherCfmEventSvlan, cEtherCfmEventIndex=cEtherCfmEventIndex, cEtherCfmEventDomainName=cEtherCfmEventDomainName, cEtherCfmEventType=cEtherCfmEventType, cEtherCfmEventLastChange=cEtherCfmEventLastChange, cEtherCfmEventServiceId=cEtherCfmEventServiceId, cEtherCfmEventLclMepid=cEtherCfmEventLclMepid, cEtherCfmEventLclMacAddress=cEtherCfmEventLclMacAddress, cEtherCfmEventLclMepCount=cEtherCfmEventLclMepCount, cEtherCfmEventLclIfCount=cEtherCfmEventLclIfCount, cEtherCfmEventRmtMepid=cEtherCfmEventRmtMepid, cEtherCfmEventRmtMacAddress=cEtherCfmEventRmtMacAddress, cEtherCfmEventRmtPortState=cEtherCfmEventRmtPortState, cEtherCfmEventRmtServiceId=cEtherCfmEventRmtServiceId, cEtherCfmEventCode=cEtherCfmEventCode, cEtherCfmEventDeleteRow=cEtherCfmEventDeleteRow, ciscoEtherCfmMIBConform=ciscoEtherCfmMIBConform, ciscoEtherCfmMIBCompliances=ciscoEtherCfmMIBCompliances, ciscoEtherCfmMIBGroups=ciscoEtherCfmMIBGroups)

# Notifications
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", cEtherCfmCcMepUp=cEtherCfmCcMepUp, cEtherCfmCcMepDown=cEtherCfmCcMepDown, cEtherCfmCcCrossconnect=cEtherCfmCcCrossconnect, cEtherCfmCcLoop=cEtherCfmCcLoop, cEtherCfmCcConfigError=cEtherCfmCcConfigError, cEtherCfmXCheckMissing=cEtherCfmXCheckMissing, cEtherCfmXCheckUnknown=cEtherCfmXCheckUnknown, cEtherCfmXCheckServiceUp=cEtherCfmXCheckServiceUp)

# Groups
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", ciscoEtherCfmMIBEventGroup=ciscoEtherCfmMIBEventGroup, ciscoEtherCfmMIBNotifGroup=ciscoEtherCfmMIBNotifGroup)

# Compliances
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", ciscoEtherCfmMIBCompliance=ciscoEtherCfmMIBCompliance)
