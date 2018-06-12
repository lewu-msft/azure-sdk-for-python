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


class OperationsList(Model):
    """OperationsList.

    :param operations: The array of feature operations.
    :type operations:
     list[~azure.mgmt.resource.features.v2015_12_01.models.OperationDefinition]
    """

    _attribute_map = {
        'operations': {'key': 'operations', 'type': '[OperationDefinition]'},
    }

    def __init__(self, **kwargs):
        super(OperationsList, self).__init__(**kwargs)
        self.operations = kwargs.get('operations', None)
