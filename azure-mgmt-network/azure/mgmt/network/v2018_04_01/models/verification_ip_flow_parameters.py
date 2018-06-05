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


class VerificationIPFlowParameters(Model):
    """Parameters that define the IP flow to be verified.

    All required parameters must be populated in order to send to Azure.

    :param target_resource_id: Required. The ID of the target resource to
     perform next-hop on.
    :type target_resource_id: str
    :param direction: Required. The direction of the packet represented as a
     5-tuple. Possible values include: 'Inbound', 'Outbound'
    :type direction: str or ~azure.mgmt.network.v2018_04_01.models.Direction
    :param protocol: Required. Protocol to be verified on. Possible values
     include: 'TCP', 'UDP'
    :type protocol: str or
     ~azure.mgmt.network.v2018_04_01.models.IpFlowProtocol
    :param local_port: Required. The local port. Acceptable values are a
     single integer in the range (0-65535). Support for * for the source port,
     which depends on the direction.
    :type local_port: str
    :param remote_port: Required. The remote port. Acceptable values are a
     single integer in the range (0-65535). Support for * for the source port,
     which depends on the direction.
    :type remote_port: str
    :param local_ip_address: Required. The local IP address. Acceptable values
     are valid IPv4 addresses.
    :type local_ip_address: str
    :param remote_ip_address: Required. The remote IP address. Acceptable
     values are valid IPv4 addresses.
    :type remote_ip_address: str
    :param target_nic_resource_id: The NIC ID. (If VM has multiple NICs and IP
     forwarding is enabled on any of them, then this parameter must be
     specified. Otherwise optional).
    :type target_nic_resource_id: str
    """

    _validation = {
        'target_resource_id': {'required': True},
        'direction': {'required': True},
        'protocol': {'required': True},
        'local_port': {'required': True},
        'remote_port': {'required': True},
        'local_ip_address': {'required': True},
        'remote_ip_address': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
        'local_port': {'key': 'localPort', 'type': 'str'},
        'remote_port': {'key': 'remotePort', 'type': 'str'},
        'local_ip_address': {'key': 'localIPAddress', 'type': 'str'},
        'remote_ip_address': {'key': 'remoteIPAddress', 'type': 'str'},
        'target_nic_resource_id': {'key': 'targetNicResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VerificationIPFlowParameters, self).__init__(**kwargs)
        self.target_resource_id = kwargs.get('target_resource_id', None)
        self.direction = kwargs.get('direction', None)
        self.protocol = kwargs.get('protocol', None)
        self.local_port = kwargs.get('local_port', None)
        self.remote_port = kwargs.get('remote_port', None)
        self.local_ip_address = kwargs.get('local_ip_address', None)
        self.remote_ip_address = kwargs.get('remote_ip_address', None)
        self.target_nic_resource_id = kwargs.get('target_nic_resource_id', None)
