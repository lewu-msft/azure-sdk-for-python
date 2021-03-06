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


class ClusterConfigurationUpgradeDescription(Model):
    """Describes the parameters for a standalone cluster configuration upgrade.

    All required parameters must be populated in order to send to Azure.

    :param cluster_config: Required. The cluster configuration.
    :type cluster_config: str
    :param health_check_retry_timeout: The length of time between attempts to
     perform a health checks if the application or cluster is not healthy.
     Default value: "PT0H0M0S" .
    :type health_check_retry_timeout: timedelta
    :param health_check_wait_duration_in_seconds: The length of time to wait
     after completing an upgrade domain before starting the health checks
     process. Default value: "PT0H0M0S" .
    :type health_check_wait_duration_in_seconds: timedelta
    :param health_check_stable_duration_in_seconds: The length of time that
     the application or cluster must remain healthy. Default value: "PT0H0M0S"
     .
    :type health_check_stable_duration_in_seconds: timedelta
    :param upgrade_domain_timeout_in_seconds: The timeout for the upgrade
     domain. Default value: "PT0H0M0S" .
    :type upgrade_domain_timeout_in_seconds: timedelta
    :param upgrade_timeout_in_seconds: The upgrade timeout. Default value:
     "PT0H0M0S" .
    :type upgrade_timeout_in_seconds: timedelta
    :param max_percent_unhealthy_applications: The maximum allowed percentage
     of unhealthy applications during the upgrade. Allowed values are integer
     values from zero to 100. Default value: 0 .
    :type max_percent_unhealthy_applications: int
    :param max_percent_unhealthy_nodes: The maximum allowed percentage of
     unhealthy nodes during the upgrade. Allowed values are integer values from
     zero to 100. Default value: 0 .
    :type max_percent_unhealthy_nodes: int
    :param max_percent_delta_unhealthy_nodes: The maximum allowed percentage
     of delta health degradation during the upgrade. Allowed values are integer
     values from zero to 100. Default value: 0 .
    :type max_percent_delta_unhealthy_nodes: int
    :param max_percent_upgrade_domain_delta_unhealthy_nodes: The maximum
     allowed percentage of upgrade domain delta health degradation during the
     upgrade. Allowed values are integer values from zero to 100. Default
     value: 0 .
    :type max_percent_upgrade_domain_delta_unhealthy_nodes: int
    """

    _validation = {
        'cluster_config': {'required': True},
    }

    _attribute_map = {
        'cluster_config': {'key': 'ClusterConfig', 'type': 'str'},
        'health_check_retry_timeout': {'key': 'HealthCheckRetryTimeout', 'type': 'duration'},
        'health_check_wait_duration_in_seconds': {'key': 'HealthCheckWaitDurationInSeconds', 'type': 'duration'},
        'health_check_stable_duration_in_seconds': {'key': 'HealthCheckStableDurationInSeconds', 'type': 'duration'},
        'upgrade_domain_timeout_in_seconds': {'key': 'UpgradeDomainTimeoutInSeconds', 'type': 'duration'},
        'upgrade_timeout_in_seconds': {'key': 'UpgradeTimeoutInSeconds', 'type': 'duration'},
        'max_percent_unhealthy_applications': {'key': 'MaxPercentUnhealthyApplications', 'type': 'int'},
        'max_percent_unhealthy_nodes': {'key': 'MaxPercentUnhealthyNodes', 'type': 'int'},
        'max_percent_delta_unhealthy_nodes': {'key': 'MaxPercentDeltaUnhealthyNodes', 'type': 'int'},
        'max_percent_upgrade_domain_delta_unhealthy_nodes': {'key': 'MaxPercentUpgradeDomainDeltaUnhealthyNodes', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ClusterConfigurationUpgradeDescription, self).__init__(**kwargs)
        self.cluster_config = kwargs.get('cluster_config', None)
        self.health_check_retry_timeout = kwargs.get('health_check_retry_timeout', "PT0H0M0S")
        self.health_check_wait_duration_in_seconds = kwargs.get('health_check_wait_duration_in_seconds', "PT0H0M0S")
        self.health_check_stable_duration_in_seconds = kwargs.get('health_check_stable_duration_in_seconds', "PT0H0M0S")
        self.upgrade_domain_timeout_in_seconds = kwargs.get('upgrade_domain_timeout_in_seconds', "PT0H0M0S")
        self.upgrade_timeout_in_seconds = kwargs.get('upgrade_timeout_in_seconds', "PT0H0M0S")
        self.max_percent_unhealthy_applications = kwargs.get('max_percent_unhealthy_applications', 0)
        self.max_percent_unhealthy_nodes = kwargs.get('max_percent_unhealthy_nodes', 0)
        self.max_percent_delta_unhealthy_nodes = kwargs.get('max_percent_delta_unhealthy_nodes', 0)
        self.max_percent_upgrade_domain_delta_unhealthy_nodes = kwargs.get('max_percent_upgrade_domain_delta_unhealthy_nodes', 0)
