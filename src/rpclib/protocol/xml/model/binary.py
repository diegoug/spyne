
#
# rpclib - Copyright (C) Rpclib contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

import logging
logger = logging.getLogger(__name__)

import base64

from lxml import etree

from rpclib.model.binary import Attachment

from _base import nillable_value
from _base import nillable_element

@nillable_value
def to_parent_element(cls, value, tns, parent_elt, name='retval'):
    '''This class method takes the data from the attachment and
    base64 encodes it as the text of an Element. An attachment can
    specify a file_name and if no data is given, it will read the data
    from the file
    '''

    element = etree.SubElement(parent_elt, '{%s}%s' % (tns,name))
    element.text = base64.encodestring(cls.to_string(value))

@nillable_element
def from_xml(cls, element):
    '''This method returns an Attachment object that contains
    the base64 decoded string of the text of the given element
    '''
    data = base64.decodestring(element.text)
    a = Attachment(data=data)
    return a

