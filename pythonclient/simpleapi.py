# ./simpleapi.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:004fd3f3be0bf1d9b4eef75999a6b3a085798c59
# Generated 2017-09-12 15:15:24.067730 by PyXB version 1.2.6 using Python 3.6.1.final.0
# Namespace http://spring.joe/springdomain.domain

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ba30b2de-97ee-11e7-b8da-c4b301c2109f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://spring.joe/springdomain.domain', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://spring.joe/springdomain.domain}CurrencyType
class CurrencyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 98, 1)
    _Documentation = None
CurrencyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrencyType, enum_prefix=None)
CurrencyType.GBP = CurrencyType._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
CurrencyType.EUR = CurrencyType._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
CurrencyType.PLN = CurrencyType._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
CurrencyType._InitializeFacetMap(CurrencyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CurrencyType', CurrencyType)
_module_typeBindings.CurrencyType = CurrencyType

# Atomic simple type: {http://spring.joe/springdomain.domain}RequestStatus
class RequestStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestStatus')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 106, 1)
    _Documentation = None
RequestStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RequestStatus, enum_prefix=None)
RequestStatus.OK = RequestStatus._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
RequestStatus.ERROR = RequestStatus._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
RequestStatus._InitializeFacetMap(RequestStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RequestStatus', RequestStatus)
_module_typeBindings.RequestStatus = RequestStatus

# Complex type {http://spring.joe/springdomain.domain}AccountDto with content type ELEMENT_ONLY
class AccountDto (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}AccountDto with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccountDto')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domainid', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 18, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}accountType uses Python identifier accountType
    __accountType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountType'), 'accountType', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domainaccountType', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 19, 3), )

    
    accountType = property(__accountType.value, __accountType.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}accountNumber uses Python identifier accountNumber
    __accountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountNumber'), 'accountNumber', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domainaccountNumber', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 20, 3), )

    
    accountNumber = property(__accountNumber.value, __accountNumber.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}customerId uses Python identifier customerId
    __customerId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerId'), 'customerId', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domaincustomerId', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 21, 3), )

    
    customerId = property(__customerId.value, __customerId.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}customerFirstName uses Python identifier customerFirstName
    __customerFirstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerFirstName'), 'customerFirstName', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domaincustomerFirstName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 22, 3), )

    
    customerFirstName = property(__customerFirstName.value, __customerFirstName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}customerLastName uses Python identifier customerLastName
    __customerLastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerLastName'), 'customerLastName', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domaincustomerLastName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 23, 3), )

    
    customerLastName = property(__customerLastName.value, __customerLastName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}customerUserName uses Python identifier customerUserName
    __customerUserName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerUserName'), 'customerUserName', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domaincustomerUserName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 24, 3), )

    
    customerUserName = property(__customerUserName.value, __customerUserName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}customerBirthDate uses Python identifier customerBirthDate
    __customerBirthDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerBirthDate'), 'customerBirthDate', '__httpspring_joespringdomain_domain_AccountDto_httpspring_joespringdomain_domaincustomerBirthDate', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 25, 3), )

    
    customerBirthDate = property(__customerBirthDate.value, __customerBirthDate.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __accountType.name() : __accountType,
        __accountNumber.name() : __accountNumber,
        __customerId.name() : __customerId,
        __customerFirstName.name() : __customerFirstName,
        __customerLastName.name() : __customerLastName,
        __customerUserName.name() : __customerUserName,
        __customerBirthDate.name() : __customerBirthDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AccountDto = AccountDto
Namespace.addCategoryObject('typeBinding', 'AccountDto', AccountDto)


# Complex type {http://spring.joe/springdomain.domain}AccountDtoList with content type ELEMENT_ONLY
class AccountDtoList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}AccountDtoList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccountDtoList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 29, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}accounts uses Python identifier accounts
    __accounts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accounts'), 'accounts', '__httpspring_joespringdomain_domain_AccountDtoList_httpspring_joespringdomain_domainaccounts', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 31, 3), )

    
    accounts = property(__accounts.value, __accounts.set, None, None)

    _ElementMap.update({
        __accounts.name() : __accounts
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AccountDtoList = AccountDtoList
Namespace.addCategoryObject('typeBinding', 'AccountDtoList', AccountDtoList)


# Complex type {http://spring.joe/springdomain.domain}AddressDto with content type ELEMENT_ONLY
class AddressDto (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}AddressDto with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressDto')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domainid', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 37, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}addressType uses Python identifier addressType
    __addressType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addressType'), 'addressType', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domainaddressType', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 38, 3), )

    
    addressType = property(__addressType.value, __addressType.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}primaryAddressLine uses Python identifier primaryAddressLine
    __primaryAddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primaryAddressLine'), 'primaryAddressLine', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domainprimaryAddressLine', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 39, 3), )

    
    primaryAddressLine = property(__primaryAddressLine.value, __primaryAddressLine.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}secondaryAddressLine uses Python identifier secondaryAddressLine
    __secondaryAddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'secondaryAddressLine'), 'secondaryAddressLine', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domainsecondaryAddressLine', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 40, 3), )

    
    secondaryAddressLine = property(__secondaryAddressLine.value, __secondaryAddressLine.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domaincity', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 41, 3), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}stateCode uses Python identifier stateCode
    __stateCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateCode'), 'stateCode', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domainstateCode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 42, 3), )

    
    stateCode = property(__stateCode.value, __stateCode.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}zipCode uses Python identifier zipCode
    __zipCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zipCode'), 'zipCode', '__httpspring_joespringdomain_domain_AddressDto_httpspring_joespringdomain_domainzipCode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 43, 3), )

    
    zipCode = property(__zipCode.value, __zipCode.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __addressType.name() : __addressType,
        __primaryAddressLine.name() : __primaryAddressLine,
        __secondaryAddressLine.name() : __secondaryAddressLine,
        __city.name() : __city,
        __stateCode.name() : __stateCode,
        __zipCode.name() : __zipCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressDto = AddressDto
Namespace.addCategoryObject('typeBinding', 'AddressDto', AddressDto)


# Complex type {http://spring.joe/springdomain.domain}AddressDtoList with content type ELEMENT_ONLY
class AddressDtoList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}AddressDtoList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressDtoList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 47, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}addresses uses Python identifier addresses
    __addresses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addresses'), 'addresses', '__httpspring_joespringdomain_domain_AddressDtoList_httpspring_joespringdomain_domainaddresses', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 49, 3), )

    
    addresses = property(__addresses.value, __addresses.set, None, None)

    _ElementMap.update({
        __addresses.name() : __addresses
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressDtoList = AddressDtoList
Namespace.addCategoryObject('typeBinding', 'AddressDtoList', AddressDtoList)


# Complex type {http://spring.joe/springdomain.domain}CustomerDto with content type ELEMENT_ONLY
class CustomerDto (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}CustomerDto with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerDto')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 53, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpspring_joespringdomain_domain_CustomerDto_httpspring_joespringdomain_domainid', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 55, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httpspring_joespringdomain_domain_CustomerDto_httpspring_joespringdomain_domainfirstName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 56, 3), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httpspring_joespringdomain_domain_CustomerDto_httpspring_joespringdomain_domainlastName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 57, 3), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}userName uses Python identifier userName
    __userName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userName'), 'userName', '__httpspring_joespringdomain_domain_CustomerDto_httpspring_joespringdomain_domainuserName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 58, 3), )

    
    userName = property(__userName.value, __userName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}birthDate uses Python identifier birthDate
    __birthDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'birthDate'), 'birthDate', '__httpspring_joespringdomain_domain_CustomerDto_httpspring_joespringdomain_domainbirthDate', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 59, 3), )

    
    birthDate = property(__birthDate.value, __birthDate.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __userName.name() : __userName,
        __birthDate.name() : __birthDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerDto = CustomerDto
Namespace.addCategoryObject('typeBinding', 'CustomerDto', CustomerDto)


# Complex type {http://spring.joe/springdomain.domain}CustomerDtoList with content type ELEMENT_ONLY
class CustomerDtoList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}CustomerDtoList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerDtoList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 63, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}customers uses Python identifier customers
    __customers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customers'), 'customers', '__httpspring_joespringdomain_domain_CustomerDtoList_httpspring_joespringdomain_domaincustomers', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 65, 3), )

    
    customers = property(__customers.value, __customers.set, None, None)

    _ElementMap.update({
        __customers.name() : __customers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomerDtoList = CustomerDtoList
Namespace.addCategoryObject('typeBinding', 'CustomerDtoList', CustomerDtoList)


# Complex type {http://spring.joe/springdomain.domain}CountryDto with content type ELEMENT_ONLY
class CountryDto (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}CountryDto with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryDto')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 69, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpspring_joespringdomain_domain_CountryDto_httpspring_joespringdomain_domainid', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 71, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpspring_joespringdomain_domain_CountryDto_httpspring_joespringdomain_domainname', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 72, 3), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httpspring_joespringdomain_domain_CountryDto_httpspring_joespringdomain_domaincode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 73, 3), )

    
    code = property(__code.value, __code.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __code.name() : __code
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CountryDto = CountryDto
Namespace.addCategoryObject('typeBinding', 'CountryDto', CountryDto)


# Complex type {http://spring.joe/springdomain.domain}CountryDtoList with content type ELEMENT_ONLY
class CountryDtoList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}CountryDtoList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryDtoList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 77, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}countries uses Python identifier countries
    __countries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countries'), 'countries', '__httpspring_joespringdomain_domain_CountryDtoList_httpspring_joespringdomain_domaincountries', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 79, 3), )

    
    countries = property(__countries.value, __countries.set, None, None)

    _ElementMap.update({
        __countries.name() : __countries
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CountryDtoList = CountryDtoList
Namespace.addCategoryObject('typeBinding', 'CountryDtoList', CountryDtoList)


# Complex type {http://spring.joe/springdomain.domain}StateDto with content type ELEMENT_ONLY
class StateDto (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}StateDto with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StateDto')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 83, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpspring_joespringdomain_domain_StateDto_httpspring_joespringdomain_domainid', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 85, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpspring_joespringdomain_domain_StateDto_httpspring_joespringdomain_domainname', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 86, 3), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httpspring_joespringdomain_domain_StateDto_httpspring_joespringdomain_domaincode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 87, 3), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpspring_joespringdomain_domain_StateDto_httpspring_joespringdomain_domaincountryCode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 88, 3), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __code.name() : __code,
        __countryCode.name() : __countryCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StateDto = StateDto
Namespace.addCategoryObject('typeBinding', 'StateDto', StateDto)


# Complex type {http://spring.joe/springdomain.domain}StateDtoList with content type ELEMENT_ONLY
class StateDtoList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}StateDtoList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StateDtoList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 92, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}states uses Python identifier states
    __states = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'states'), 'states', '__httpspring_joespringdomain_domain_StateDtoList_httpspring_joespringdomain_domainstates', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 94, 3), )

    
    states = property(__states.value, __states.set, None, None)

    _ElementMap.update({
        __states.name() : __states
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StateDtoList = StateDtoList
Namespace.addCategoryObject('typeBinding', 'StateDtoList', StateDtoList)


# Complex type {http://spring.joe/springdomain.domain}ApiFieldError with content type ELEMENT_ONLY
class ApiFieldError (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}ApiFieldError with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ApiFieldError')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 113, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httpspring_joespringdomain_domain_ApiFieldError_httpspring_joespringdomain_domaincode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 115, 3), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'field'), 'field', '__httpspring_joespringdomain_domain_ApiFieldError_httpspring_joespringdomain_domainfield', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 116, 3), )

    
    field = property(__field.value, __field.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'message'), 'message', '__httpspring_joespringdomain_domain_ApiFieldError_httpspring_joespringdomain_domainmessage', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 117, 3), )

    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __field.name() : __field,
        __message.name() : __message
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ApiFieldError = ApiFieldError
Namespace.addCategoryObject('typeBinding', 'ApiFieldError', ApiFieldError)


