# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class IotHubDescription(Resource):
    """The description of the IoT hub.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param etag: The Etag field is *not* required. If it is provided in the
     response body, it must also be provided as a header per the normal ETag
     convention.
    :type etag: str
    :param properties: IotHub properties
    :type properties: ~azure.mgmt.iothub.models.IotHubProperties
    :param sku: Required. IotHub SKU info
    :type sku: ~azure.mgmt.iothub.models.IotHubSkuInfo
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'IotHubProperties'},
        'sku': {'key': 'sku', 'type': 'IotHubSkuInfo'},
    }

    def __init__(self, *, location: str, sku, tags=None, etag: str=None, properties=None, **kwargs) -> None:
        super(IotHubDescription, self).__init__(location=location, tags=tags, **kwargs)
        self.etag = etag
        self.properties = properties
        self.sku = sku
