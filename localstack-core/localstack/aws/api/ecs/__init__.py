from datetime import datetime
from enum import StrEnum
from typing import IO, TypedDict
from collections.abc import Iterable, Iterator

from localstack.aws.api import handler, RequestContext, ServiceException, ServiceRequest
AllowedInstanceType = str
Boolean = bool
BoxedBoolean = bool
BoxedDouble = float
BoxedInteger = int
CapacityProviderStrategyItemBase = int
CapacityProviderStrategyItemWeight = int
Double = float
Duration = int
EBSKMSKeyId = str
EBSSnapshotId = str
EBSVolumeType = str
ECSVolumeName = str
ExcludedInstanceType = str
IAMRoleArn = str
Integer = int
ManagedScalingInstanceWarmupPeriod = int
ManagedScalingStepSize = int
ManagedScalingTargetCapacity = int
PortNumber = int
SensitiveString = str
String = str
TagKey = str
TagValue = str
TaskVolumeStorageGiB = int
class AcceleratorManufacturer(StrEnum):
    amazon_web_services = "amazon-web-services"
    amd = "amd"
    nvidia = "nvidia"
    xilinx = "xilinx"
    habana = "habana"

class AcceleratorName(StrEnum):
    a100 = "a100"
    inferentia = "inferentia"
    k520 = "k520"
    k80 = "k80"
    m60 = "m60"
    radeon_pro_v520 = "radeon-pro-v520"
    t4 = "t4"
    vu9p = "vu9p"
    v100 = "v100"
    a10g = "a10g"
    h100 = "h100"
    t4g = "t4g"

class AcceleratorType(StrEnum):
    gpu = "gpu"
    fpga = "fpga"
    inference = "inference"

