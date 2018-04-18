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


class Job(Resource):
    """Contains information about the job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :ivar location: The location of the resource
    :vartype location: str
    :ivar tags: The tags of the resource
    :vartype tags: dict[str, str]
    :param experiment_name: Describe the experiment information of the job
    :type experiment_name: str
    :param priority: Priority associated with the job. Priority associated
     with the job. Priority values can range from -1000 to 1000, with -1000
     being the lowest priority and 1000 being the highest priority. The default
     value is 0. Default value: 0 .
    :type priority: int
    :param cluster: Specifies the Id of the cluster on which this job will
     run.
    :type cluster: ~azure.mgmt.batchai.models.ResourceId
    :param mount_volumes: Information on mount volumes to be used by the job.
     These volumes will be mounted before the job execution and will be
     unmouted after the job completion. The volumes will be mounted at location
     specified by $AZ_BATCHAI_JOB_MOUNT_ROOT environment variable.
    :type mount_volumes: ~azure.mgmt.batchai.models.MountVolumes
    :param job_output_directory_path_segment: A segment of job's output
     directories path created by BatchAI. Batch AI creates job's output
     directories under an unique path to avoid conflicts between jobs. This
     value contains a path segment generated by Batch AI to make the path
     unique and can be used to find the output directory on the node or mounted
     filesystem.
    :type job_output_directory_path_segment: str
    :param node_count: Number of compute nodes to run the job on. The job will
     be gang scheduled on that many compute nodes
    :type node_count: int
    :param container_settings: If provided the job will run in the specified
     container. If the container was downloaded as part of cluster setup then
     the same container image will be used. If not provided, the job will run
     on the VM.
    :type container_settings: ~azure.mgmt.batchai.models.ContainerSettings
    :param tool_type: The toolkit type of this job. Possible values are: cntk,
     tensorflow, caffe, caffe2, chainer, pytorch, custom. Possible values
     include: 'cntk', 'tensorflow', 'caffe', 'caffe2', 'chainer', 'custom'
    :type tool_type: str or ~azure.mgmt.batchai.models.ToolType
    :param cntk_settings: Specifies the settings for CNTK (aka Microsoft
     Cognitive Toolkit) job.
    :type cntk_settings: ~azure.mgmt.batchai.models.CNTKsettings
    :param py_torch_settings: Specifies the settings for pyTorch job.
    :type py_torch_settings: ~azure.mgmt.batchai.models.PyTorchSettings
    :param tensor_flow_settings: Specifies the settings for Tensor Flow job.
    :type tensor_flow_settings: ~azure.mgmt.batchai.models.TensorFlowSettings
    :param caffe_settings: Specifies the settings for Caffe job.
    :type caffe_settings: ~azure.mgmt.batchai.models.CaffeSettings
    :param chainer_settings: Specifies the settings for Chainer job.
    :type chainer_settings: ~azure.mgmt.batchai.models.ChainerSettings
    :param custom_toolkit_settings: Specifies the settings for custom tool kit
     job.
    :type custom_toolkit_settings:
     ~azure.mgmt.batchai.models.CustomToolkitSettings
    :param job_preparation: Specifies the actions to be performed before tool
     kit is launched. The specified actions will run on all the nodes that are
     part of the job
    :type job_preparation: ~azure.mgmt.batchai.models.JobPreparation
    :param std_out_err_path_prefix: The path where the Batch AI service will
     upload stdout and stderror of the job.
    :type std_out_err_path_prefix: str
    :param input_directories: Specifies the list of input directories for the
     Job.
    :type input_directories: list[~azure.mgmt.batchai.models.InputDirectory]
    :param output_directories: Specifies the list of output directories where
     the models will be created.
    :type output_directories: list[~azure.mgmt.batchai.models.OutputDirectory]
    :param environment_variables: Additional environment variables to set on
     the job. Batch AI will setup these additional environment variables for
     the job.
    :type environment_variables:
     list[~azure.mgmt.batchai.models.EnvironmentVariable]
    :param secrets: Additional environment variables with secret values to set
     on the job. Batch AI will setup these additional environment variables for
     the job. Server will never report values of these variables back.
    :type secrets:
     list[~azure.mgmt.batchai.models.EnvironmentVariableWithSecretValue]
    :param constraints: Constraints associated with the Job.
    :type constraints: ~azure.mgmt.batchai.models.JobPropertiesConstraints
    :ivar creation_time: The job creation time. The creation time of the job.
    :vartype creation_time: datetime
    :ivar provisioning_state: The provisioned state of the Batch AI job.
     Possible values include: 'creating', 'succeeded', 'failed', 'deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.batchai.models.ProvisioningState
    :ivar provisioning_state_transition_time: The time at which the job
     entered its current provisioning state. The time at which the job entered
     its current provisioning state.
    :vartype provisioning_state_transition_time: datetime
    :param execution_state: The current state of the job. The current state of
     the job. Possible values are: queued - The job is queued and able to run.
     A job enters this state when it is created, or when it is awaiting a retry
     after a failed run. running - The job is running on a compute cluster.
     This includes job-level preparation such as downloading resource files or
     set up container specified on the job - it does not necessarily mean that
     the job command line has started executing. terminating - The job is
     terminated by the user, the terminate operation is in progress. succeeded
     - The job has completed running succesfully and exited with exit code 0.
     failed - The job has finished unsuccessfully (failed with a non-zero exit
     code) and has exhausted its retry limit. A job is also marked as failed if
     an error occurred launching the job. Possible values include: 'queued',
     'running', 'terminating', 'succeeded', 'failed'
    :type execution_state: str or ~azure.mgmt.batchai.models.ExecutionState
    :ivar execution_state_transition_time: The time at which the job entered
     its current execution state. The time at which the job entered its current
     execution state.
    :vartype execution_state_transition_time: datetime
    :param execution_info: Contains information about the execution of a job
     in the Azure Batch service.
    :type execution_info:
     ~azure.mgmt.batchai.models.JobPropertiesExecutionInfo
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'creation_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'provisioning_state_transition_time': {'readonly': True},
        'execution_state_transition_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'experiment_name': {'key': 'properties.experimentName', 'type': 'str'},
        'priority': {'key': 'properties.priority', 'type': 'int'},
        'cluster': {'key': 'properties.cluster', 'type': 'ResourceId'},
        'mount_volumes': {'key': 'properties.mountVolumes', 'type': 'MountVolumes'},
        'job_output_directory_path_segment': {'key': 'properties.jobOutputDirectoryPathSegment', 'type': 'str'},
        'node_count': {'key': 'properties.nodeCount', 'type': 'int'},
        'container_settings': {'key': 'properties.containerSettings', 'type': 'ContainerSettings'},
        'tool_type': {'key': 'properties.toolType', 'type': 'str'},
        'cntk_settings': {'key': 'properties.cntkSettings', 'type': 'CNTKsettings'},
        'py_torch_settings': {'key': 'properties.pyTorchSettings', 'type': 'PyTorchSettings'},
        'tensor_flow_settings': {'key': 'properties.tensorFlowSettings', 'type': 'TensorFlowSettings'},
        'caffe_settings': {'key': 'properties.caffeSettings', 'type': 'CaffeSettings'},
        'chainer_settings': {'key': 'properties.chainerSettings', 'type': 'ChainerSettings'},
        'custom_toolkit_settings': {'key': 'properties.customToolkitSettings', 'type': 'CustomToolkitSettings'},
        'job_preparation': {'key': 'properties.jobPreparation', 'type': 'JobPreparation'},
        'std_out_err_path_prefix': {'key': 'properties.stdOutErrPathPrefix', 'type': 'str'},
        'input_directories': {'key': 'properties.inputDirectories', 'type': '[InputDirectory]'},
        'output_directories': {'key': 'properties.outputDirectories', 'type': '[OutputDirectory]'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'secrets': {'key': 'properties.secrets', 'type': '[EnvironmentVariableWithSecretValue]'},
        'constraints': {'key': 'properties.constraints', 'type': 'JobPropertiesConstraints'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'provisioning_state_transition_time': {'key': 'properties.provisioningStateTransitionTime', 'type': 'iso-8601'},
        'execution_state': {'key': 'properties.executionState', 'type': 'ExecutionState'},
        'execution_state_transition_time': {'key': 'properties.executionStateTransitionTime', 'type': 'iso-8601'},
        'execution_info': {'key': 'properties.executionInfo', 'type': 'JobPropertiesExecutionInfo'},
    }

    def __init__(self, **kwargs):
        super(Job, self).__init__(**kwargs)
        self.experiment_name = kwargs.get('experiment_name', None)
        self.priority = kwargs.get('priority', 0)
        self.cluster = kwargs.get('cluster', None)
        self.mount_volumes = kwargs.get('mount_volumes', None)
        self.job_output_directory_path_segment = kwargs.get('job_output_directory_path_segment', None)
        self.node_count = kwargs.get('node_count', None)
        self.container_settings = kwargs.get('container_settings', None)
        self.tool_type = kwargs.get('tool_type', None)
        self.cntk_settings = kwargs.get('cntk_settings', None)
        self.py_torch_settings = kwargs.get('py_torch_settings', None)
        self.tensor_flow_settings = kwargs.get('tensor_flow_settings', None)
        self.caffe_settings = kwargs.get('caffe_settings', None)
        self.chainer_settings = kwargs.get('chainer_settings', None)
        self.custom_toolkit_settings = kwargs.get('custom_toolkit_settings', None)
        self.job_preparation = kwargs.get('job_preparation', None)
        self.std_out_err_path_prefix = kwargs.get('std_out_err_path_prefix', None)
        self.input_directories = kwargs.get('input_directories', None)
        self.output_directories = kwargs.get('output_directories', None)
        self.environment_variables = kwargs.get('environment_variables', None)
        self.secrets = kwargs.get('secrets', None)
        self.constraints = kwargs.get('constraints', None)
        self.creation_time = None
        self.provisioning_state = None
        self.provisioning_state_transition_time = None
        self.execution_state = kwargs.get('execution_state', None)
        self.execution_state_transition_time = None
        self.execution_info = kwargs.get('execution_info', None)
