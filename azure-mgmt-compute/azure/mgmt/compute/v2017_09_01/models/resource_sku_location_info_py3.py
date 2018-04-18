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

from msrest.serialization import Model


class ResourceSkuLocationInfo(Model):
    """ResourceSkuLocationInfo.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar location: Location of the SKU
    :vartype location: str
    :ivar zones: List of availability zones where the SKU is supported.
    :vartype zones: list[str]
    """

    _validation = {
        'location': {'readonly': True},
        'zones': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ResourceSkuLocationInfo, self).__init__(**kwargs)
        self.location = None
        self.zones = None