# Complex type {http://spring.joe/springdomain.domain}ApiGlobalError with content type ELEMENT_ONLY
class ApiGlobalError (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spring.joe/springdomain.domain}ApiGlobalError with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ApiGlobalError')
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 121, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httpspring_joespringdomain_domain_ApiGlobalError_httpspring_joespringdomain_domaincode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 123, 3), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'message'), 'message', '__httpspring_joespringdomain_domain_ApiGlobalError_httpspring_joespringdomain_domainmessage', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 124, 3), )

    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __message.name() : __message
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ApiGlobalError = ApiGlobalError
Namespace.addCategoryObject('typeBinding', 'ApiGlobalError', ApiGlobalError)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}fieldErrors uses Python identifier fieldErrors
    __fieldErrors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fieldErrors'), 'fieldErrors', '__httpspring_joespringdomain_domain_CTD_ANON_httpspring_joespringdomain_domainfieldErrors', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 131, 4), )

    
    fieldErrors = property(__fieldErrors.value, __fieldErrors.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}globalErrors uses Python identifier globalErrors
    __globalErrors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'globalErrors'), 'globalErrors', '__httpspring_joespringdomain_domain_CTD_ANON_httpspring_joespringdomain_domainglobalErrors', True, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 132, 4), )

    
    globalErrors = property(__globalErrors.value, __globalErrors.set, None, None)

    _ElementMap.update({
        __fieldErrors.name() : __fieldErrors,
        __globalErrors.name() : __globalErrors
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 142, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpspring_joespringdomain_domain_CTD_ANON__httpspring_joespringdomain_domaincountryCode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 144, 4), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    _ElementMap.update({
        __countryCode.name() : __countryCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 150, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country'), 'country', '__httpspring_joespringdomain_domain_CTD_ANON_2_httpspring_joespringdomain_domaincountry', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 152, 4), )

    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 158, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}countries uses Python identifier countries
    __countries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countries'), 'countries', '__httpspring_joespringdomain_domain_CTD_ANON_3_httpspring_joespringdomain_domaincountries', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 160, 4), )

    
    countries = property(__countries.value, __countries.set, None, None)

    _ElementMap.update({
        __countries.name() : __countries
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 166, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpspring_joespringdomain_domain_CTD_ANON_4_httpspring_joespringdomain_domaincountryCode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 168, 4), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    _ElementMap.update({
        __countryCode.name() : __countryCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 174, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}stateCode uses Python identifier stateCode
    __stateCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateCode'), 'stateCode', '__httpspring_joespringdomain_domain_CTD_ANON_5_httpspring_joespringdomain_domainstateCode', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 176, 4), )

    
    stateCode = property(__stateCode.value, __stateCode.set, None, None)

    _ElementMap.update({
        __stateCode.name() : __stateCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 182, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__httpspring_joespringdomain_domain_CTD_ANON_6_httpspring_joespringdomain_domainstate', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 184, 4), )

    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        __state.name() : __state
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 190, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}states uses Python identifier states
    __states = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'states'), 'states', '__httpspring_joespringdomain_domain_CTD_ANON_7_httpspring_joespringdomain_domainstates', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 192, 4), )

    
    states = property(__states.value, __states.set, None, None)

    _ElementMap.update({
        __states.name() : __states
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 206, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httpspring_joespringdomain_domain_CTD_ANON_8_httpspring_joespringdomain_domainfirstName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 208, 4), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httpspring_joespringdomain_domain_CTD_ANON_8_httpspring_joespringdomain_domainlastName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 209, 4), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}userName uses Python identifier userName
    __userName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userName'), 'userName', '__httpspring_joespringdomain_domain_CTD_ANON_8_httpspring_joespringdomain_domainuserName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 210, 4), )

    
    userName = property(__userName.value, __userName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}birthDate uses Python identifier birthDate
    __birthDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'birthDate'), 'birthDate', '__httpspring_joespringdomain_domain_CTD_ANON_8_httpspring_joespringdomain_domainbirthDate', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 211, 4), )

    
    birthDate = property(__birthDate.value, __birthDate.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}password uses Python identifier password
    __password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'password'), 'password', '__httpspring_joespringdomain_domain_CTD_ANON_8_httpspring_joespringdomain_domainpassword', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 212, 4), )

    
    password = property(__password.value, __password.set, None, None)

    _ElementMap.update({
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __userName.name() : __userName,
        __birthDate.name() : __birthDate,
        __password.name() : __password
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 218, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpspring_joespringdomain_domain_CTD_ANON_9_httpspring_joespringdomain_domainid', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 220, 4), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}includeAddresses uses Python identifier includeAddresses
    __includeAddresses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeAddresses'), 'includeAddresses', '__httpspring_joespringdomain_domain_CTD_ANON_9_httpspring_joespringdomain_domainincludeAddresses', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 221, 4), )

    
    includeAddresses = property(__includeAddresses.value, __includeAddresses.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __includeAddresses.name() : __includeAddresses
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 227, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}userName uses Python identifier userName
    __userName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userName'), 'userName', '__httpspring_joespringdomain_domain_CTD_ANON_10_httpspring_joespringdomain_domainuserName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 229, 4), )

    
    userName = property(__userName.value, __userName.set, None, None)

    
    # Element {http://spring.joe/springdomain.domain}includeAddresses uses Python identifier includeAddresses
    __includeAddresses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeAddresses'), 'includeAddresses', '__httpspring_joespringdomain_domain_CTD_ANON_10_httpspring_joespringdomain_domainincludeAddresses', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 230, 4), )

    
    includeAddresses = property(__includeAddresses.value, __includeAddresses.set, None, None)

    _ElementMap.update({
        __userName.name() : __userName,
        __includeAddresses.name() : __includeAddresses
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 236, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}customer uses Python identifier customer
    __customer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customer'), 'customer', '__httpspring_joespringdomain_domain_CTD_ANON_11_httpspring_joespringdomain_domaincustomer', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 238, 4), )

    
    customer = property(__customer.value, __customer.set, None, None)

    _ElementMap.update({
        __customer.name() : __customer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 244, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}customers uses Python identifier customers
    __customers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customers'), 'customers', '__httpspring_joespringdomain_domain_CTD_ANON_12_httpspring_joespringdomain_domaincustomers', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 246, 4), )

    
    customers = property(__customers.value, __customers.set, None, None)

    _ElementMap.update({
        __customers.name() : __customers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 252, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}searchTerm uses Python identifier searchTerm
    __searchTerm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searchTerm'), 'searchTerm', '__httpspring_joespringdomain_domain_CTD_ANON_13_httpspring_joespringdomain_domainsearchTerm', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 254, 4), )

    
    searchTerm = property(__searchTerm.value, __searchTerm.set, None, None)

    _ElementMap.update({
        __searchTerm.name() : __searchTerm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 260, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}userName uses Python identifier userName
    __userName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userName'), 'userName', '__httpspring_joespringdomain_domain_CTD_ANON_14_httpspring_joespringdomain_domainuserName', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 262, 4), )

    
    userName = property(__userName.value, __userName.set, None, None)

    _ElementMap.update({
        __userName.name() : __userName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 268, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpspring_joespringdomain_domain_CTD_ANON_15_httpspring_joespringdomain_domainstatus', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 270, 4), )

    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __status.name() : __status
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 276, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spring.joe/springdomain.domain}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpspring_joespringdomain_domain_CTD_ANON_16_httpspring_joespringdomain_domainstatus', False, pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 278, 4), )

    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __status.name() : __status
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


ErrorResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ErrorResponse'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 128, 1))
Namespace.addCategoryObject('elementBinding', ErrorResponse.name().localName(), ErrorResponse)

CountryByCodeRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountryByCodeRequest'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 141, 1))
Namespace.addCategoryObject('elementBinding', CountryByCodeRequest.name().localName(), CountryByCodeRequest)

CountryResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountryResponse'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 149, 1))
Namespace.addCategoryObject('elementBinding', CountryResponse.name().localName(), CountryResponse)

CountriesResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountriesResponse'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 157, 1))
Namespace.addCategoryObject('elementBinding', CountriesResponse.name().localName(), CountriesResponse)

StatesByCountryRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StatesByCountryRequest'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 165, 1))
Namespace.addCategoryObject('elementBinding', StatesByCountryRequest.name().localName(), StatesByCountryRequest)

StateByCodeRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StateByCodeRequest'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 173, 1))
Namespace.addCategoryObject('elementBinding', StateByCodeRequest.name().localName(), StateByCodeRequest)

StateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StateResponse'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 181, 1))
Namespace.addCategoryObject('elementBinding', StateResponse.name().localName(), StateResponse)

StatesResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StatesResponse'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 189, 1))
Namespace.addCategoryObject('elementBinding', StatesResponse.name().localName(), StatesResponse)

CreateCustomerRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreateCustomerRequest'), CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 205, 1))
Namespace.addCategoryObject('elementBinding', CreateCustomerRequest.name().localName(), CreateCustomerRequest)

GetCustomerByIdRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCustomerByIdRequest'), CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 217, 1))
Namespace.addCategoryObject('elementBinding', GetCustomerByIdRequest.name().localName(), GetCustomerByIdRequest)

GetCustomerByUserNameRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCustomerByUserNameRequest'), CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 226, 1))
Namespace.addCategoryObject('elementBinding', GetCustomerByUserNameRequest.name().localName(), GetCustomerByUserNameRequest)

CustomerResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CustomerResponse'), CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 235, 1))
Namespace.addCategoryObject('elementBinding', CustomerResponse.name().localName(), CustomerResponse)

CustomersResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CustomersResponse'), CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 243, 1))
Namespace.addCategoryObject('elementBinding', CustomersResponse.name().localName(), CustomersResponse)

CustomerSearchRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CustomerSearchRequest'), CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 251, 1))
Namespace.addCategoryObject('elementBinding', CustomerSearchRequest.name().localName(), CustomerSearchRequest)

DeleteCustomerRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeleteCustomerRequest'), CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 259, 1))
Namespace.addCategoryObject('elementBinding', DeleteCustomerRequest.name().localName(), DeleteCustomerRequest)

DeleteCustomerResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeleteCustomerResponse'), CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 267, 1))
Namespace.addCategoryObject('elementBinding', DeleteCustomerResponse.name().localName(), DeleteCustomerResponse)

DeleteAllCustomersResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeleteAllCustomersResponse'), CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 275, 1))
Namespace.addCategoryObject('elementBinding', DeleteAllCustomersResponse.name().localName(), DeleteAllCustomersResponse)



AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.long, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 18, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountType'), pyxb.binding.datatypes.string, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 19, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountNumber'), pyxb.binding.datatypes.string, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 20, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerId'), pyxb.binding.datatypes.long, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 21, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerFirstName'), pyxb.binding.datatypes.string, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 22, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerLastName'), pyxb.binding.datatypes.string, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 23, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerUserName'), pyxb.binding.datatypes.string, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 24, 3)))

AccountDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerBirthDate'), pyxb.binding.datatypes.date, scope=AccountDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 25, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 18, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountType')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountNumber')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 20, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerId')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 21, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerFirstName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 22, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerLastName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 23, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerUserName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 24, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccountDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerBirthDate')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 25, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AccountDto._Automaton = _BuildAutomaton()




AccountDtoList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accounts'), AccountDto, scope=AccountDtoList, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 31, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 31, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AccountDtoList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accounts')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AccountDtoList._Automaton = _BuildAutomaton_()




AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.long, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 37, 3)))

AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addressType'), pyxb.binding.datatypes.string, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 38, 3)))

AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryAddressLine'), pyxb.binding.datatypes.string, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 39, 3)))

AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'secondaryAddressLine'), pyxb.binding.datatypes.string, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 40, 3)))

AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 41, 3)))

AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateCode'), pyxb.binding.datatypes.string, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 42, 3)))

AddressDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zipCode'), pyxb.binding.datatypes.string, scope=AddressDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 43, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 37, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addressType')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryAddressLine')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 39, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'secondaryAddressLine')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 40, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 41, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateCode')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 42, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zipCode')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 43, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddressDto._Automaton = _BuildAutomaton_2()




AddressDtoList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addresses'), AddressDto, scope=AddressDtoList, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 49, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 49, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddressDtoList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addresses')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AddressDtoList._Automaton = _BuildAutomaton_3()




CustomerDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.long, scope=CustomerDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 55, 3)))

CustomerDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), pyxb.binding.datatypes.string, scope=CustomerDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 56, 3)))

CustomerDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), pyxb.binding.datatypes.string, scope=CustomerDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 57, 3)))

CustomerDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userName'), pyxb.binding.datatypes.string, scope=CustomerDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 58, 3)))

CustomerDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'birthDate'), pyxb.binding.datatypes.date, scope=CustomerDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 59, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CustomerDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CustomerDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CustomerDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CustomerDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 58, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CustomerDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'birthDate')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 59, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CustomerDto._Automaton = _BuildAutomaton_4()




CustomerDtoList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customers'), CustomerDto, scope=CustomerDtoList, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 65, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 65, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CustomerDtoList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customers')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 65, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CustomerDtoList._Automaton = _BuildAutomaton_5()




CountryDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.long, scope=CountryDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 71, 3)))

CountryDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=CountryDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 72, 3)))

CountryDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), pyxb.binding.datatypes.string, scope=CountryDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 73, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CountryDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CountryDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 72, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CountryDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 73, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CountryDto._Automaton = _BuildAutomaton_6()




CountryDtoList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countries'), CountryDto, scope=CountryDtoList, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 79, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 79, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CountryDtoList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countries')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 79, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CountryDtoList._Automaton = _BuildAutomaton_7()




StateDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.long, scope=StateDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 85, 3)))

StateDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=StateDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 86, 3)))

StateDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), pyxb.binding.datatypes.string, scope=StateDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 87, 3)))

StateDto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), pyxb.binding.datatypes.string, scope=StateDto, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 88, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StateDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 85, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StateDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 86, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StateDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 87, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StateDto._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 88, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StateDto._Automaton = _BuildAutomaton_8()




StateDtoList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'states'), StateDto, scope=StateDtoList, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 94, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 94, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StateDtoList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'states')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 94, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StateDtoList._Automaton = _BuildAutomaton_9()




ApiFieldError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), pyxb.binding.datatypes.string, scope=ApiFieldError, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 115, 3)))

ApiFieldError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field'), pyxb.binding.datatypes.string, scope=ApiFieldError, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 116, 3)))

ApiFieldError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), pyxb.binding.datatypes.string, scope=ApiFieldError, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 117, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApiFieldError._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 115, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApiFieldError._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'field')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 116, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ApiFieldError._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 117, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ApiFieldError._Automaton = _BuildAutomaton_10()




ApiGlobalError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), pyxb.binding.datatypes.string, scope=ApiGlobalError, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 123, 3)))

ApiGlobalError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), pyxb.binding.datatypes.string, scope=ApiGlobalError, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 124, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApiGlobalError._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 123, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ApiGlobalError._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 124, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ApiGlobalError._Automaton = _BuildAutomaton_11()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fieldErrors'), ApiFieldError, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 131, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'globalErrors'), ApiGlobalError, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 132, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 131, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 132, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fieldErrors')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 131, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'globalErrors')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 132, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_12()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 144, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 144, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_13()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country'), CountryDto, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 152, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 152, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_14()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countries'), CountryDtoList, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 160, 4)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countries')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 160, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_15()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 168, 4)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 168, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_16()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 176, 4)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateCode')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 176, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_17()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), StateDto, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 184, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 184, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_18()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'states'), StateDtoList, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 192, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'states')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 192, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_19()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 208, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 209, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userName'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 210, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'birthDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 211, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'password'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 212, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 208, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 209, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 210, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'birthDate')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 211, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'password')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 212, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_20()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.long, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 220, 4)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeAddresses'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 221, 4), unicode_default='false'))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 220, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeAddresses')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 221, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_21()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userName'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 229, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeAddresses'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 230, 4), unicode_default='false'))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 229, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeAddresses')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 230, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_22()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customer'), CustomerDto, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 238, 4)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customer')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 238, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_23()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customers'), CustomerDtoList, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 246, 4)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customers')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 246, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_24()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchTerm'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 254, 4)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searchTerm')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 254, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_25()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userName'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 262, 4)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userName')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 262, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_26()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), RequestStatus, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 270, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 270, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_27()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), RequestStatus, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 278, 4)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/Users/joseph_sicree/Documents/Development/Java-Spring-Demo/domain.xsd', 278, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_28()

