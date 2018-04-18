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


class UnmanagedFileSystemReference(Model):
    """Details of the file system to mount on the compute cluster nodes.

    All required parameters must be populated in order to send to Azure.

    :param mount_command: Required. Command used to mount the unmanaged file
     system.
    :type mount_command: str
    :param relative_mount_path: Required. Specifies the relative path on the
     compute cluster node where the file system will be mounted. Note that all
     cluster level unmanaged file system will be mounted under
     $AZ_BATCHAI_MOUNT_ROOT location and job level unmanaged file system will
     be mounted under $AZ_BATCHAI_JOB_MOUNT_ROOT.
    :type relative_mount_path: str
    """

    _validation = {
        'mount_command': {'required': True},
        'relative_mount_path': {'required': True},
    }

    _attribute_map = {
        'mount_command': {'key': 'mountCommand', 'type': 'str'},
        'relative_mount_path': {'key': 'relativeMountPath', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UnmanagedFileSystemReference, self).__init__(**kwargs)
        self.mount_command = kwargs.get('mount_command', None)
        self.relative_mount_path = kwargs.get('relative_mount_path', None)
