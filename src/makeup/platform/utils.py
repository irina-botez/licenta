from zope.interface import Invalid
from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.CMFDefault.utils import checkEmailAddress
from makeup.platform import _


def check_phone(value):
    """Romania phone number validation"""

    if len(value) < 10 or not value.isdigit():
        raise Invalid(_(u"Invalid phone number"))
    return True

def validate_email(email):
    """Email adress validation"""
    try:
        checkEmailAddress(email)
    except EmailAddressInvalid:
        raise EmailAddressInvalid(email)
    return True