class AccessType(StrEnum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

class AgentUpdateStatus(StrEnum):
    PENDING = "PENDING"
    STAGING = "STAGING"
    STAGED = "STAGED"
    UPDATING = "UPDATING"
    UPDATED = "UPDATED"
    FAILED = "FAILED"

class ApplicationProtocol(StrEnum):
    http = "http"
    http2 = "http2"
    grpc = "grpc"

class AssignPublicIp(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class AvailabilityZoneRebalancing(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class BareMetal(StrEnum):
    included = "included"
    required = "required"
    excluded = "excluded"

class BurstablePerformance(StrEnum):
    included = "included"
    required = "required"
    excluded = "excluded"

class CPUArchitecture(StrEnum):
    X86_64 = "X86_64"
    ARM64 = "ARM64"

class CapacityOptionType(StrEnum):
    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"
    RESERVED = "RESERVED"

class CapacityProviderField(StrEnum):
    TAGS = "TAGS"

class CapacityProviderStatus(StrEnum):
    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    DEPROVISIONING = "DEPROVISIONING"
    INACTIVE = "INACTIVE"

class CapacityProviderType(StrEnum):
    EC2_AUTOSCALING = "EC2_AUTOSCALING"
    MANAGED_INSTANCES = "MANAGED_INSTANCES"
    FARGATE = "FARGATE"
    FARGATE_SPOT = "FARGATE_SPOT"

class CapacityProviderUpdateStatus(StrEnum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"

class CapacityReservationPreference(StrEnum):
    RESERVATIONS_ONLY = "RESERVATIONS_ONLY"
    RESERVATIONS_FIRST = "RESERVATIONS_FIRST"
    RESERVATIONS_EXCLUDED = "RESERVATIONS_EXCLUDED"

class ClusterField(StrEnum):
    ATTACHMENTS = "ATTACHMENTS"
    CONFIGURATIONS = "CONFIGURATIONS"
    SETTINGS = "SETTINGS"
    STATISTICS = "STATISTICS"
    TAGS = "TAGS"

class ClusterSettingName(StrEnum):
    containerInsights = "containerInsights"

class Compatibility(StrEnum):
    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"
    MANAGED_INSTANCES = "MANAGED_INSTANCES"

class Connectivity(StrEnum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"

class ContainerCondition(StrEnum):
    START = "START"
    COMPLETE = "COMPLETE"
    SUCCESS = "SUCCESS"
    HEALTHY = "HEALTHY"

class ContainerInstanceField(StrEnum):
    TAGS = "TAGS"
    CONTAINER_INSTANCE_HEALTH = "CONTAINER_INSTANCE_HEALTH"

class ContainerInstanceStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"
    REGISTERING = "REGISTERING"
    DEREGISTERING = "DEREGISTERING"
    REGISTRATION_FAILED = "REGISTRATION_FAILED"

class CpuManufacturer(StrEnum):
    intel = "intel"
    amd = "amd"
    amazon_web_services = "amazon-web-services"

class DeploymentControllerType(StrEnum):
    ECS = "ECS"
    CODE_DEPLOY = "CODE_DEPLOY"
    EXTERNAL = "EXTERNAL"

class DeploymentLifecycleHookStage(StrEnum):
    RECONCILE_SERVICE = "RECONCILE_SERVICE"
    PRE_SCALE_UP = "PRE_SCALE_UP"
    POST_SCALE_UP = "POST_SCALE_UP"
    TEST_TRAFFIC_SHIFT = "TEST_TRAFFIC_SHIFT"
    POST_TEST_TRAFFIC_SHIFT = "POST_TEST_TRAFFIC_SHIFT"
    PRODUCTION_TRAFFIC_SHIFT = "PRODUCTION_TRAFFIC_SHIFT"
    POST_PRODUCTION_TRAFFIC_SHIFT = "POST_PRODUCTION_TRAFFIC_SHIFT"

class DeploymentRolloutState(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"

class DeploymentStrategy(StrEnum):
    ROLLING = "ROLLING"
    BLUE_GREEN = "BLUE_GREEN"
    LINEAR = "LINEAR"
    CANARY = "CANARY"

class DesiredStatus(StrEnum):
    RUNNING = "RUNNING"
    PENDING = "PENDING"
    STOPPED = "STOPPED"

class DeviceCgroupPermission(StrEnum):
    read = "read"
    write = "write"
    mknod = "mknod"

class EBSResourceType(StrEnum):
    volume = "volume"

class EFSAuthorizationConfigIAM(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class EFSTransitEncryption(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class EnvironmentFileType(StrEnum):
    s3 = "s3"

class ExecuteCommandLogging(StrEnum):
    NONE = "NONE"
    DEFAULT = "DEFAULT"
    OVERRIDE = "OVERRIDE"

class ExpressGatewayServiceInclude(StrEnum):
    TAGS = "TAGS"

class ExpressGatewayServiceScalingMetric(StrEnum):
    AVERAGE_CPU = "AVERAGE_CPU"
    AVERAGE_MEMORY = "AVERAGE_MEMORY"
    REQUEST_COUNT_PER_TARGET = "REQUEST_COUNT_PER_TARGET"

class ExpressGatewayServiceStatusCode(StrEnum):
    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"
    INACTIVE = "INACTIVE"

class FirelensConfigurationType(StrEnum):
    fluentd = "fluentd"
    fluentbit = "fluentbit"

class HealthStatus(StrEnum):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"

class InstanceGeneration(StrEnum):
    current = "current"
    previous = "previous"

class InstanceHealthCheckState(StrEnum):
    OK = "OK"
    IMPAIRED = "IMPAIRED"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    INITIALIZING = "INITIALIZING"

class InstanceHealthCheckType(StrEnum):
    CONTAINER_RUNTIME = "CONTAINER_RUNTIME"

class IpcMode(StrEnum):
    host = "host"
    task = "task"
    none = "none"

class LaunchType(StrEnum):
    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"
    MANAGED_INSTANCES = "MANAGED_INSTANCES"

class LocalStorage(StrEnum):
    included = "included"
    required = "required"
    excluded = "excluded"

class LocalStorageType(StrEnum):
    hdd = "hdd"
    ssd = "ssd"

class LogDriver(StrEnum):
    json_file = "json-file"
    syslog = "syslog"
    journald = "journald"
    gelf = "gelf"
    fluentd = "fluentd"
    awslogs = "awslogs"
    splunk = "splunk"
    awsfirelens = "awsfirelens"

class ManagedAgentName(StrEnum):
    ExecuteCommandAgent = "ExecuteCommandAgent"

class ManagedDraining(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class ManagedInstancesMonitoringOptions(StrEnum):
    BASIC = "BASIC"
    DETAILED = "DETAILED"

class ManagedResourceStatus(StrEnum):
    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    DEPROVISIONING = "DEPROVISIONING"
    DELETED = "DELETED"
    FAILED = "FAILED"

class ManagedScalingStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class ManagedTerminationProtection(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class NetworkMode(StrEnum):
    bridge = "bridge"
    host = "host"
    awsvpc = "awsvpc"
    none = "none"

class OSFamily(StrEnum):
    WINDOWS_SERVER_2019_FULL = "WINDOWS_SERVER_2019_FULL"
    WINDOWS_SERVER_2019_CORE = "WINDOWS_SERVER_2019_CORE"
    WINDOWS_SERVER_2016_FULL = "WINDOWS_SERVER_2016_FULL"
    WINDOWS_SERVER_2004_CORE = "WINDOWS_SERVER_2004_CORE"
    WINDOWS_SERVER_2022_CORE = "WINDOWS_SERVER_2022_CORE"
    WINDOWS_SERVER_2022_FULL = "WINDOWS_SERVER_2022_FULL"
    WINDOWS_SERVER_2025_CORE = "WINDOWS_SERVER_2025_CORE"
    WINDOWS_SERVER_2025_FULL = "WINDOWS_SERVER_2025_FULL"
    WINDOWS_SERVER_20H2_CORE = "WINDOWS_SERVER_20H2_CORE"
    LINUX = "LINUX"

class PidMode(StrEnum):
    host = "host"
    task = "task"

class PlacementConstraintType(StrEnum):
    distinctInstance = "distinctInstance"
    memberOf = "memberOf"

class PlacementStrategyType(StrEnum):
    random = "random"
    spread = "spread"
    binpack = "binpack"

class PlatformDeviceType(StrEnum):
    GPU = "GPU"

class PropagateMITags(StrEnum):
    CAPACITY_PROVIDER = "CAPACITY_PROVIDER"
    NONE = "NONE"

class PropagateTags(StrEnum):
    TASK_DEFINITION = "TASK_DEFINITION"
    SERVICE = "SERVICE"
    NONE = "NONE"

class ProxyConfigurationType(StrEnum):
    APPMESH = "APPMESH"

class ResourceManagementType(StrEnum):
    CUSTOMER = "CUSTOMER"
    ECS = "ECS"

class ResourceType(StrEnum):
    GPU = "GPU"
    InferenceAccelerator = "InferenceAccelerator"

class ScaleUnit(StrEnum):
    PERCENT = "PERCENT"

class SchedulingStrategy(StrEnum):
    REPLICA = "REPLICA"
    DAEMON = "DAEMON"

class Scope(StrEnum):
    task = "task"
    shared = "shared"

class ServiceConnectAccessLoggingFormat(StrEnum):
    TEXT = "TEXT"
    JSON = "JSON"

class ServiceConnectIncludeQueryParameters(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"

class ServiceDeploymentLifecycleStage(StrEnum):
    RECONCILE_SERVICE = "RECONCILE_SERVICE"
    PRE_SCALE_UP = "PRE_SCALE_UP"
    SCALE_UP = "SCALE_UP"
    POST_SCALE_UP = "POST_SCALE_UP"
    TEST_TRAFFIC_SHIFT = "TEST_TRAFFIC_SHIFT"
    POST_TEST_TRAFFIC_SHIFT = "POST_TEST_TRAFFIC_SHIFT"
    PRODUCTION_TRAFFIC_SHIFT = "PRODUCTION_TRAFFIC_SHIFT"
    POST_PRODUCTION_TRAFFIC_SHIFT = "POST_PRODUCTION_TRAFFIC_SHIFT"
    BAKE_TIME = "BAKE_TIME"
    CLEAN_UP = "CLEAN_UP"

class ServiceDeploymentRollbackMonitorsStatus(StrEnum):
    TRIGGERED = "TRIGGERED"
    MONITORING = "MONITORING"
    MONITORING_COMPLETE = "MONITORING_COMPLETE"
    DISABLED = "DISABLED"

class ServiceDeploymentStatus(StrEnum):
    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"
    STOPPED = "STOPPED"
    STOP_REQUESTED = "STOP_REQUESTED"
    IN_PROGRESS = "IN_PROGRESS"
    ROLLBACK_REQUESTED = "ROLLBACK_REQUESTED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_SUCCESSFUL = "ROLLBACK_SUCCESSFUL"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"

class ServiceField(StrEnum):
    TAGS = "TAGS"

class SettingName(StrEnum):
    serviceLongArnFormat = "serviceLongArnFormat"
    taskLongArnFormat = "taskLongArnFormat"
    containerInstanceLongArnFormat = "containerInstanceLongArnFormat"
    awsvpcTrunking = "awsvpcTrunking"
    containerInsights = "containerInsights"
    fargateFIPSMode = "fargateFIPSMode"
    tagResourceAuthorization = "tagResourceAuthorization"
    fargateTaskRetirementWaitPeriod = "fargateTaskRetirementWaitPeriod"
    guardDutyActivate = "guardDutyActivate"
    defaultLogDriverMode = "defaultLogDriverMode"
    fargateEventWindows = "fargateEventWindows"

class SettingType(StrEnum):
    user = "user"
    aws_managed = "aws_managed"

class SortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"

class StabilityStatus(StrEnum):
    STEADY_STATE = "STEADY_STATE"
    STABILIZING = "STABILIZING"

class StopServiceDeploymentStopType(StrEnum):
    ABORT = "ABORT"
    ROLLBACK = "ROLLBACK"

class TargetType(StrEnum):
    container_instance = "container-instance"

class TaskDefinitionFamilyStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ALL = "ALL"

class TaskDefinitionField(StrEnum):
    TAGS = "TAGS"

class TaskDefinitionPlacementConstraintType(StrEnum):
    memberOf = "memberOf"

class TaskDefinitionStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"

class TaskField(StrEnum):
    TAGS = "TAGS"

class TaskFilesystemType(StrEnum):
    ext3 = "ext3"
    ext4 = "ext4"
    xfs = "xfs"
    ntfs = "ntfs"

class TaskSetField(StrEnum):
    TAGS = "TAGS"

class TaskStopCode(StrEnum):
    TaskFailedToStart = "TaskFailedToStart"
    EssentialContainerExited = "EssentialContainerExited"
    UserInitiated = "UserInitiated"
    ServiceSchedulerInitiated = "ServiceSchedulerInitiated"
    SpotInterruption = "SpotInterruption"
    TerminationNotice = "TerminationNotice"

class TransportProtocol(StrEnum):
    tcp = "tcp"
    udp = "udp"

class UlimitName(StrEnum):
    core = "core"
    cpu = "cpu"
    data = "data"
    fsize = "fsize"
    locks = "locks"
    memlock = "memlock"
    msgqueue = "msgqueue"
    nice = "nice"
    nofile = "nofile"
    nproc = "nproc"
    rss = "rss"
    rtprio = "rtprio"
    rttime = "rttime"
    sigpending = "sigpending"
    stack = "stack"

class VersionConsistency(StrEnum):
    enabled = "enabled"
    disabled = "disabled"

class AccessDeniedException(ServiceException):
    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400

class AttributeLimitExceededException(ServiceException):
    code: str = "AttributeLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400

class BlockedException(ServiceException):
    code: str = "BlockedException"
    sender_fault: bool = False
    status_code: int = 400

class ClientException(ServiceException):
    code: str = "ClientException"
    sender_fault: bool = False
    status_code: int = 400

class ClusterContainsCapacityProviderException(ServiceException):
    code: str = "ClusterContainsCapacityProviderException"
    sender_fault: bool = False
    status_code: int = 400

class ClusterContainsContainerInstancesException(ServiceException):
    code: str = "ClusterContainsContainerInstancesException"
    sender_fault: bool = False
    status_code: int = 400

class ClusterContainsServicesException(ServiceException):
    code: str = "ClusterContainsServicesException"
    sender_fault: bool = False
    status_code: int = 400

class ClusterContainsTasksException(ServiceException):
    code: str = "ClusterContainsTasksException"
    sender_fault: bool = False
    status_code: int = 400

class ClusterNotFoundException(ServiceException):
    code: str = "ClusterNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

ResourceIds = list[String]
class ConflictException(ServiceException):
    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400
    resourceIds: ResourceIds | None

class InvalidParameterException(ServiceException):
    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400

class LimitExceededException(ServiceException):
    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400

class MissingVersionException(ServiceException):
    code: str = "MissingVersionException"
    sender_fault: bool = False
    status_code: int = 400

class NamespaceNotFoundException(ServiceException):
    code: str = "NamespaceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class NoUpdateAvailableException(ServiceException):
    code: str = "NoUpdateAvailableException"
    sender_fault: bool = False
    status_code: int = 400

class PlatformTaskDefinitionIncompatibilityException(ServiceException):
    code: str = "PlatformTaskDefinitionIncompatibilityException"
    sender_fault: bool = False
    status_code: int = 400

class PlatformUnknownException(ServiceException):
    code: str = "PlatformUnknownException"
    sender_fault: bool = False
    status_code: int = 400

class ResourceInUseException(ServiceException):
    code: str = "ResourceInUseException"
    sender_fault: bool = False
    status_code: int = 400

class ResourceNotFoundException(ServiceException):
    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ServerException(ServiceException):
    code: str = "ServerException"
    sender_fault: bool = False
    status_code: int = 400

class ServiceDeploymentNotFoundException(ServiceException):
    code: str = "ServiceDeploymentNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ServiceNotActiveException(ServiceException):
    code: str = "ServiceNotActiveException"
    sender_fault: bool = False
    status_code: int = 400

class ServiceNotFoundException(ServiceException):
    code: str = "ServiceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class TargetNotConnectedException(ServiceException):
    code: str = "TargetNotConnectedException"
    sender_fault: bool = False
    status_code: int = 400

class TargetNotFoundException(ServiceException):
    code: str = "TargetNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class TaskSetNotFoundException(ServiceException):
    code: str = "TaskSetNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class UnsupportedFeatureException(ServiceException):
    code: str = "UnsupportedFeatureException"
    sender_fault: bool = False
    status_code: int = 400

class UpdateInProgressException(ServiceException):
    code: str = "UpdateInProgressException"
    sender_fault: bool = False
    status_code: int = 400

class AcceleratorCountRequest(TypedDict, total=False):
    min: BoxedInteger | None
    max: BoxedInteger | None

AcceleratorManufacturerSet = list[AcceleratorManufacturer]
AcceleratorNameSet = list[AcceleratorName]
class AcceleratorTotalMemoryMiBRequest(TypedDict, total=False):
    min: BoxedInteger | None
    max: BoxedInteger | None

AcceleratorTypeSet = list[AcceleratorType]
class AdvancedConfiguration(TypedDict, total=False):
    alternateTargetGroupArn: String | None
    productionListenerRule: String | None
    testListenerRule: String | None
    roleArn: String | None

AllowedInstanceTypeSet = list[AllowedInstanceType]
class KeyValuePair(TypedDict, total=False):
    name: String | None
    value: String | None

AttachmentDetails = list[KeyValuePair]
Attachment = TypedDict("Attachment", {
    "id": String | None,
    "type": String | None,
    "status": String | None,
    "details": AttachmentDetails | None,
}, total=False)
class AttachmentStateChange(TypedDict, total=False):
    attachmentArn: String
    status: String

AttachmentStateChanges = list[AttachmentStateChange]
Attachments = list[Attachment]
class Attribute(TypedDict, total=False):
    name: String
    value: String | None
    targetType: TargetType | None
    targetId: String | None

Attributes = list[Attribute]
class ManagedScaling(TypedDict, total=False):
    status: ManagedScalingStatus | None
    targetCapacity: ManagedScalingTargetCapacity | None
    minimumScalingStepSize: ManagedScalingStepSize | None
    maximumScalingStepSize: ManagedScalingStepSize | None
    instanceWarmupPeriod: ManagedScalingInstanceWarmupPeriod | None

class AutoScalingGroupProvider(TypedDict, total=False):
    autoScalingGroupArn: String
    managedScaling: ManagedScaling | None
    managedTerminationProtection: ManagedTerminationProtection | None
    managedDraining: ManagedDraining | None

class AutoScalingGroupProviderUpdate(TypedDict, total=False):
    managedScaling: ManagedScaling | None
    managedTerminationProtection: ManagedTerminationProtection | None
    managedDraining: ManagedDraining | None

StringList = list[String]
class AwsVpcConfiguration(TypedDict, total=False):
    subnets: StringList
    securityGroups: StringList | None
    assignPublicIp: AssignPublicIp | None

class BaselineEbsBandwidthMbpsRequest(TypedDict, total=False):
    min: BoxedInteger | None
    max: BoxedInteger | None

class CanaryConfiguration(TypedDict, total=False):
    canaryPercent: Double | None
    canaryBakeTimeInMinutes: Integer | None

class Tag(TypedDict, total=False):
    key: TagKey | None
    value: TagValue | None

Tags = list[Tag]
class InfrastructureOptimization(TypedDict, total=False):
    scaleInAfter: BoxedInteger | None

class CapacityReservationRequest(TypedDict, total=False):
    reservationGroupArn: String | None
    reservationPreference: CapacityReservationPreference | None

class NetworkBandwidthGbpsRequest(TypedDict, total=False):
    min: BoxedDouble | None
    max: BoxedDouble | None

class TotalLocalStorageGBRequest(TypedDict, total=False):
    min: BoxedDouble | None
    max: BoxedDouble | None

LocalStorageTypeSet = list[LocalStorageType]
class NetworkInterfaceCountRequest(TypedDict, total=False):
    min: BoxedInteger | None
    max: BoxedInteger | None

InstanceGenerationSet = list[InstanceGeneration]
ExcludedInstanceTypeSet = list[ExcludedInstanceType]
class MemoryGiBPerVCpuRequest(TypedDict, total=False):
    min: BoxedDouble | None
    max: BoxedDouble | None

CpuManufacturerSet = list[CpuManufacturer]
class MemoryMiBRequest(TypedDict, total=False):
    min: BoxedInteger
    max: BoxedInteger | None

class VCpuCountRangeRequest(TypedDict, total=False):
    min: BoxedInteger
    max: BoxedInteger | None

class InstanceRequirementsRequest(TypedDict, total=False):
    vCpuCount: VCpuCountRangeRequest
    memoryMiB: MemoryMiBRequest
    cpuManufacturers: CpuManufacturerSet | None
    memoryGiBPerVCpu: MemoryGiBPerVCpuRequest | None
    excludedInstanceTypes: ExcludedInstanceTypeSet | None
    instanceGenerations: InstanceGenerationSet | None
    spotMaxPricePercentageOverLowestPrice: BoxedInteger | None
    onDemandMaxPricePercentageOverLowestPrice: BoxedInteger | None
    bareMetal: BareMetal | None
    burstablePerformance: BurstablePerformance | None
    requireHibernateSupport: BoxedBoolean | None
    networkInterfaceCount: NetworkInterfaceCountRequest | None
    localStorage: LocalStorage | None
    localStorageTypes: LocalStorageTypeSet | None
    totalLocalStorageGB: TotalLocalStorageGBRequest | None
    baselineEbsBandwidthMbps: BaselineEbsBandwidthMbpsRequest | None
    acceleratorTypes: AcceleratorTypeSet | None
    acceleratorCount: AcceleratorCountRequest | None
    acceleratorManufacturers: AcceleratorManufacturerSet | None
    acceleratorNames: AcceleratorNameSet | None
    acceleratorTotalMemoryMiB: AcceleratorTotalMemoryMiBRequest | None
    networkBandwidthGbps: NetworkBandwidthGbpsRequest | None
    allowedInstanceTypes: AllowedInstanceTypeSet | None
    maxSpotPriceAsPercentageOfOptimalOnDemandPrice: BoxedInteger | None

class ManagedInstancesStorageConfiguration(TypedDict, total=False):
    storageSizeGiB: TaskVolumeStorageGiB | None

class ManagedInstancesNetworkConfiguration(TypedDict, total=False):
    subnets: StringList | None
    securityGroups: StringList | None

class InstanceLaunchTemplate(TypedDict, total=False):
    ec2InstanceProfileArn: String
    networkConfiguration: ManagedInstancesNetworkConfiguration
    storageConfiguration: ManagedInstancesStorageConfiguration | None
    monitoring: ManagedInstancesMonitoringOptions | None
    capacityOptionType: CapacityOptionType | None
    instanceRequirements: InstanceRequirementsRequest | None
    fipsEnabled: BoxedBoolean | None
    capacityReservations: CapacityReservationRequest | None

class ManagedInstancesProvider(TypedDict, total=False):
    infrastructureRoleArn: String | None
    instanceLaunchTemplate: InstanceLaunchTemplate | None
    propagateTags: PropagateMITags | None
    infrastructureOptimization: InfrastructureOptimization | None

CapacityProvider = TypedDict("CapacityProvider", {
    "capacityProviderArn": String | None,
    "name": String | None,
    "cluster": String | None,
    "status": CapacityProviderStatus | None,
    "autoScalingGroupProvider": AutoScalingGroupProvider | None,
    "managedInstancesProvider": ManagedInstancesProvider | None,
    "updateStatus": CapacityProviderUpdateStatus | None,
    "updateStatusReason": String | None,
    "tags": Tags | None,
    "type": CapacityProviderType | None,
}, total=False)
CapacityProviderFieldList = list[CapacityProviderField]
class CapacityProviderStrategyItem(TypedDict, total=False):
    capacityProvider: String
    weight: CapacityProviderStrategyItemWeight | None
    base: CapacityProviderStrategyItemBase | None

CapacityProviderStrategy = list[CapacityProviderStrategyItem]
CapacityProviders = list[CapacityProvider]
class ClusterServiceConnectDefaults(TypedDict, total=False):
    namespace: String | None

class ClusterSetting(TypedDict, total=False):
    name: ClusterSettingName | None
    value: String | None

ClusterSettings = list[ClusterSetting]
Statistics = list[KeyValuePair]
class ManagedStorageConfiguration(TypedDict, total=False):
    kmsKeyId: String | None
    fargateEphemeralStorageKmsKeyId: String | None

class ExecuteCommandLogConfiguration(TypedDict, total=False):
    cloudWatchLogGroupName: String | None
    cloudWatchEncryptionEnabled: Boolean | None
    s3BucketName: String | None
    s3EncryptionEnabled: Boolean | None
    s3KeyPrefix: String | None

class ExecuteCommandConfiguration(TypedDict, total=False):
    kmsKeyId: String | None
    logging: ExecuteCommandLogging | None
    logConfiguration: ExecuteCommandLogConfiguration | None

class ClusterConfiguration(TypedDict, total=False):
    executeCommandConfiguration: ExecuteCommandConfiguration | None
    managedStorageConfiguration: ManagedStorageConfiguration | None

class Cluster(TypedDict, total=False):
    clusterArn: String | None
    clusterName: String | None
    configuration: ClusterConfiguration | None
    status: String | None
    registeredContainerInstancesCount: Integer | None
    runningTasksCount: Integer | None
    pendingTasksCount: Integer | None
    activeServicesCount: Integer | None
    statistics: Statistics | None
    tags: Tags | None
    settings: ClusterSettings | None
    capacityProviders: StringList | None
    defaultCapacityProviderStrategy: CapacityProviderStrategy | None
    attachments: Attachments | None
    attachmentsStatus: String | None
    serviceConnectDefaults: ClusterServiceConnectDefaults | None

ClusterFieldList = list[ClusterField]
class ClusterServiceConnectDefaultsRequest(TypedDict, total=False):
    namespace: String

Clusters = list[Cluster]
CompatibilityList = list[Compatibility]
GpuIds = list[String]
Timestamp = datetime
class ManagedAgent(TypedDict, total=False):
    lastStartedAt: Timestamp | None
    name: ManagedAgentName | None
    reason: String | None
    lastStatus: String | None

ManagedAgents = list[ManagedAgent]
class NetworkInterface(TypedDict, total=False):
    attachmentId: String | None
    privateIpv4Address: String | None
    ipv6Address: String | None

NetworkInterfaces = list[NetworkInterface]
class NetworkBinding(TypedDict, total=False):
    bindIP: String | None
    containerPort: BoxedInteger | None
    hostPort: BoxedInteger | None
    protocol: TransportProtocol | None
    containerPortRange: String | None
    hostPortRange: String | None

NetworkBindings = list[NetworkBinding]
class Container(TypedDict, total=False):
    containerArn: String | None
    taskArn: String | None
    name: String | None
    image: String | None
    imageDigest: String | None
    runtimeId: String | None
    lastStatus: String | None
    exitCode: BoxedInteger | None
    reason: String | None
    networkBindings: NetworkBindings | None
    networkInterfaces: NetworkInterfaces | None
    healthStatus: HealthStatus | None
    managedAgents: ManagedAgents | None
    cpu: String | None
    memory: String | None
    memoryReservation: String | None
    gpuIds: GpuIds | None

FirelensConfigurationOptionsMap = dict[String, String]
FirelensConfiguration = TypedDict("FirelensConfiguration", {
    "type": FirelensConfigurationType,
    "options": FirelensConfigurationOptionsMap | None,
}, total=False)
ResourceRequirement = TypedDict("ResourceRequirement", {
    "value": String,
    "type": ResourceType,
}, total=False)
ResourceRequirements = list[ResourceRequirement]
class SystemControl(TypedDict, total=False):
    namespace: String | None
    value: String | None

SystemControls = list[SystemControl]
class HealthCheck(TypedDict, total=False):
    command: StringList
    interval: BoxedInteger | None
    timeout: BoxedInteger | None
    retries: BoxedInteger | None
    startPeriod: BoxedInteger | None

class Secret(TypedDict, total=False):
    name: String
    valueFrom: String

SecretList = list[Secret]
LogConfigurationOptionsMap = dict[String, String]
class LogConfiguration(TypedDict, total=False):
    logDriver: LogDriver
    options: LogConfigurationOptionsMap | None
    secretOptions: SecretList | None

class Ulimit(TypedDict, total=False):
    name: UlimitName
    softLimit: Integer
    hardLimit: Integer

UlimitList = list[Ulimit]
DockerLabelsMap = dict[String, String]
class HostEntry(TypedDict, total=False):
    hostname: String
    ipAddress: String

HostEntryList = list[HostEntry]
class ContainerDependency(TypedDict, total=False):
    containerName: String
    condition: ContainerCondition

ContainerDependencies = list[ContainerDependency]
class Tmpfs(TypedDict, total=False):
    containerPath: String
    size: Integer
    mountOptions: StringList | None

TmpfsList = list[Tmpfs]
DeviceCgroupPermissions = list[DeviceCgroupPermission]
class Device(TypedDict, total=False):
    hostPath: String
    containerPath: String | None
    permissions: DeviceCgroupPermissions | None

DevicesList = list[Device]
class KernelCapabilities(TypedDict, total=False):
    add: StringList | None
    drop: StringList | None

class LinuxParameters(TypedDict, total=False):
    capabilities: KernelCapabilities | None
    devices: DevicesList | None
    initProcessEnabled: BoxedBoolean | None
    sharedMemorySize: BoxedInteger | None
    tmpfs: TmpfsList | None
    maxSwap: BoxedInteger | None
    swappiness: BoxedInteger | None

class VolumeFrom(TypedDict, total=False):
    sourceContainer: String | None
    readOnly: BoxedBoolean | None

VolumeFromList = list[VolumeFrom]
class MountPoint(TypedDict, total=False):
    sourceVolume: String | None
    containerPath: String | None
    readOnly: BoxedBoolean | None

MountPointList = list[MountPoint]
EnvironmentFile = TypedDict("EnvironmentFile", {
    "value": String,
    "type": EnvironmentFileType,
}, total=False)
EnvironmentFiles = list[EnvironmentFile]
EnvironmentVariables = list[KeyValuePair]
IntegerList = list[BoxedInteger]
class ContainerRestartPolicy(TypedDict, total=False):
    enabled: BoxedBoolean
    ignoredExitCodes: IntegerList | None
    restartAttemptPeriod: BoxedInteger | None

class PortMapping(TypedDict, total=False):
    containerPort: BoxedInteger | None
    hostPort: BoxedInteger | None
    protocol: TransportProtocol | None
    name: String | None
    appProtocol: ApplicationProtocol | None
    containerPortRange: String | None

PortMappingList = list[PortMapping]
class RepositoryCredentials(TypedDict, total=False):
    credentialsParameter: String

class ContainerDefinition(TypedDict, total=False):
    name: String | None
    image: String | None
    repositoryCredentials: RepositoryCredentials | None
    cpu: Integer | None
    memory: BoxedInteger | None
    memoryReservation: BoxedInteger | None
    links: StringList | None
    portMappings: PortMappingList | None
    essential: BoxedBoolean | None
    restartPolicy: ContainerRestartPolicy | None
    entryPoint: StringList | None
    command: StringList | None
    environment: EnvironmentVariables | None
    environmentFiles: EnvironmentFiles | None
    mountPoints: MountPointList | None
    volumesFrom: VolumeFromList | None
    linuxParameters: LinuxParameters | None
    secrets: SecretList | None
    dependsOn: ContainerDependencies | None
    startTimeout: BoxedInteger | None
    stopTimeout: BoxedInteger | None
    versionConsistency: VersionConsistency | None
    hostname: String | None
    user: String | None
    workingDirectory: String | None
    disableNetworking: BoxedBoolean | None
    privileged: BoxedBoolean | None
    readonlyRootFilesystem: BoxedBoolean | None
    dnsServers: StringList | None
    dnsSearchDomains: StringList | None
    extraHosts: HostEntryList | None
    dockerSecurityOptions: StringList | None
    interactive: BoxedBoolean | None
    pseudoTerminal: BoxedBoolean | None
    dockerLabels: DockerLabelsMap | None
    ulimits: UlimitList | None
    logConfiguration: LogConfiguration | None
    healthCheck: HealthCheck | None
    systemControls: SystemControls | None
    resourceRequirements: ResourceRequirements | None
    firelensConfiguration: FirelensConfiguration | None
    credentialSpecs: StringList | None

ContainerDefinitions = list[ContainerDefinition]
class ContainerImage(TypedDict, total=False):
    containerName: String | None
    imageDigest: String | None
    image: String | None

ContainerImages = list[ContainerImage]
InstanceHealthCheckResult = TypedDict("InstanceHealthCheckResult", {
    "type": InstanceHealthCheckType | None,
    "status": InstanceHealthCheckState | None,
    "lastUpdated": Timestamp | None,
    "lastStatusChange": Timestamp | None,
}, total=False)
InstanceHealthCheckResultList = list[InstanceHealthCheckResult]
class ContainerInstanceHealthStatus(TypedDict, total=False):
    overallStatus: InstanceHealthCheckState | None
    details: InstanceHealthCheckResultList | None

Long = int
Resource = TypedDict("Resource", {
    "name": String | None,
    "type": String | None,
    "doubleValue": Double | None,
    "longValue": Long | None,
    "integerValue": Integer | None,
    "stringSetValue": StringList | None,
}, total=False)
Resources = list[Resource]
class VersionInfo(TypedDict, total=False):
    agentVersion: String | None
    agentHash: String | None
    dockerVersion: String | None

class ContainerInstance(TypedDict, total=False):
    containerInstanceArn: String | None
    ec2InstanceId: String | None
    capacityProviderName: String | None
    version: Long | None
    versionInfo: VersionInfo | None
    remainingResources: Resources | None
    registeredResources: Resources | None
    status: String | None
    statusReason: String | None
    agentConnected: Boolean | None
    runningTasksCount: Integer | None
    pendingTasksCount: Integer | None
    agentUpdateStatus: AgentUpdateStatus | None
    attributes: Attributes | None
    registeredAt: Timestamp | None
    attachments: Attachments | None
    tags: Tags | None
    healthStatus: ContainerInstanceHealthStatus | None

ContainerInstanceFieldList = list[ContainerInstanceField]
ContainerInstances = list[ContainerInstance]
class ContainerOverride(TypedDict, total=False):
    name: String | None
    command: StringList | None
    environment: EnvironmentVariables | None
    environmentFiles: EnvironmentFiles | None
    cpu: BoxedInteger | None
    memory: BoxedInteger | None
    memoryReservation: BoxedInteger | None
    resourceRequirements: ResourceRequirements | None

ContainerOverrides = list[ContainerOverride]
class ContainerStateChange(TypedDict, total=False):
    containerName: String | None
    imageDigest: String | None
    runtimeId: String | None
    exitCode: BoxedInteger | None
    networkBindings: NetworkBindings | None
    reason: String | None
    status: String | None

ContainerStateChanges = list[ContainerStateChange]
Containers = list[Container]
class CreateManagedInstancesProviderConfiguration(TypedDict, total=False):
    infrastructureRoleArn: String
    instanceLaunchTemplate: InstanceLaunchTemplate
    propagateTags: PropagateMITags | None
    infrastructureOptimization: InfrastructureOptimization | None

class CreateCapacityProviderRequest(ServiceRequest):
    name: String
    cluster: String | None
    autoScalingGroupProvider: AutoScalingGroupProvider | None
    managedInstancesProvider: CreateManagedInstancesProviderConfiguration | None
    tags: Tags | None

class CreateCapacityProviderResponse(TypedDict, total=False):
    capacityProvider: CapacityProvider | None

class CreateClusterRequest(ServiceRequest):
    clusterName: String | None
    tags: Tags | None
    settings: ClusterSettings | None
    configuration: ClusterConfiguration | None
    capacityProviders: StringList | None
    defaultCapacityProviderStrategy: CapacityProviderStrategy | None
    serviceConnectDefaults: ClusterServiceConnectDefaultsRequest | None

class CreateClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class ExpressGatewayScalingTarget(TypedDict, total=False):
    minTaskCount: BoxedInteger | None
    maxTaskCount: BoxedInteger | None
    autoScalingMetric: ExpressGatewayServiceScalingMetric | None
    autoScalingTargetValue: BoxedInteger | None

class ExpressGatewayServiceNetworkConfiguration(TypedDict, total=False):
    securityGroups: StringList | None
    subnets: StringList | None

class ExpressGatewayRepositoryCredentials(TypedDict, total=False):
    credentialsParameter: String | None

class ExpressGatewayServiceAwsLogsConfiguration(TypedDict, total=False):
    logGroup: String
    logStreamPrefix: String

class ExpressGatewayContainer(TypedDict, total=False):
    image: String
    containerPort: BoxedInteger | None
    awsLogsConfiguration: ExpressGatewayServiceAwsLogsConfiguration | None
    repositoryCredentials: ExpressGatewayRepositoryCredentials | None
    command: StringList | None
    environment: EnvironmentVariables | None
    secrets: SecretList | None

class CreateExpressGatewayServiceRequest(ServiceRequest):
    executionRoleArn: String
    infrastructureRoleArn: String
    serviceName: String | None
    cluster: String | None
    healthCheckPath: String | None
    primaryContainer: ExpressGatewayContainer
    taskRoleArn: String | None
    networkConfiguration: ExpressGatewayServiceNetworkConfiguration | None
    cpu: String | None
    memory: String | None
    scalingTarget: ExpressGatewayScalingTarget | None
    tags: Tags | None

class IngressPathSummary(TypedDict, total=False):
    accessType: AccessType
    endpoint: String

IngressPathSummaries = list[IngressPathSummary]
class ExpressGatewayServiceConfiguration(TypedDict, total=False):
    serviceRevisionArn: String | None
    executionRoleArn: String | None
    taskRoleArn: String | None
    cpu: String | None
    memory: String | None
    networkConfiguration: ExpressGatewayServiceNetworkConfiguration | None
    healthCheckPath: String | None
    primaryContainer: ExpressGatewayContainer | None
    scalingTarget: ExpressGatewayScalingTarget | None
    ingressPaths: IngressPathSummaries | None
    createdAt: Timestamp | None

ExpressGatewayServiceConfigurations = list[ExpressGatewayServiceConfiguration]
class ExpressGatewayServiceStatus(TypedDict, total=False):
    statusCode: ExpressGatewayServiceStatusCode | None
    statusReason: String | None

class ECSExpressGatewayService(TypedDict, total=False):
    cluster: String | None
    serviceName: String | None
    serviceArn: String | None
    infrastructureRoleArn: String | None
    status: ExpressGatewayServiceStatus | None
    currentDeployment: String | None
    activeConfigurations: ExpressGatewayServiceConfigurations | None
    tags: Tags | None
    createdAt: Timestamp | None
    updatedAt: Timestamp | None

class CreateExpressGatewayServiceResponse(TypedDict, total=False):
    service: ECSExpressGatewayService | None

class VpcLatticeConfiguration(TypedDict, total=False):
    roleArn: IAMRoleArn
    targetGroupArn: String
    portName: String

VpcLatticeConfigurations = list[VpcLatticeConfiguration]
class EBSTagSpecification(TypedDict, total=False):
    resourceType: EBSResourceType
    tags: Tags | None
    propagateTags: PropagateTags | None

EBSTagSpecifications = list[EBSTagSpecification]
class ServiceManagedEBSVolumeConfiguration(TypedDict, total=False):
    encrypted: BoxedBoolean | None
    kmsKeyId: EBSKMSKeyId | None
    volumeType: EBSVolumeType | None
    sizeInGiB: BoxedInteger | None
    snapshotId: EBSSnapshotId | None
    volumeInitializationRate: BoxedInteger | None
    iops: BoxedInteger | None
    throughput: BoxedInteger | None
    tagSpecifications: EBSTagSpecifications | None
    roleArn: IAMRoleArn
    filesystemType: TaskFilesystemType | None

class ServiceVolumeConfiguration(TypedDict, total=False):
    name: ECSVolumeName
    managedEBSVolume: ServiceManagedEBSVolumeConfiguration | None

ServiceVolumeConfigurations = list[ServiceVolumeConfiguration]
class ServiceConnectAccessLogConfiguration(TypedDict, total=False):
    format: ServiceConnectAccessLoggingFormat
    includeQueryParameters: ServiceConnectIncludeQueryParameters | None

class ServiceConnectTlsCertificateAuthority(TypedDict, total=False):
    awsPcaAuthorityArn: String | None

class ServiceConnectTlsConfiguration(TypedDict, total=False):
    issuerCertificateAuthority: ServiceConnectTlsCertificateAuthority
    kmsKey: String | None
    roleArn: String | None

class TimeoutConfiguration(TypedDict, total=False):
    idleTimeoutSeconds: Duration | None
    perRequestTimeoutSeconds: Duration | None

class ServiceConnectTestTrafficHeaderMatchRules(TypedDict, total=False):
    exact: String

class ServiceConnectTestTrafficHeaderRules(TypedDict, total=False):
    name: String
    value: ServiceConnectTestTrafficHeaderMatchRules | None

class ServiceConnectTestTrafficRules(TypedDict, total=False):
    header: ServiceConnectTestTrafficHeaderRules

class ServiceConnectClientAlias(TypedDict, total=False):
    port: PortNumber
    dnsName: String | None
    testTrafficRules: ServiceConnectTestTrafficRules | None

ServiceConnectClientAliasList = list[ServiceConnectClientAlias]
class ServiceConnectService(TypedDict, total=False):
    portName: String
    discoveryName: String | None
    clientAliases: ServiceConnectClientAliasList | None
    ingressPortOverride: PortNumber | None
    timeout: TimeoutConfiguration | None
    tls: ServiceConnectTlsConfiguration | None

ServiceConnectServiceList = list[ServiceConnectService]
class ServiceConnectConfiguration(TypedDict, total=False):
    enabled: Boolean
    namespace: String | None
    services: ServiceConnectServiceList | None
    logConfiguration: LogConfiguration | None
    accessLogConfiguration: ServiceConnectAccessLogConfiguration | None

DeploymentController = TypedDict("DeploymentController", {
    "type": DeploymentControllerType,
}, total=False)
class NetworkConfiguration(TypedDict, total=False):
    awsvpcConfiguration: AwsVpcConfiguration | None

PlacementStrategy = TypedDict("PlacementStrategy", {
    "type": PlacementStrategyType | None,
    "field": String | None,
}, total=False)
PlacementStrategies = list[PlacementStrategy]
PlacementConstraint = TypedDict("PlacementConstraint", {
    "type": PlacementConstraintType | None,
    "expression": String | None,
}, total=False)
PlacementConstraints = list[PlacementConstraint]
class LinearConfiguration(TypedDict, total=False):
    stepPercent: Double | None
    stepBakeTimeInMinutes: Integer | None

class HookDetails(TypedDict, total=False):
    pass

DeploymentLifecycleHookStageList = list[DeploymentLifecycleHookStage]
class DeploymentLifecycleHook(TypedDict, total=False):
    hookTargetArn: String | None
    roleArn: IAMRoleArn | None
    lifecycleStages: DeploymentLifecycleHookStageList | None
    hookDetails: HookDetails | None

DeploymentLifecycleHookList = list[DeploymentLifecycleHook]
class DeploymentAlarms(TypedDict, total=False):
    alarmNames: StringList
    rollback: Boolean
    enable: Boolean

class DeploymentCircuitBreaker(TypedDict, total=False):
    enable: Boolean
    rollback: Boolean

class DeploymentConfiguration(TypedDict, total=False):
    deploymentCircuitBreaker: DeploymentCircuitBreaker | None
    maximumPercent: BoxedInteger | None
    minimumHealthyPercent: BoxedInteger | None
    alarms: DeploymentAlarms | None
    strategy: DeploymentStrategy | None
    bakeTimeInMinutes: BoxedInteger | None
    lifecycleHooks: DeploymentLifecycleHookList | None
    linearConfiguration: LinearConfiguration | None
    canaryConfiguration: CanaryConfiguration | None

class ServiceRegistry(TypedDict, total=False):
    registryArn: String | None
    port: BoxedInteger | None
    containerName: String | None
    containerPort: BoxedInteger | None

ServiceRegistries = list[ServiceRegistry]
class LoadBalancer(TypedDict, total=False):
    targetGroupArn: String | None
    loadBalancerName: String | None
    containerName: String | None
    containerPort: BoxedInteger | None
    advancedConfiguration: AdvancedConfiguration | None

LoadBalancers = list[LoadBalancer]
class CreateServiceRequest(ServiceRequest):
    cluster: String | None
    serviceName: String
    taskDefinition: String | None
    availabilityZoneRebalancing: AvailabilityZoneRebalancing | None
    loadBalancers: LoadBalancers | None
    serviceRegistries: ServiceRegistries | None
    desiredCount: BoxedInteger | None
    clientToken: String | None
    launchType: LaunchType | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    platformVersion: String | None
    role: String | None
    deploymentConfiguration: DeploymentConfiguration | None
    placementConstraints: PlacementConstraints | None
    placementStrategy: PlacementStrategies | None
    networkConfiguration: NetworkConfiguration | None
    healthCheckGracePeriodSeconds: BoxedInteger | None
    schedulingStrategy: SchedulingStrategy | None
    deploymentController: DeploymentController | None
    tags: Tags | None
    enableECSManagedTags: Boolean | None
    propagateTags: PropagateTags | None
    enableExecuteCommand: Boolean | None
    serviceConnectConfiguration: ServiceConnectConfiguration | None
    volumeConfigurations: ServiceVolumeConfigurations | None
    vpcLatticeConfigurations: VpcLatticeConfigurations | None

class ServiceCurrentRevisionSummary(TypedDict, total=False):
    arn: String | None
    requestedTaskCount: Integer | None
    runningTaskCount: Integer | None
    pendingTaskCount: Integer | None

ServiceCurrentRevisionSummaryList = list[ServiceCurrentRevisionSummary]
class ServiceEvent(TypedDict, total=False):
    id: String | None
    createdAt: Timestamp | None
    message: String | None

ServiceEvents = list[ServiceEvent]
class DeploymentEphemeralStorage(TypedDict, total=False):
    kmsKeyId: String | None

class ServiceConnectServiceResource(TypedDict, total=False):
    discoveryName: String | None
    discoveryArn: String | None

ServiceConnectServiceResourceList = list[ServiceConnectServiceResource]
class Deployment(TypedDict, total=False):
    id: String | None
    status: String | None
    taskDefinition: String | None
    desiredCount: Integer | None
    pendingCount: Integer | None
    runningCount: Integer | None
    failedTasks: Integer | None
    createdAt: Timestamp | None
    updatedAt: Timestamp | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    launchType: LaunchType | None
    platformVersion: String | None
    platformFamily: String | None
    networkConfiguration: NetworkConfiguration | None
    rolloutState: DeploymentRolloutState | None
    rolloutStateReason: String | None
    serviceConnectConfiguration: ServiceConnectConfiguration | None
    serviceConnectResources: ServiceConnectServiceResourceList | None
    volumeConfigurations: ServiceVolumeConfigurations | None
    fargateEphemeralStorage: DeploymentEphemeralStorage | None
    vpcLatticeConfigurations: VpcLatticeConfigurations | None

Deployments = list[Deployment]
class Scale(TypedDict, total=False):
    value: Double | None
    unit: ScaleUnit | None

class TaskSet(TypedDict, total=False):
    id: String | None
    taskSetArn: String | None
    serviceArn: String | None
    clusterArn: String | None
    startedBy: String | None
    externalId: String | None
    status: String | None
    taskDefinition: String | None
    computedDesiredCount: Integer | None
    pendingCount: Integer | None
    runningCount: Integer | None
    createdAt: Timestamp | None
    updatedAt: Timestamp | None
    launchType: LaunchType | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    platformVersion: String | None
    platformFamily: String | None
    networkConfiguration: NetworkConfiguration | None
    loadBalancers: LoadBalancers | None
    serviceRegistries: ServiceRegistries | None
    scale: Scale | None
    stabilityStatus: StabilityStatus | None
    stabilityStatusAt: Timestamp | None
    tags: Tags | None
    fargateEphemeralStorage: DeploymentEphemeralStorage | None

TaskSets = list[TaskSet]
class Service(TypedDict, total=False):
    serviceArn: String | None
    serviceName: String | None
    clusterArn: String | None
    loadBalancers: LoadBalancers | None
    serviceRegistries: ServiceRegistries | None
    status: String | None
    desiredCount: Integer | None
    runningCount: Integer | None
    pendingCount: Integer | None
    launchType: LaunchType | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    platformVersion: String | None
    platformFamily: String | None
    taskDefinition: String | None
    deploymentConfiguration: DeploymentConfiguration | None
    taskSets: TaskSets | None
    deployments: Deployments | None
    roleArn: String | None
    events: ServiceEvents | None
    createdAt: Timestamp | None
    currentServiceDeployment: String | None
    currentServiceRevisions: ServiceCurrentRevisionSummaryList | None
    placementConstraints: PlacementConstraints | None
    placementStrategy: PlacementStrategies | None
    networkConfiguration: NetworkConfiguration | None
    healthCheckGracePeriodSeconds: BoxedInteger | None
    schedulingStrategy: SchedulingStrategy | None
    deploymentController: DeploymentController | None
    tags: Tags | None
    createdBy: String | None
    enableECSManagedTags: Boolean | None
    propagateTags: PropagateTags | None
    enableExecuteCommand: Boolean | None
    availabilityZoneRebalancing: AvailabilityZoneRebalancing | None
    resourceManagementType: ResourceManagementType | None

class CreateServiceResponse(TypedDict, total=False):
    service: Service | None

class CreateTaskSetRequest(ServiceRequest):
    service: String
    cluster: String
    externalId: String | None
    taskDefinition: String
    networkConfiguration: NetworkConfiguration | None
    loadBalancers: LoadBalancers | None
    serviceRegistries: ServiceRegistries | None
    launchType: LaunchType | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    platformVersion: String | None
    scale: Scale | None
    clientToken: String | None
    tags: Tags | None

class CreateTaskSetResponse(TypedDict, total=False):
    taskSet: TaskSet | None

class CreatedAt(TypedDict, total=False):
    before: Timestamp | None
    after: Timestamp | None

class DeleteAccountSettingRequest(ServiceRequest):
    name: SettingName
    principalArn: String | None

Setting = TypedDict("Setting", {
    "name": SettingName | None,
    "value": String | None,
    "principalArn": String | None,
    "type": SettingType | None,
}, total=False)
class DeleteAccountSettingResponse(TypedDict, total=False):
    setting: Setting | None

class DeleteAttributesRequest(ServiceRequest):
    cluster: String | None
    attributes: Attributes

class DeleteAttributesResponse(TypedDict, total=False):
    attributes: Attributes | None

class DeleteCapacityProviderRequest(ServiceRequest):
    capacityProvider: String
    cluster: String | None

class DeleteCapacityProviderResponse(TypedDict, total=False):
    capacityProvider: CapacityProvider | None

class DeleteClusterRequest(ServiceRequest):
    cluster: String

class DeleteClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class DeleteExpressGatewayServiceRequest(ServiceRequest):
    serviceArn: String

class DeleteExpressGatewayServiceResponse(TypedDict, total=False):
    service: ECSExpressGatewayService | None

class DeleteServiceRequest(ServiceRequest):
    cluster: String | None
    service: String
    force: BoxedBoolean | None

class DeleteServiceResponse(TypedDict, total=False):
    service: Service | None

class DeleteTaskDefinitionsRequest(ServiceRequest):
    taskDefinitions: StringList

class Failure(TypedDict, total=False):
    arn: String | None
    reason: String | None
    detail: String | None

Failures = list[Failure]
class EphemeralStorage(TypedDict, total=False):
    sizeInGiB: Integer

ProxyConfigurationProperties = list[KeyValuePair]
ProxyConfiguration = TypedDict("ProxyConfiguration", {
    "type": ProxyConfigurationType | None,
    "containerName": String,
    "properties": ProxyConfigurationProperties | None,
}, total=False)
class InferenceAccelerator(TypedDict, total=False):
    deviceName: String
    deviceType: String

InferenceAccelerators = list[InferenceAccelerator]
class RuntimePlatform(TypedDict, total=False):
    cpuArchitecture: CPUArchitecture | None
    operatingSystemFamily: OSFamily | None

TaskDefinitionPlacementConstraint = TypedDict("TaskDefinitionPlacementConstraint", {
    "type": TaskDefinitionPlacementConstraintType | None,
    "expression": String | None,
}, total=False)
TaskDefinitionPlacementConstraints = list[TaskDefinitionPlacementConstraint]
RequiresAttributes = list[Attribute]
class FSxWindowsFileServerAuthorizationConfig(TypedDict, total=False):
    credentialsParameter: String
    domain: String

class FSxWindowsFileServerVolumeConfiguration(TypedDict, total=False):
    fileSystemId: String
    rootDirectory: String
    authorizationConfig: FSxWindowsFileServerAuthorizationConfig

class EFSAuthorizationConfig(TypedDict, total=False):
    accessPointId: String | None
    iam: EFSAuthorizationConfigIAM | None

class EFSVolumeConfiguration(TypedDict, total=False):
    fileSystemId: String
    rootDirectory: String | None
    transitEncryption: EFSTransitEncryption | None
    transitEncryptionPort: BoxedInteger | None
    authorizationConfig: EFSAuthorizationConfig | None

StringMap = dict[String, String]
class DockerVolumeConfiguration(TypedDict, total=False):
    scope: Scope | None
    autoprovision: BoxedBoolean | None
    driver: String | None
    driverOpts: StringMap | None
    labels: StringMap | None

class HostVolumeProperties(TypedDict, total=False):
    sourcePath: String | None

class Volume(TypedDict, total=False):
    name: String | None
    host: HostVolumeProperties | None
    dockerVolumeConfiguration: DockerVolumeConfiguration | None
    efsVolumeConfiguration: EFSVolumeConfiguration | None
    fsxWindowsFileServerVolumeConfiguration: FSxWindowsFileServerVolumeConfiguration | None
    configuredAtLaunch: BoxedBoolean | None

VolumeList = list[Volume]
class TaskDefinition(TypedDict, total=False):
    taskDefinitionArn: String | None
    containerDefinitions: ContainerDefinitions | None
    family: String | None
    taskRoleArn: String | None
    executionRoleArn: String | None
    networkMode: NetworkMode | None
    revision: Integer | None
    volumes: VolumeList | None
    status: TaskDefinitionStatus | None
    requiresAttributes: RequiresAttributes | None
    placementConstraints: TaskDefinitionPlacementConstraints | None
    compatibilities: CompatibilityList | None
    runtimePlatform: RuntimePlatform | None
    requiresCompatibilities: CompatibilityList | None
    cpu: String | None
    memory: String | None
    inferenceAccelerators: InferenceAccelerators | None
    pidMode: PidMode | None
    ipcMode: IpcMode | None
    proxyConfiguration: ProxyConfiguration | None
    registeredAt: Timestamp | None
    deregisteredAt: Timestamp | None
    registeredBy: String | None
    ephemeralStorage: EphemeralStorage | None
    enableFaultInjection: BoxedBoolean | None

TaskDefinitionList = list[TaskDefinition]
class DeleteTaskDefinitionsResponse(TypedDict, total=False):
    taskDefinitions: TaskDefinitionList | None
    failures: Failures | None

class DeleteTaskSetRequest(ServiceRequest):
    cluster: String
    service: String
    taskSet: String
    force: BoxedBoolean | None

class DeleteTaskSetResponse(TypedDict, total=False):
    taskSet: TaskSet | None

class DeregisterContainerInstanceRequest(ServiceRequest):
    cluster: String | None
    containerInstance: String
    force: BoxedBoolean | None

class DeregisterContainerInstanceResponse(TypedDict, total=False):
    containerInstance: ContainerInstance | None

class DeregisterTaskDefinitionRequest(ServiceRequest):
    taskDefinition: String

class DeregisterTaskDefinitionResponse(TypedDict, total=False):
    taskDefinition: TaskDefinition | None

class DescribeCapacityProvidersRequest(ServiceRequest):
    capacityProviders: StringList | None
    cluster: String | None
    include: CapacityProviderFieldList | None
    maxResults: BoxedInteger | None
    nextToken: String | None

class DescribeCapacityProvidersResponse(TypedDict, total=False):
    capacityProviders: CapacityProviders | None
    failures: Failures | None
    nextToken: String | None

class DescribeClustersRequest(ServiceRequest):
    clusters: StringList | None
    include: ClusterFieldList | None

class DescribeClustersResponse(TypedDict, total=False):
    clusters: Clusters | None
    failures: Failures | None

class DescribeContainerInstancesRequest(ServiceRequest):
    cluster: String | None
    containerInstances: StringList
    include: ContainerInstanceFieldList | None

class DescribeContainerInstancesResponse(TypedDict, total=False):
    containerInstances: ContainerInstances | None
    failures: Failures | None

ExpressGatewayServiceIncludeList = list[ExpressGatewayServiceInclude]
class DescribeExpressGatewayServiceRequest(ServiceRequest):
    serviceArn: String
    include: ExpressGatewayServiceIncludeList | None

class DescribeExpressGatewayServiceResponse(TypedDict, total=False):
    service: ECSExpressGatewayService | None

class DescribeServiceDeploymentsRequest(ServiceRequest):
    serviceDeploymentArns: StringList

class ServiceDeploymentAlarms(TypedDict, total=False):
    status: ServiceDeploymentRollbackMonitorsStatus | None
    alarmNames: StringList | None
    triggeredAlarmNames: StringList | None

class ServiceDeploymentCircuitBreaker(TypedDict, total=False):
    status: ServiceDeploymentRollbackMonitorsStatus | None
    failureCount: Integer | None
    threshold: Integer | None

class Rollback(TypedDict, total=False):
    reason: String | None
    startedAt: Timestamp | None
    serviceRevisionArn: String | None

class ServiceRevisionSummary(TypedDict, total=False):
    arn: String | None
    requestedTaskCount: Integer | None
    runningTaskCount: Integer | None
    pendingTaskCount: Integer | None
    requestedTestTrafficWeight: Double | None
    requestedProductionTrafficWeight: Double | None

ServiceRevisionsSummaryList = list[ServiceRevisionSummary]
class ServiceDeployment(TypedDict, total=False):
    serviceDeploymentArn: String | None
    serviceArn: String | None
    clusterArn: String | None
    createdAt: Timestamp | None
    startedAt: Timestamp | None
    finishedAt: Timestamp | None
    stoppedAt: Timestamp | None
    updatedAt: Timestamp | None
    sourceServiceRevisions: ServiceRevisionsSummaryList | None
    targetServiceRevision: ServiceRevisionSummary | None
    status: ServiceDeploymentStatus | None
    statusReason: String | None
    lifecycleStage: ServiceDeploymentLifecycleStage | None
    deploymentConfiguration: DeploymentConfiguration | None
    rollback: Rollback | None
    deploymentCircuitBreaker: ServiceDeploymentCircuitBreaker | None
    alarms: ServiceDeploymentAlarms | None

ServiceDeployments = list[ServiceDeployment]
class DescribeServiceDeploymentsResponse(TypedDict, total=False):
    serviceDeployments: ServiceDeployments | None
    failures: Failures | None

class DescribeServiceRevisionsRequest(ServiceRequest):
    serviceRevisionArns: StringList

class ManagedLogGroup(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp
    logGroupName: String

ManagedLogGroups = list[ManagedLogGroup]
class ManagedSecurityGroup(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp

ManagedSecurityGroups = list[ManagedSecurityGroup]
class ManagedMetricAlarm(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp

ManagedMetricAlarms = list[ManagedMetricAlarm]
class ManagedApplicationAutoScalingPolicy(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp
    policyType: String
    targetValue: Double
    metric: String

ManagedApplicationAutoScalingPolicies = list[ManagedApplicationAutoScalingPolicy]
class ManagedScalableTarget(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp
    minCapacity: Integer
    maxCapacity: Integer

class ManagedAutoScaling(TypedDict, total=False):
    scalableTarget: ManagedScalableTarget | None
    applicationAutoScalingPolicies: ManagedApplicationAutoScalingPolicies | None

class ManagedTargetGroup(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp
    healthCheckPath: String
    healthCheckPort: Integer
    port: Integer

ManagedTargetGroups = list[ManagedTargetGroup]
class ManagedListenerRule(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp

class ManagedListener(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp

class ManagedCertificate(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp
    domainName: String

class ManagedLoadBalancer(TypedDict, total=False):
    arn: String | None
    status: ManagedResourceStatus
    statusReason: String | None
    updatedAt: Timestamp
    scheme: String
    subnetIds: StringList | None
    securityGroupIds: StringList | None

class ManagedIngressPath(TypedDict, total=False):
    accessType: AccessType
    endpoint: String
    loadBalancer: ManagedLoadBalancer | None
    loadBalancerSecurityGroups: ManagedSecurityGroups | None
    certificate: ManagedCertificate | None
    listener: ManagedListener | None
    rule: ManagedListenerRule | None
    targetGroups: ManagedTargetGroups | None

ManagedIngressPaths = list[ManagedIngressPath]
class ECSManagedResources(TypedDict, total=False):
    ingressPaths: ManagedIngressPaths | None
    autoScaling: ManagedAutoScaling | None
    metricAlarms: ManagedMetricAlarms | None
    serviceSecurityGroups: ManagedSecurityGroups | None
    logGroups: ManagedLogGroups | None

class ServiceRevisionLoadBalancer(TypedDict, total=False):
    targetGroupArn: String | None
    productionListenerRule: String | None

ServiceRevisionLoadBalancers = list[ServiceRevisionLoadBalancer]
class ResolvedConfiguration(TypedDict, total=False):
    loadBalancers: ServiceRevisionLoadBalancers | None

class ServiceRevision(TypedDict, total=False):
    serviceRevisionArn: String | None
    serviceArn: String | None
    clusterArn: String | None
    taskDefinition: String | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    launchType: LaunchType | None
    platformVersion: String | None
    platformFamily: String | None
    loadBalancers: LoadBalancers | None
    serviceRegistries: ServiceRegistries | None
    networkConfiguration: NetworkConfiguration | None
    containerImages: ContainerImages | None
    guardDutyEnabled: Boolean | None
    serviceConnectConfiguration: ServiceConnectConfiguration | None
    volumeConfigurations: ServiceVolumeConfigurations | None
    fargateEphemeralStorage: DeploymentEphemeralStorage | None
    createdAt: Timestamp | None
    vpcLatticeConfigurations: VpcLatticeConfigurations | None
    resolvedConfiguration: ResolvedConfiguration | None
    ecsManagedResources: ECSManagedResources | None

ServiceRevisions = list[ServiceRevision]
class DescribeServiceRevisionsResponse(TypedDict, total=False):
    serviceRevisions: ServiceRevisions | None
    failures: Failures | None

ServiceFieldList = list[ServiceField]
class DescribeServicesRequest(ServiceRequest):
    cluster: String | None
    services: StringList
    include: ServiceFieldList | None

Services = list[Service]
class DescribeServicesResponse(TypedDict, total=False):
    services: Services | None
    failures: Failures | None

TaskDefinitionFieldList = list[TaskDefinitionField]
class DescribeTaskDefinitionRequest(ServiceRequest):
    taskDefinition: String
    include: TaskDefinitionFieldList | None

class DescribeTaskDefinitionResponse(TypedDict, total=False):
    taskDefinition: TaskDefinition | None
    tags: Tags | None

TaskSetFieldList = list[TaskSetField]
class DescribeTaskSetsRequest(ServiceRequest):
    cluster: String
    service: String
    taskSets: StringList | None
    include: TaskSetFieldList | None

class DescribeTaskSetsResponse(TypedDict, total=False):
    taskSets: TaskSets | None
    failures: Failures | None

TaskFieldList = list[TaskField]
class DescribeTasksRequest(ServiceRequest):
    cluster: String | None
    tasks: StringList
    include: TaskFieldList | None

class TaskEphemeralStorage(TypedDict, total=False):
    sizeInGiB: Integer | None
    kmsKeyId: String | None

class InferenceAcceleratorOverride(TypedDict, total=False):
    deviceName: String | None
    deviceType: String | None

InferenceAcceleratorOverrides = list[InferenceAcceleratorOverride]
class TaskOverride(TypedDict, total=False):
    containerOverrides: ContainerOverrides | None
    cpu: String | None
    inferenceAcceleratorOverrides: InferenceAcceleratorOverrides | None
    executionRoleArn: String | None
    memory: String | None
    taskRoleArn: String | None
    ephemeralStorage: EphemeralStorage | None

class Task(TypedDict, total=False):
    attachments: Attachments | None
    attributes: Attributes | None
    availabilityZone: String | None
    capacityProviderName: String | None
    clusterArn: String | None
    connectivity: Connectivity | None
    connectivityAt: Timestamp | None
    containerInstanceArn: String | None
    containers: Containers | None
    cpu: String | None
    createdAt: Timestamp | None
    desiredStatus: String | None
    enableExecuteCommand: Boolean | None
    executionStoppedAt: Timestamp | None
    group: String | None
    healthStatus: HealthStatus | None
    inferenceAccelerators: InferenceAccelerators | None
    lastStatus: String | None
    launchType: LaunchType | None
    memory: String | None
    overrides: TaskOverride | None
    platformVersion: String | None
    platformFamily: String | None
    pullStartedAt: Timestamp | None
    pullStoppedAt: Timestamp | None
    startedAt: Timestamp | None
    startedBy: String | None
    stopCode: TaskStopCode | None
    stoppedAt: Timestamp | None
    stoppedReason: String | None
    stoppingAt: Timestamp | None
    tags: Tags | None
    taskArn: String | None
    taskDefinitionArn: String | None
    version: Long | None
    ephemeralStorage: EphemeralStorage | None
    fargateEphemeralStorage: TaskEphemeralStorage | None

Tasks = list[Task]
class DescribeTasksResponse(TypedDict, total=False):
    tasks: Tasks | None
    failures: Failures | None

class DiscoverPollEndpointRequest(ServiceRequest):
    containerInstance: String | None
    cluster: String | None

class DiscoverPollEndpointResponse(TypedDict, total=False):
    endpoint: String | None
    telemetryEndpoint: String | None
    serviceConnectEndpoint: String | None

class ExecuteCommandRequest(ServiceRequest):
    cluster: String | None
    container: String | None
    command: String
    interactive: Boolean
    task: String

class Session(TypedDict, total=False):
    sessionId: String | None
    streamUrl: String | None
    tokenValue: SensitiveString | None

class ExecuteCommandResponse(TypedDict, total=False):
    clusterArn: String | None
    containerArn: String | None
    containerName: String | None
    interactive: Boolean | None
    session: Session | None
    taskArn: String | None

class GetTaskProtectionRequest(ServiceRequest):
    cluster: String
    tasks: StringList | None

class ProtectedTask(TypedDict, total=False):
    taskArn: String | None
    protectionEnabled: Boolean | None
    expirationDate: Timestamp | None

ProtectedTasks = list[ProtectedTask]
class GetTaskProtectionResponse(TypedDict, total=False):
    protectedTasks: ProtectedTasks | None
    failures: Failures | None

class InstanceLaunchTemplateUpdate(TypedDict, total=False):
    ec2InstanceProfileArn: String | None
    networkConfiguration: ManagedInstancesNetworkConfiguration | None
    storageConfiguration: ManagedInstancesStorageConfiguration | None
    monitoring: ManagedInstancesMonitoringOptions | None
    instanceRequirements: InstanceRequirementsRequest | None
    capacityReservations: CapacityReservationRequest | None

class ListAccountSettingsRequest(ServiceRequest):
    name: SettingName | None
    value: String | None
    principalArn: String | None
    effectiveSettings: Boolean | None
    nextToken: String | None
    maxResults: Integer | None

Settings = list[Setting]
class ListAccountSettingsResponse(TypedDict, total=False):
    settings: Settings | None
    nextToken: String | None

class ListAttributesRequest(ServiceRequest):
    cluster: String | None
    targetType: TargetType
    attributeName: String | None
    attributeValue: String | None
    nextToken: String | None
    maxResults: BoxedInteger | None

class ListAttributesResponse(TypedDict, total=False):
    attributes: Attributes | None
    nextToken: String | None

class ListClustersRequest(ServiceRequest):
    nextToken: String | None
    maxResults: BoxedInteger | None

class ListClustersResponse(TypedDict, total=False):
    clusterArns: StringList | None
    nextToken: String | None

class ListContainerInstancesRequest(ServiceRequest):
    cluster: String | None
    filter: String | None
    nextToken: String | None
    maxResults: BoxedInteger | None
    status: ContainerInstanceStatus | None

class ListContainerInstancesResponse(TypedDict, total=False):
    containerInstanceArns: StringList | None
    nextToken: String | None

ServiceDeploymentStatusList = list[ServiceDeploymentStatus]
class ListServiceDeploymentsRequest(ServiceRequest):
    service: String
    cluster: String | None
    status: ServiceDeploymentStatusList | None
    createdAt: CreatedAt | None
    nextToken: String | None
    maxResults: BoxedInteger | None

class ServiceDeploymentBrief(TypedDict, total=False):
    serviceDeploymentArn: String | None
    serviceArn: String | None
    clusterArn: String | None
    startedAt: Timestamp | None
    createdAt: Timestamp | None
    finishedAt: Timestamp | None
    targetServiceRevisionArn: String | None
    status: ServiceDeploymentStatus | None
    statusReason: String | None

ServiceDeploymentsBrief = list[ServiceDeploymentBrief]
class ListServiceDeploymentsResponse(TypedDict, total=False):
    serviceDeployments: ServiceDeploymentsBrief | None
    nextToken: String | None

class ListServicesByNamespaceRequest(ServiceRequest):
    namespace: String
    nextToken: String | None
    maxResults: BoxedInteger | None

class ListServicesByNamespaceResponse(TypedDict, total=False):
    serviceArns: StringList | None
    nextToken: String | None

class ListServicesRequest(ServiceRequest):
    cluster: String | None
    nextToken: String | None
    maxResults: BoxedInteger | None
    launchType: LaunchType | None
    schedulingStrategy: SchedulingStrategy | None
    resourceManagementType: ResourceManagementType | None

class ListServicesResponse(TypedDict, total=False):
    serviceArns: StringList | None
    nextToken: String | None

class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: String

class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Tags | None

class ListTaskDefinitionFamiliesRequest(ServiceRequest):
    familyPrefix: String | None
    status: TaskDefinitionFamilyStatus | None
    nextToken: String | None
    maxResults: BoxedInteger | None

class ListTaskDefinitionFamiliesResponse(TypedDict, total=False):
    families: StringList | None
    nextToken: String | None

class ListTaskDefinitionsRequest(ServiceRequest):
    familyPrefix: String | None
    status: TaskDefinitionStatus | None
    sort: SortOrder | None
    nextToken: String | None
    maxResults: BoxedInteger | None

class ListTaskDefinitionsResponse(TypedDict, total=False):
    taskDefinitionArns: StringList | None
    nextToken: String | None

class ListTasksRequest(ServiceRequest):
    cluster: String | None
    containerInstance: String | None
    family: String | None
    nextToken: String | None
    maxResults: BoxedInteger | None
    startedBy: String | None
    serviceName: String | None
    desiredStatus: DesiredStatus | None
    launchType: LaunchType | None

class ListTasksResponse(TypedDict, total=False):
    taskArns: StringList | None
    nextToken: String | None

class ManagedAgentStateChange(TypedDict, total=False):
    containerName: String
    managedAgentName: ManagedAgentName
    status: String
    reason: String | None

ManagedAgentStateChanges = list[ManagedAgentStateChange]
PlatformDevice = TypedDict("PlatformDevice", {
    "id": String,
    "type": PlatformDeviceType,
}, total=False)
PlatformDevices = list[PlatformDevice]
class PutAccountSettingDefaultRequest(ServiceRequest):
    name: SettingName
    value: String

class PutAccountSettingDefaultResponse(TypedDict, total=False):
    setting: Setting | None

class PutAccountSettingRequest(ServiceRequest):
    name: SettingName
    value: String
    principalArn: String | None

class PutAccountSettingResponse(TypedDict, total=False):
    setting: Setting | None

class PutAttributesRequest(ServiceRequest):
    cluster: String | None
    attributes: Attributes

class PutAttributesResponse(TypedDict, total=False):
    attributes: Attributes | None

class PutClusterCapacityProvidersRequest(ServiceRequest):
    cluster: String
    capacityProviders: StringList
    defaultCapacityProviderStrategy: CapacityProviderStrategy

class PutClusterCapacityProvidersResponse(TypedDict, total=False):
    cluster: Cluster | None

class RegisterContainerInstanceRequest(ServiceRequest):
    cluster: String | None
    instanceIdentityDocument: String | None
    instanceIdentityDocumentSignature: String | None
    totalResources: Resources | None
    versionInfo: VersionInfo | None
    containerInstanceArn: String | None
    attributes: Attributes | None
    platformDevices: PlatformDevices | None
    tags: Tags | None

class RegisterContainerInstanceResponse(TypedDict, total=False):
    containerInstance: ContainerInstance | None

class RegisterTaskDefinitionRequest(ServiceRequest):
    family: String
    taskRoleArn: String | None
    executionRoleArn: String | None
    networkMode: NetworkMode | None
    containerDefinitions: ContainerDefinitions
    volumes: VolumeList | None
    placementConstraints: TaskDefinitionPlacementConstraints | None
    requiresCompatibilities: CompatibilityList | None
    cpu: String | None
    memory: String | None
    tags: Tags | None
    pidMode: PidMode | None
    ipcMode: IpcMode | None
    proxyConfiguration: ProxyConfiguration | None
    inferenceAccelerators: InferenceAccelerators | None
    ephemeralStorage: EphemeralStorage | None
    runtimePlatform: RuntimePlatform | None
    enableFaultInjection: BoxedBoolean | None

class RegisterTaskDefinitionResponse(TypedDict, total=False):
    taskDefinition: TaskDefinition | None
    tags: Tags | None

class TaskManagedEBSVolumeTerminationPolicy(TypedDict, total=False):
    deleteOnTermination: BoxedBoolean

class TaskManagedEBSVolumeConfiguration(TypedDict, total=False):
    encrypted: BoxedBoolean | None
    kmsKeyId: EBSKMSKeyId | None
    volumeType: EBSVolumeType | None
    sizeInGiB: BoxedInteger | None
    snapshotId: EBSSnapshotId | None
    volumeInitializationRate: BoxedInteger | None
    iops: BoxedInteger | None
    throughput: BoxedInteger | None
    tagSpecifications: EBSTagSpecifications | None
    roleArn: IAMRoleArn
    terminationPolicy: TaskManagedEBSVolumeTerminationPolicy | None
    filesystemType: TaskFilesystemType | None

class TaskVolumeConfiguration(TypedDict, total=False):
    name: ECSVolumeName
    managedEBSVolume: TaskManagedEBSVolumeConfiguration | None

TaskVolumeConfigurations = list[TaskVolumeConfiguration]
class RunTaskRequest(ServiceRequest):
    capacityProviderStrategy: CapacityProviderStrategy | None
    cluster: String | None
    count: BoxedInteger | None
    enableECSManagedTags: Boolean | None
    enableExecuteCommand: Boolean | None
    group: String | None
    launchType: LaunchType | None
    networkConfiguration: NetworkConfiguration | None
    overrides: TaskOverride | None
    placementConstraints: PlacementConstraints | None
    placementStrategy: PlacementStrategies | None
    platformVersion: String | None
    propagateTags: PropagateTags | None
    referenceId: String | None
    startedBy: String | None
    tags: Tags | None
    taskDefinition: String
    clientToken: String | None
    volumeConfigurations: TaskVolumeConfigurations | None

class RunTaskResponse(TypedDict, total=False):
    tasks: Tasks | None
    failures: Failures | None

class StartTaskRequest(ServiceRequest):
    cluster: String | None
    containerInstances: StringList
    enableECSManagedTags: Boolean | None
    enableExecuteCommand: Boolean | None
    group: String | None
    networkConfiguration: NetworkConfiguration | None
    overrides: TaskOverride | None
    propagateTags: PropagateTags | None
    referenceId: String | None
    startedBy: String | None
    tags: Tags | None
    taskDefinition: String
    volumeConfigurations: TaskVolumeConfigurations | None

class StartTaskResponse(TypedDict, total=False):
    tasks: Tasks | None
    failures: Failures | None

class StopServiceDeploymentRequest(ServiceRequest):
    serviceDeploymentArn: String
    stopType: StopServiceDeploymentStopType | None

class StopServiceDeploymentResponse(TypedDict, total=False):
    serviceDeploymentArn: String | None

class StopTaskRequest(ServiceRequest):
    cluster: String | None
    task: String
    reason: String | None

class StopTaskResponse(TypedDict, total=False):
    task: Task | None

class SubmitAttachmentStateChangesRequest(ServiceRequest):
    cluster: String | None
    attachments: AttachmentStateChanges

class SubmitAttachmentStateChangesResponse(TypedDict, total=False):
    acknowledgment: String | None

class SubmitContainerStateChangeRequest(ServiceRequest):
    cluster: String | None
    task: String | None
    containerName: String | None
    runtimeId: String | None
    status: String | None
    exitCode: BoxedInteger | None
    reason: String | None
    networkBindings: NetworkBindings | None

class SubmitContainerStateChangeResponse(TypedDict, total=False):
    acknowledgment: String | None

class SubmitTaskStateChangeRequest(ServiceRequest):
    cluster: String | None
    task: String | None
    status: String | None
    reason: String | None
    containers: ContainerStateChanges | None
    attachments: AttachmentStateChanges | None
    managedAgents: ManagedAgentStateChanges | None
    pullStartedAt: Timestamp | None
    pullStoppedAt: Timestamp | None
    executionStoppedAt: Timestamp | None

class SubmitTaskStateChangeResponse(TypedDict, total=False):
    acknowledgment: String | None

TagKeys = list[TagKey]
class TagResourceRequest(ServiceRequest):
    resourceArn: String
    tags: Tags

class TagResourceResponse(TypedDict, total=False):
    pass

class UntagResourceRequest(ServiceRequest):
    resourceArn: String
    tagKeys: TagKeys

class UntagResourceResponse(TypedDict, total=False):
    pass

class UpdateManagedInstancesProviderConfiguration(TypedDict, total=False):
    infrastructureRoleArn: String
    instanceLaunchTemplate: InstanceLaunchTemplateUpdate
    propagateTags: PropagateMITags | None
    infrastructureOptimization: InfrastructureOptimization | None

class UpdateCapacityProviderRequest(ServiceRequest):
    name: String
    cluster: String | None
    autoScalingGroupProvider: AutoScalingGroupProviderUpdate | None
    managedInstancesProvider: UpdateManagedInstancesProviderConfiguration | None

class UpdateCapacityProviderResponse(TypedDict, total=False):
    capacityProvider: CapacityProvider | None

class UpdateClusterRequest(ServiceRequest):
    cluster: String
    settings: ClusterSettings | None
    configuration: ClusterConfiguration | None
    serviceConnectDefaults: ClusterServiceConnectDefaultsRequest | None

class UpdateClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class UpdateClusterSettingsRequest(ServiceRequest):
    cluster: String
    settings: ClusterSettings

class UpdateClusterSettingsResponse(TypedDict, total=False):
    cluster: Cluster | None

class UpdateContainerAgentRequest(ServiceRequest):
    cluster: String | None
    containerInstance: String

class UpdateContainerAgentResponse(TypedDict, total=False):
    containerInstance: ContainerInstance | None

class UpdateContainerInstancesStateRequest(ServiceRequest):
    cluster: String | None
    containerInstances: StringList
    status: ContainerInstanceStatus

class UpdateContainerInstancesStateResponse(TypedDict, total=False):
    containerInstances: ContainerInstances | None
    failures: Failures | None

class UpdateExpressGatewayServiceRequest(ServiceRequest):
    serviceArn: String
    executionRoleArn: String | None
    healthCheckPath: String | None
    primaryContainer: ExpressGatewayContainer | None
    taskRoleArn: String | None
    networkConfiguration: ExpressGatewayServiceNetworkConfiguration | None
    cpu: String | None
    memory: String | None
    scalingTarget: ExpressGatewayScalingTarget | None

class UpdatedExpressGatewayService(TypedDict, total=False):
    serviceArn: String | None
    cluster: String | None
    serviceName: String | None
    status: ExpressGatewayServiceStatus | None
    targetConfiguration: ExpressGatewayServiceConfiguration | None
    createdAt: Timestamp | None
    updatedAt: Timestamp | None

class UpdateExpressGatewayServiceResponse(TypedDict, total=False):
    service: UpdatedExpressGatewayService | None

class UpdateServicePrimaryTaskSetRequest(ServiceRequest):
    cluster: String
    service: String
    primaryTaskSet: String

class UpdateServicePrimaryTaskSetResponse(TypedDict, total=False):
    taskSet: TaskSet | None

class UpdateServiceRequest(ServiceRequest):
    cluster: String | None
    service: String
    desiredCount: BoxedInteger | None
    taskDefinition: String | None
    capacityProviderStrategy: CapacityProviderStrategy | None
    deploymentConfiguration: DeploymentConfiguration | None
    availabilityZoneRebalancing: AvailabilityZoneRebalancing | None
    networkConfiguration: NetworkConfiguration | None
    placementConstraints: PlacementConstraints | None
    placementStrategy: PlacementStrategies | None
    platformVersion: String | None
    forceNewDeployment: Boolean | None
    healthCheckGracePeriodSeconds: BoxedInteger | None
    deploymentController: DeploymentController | None
    enableExecuteCommand: BoxedBoolean | None
    enableECSManagedTags: BoxedBoolean | None
    loadBalancers: LoadBalancers | None
    propagateTags: PropagateTags | None
    serviceRegistries: ServiceRegistries | None
    serviceConnectConfiguration: ServiceConnectConfiguration | None
    volumeConfigurations: ServiceVolumeConfigurations | None
    vpcLatticeConfigurations: VpcLatticeConfigurations | None

class UpdateServiceResponse(TypedDict, total=False):
    service: Service | None

class UpdateTaskProtectionRequest(ServiceRequest):
    cluster: String
    tasks: StringList
    protectionEnabled: Boolean
    expiresInMinutes: BoxedInteger | None

class UpdateTaskProtectionResponse(TypedDict, total=False):
    protectedTasks: ProtectedTasks | None
    failures: Failures | None

class UpdateTaskSetRequest(ServiceRequest):
    cluster: String
    service: String
    taskSet: String
    scale: Scale

class UpdateTaskSetResponse(TypedDict, total=False):
    taskSet: TaskSet | None

class EcsApi:

    service: str = "ecs"
    version: str = "2014-11-13"

    @handler("CreateCapacityProvider")
    def create_capacity_provider(self, context: RequestContext, name: String, cluster: String | None = None, auto_scaling_group_provider: AutoScalingGroupProvider | None = None, managed_instances_provider: CreateManagedInstancesProviderConfiguration | None = None, tags: Tags | None = None, **kwargs) -> CreateCapacityProviderResponse:
        raise NotImplementedError

    @handler("CreateCluster")
    def create_cluster(self, context: RequestContext, cluster_name: String | None = None, tags: Tags | None = None, settings: ClusterSettings | None = None, configuration: ClusterConfiguration | None = None, capacity_providers: StringList | None = None, default_capacity_provider_strategy: CapacityProviderStrategy | None = None, service_connect_defaults: ClusterServiceConnectDefaultsRequest | None = None, **kwargs) -> CreateClusterResponse:
        raise NotImplementedError

    @handler("CreateExpressGatewayService")
    def create_express_gateway_service(self, context: RequestContext, execution_role_arn: String, infrastructure_role_arn: String, primary_container: ExpressGatewayContainer, service_name: String | None = None, cluster: String | None = None, health_check_path: String | None = None, task_role_arn: String | None = None, network_configuration: ExpressGatewayServiceNetworkConfiguration | None = None, cpu: String | None = None, memory: String | None = None, scaling_target: ExpressGatewayScalingTarget | None = None, tags: Tags | None = None, **kwargs) -> CreateExpressGatewayServiceResponse:
        raise NotImplementedError

    @handler("CreateService")
    def create_service(self, context: RequestContext, service_name: String, cluster: String | None = None, task_definition: String | None = None, availability_zone_rebalancing: AvailabilityZoneRebalancing | None = None, load_balancers: LoadBalancers | None = None, service_registries: ServiceRegistries | None = None, desired_count: BoxedInteger | None = None, client_token: String | None = None, launch_type: LaunchType | None = None, capacity_provider_strategy: CapacityProviderStrategy | None = None, platform_version: String | None = None, role: String | None = None, deployment_configuration: DeploymentConfiguration | None = None, placement_constraints: PlacementConstraints | None = None, placement_strategy: PlacementStrategies | None = None, network_configuration: NetworkConfiguration | None = None, health_check_grace_period_seconds: BoxedInteger | None = None, scheduling_strategy: SchedulingStrategy | None = None, deployment_controller: DeploymentController | None = None, tags: Tags | None = None, enable_ecs_managed_tags: Boolean | None = None, propagate_tags: PropagateTags | None = None, enable_execute_command: Boolean | None = None, service_connect_configuration: ServiceConnectConfiguration | None = None, volume_configurations: ServiceVolumeConfigurations | None = None, vpc_lattice_configurations: VpcLatticeConfigurations | None = None, **kwargs) -> CreateServiceResponse:
        raise NotImplementedError

    @handler("CreateTaskSet")
    def create_task_set(self, context: RequestContext, service: String, cluster: String, task_definition: String, external_id: String | None = None, network_configuration: NetworkConfiguration | None = None, load_balancers: LoadBalancers | None = None, service_registries: ServiceRegistries | None = None, launch_type: LaunchType | None = None, capacity_provider_strategy: CapacityProviderStrategy | None = None, platform_version: String | None = None, scale: Scale | None = None, client_token: String | None = None, tags: Tags | None = None, **kwargs) -> CreateTaskSetResponse:
        raise NotImplementedError

    @handler("DeleteAccountSetting")
    def delete_account_setting(self, context: RequestContext, name: SettingName, principal_arn: String | None = None, **kwargs) -> DeleteAccountSettingResponse:
        raise NotImplementedError

    @handler("DeleteAttributes")
    def delete_attributes(self, context: RequestContext, attributes: Attributes, cluster: String | None = None, **kwargs) -> DeleteAttributesResponse:
        raise NotImplementedError

    @handler("DeleteCapacityProvider")
    def delete_capacity_provider(self, context: RequestContext, capacity_provider: String, cluster: String | None = None, **kwargs) -> DeleteCapacityProviderResponse:
        raise NotImplementedError

    @handler("DeleteCluster")
    def delete_cluster(self, context: RequestContext, cluster: String, **kwargs) -> DeleteClusterResponse:
        raise NotImplementedError

    @handler("DeleteExpressGatewayService")
    def delete_express_gateway_service(self, context: RequestContext, service_arn: String, **kwargs) -> DeleteExpressGatewayServiceResponse:
        raise NotImplementedError

    @handler("DeleteService")
    def delete_service(self, context: RequestContext, service: String, cluster: String | None = None, force: BoxedBoolean | None = None, **kwargs) -> DeleteServiceResponse:
        raise NotImplementedError

    @handler("DeleteTaskDefinitions")
    def delete_task_definitions(self, context: RequestContext, task_definitions: StringList, **kwargs) -> DeleteTaskDefinitionsResponse:
        raise NotImplementedError

    @handler("DeleteTaskSet")
    def delete_task_set(self, context: RequestContext, cluster: String, service: String, task_set: String, force: BoxedBoolean | None = None, **kwargs) -> DeleteTaskSetResponse:
        raise NotImplementedError

    @handler("DeregisterContainerInstance")
    def deregister_container_instance(self, context: RequestContext, container_instance: String, cluster: String | None = None, force: BoxedBoolean | None = None, **kwargs) -> DeregisterContainerInstanceResponse:
        raise NotImplementedError

    @handler("DeregisterTaskDefinition")
    def deregister_task_definition(self, context: RequestContext, task_definition: String, **kwargs) -> DeregisterTaskDefinitionResponse:
        raise NotImplementedError

    @handler("DescribeCapacityProviders")
    def describe_capacity_providers(self, context: RequestContext, capacity_providers: StringList | None = None, cluster: String | None = None, include: CapacityProviderFieldList | None = None, max_results: BoxedInteger | None = None, next_token: String | None = None, **kwargs) -> DescribeCapacityProvidersResponse:
        raise NotImplementedError

    @handler("DescribeClusters")
    def describe_clusters(self, context: RequestContext, clusters: StringList | None = None, include: ClusterFieldList | None = None, **kwargs) -> DescribeClustersResponse:
        raise NotImplementedError

    @handler("DescribeContainerInstances")
    def describe_container_instances(self, context: RequestContext, container_instances: StringList, cluster: String | None = None, include: ContainerInstanceFieldList | None = None, **kwargs) -> DescribeContainerInstancesResponse:
        raise NotImplementedError

    @handler("DescribeExpressGatewayService")
    def describe_express_gateway_service(self, context: RequestContext, service_arn: String, include: ExpressGatewayServiceIncludeList | None = None, **kwargs) -> DescribeExpressGatewayServiceResponse:
        raise NotImplementedError

    @handler("DescribeServiceDeployments")
    def describe_service_deployments(self, context: RequestContext, service_deployment_arns: StringList, **kwargs) -> DescribeServiceDeploymentsResponse:
        raise NotImplementedError

    @handler("DescribeServiceRevisions")
    def describe_service_revisions(self, context: RequestContext, service_revision_arns: StringList, **kwargs) -> DescribeServiceRevisionsResponse:
        raise NotImplementedError

    @handler("DescribeServices")
    def describe_services(self, context: RequestContext, services: StringList, cluster: String | None = None, include: ServiceFieldList | None = None, **kwargs) -> DescribeServicesResponse:
        raise NotImplementedError

    @handler("DescribeTaskDefinition")
    def describe_task_definition(self, context: RequestContext, task_definition: String, include: TaskDefinitionFieldList | None = None, **kwargs) -> DescribeTaskDefinitionResponse:
        raise NotImplementedError

    @handler("DescribeTaskSets")
    def describe_task_sets(self, context: RequestContext, cluster: String, service: String, task_sets: StringList | None = None, include: TaskSetFieldList | None = None, **kwargs) -> DescribeTaskSetsResponse:
        raise NotImplementedError

    @handler("DescribeTasks")
    def describe_tasks(self, context: RequestContext, tasks: StringList, cluster: String | None = None, include: TaskFieldList | None = None, **kwargs) -> DescribeTasksResponse:
        raise NotImplementedError

    @handler("DiscoverPollEndpoint")
    def discover_poll_endpoint(self, context: RequestContext, container_instance: String | None = None, cluster: String | None = None, **kwargs) -> DiscoverPollEndpointResponse:
        raise NotImplementedError

    @handler("ExecuteCommand")
    def execute_command(self, context: RequestContext, command: String, interactive: Boolean, task: String, cluster: String | None = None, container: String | None = None, **kwargs) -> ExecuteCommandResponse:
        raise NotImplementedError

    @handler("GetTaskProtection")
    def get_task_protection(self, context: RequestContext, cluster: String, tasks: StringList | None = None, **kwargs) -> GetTaskProtectionResponse:
        raise NotImplementedError

    @handler("ListAccountSettings")
    def list_account_settings(self, context: RequestContext, name: SettingName | None = None, value: String | None = None, principal_arn: String | None = None, effective_settings: Boolean | None = None, next_token: String | None = None, max_results: Integer | None = None, **kwargs) -> ListAccountSettingsResponse:
        raise NotImplementedError

    @handler("ListAttributes")
    def list_attributes(self, context: RequestContext, target_type: TargetType, cluster: String | None = None, attribute_name: String | None = None, attribute_value: String | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, **kwargs) -> ListAttributesResponse:
        raise NotImplementedError

    @handler("ListClusters")
    def list_clusters(self, context: RequestContext, next_token: String | None = None, max_results: BoxedInteger | None = None, **kwargs) -> ListClustersResponse:
        raise NotImplementedError

    @handler("ListContainerInstances")
    def list_container_instances(self, context: RequestContext, cluster: String | None = None, filter: String | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, status: ContainerInstanceStatus | None = None, **kwargs) -> ListContainerInstancesResponse:
        raise NotImplementedError

    @handler("ListServiceDeployments")
    def list_service_deployments(self, context: RequestContext, service: String, cluster: String | None = None, status: ServiceDeploymentStatusList | None = None, created_at: CreatedAt | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, **kwargs) -> ListServiceDeploymentsResponse:
        raise NotImplementedError

    @handler("ListServices")
    def list_services(self, context: RequestContext, cluster: String | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, launch_type: LaunchType | None = None, scheduling_strategy: SchedulingStrategy | None = None, resource_management_type: ResourceManagementType | None = None, **kwargs) -> ListServicesResponse:
        raise NotImplementedError

    @handler("ListServicesByNamespace")
    def list_services_by_namespace(self, context: RequestContext, namespace: String, next_token: String | None = None, max_results: BoxedInteger | None = None, **kwargs) -> ListServicesByNamespaceResponse:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(self, context: RequestContext, resource_arn: String, **kwargs) -> ListTagsForResourceResponse:
        raise NotImplementedError

    @handler("ListTaskDefinitionFamilies")
    def list_task_definition_families(self, context: RequestContext, family_prefix: String | None = None, status: TaskDefinitionFamilyStatus | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, **kwargs) -> ListTaskDefinitionFamiliesResponse:
        raise NotImplementedError

    @handler("ListTaskDefinitions")
    def list_task_definitions(self, context: RequestContext, family_prefix: String | None = None, status: TaskDefinitionStatus | None = None, sort: SortOrder | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, **kwargs) -> ListTaskDefinitionsResponse:
        raise NotImplementedError

    @handler("ListTasks")
    def list_tasks(self, context: RequestContext, cluster: String | None = None, container_instance: String | None = None, family: String | None = None, next_token: String | None = None, max_results: BoxedInteger | None = None, started_by: String | None = None, service_name: String | None = None, desired_status: DesiredStatus | None = None, launch_type: LaunchType | None = None, **kwargs) -> ListTasksResponse:
        raise NotImplementedError

    @handler("PutAccountSetting")
    def put_account_setting(self, context: RequestContext, name: SettingName, value: String, principal_arn: String | None = None, **kwargs) -> PutAccountSettingResponse:
        raise NotImplementedError

    @handler("PutAccountSettingDefault")
    def put_account_setting_default(self, context: RequestContext, name: SettingName, value: String, **kwargs) -> PutAccountSettingDefaultResponse:
        raise NotImplementedError

    @handler("PutAttributes")
    def put_attributes(self, context: RequestContext, attributes: Attributes, cluster: String | None = None, **kwargs) -> PutAttributesResponse:
        raise NotImplementedError

    @handler("PutClusterCapacityProviders")
    def put_cluster_capacity_providers(self, context: RequestContext, cluster: String, capacity_providers: StringList, default_capacity_provider_strategy: CapacityProviderStrategy, **kwargs) -> PutClusterCapacityProvidersResponse:
        raise NotImplementedError

    @handler("RegisterContainerInstance")
    def register_container_instance(self, context: RequestContext, cluster: String | None = None, instance_identity_document: String | None = None, instance_identity_document_signature: String | None = None, total_resources: Resources | None = None, version_info: VersionInfo | None = None, container_instance_arn: String | None = None, attributes: Attributes | None = None, platform_devices: PlatformDevices | None = None, tags: Tags | None = None, **kwargs) -> RegisterContainerInstanceResponse:
        raise NotImplementedError

    @handler("RegisterTaskDefinition")
    def register_task_definition(self, context: RequestContext, family: String, container_definitions: ContainerDefinitions, task_role_arn: String | None = None, execution_role_arn: String | None = None, network_mode: NetworkMode | None = None, volumes: VolumeList | None = None, placement_constraints: TaskDefinitionPlacementConstraints | None = None, requires_compatibilities: CompatibilityList | None = None, cpu: String | None = None, memory: String | None = None, tags: Tags | None = None, pid_mode: PidMode | None = None, ipc_mode: IpcMode | None = None, proxy_configuration: ProxyConfiguration | None = None, inference_accelerators: InferenceAccelerators | None = None, ephemeral_storage: EphemeralStorage | None = None, runtime_platform: RuntimePlatform | None = None, enable_fault_injection: BoxedBoolean | None = None, **kwargs) -> RegisterTaskDefinitionResponse:
        raise NotImplementedError

    @handler("RunTask")
    def run_task(self, context: RequestContext, task_definition: String, capacity_provider_strategy: CapacityProviderStrategy | None = None, cluster: String | None = None, count: BoxedInteger | None = None, enable_ecs_managed_tags: Boolean | None = None, enable_execute_command: Boolean | None = None, group: String | None = None, launch_type: LaunchType | None = None, network_configuration: NetworkConfiguration | None = None, overrides: TaskOverride | None = None, placement_constraints: PlacementConstraints | None = None, placement_strategy: PlacementStrategies | None = None, platform_version: String | None = None, propagate_tags: PropagateTags | None = None, reference_id: String | None = None, started_by: String | None = None, tags: Tags | None = None, client_token: String | None = None, volume_configurations: TaskVolumeConfigurations | None = None, **kwargs) -> RunTaskResponse:
        raise NotImplementedError

    @handler("StartTask")
    def start_task(self, context: RequestContext, container_instances: StringList, task_definition: String, cluster: String | None = None, enable_ecs_managed_tags: Boolean | None = None, enable_execute_command: Boolean | None = None, group: String | None = None, network_configuration: NetworkConfiguration | None = None, overrides: TaskOverride | None = None, propagate_tags: PropagateTags | None = None, reference_id: String | None = None, started_by: String | None = None, tags: Tags | None = None, volume_configurations: TaskVolumeConfigurations | None = None, **kwargs) -> StartTaskResponse:
        raise NotImplementedError

    @handler("StopServiceDeployment")
    def stop_service_deployment(self, context: RequestContext, service_deployment_arn: String, stop_type: StopServiceDeploymentStopType | None = None, **kwargs) -> StopServiceDeploymentResponse:
        raise NotImplementedError

    @handler("StopTask")
    def stop_task(self, context: RequestContext, task: String, cluster: String | None = None, reason: String | None = None, **kwargs) -> StopTaskResponse:
        raise NotImplementedError

    @handler("SubmitAttachmentStateChanges")
    def submit_attachment_state_changes(self, context: RequestContext, attachments: AttachmentStateChanges, cluster: String | None = None, **kwargs) -> SubmitAttachmentStateChangesResponse:
        raise NotImplementedError

    @handler("SubmitContainerStateChange")
    def submit_container_state_change(self, context: RequestContext, cluster: String | None = None, task: String | None = None, container_name: String | None = None, runtime_id: String | None = None, status: String | None = None, exit_code: BoxedInteger | None = None, reason: String | None = None, network_bindings: NetworkBindings | None = None, **kwargs) -> SubmitContainerStateChangeResponse:
        raise NotImplementedError

    @handler("SubmitTaskStateChange")
    def submit_task_state_change(self, context: RequestContext, cluster: String | None = None, task: String | None = None, status: String | None = None, reason: String | None = None, containers: ContainerStateChanges | None = None, attachments: AttachmentStateChanges | None = None, managed_agents: ManagedAgentStateChanges | None = None, pull_started_at: Timestamp | None = None, pull_stopped_at: Timestamp | None = None, execution_stopped_at: Timestamp | None = None, **kwargs) -> SubmitTaskStateChangeResponse:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(self, context: RequestContext, resource_arn: String, tags: Tags, **kwargs) -> TagResourceResponse:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(self, context: RequestContext, resource_arn: String, tag_keys: TagKeys, **kwargs) -> UntagResourceResponse:
        raise NotImplementedError

    @handler("UpdateCapacityProvider")
    def update_capacity_provider(self, context: RequestContext, name: String, cluster: String | None = None, auto_scaling_group_provider: AutoScalingGroupProviderUpdate | None = None, managed_instances_provider: UpdateManagedInstancesProviderConfiguration | None = None, **kwargs) -> UpdateCapacityProviderResponse:
        raise NotImplementedError

    @handler("UpdateCluster")
    def update_cluster(self, context: RequestContext, cluster: String, settings: ClusterSettings | None = None, configuration: ClusterConfiguration | None = None, service_connect_defaults: ClusterServiceConnectDefaultsRequest | None = None, **kwargs) -> UpdateClusterResponse:
        raise NotImplementedError

    @handler("UpdateClusterSettings")
    def update_cluster_settings(self, context: RequestContext, cluster: String, settings: ClusterSettings, **kwargs) -> UpdateClusterSettingsResponse:
        raise NotImplementedError

    @handler("UpdateContainerAgent")
    def update_container_agent(self, context: RequestContext, container_instance: String, cluster: String | None = None, **kwargs) -> UpdateContainerAgentResponse:
        raise NotImplementedError

    @handler("UpdateContainerInstancesState")
    def update_container_instances_state(self, context: RequestContext, container_instances: StringList, status: ContainerInstanceStatus, cluster: String | None = None, **kwargs) -> UpdateContainerInstancesStateResponse:
        raise NotImplementedError

    @handler("UpdateExpressGatewayService")
    def update_express_gateway_service(self, context: RequestContext, service_arn: String, execution_role_arn: String | None = None, health_check_path: String | None = None, primary_container: ExpressGatewayContainer | None = None, task_role_arn: String | None = None, network_configuration: ExpressGatewayServiceNetworkConfiguration | None = None, cpu: String | None = None, memory: String | None = None, scaling_target: ExpressGatewayScalingTarget | None = None, **kwargs) -> UpdateExpressGatewayServiceResponse:
        raise NotImplementedError

    @handler("UpdateService")
    def update_service(self, context: RequestContext, service: String, cluster: String | None = None, desired_count: BoxedInteger | None = None, task_definition: String | None = None, capacity_provider_strategy: CapacityProviderStrategy | None = None, deployment_configuration: DeploymentConfiguration | None = None, availability_zone_rebalancing: AvailabilityZoneRebalancing | None = None, network_configuration: NetworkConfiguration | None = None, placement_constraints: PlacementConstraints | None = None, placement_strategy: PlacementStrategies | None = None, platform_version: String | None = None, force_new_deployment: Boolean | None = None, health_check_grace_period_seconds: BoxedInteger | None = None, deployment_controller: DeploymentController | None = None, enable_execute_command: BoxedBoolean | None = None, enable_ecs_managed_tags: BoxedBoolean | None = None, load_balancers: LoadBalancers | None = None, propagate_tags: PropagateTags | None = None, service_registries: ServiceRegistries | None = None, service_connect_configuration: ServiceConnectConfiguration | None = None, volume_configurations: ServiceVolumeConfigurations | None = None, vpc_lattice_configurations: VpcLatticeConfigurations | None = None, **kwargs) -> UpdateServiceResponse:
        raise NotImplementedError

    @handler("UpdateServicePrimaryTaskSet")
    def update_service_primary_task_set(self, context: RequestContext, cluster: String, service: String, primary_task_set: String, **kwargs) -> UpdateServicePrimaryTaskSetResponse:
        raise NotImplementedError

    @handler("UpdateTaskProtection")
    def update_task_protection(self, context: RequestContext, cluster: String, tasks: StringList, protection_enabled: Boolean, expires_in_minutes: BoxedInteger | None = None, **kwargs) -> UpdateTaskProtectionResponse:
        raise NotImplementedError

    @handler("UpdateTaskSet")
    def update_task_set(self, context: RequestContext, cluster: String, service: String, task_set: String, scale: Scale, **kwargs) -> UpdateTaskSetResponse:
        raise NotImplementedError
