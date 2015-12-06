# PySNMP SMI module. Autogenerated from smidump -f python TRANSPORT-ADDRESS-MIB
# by libsmi2pysnmp-0.1.3 at Tue Apr  3 16:58:37 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

try:
    from socket import inet_ntop, inet_pton, AF_INET, AF_INET6, has_ipv6
except ImportError:
    has_ipv6 = False

if not has_ipv6:
    from socket import inet_ntoa, inet_aton, AF_INET
    inet_ntop = lambda x,y: inet_ntoa(y)
    inet_pton = lambda x,y: inet_aton(y)
    AF_INET6 = None
    
from pyasn1.compat.octets import int2oct, oct2int
from pysnmp import error

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class TransportAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class TransportAddressDns(TextualConvention, OctetString):
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)
    
class TransportAddressIPv4(TextualConvention, OctetString):
    displayHint = "1d.1d.1d.1d:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(6,6)
    fixedLength = 6
 
    def prettyIn(self, value):
        if isinstance(value, tuple):
            # Wild hack -- need to implement TextualConvention.prettyIn
            value = inet_pton(AF_INET, value[0]) + \
                    int2oct((value[1] >> 8) & 0xff) + \
                    int2oct(value[1] & 0xff)
        return OctetString.prettyIn(self, value)

    # Socket address syntax coercion
    def __getitem__(self, i):
        if not hasattr(self, '__tuple_value'):
            v = self.asOctets()
            self.__tuple_value = (
                inet_ntop(AF_INET, v[:4]),
                oct2int(v[4]) << 8 | oct2int(v[5]),
            )
        return self.__tuple_value[i]
    
class TransportAddressIPv4z(TextualConvention, OctetString):
    displayHint = "1d.1d.1d.1d%4d:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(10,10)
    fixedLength = 10
    
class TransportAddressIPv6(TextualConvention, OctetString):
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(18,18)
    fixedLength = 18

    def prettyIn(self, value):
        if AF_INET6 is None:
            raise error.PySnmpError('IPv6 not supported by platform')
        if isinstance(value, tuple):
            value = inet_pton(AF_INET6, value[0]) + \
                    int2oct((value[1] >> 8) & 0xff) + \
                    int2oct(value[1] & 0xff)
        return OctetString.prettyIn(self, value)

    # Socket address syntax coercion
    def __getitem__(self, i):
        if not hasattr(self, '__tuple_value'):
            if AF_INET6 is None:
                raise error.PySnmpError('IPv6 not supported by platform')
            v = self.asOctets()
            self.__tuple_value = (
                inet_ntop(AF_INET6, v[:16]),
                oct2int(v[16]) << 8 | oct2int(v[17]),
                0,
                0)
        return self.__tuple_value[i]
    
class TransportAddressIPv6z(TextualConvention, OctetString):
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x%4d]0a:2d"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(22,22)
    fixedLength = 22
    
class TransportAddressLocal(TextualConvention, OctetString):
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)
    
class TransportAddressType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(12,9,14,2,7,8,0,11,1,15,16,3,4,10,6,5,13,)
    namedValues = NamedValues(("unknown", 0), ("udpIpv4", 1), ("sctpIpv6", 10), ("sctpIpv4z", 11), ("sctpIpv6z", 12), ("local", 13), ("udpDns", 14), ("tcpDns", 15), ("sctpDns", 16), ("udpIpv6", 2), ("udpIpv4z", 3), ("udpIpv6z", 4), ("tcpIpv4", 5), ("tcpIpv6", 6), ("tcpIpv4z", 7), ("tcpIpv6z", 8), ("sctpIpv4", 9), )
    
class TransportDomain(ObjectIdentifier):
    pass


# Objects

transportAddressMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 100)).setRevisions(("2002-11-01 00:00",))
if mibBuilder.loadTexts: transportAddressMIB.setOrganization("IETF Operations and Management Area")
if mibBuilder.loadTexts: transportAddressMIB.setContactInfo("Juergen Schoenwaelder (Editor)\nTU Braunschweig\nBueltenweg 74/75\n38106 Braunschweig, Germany\n\nPhone: +49 531 391-3289\nEMail: schoenw@ibr.cs.tu-bs.de\n\nSend comments to <mibs@ops.ietf.org>.")
if mibBuilder.loadTexts: transportAddressMIB.setDescription("This MIB module provides commonly used transport\naddress definitions.\n\nCopyright (C) The Internet Society (2002). This version of\nthis MIB module is part of RFC 3419; see the RFC itself for\nfull legal notices.")
transportDomains = MibIdentifier((1, 3, 6, 1, 2, 1, 100, 1))
transportDomainUdpIpv4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 1))
if mibBuilder.loadTexts: transportDomainUdpIpv4.setDescription("The UDP over IPv4 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv4 for\nglobal IPv4 addresses.")
transportDomainUdpIpv6 = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 2))
if mibBuilder.loadTexts: transportDomainUdpIpv6.setDescription("The UDP over IPv6 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv6 for\nglobal IPv6 addresses.")
transportDomainUdpIpv4z = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 3))
if mibBuilder.loadTexts: transportDomainUdpIpv4z.setDescription("The UDP over IPv4 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv4z for\nscoped IPv4 addresses with a zone index.")
transportDomainUdpIpv6z = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 4))
if mibBuilder.loadTexts: transportDomainUdpIpv6z.setDescription("The UDP over IPv6 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv6z for\nscoped IPv6 addresses with a zone index.")
transportDomainTcpIpv4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 5))
if mibBuilder.loadTexts: transportDomainTcpIpv4.setDescription("The TCP over IPv4 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv4 for\nglobal IPv4 addresses.")
transportDomainTcpIpv6 = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 6))
if mibBuilder.loadTexts: transportDomainTcpIpv6.setDescription("The TCP over IPv6 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv6 for\nglobal IPv6 addresses.")
transportDomainTcpIpv4z = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 7))
if mibBuilder.loadTexts: transportDomainTcpIpv4z.setDescription("The TCP over IPv4 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv4z for\nscoped IPv4 addresses with a zone index.")
transportDomainTcpIpv6z = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 8))
if mibBuilder.loadTexts: transportDomainTcpIpv6z.setDescription("The TCP over IPv6 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv6z for\nscoped IPv6 addresses with a zone index.")
transportDomainSctpIpv4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 9))
if mibBuilder.loadTexts: transportDomainSctpIpv4.setDescription("The SCTP over IPv4 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv4 for\nglobal IPv4 addresses. This transport domain usually\nrepresents the primary address on multihomed SCTP\nendpoints.")
transportDomainSctpIpv6 = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 10))
if mibBuilder.loadTexts: transportDomainSctpIpv6.setDescription("The SCTP over IPv6 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv6 for\nglobal IPv6 addresses. This transport domain usually\nrepresents the primary address on multihomed SCTP\nendpoints.")
transportDomainSctpIpv4z = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 11))
if mibBuilder.loadTexts: transportDomainSctpIpv4z.setDescription("The SCTP over IPv4 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv4z for\nscoped IPv4 addresses with a zone index. This transport\ndomain usually represents the primary address on\nmultihomed SCTP endpoints.")
transportDomainSctpIpv6z = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 12))
if mibBuilder.loadTexts: transportDomainSctpIpv6z.setDescription("The SCTP over IPv6 transport domain.  The corresponding\ntransport address is of type TransportAddressIPv6z for\nscoped IPv6 addresses with a zone index. This transport\ndomain usually represents the primary address on\nmultihomed SCTP endpoints.")
transportDomainLocal = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 13))
if mibBuilder.loadTexts: transportDomainLocal.setDescription("The Posix Local IPC transport domain. The corresponding\ntransport address is of type TransportAddressLocal.\n\nThe Posix Local IPC transport domain incorporates the\nwell-known UNIX domain sockets.")
transportDomainUdpDns = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 14))
if mibBuilder.loadTexts: transportDomainUdpDns.setDescription("The UDP transport domain using fully qualified domain\nnames. The corresponding transport address is of type\nTransportAddressDns.")
transportDomainTcpDns = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 15))
if mibBuilder.loadTexts: transportDomainTcpDns.setDescription("The TCP transport domain using fully qualified domain\nnames. The corresponding transport address is of type\nTransportAddressDns.")
transportDomainSctpDns = ObjectIdentity((1, 3, 6, 1, 2, 1, 100, 1, 16))
if mibBuilder.loadTexts: transportDomainSctpDns.setDescription("The SCTP transport domain using fully qualified domain\nnames. The corresponding transport address is of type\nTransportAddressDns.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("TRANSPORT-ADDRESS-MIB", PYSNMP_MODULE_ID=transportAddressMIB)

# Types
mibBuilder.exportSymbols("TRANSPORT-ADDRESS-MIB", TransportAddress=TransportAddress, TransportAddressDns=TransportAddressDns, TransportAddressIPv4=TransportAddressIPv4, TransportAddressIPv4z=TransportAddressIPv4z, TransportAddressIPv6=TransportAddressIPv6, TransportAddressIPv6z=TransportAddressIPv6z, TransportAddressLocal=TransportAddressLocal, TransportAddressType=TransportAddressType, TransportDomain=TransportDomain)

# Objects
mibBuilder.exportSymbols("TRANSPORT-ADDRESS-MIB", transportAddressMIB=transportAddressMIB, transportDomains=transportDomains, transportDomainUdpIpv4=transportDomainUdpIpv4, transportDomainUdpIpv6=transportDomainUdpIpv6, transportDomainUdpIpv4z=transportDomainUdpIpv4z, transportDomainUdpIpv6z=transportDomainUdpIpv6z, transportDomainTcpIpv4=transportDomainTcpIpv4, transportDomainTcpIpv6=transportDomainTcpIpv6, transportDomainTcpIpv4z=transportDomainTcpIpv4z, transportDomainTcpIpv6z=transportDomainTcpIpv6z, transportDomainSctpIpv4=transportDomainSctpIpv4, transportDomainSctpIpv6=transportDomainSctpIpv6, transportDomainSctpIpv4z=transportDomainSctpIpv4z, transportDomainSctpIpv6z=transportDomainSctpIpv6z, transportDomainLocal=transportDomainLocal, transportDomainUdpDns=transportDomainUdpDns, transportDomainTcpDns=transportDomainTcpDns, transportDomainSctpDns=transportDomainSctpDns)
