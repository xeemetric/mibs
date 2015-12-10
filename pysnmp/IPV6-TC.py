# PySNMP SMI module. Autogenerated from smidump -f python IPV6-TC
# by libsmi2pysnmp-0.1.3 at Tue Dec  8 22:35:21 2015,
# Python version sys.version_info(major=2, minor=7, micro=9, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "MibIdentifier", "TimeTicks")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class Ipv6Address(TextualConvention, OctetString):
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(16,16)
    fixedLength = 16
    
class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,8)
    
class Ipv6AddressPrefix(TextualConvention, OctetString):
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,16)
    
class Ipv6IfIndex(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,2147483647)
    
class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    

# Exports

# Types
mibBuilder.exportSymbols("IPV6-TC", Ipv6Address=Ipv6Address, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6IfIndex=Ipv6IfIndex, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero)

