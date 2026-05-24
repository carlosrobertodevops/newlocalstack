from datetime import datetime
from enum import StrEnum
from typing import IO, TypedDict
from collections.abc import Iterable, Iterator

from localstack.aws.api import handler, RequestContext, ServiceException, ServiceRequest
Boolean = bool
BoxedBoolean = bool
BoxedInteger = int
Capacity = int
ClusterName = str
DescribeAddonVersionsRequestMaxResults = int
DescribeClusterVersionMaxResults = int
EksAnywhereSubscriptionName = str
FargateProfilesRequestMaxResults = int
Integer = int
ListAccessEntriesRequestMaxResults = int
ListAccessPoliciesRequestMaxResults = int
ListAddonsRequestMaxResults = int
ListAssociatedAccessPoliciesRequestMaxResults = int
ListCapabilitiesRequestMaxResults = int
ListClustersRequestMaxResults = int
ListEksAnywhereSubscriptionsRequestMaxResults = int
ListIdentityProviderConfigsRequestMaxResults = int
ListInsightsMaxResults = int
ListNodegroupsRequestMaxResults = int
ListPodIdentityAssociationsMaxResults = int
ListUpdatesRequestMaxResults = int
NonZeroInteger = int
PercentCapacity = int
RoleArn = str
String = str
TagKey = str
TagValue = str
ZeroCapacity = int
labelKey = str
labelValue = str
namespace = str
requiredClaimsKey = str
requiredClaimsValue = str
taintKey = str
taintValue = str
class AMITypes(StrEnum):
    AL2_x86_64 = "AL2_x86_64"
    AL2_x86_64_GPU = "AL2_x86_64_GPU"
    AL2_ARM_64 = "AL2_ARM_64"
    CUSTOM = "CUSTOM"
    BOTTLEROCKET_ARM_64 = "BOTTLEROCKET_ARM_64"
    BOTTLEROCKET_x86_64 = "BOTTLEROCKET_x86_64"
    BOTTLEROCKET_ARM_64_FIPS = "BOTTLEROCKET_ARM_64_FIPS"
    BOTTLEROCKET_x86_64_FIPS = "BOTTLEROCKET_x86_64_FIPS"
    BOTTLEROCKET_ARM_64_NVIDIA = "BOTTLEROCKET_ARM_64_NVIDIA"
    BOTTLEROCKET_x86_64_NVIDIA = "BOTTLEROCKET_x86_64_NVIDIA"
    BOTTLEROCKET_ARM_64_NVIDIA_FIPS = "BOTTLEROCKET_ARM_64_NVIDIA_FIPS"
    BOTTLEROCKET_x86_64_NVIDIA_FIPS = "BOTTLEROCKET_x86_64_NVIDIA_FIPS"
    WINDOWS_CORE_2019_x86_64 = "WINDOWS_CORE_2019_x86_64"
    WINDOWS_FULL_2019_x86_64 = "WINDOWS_FULL_2019_x86_64"
    WINDOWS_CORE_2022_x86_64 = "WINDOWS_CORE_2022_x86_64"
    WINDOWS_FULL_2022_x86_64 = "WINDOWS_FULL_2022_x86_64"
    WINDOWS_CORE_2025_x86_64 = "WINDOWS_CORE_2025_x86_64"
    WINDOWS_FULL_2025_x86_64 = "WINDOWS_FULL_2025_x86_64"
    AL2023_x86_64_STANDARD = "AL2023_x86_64_STANDARD"
    AL2023_ARM_64_STANDARD = "AL2023_ARM_64_STANDARD"
    AL2023_x86_64_NEURON = "AL2023_x86_64_NEURON"
    AL2023_x86_64_NVIDIA = "AL2023_x86_64_NVIDIA"
    AL2023_ARM_64_NVIDIA = "AL2023_ARM_64_NVIDIA"

class AccessScopeType(StrEnum):
    cluster = "cluster"
    namespace = "namespace"

class AddonIssueCode(StrEnum):
    AccessDenied = "AccessDenied"
    InternalFailure = "InternalFailure"
    ClusterUnreachable = "ClusterUnreachable"
    InsufficientNumberOfReplicas = "InsufficientNumberOfReplicas"
    ConfigurationConflict = "ConfigurationConflict"
    AdmissionRequestDenied = "AdmissionRequestDenied"
    UnsupportedAddonModification = "UnsupportedAddonModification"
    K8sResourceNotFound = "K8sResourceNotFound"
    AddonSubscriptionNeeded = "AddonSubscriptionNeeded"
    AddonPermissionFailure = "AddonPermissionFailure"

class AddonStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    DEGRADED = "DEGRADED"
    UPDATE_FAILED = "UPDATE_FAILED"

class ArgoCdRole(StrEnum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"

class AuthenticationMode(StrEnum):
    API = "API"
    API_AND_CONFIG_MAP = "API_AND_CONFIG_MAP"
    CONFIG_MAP = "CONFIG_MAP"

class CapabilityDeletePropagationPolicy(StrEnum):
    RETAIN = "RETAIN"

class CapabilityIssueCode(StrEnum):
    AccessDenied = "AccessDenied"
    ClusterUnreachable = "ClusterUnreachable"

class CapabilityStatus(StrEnum):
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"

class CapabilityType(StrEnum):
    ACK = "ACK"
    KRO = "KRO"
    ARGOCD = "ARGOCD"

class CapacityTypes(StrEnum):
    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"
    CAPACITY_BLOCK = "CAPACITY_BLOCK"

class Category(StrEnum):
    UPGRADE_READINESS = "UPGRADE_READINESS"
    MISCONFIGURATION = "MISCONFIGURATION"

class ClusterIssueCode(StrEnum):
    AccessDenied = "AccessDenied"
    ClusterUnreachable = "ClusterUnreachable"
    ConfigurationConflict = "ConfigurationConflict"
    InternalFailure = "InternalFailure"
    ResourceLimitExceeded = "ResourceLimitExceeded"
    ResourceNotFound = "ResourceNotFound"
    IamRoleNotFound = "IamRoleNotFound"
    VpcNotFound = "VpcNotFound"
    InsufficientFreeAddresses = "InsufficientFreeAddresses"
    Ec2ServiceNotSubscribed = "Ec2ServiceNotSubscribed"
    Ec2SubnetNotFound = "Ec2SubnetNotFound"
    Ec2SecurityGroupNotFound = "Ec2SecurityGroupNotFound"
    KmsGrantRevoked = "KmsGrantRevoked"
    KmsKeyNotFound = "KmsKeyNotFound"
    KmsKeyMarkedForDeletion = "KmsKeyMarkedForDeletion"
    KmsKeyDisabled = "KmsKeyDisabled"
    StsRegionalEndpointDisabled = "StsRegionalEndpointDisabled"
    UnsupportedVersion = "UnsupportedVersion"
    Other = "Other"

class ClusterStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    PENDING = "PENDING"

class ClusterVersionStatus(StrEnum):
    unsupported = "unsupported"
    standard_support = "standard-support"
    extended_support = "extended-support"

class ConnectorConfigProvider(StrEnum):
    EKS_ANYWHERE = "EKS_ANYWHERE"
    ANTHOS = "ANTHOS"
    GKE = "GKE"
    AKS = "AKS"
    OPENSHIFT = "OPENSHIFT"
    TANZU = "TANZU"
    RANCHER = "RANCHER"
    EC2 = "EC2"
    OTHER = "OTHER"

class EksAnywhereSubscriptionLicenseType(StrEnum):
    Cluster = "Cluster"

class EksAnywhereSubscriptionStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    EXPIRING = "EXPIRING"
    EXPIRED = "EXPIRED"
    DELETING = "DELETING"

class EksAnywhereSubscriptionTermUnit(StrEnum):
    MONTHS = "MONTHS"

class ErrorCode(StrEnum):
    SubnetNotFound = "SubnetNotFound"
    SecurityGroupNotFound = "SecurityGroupNotFound"
    EniLimitReached = "EniLimitReached"
    IpNotAvailable = "IpNotAvailable"
    AccessDenied = "AccessDenied"
    OperationNotPermitted = "OperationNotPermitted"
    VpcIdNotFound = "VpcIdNotFound"
    Unknown = "Unknown"
    NodeCreationFailure = "NodeCreationFailure"
    PodEvictionFailure = "PodEvictionFailure"
    InsufficientFreeAddresses = "InsufficientFreeAddresses"
    ClusterUnreachable = "ClusterUnreachable"
    InsufficientNumberOfReplicas = "InsufficientNumberOfReplicas"
    ConfigurationConflict = "ConfigurationConflict"
    AdmissionRequestDenied = "AdmissionRequestDenied"
    UnsupportedAddonModification = "UnsupportedAddonModification"
    K8sResourceNotFound = "K8sResourceNotFound"

class FargateProfileIssueCode(StrEnum):
    PodExecutionRoleAlreadyInUse = "PodExecutionRoleAlreadyInUse"
    AccessDenied = "AccessDenied"
    ClusterUnreachable = "ClusterUnreachable"
    InternalFailure = "InternalFailure"

class FargateProfileStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"

class InsightStatusValue(StrEnum):
    PASSING = "PASSING"
    WARNING = "WARNING"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"

class InsightsRefreshStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"

class IpFamily(StrEnum):
    ipv4 = "ipv4"
    ipv6 = "ipv6"

class LogType(StrEnum):
    api = "api"
    audit = "audit"
    authenticator = "authenticator"
    controllerManager = "controllerManager"
    scheduler = "scheduler"

class NodegroupIssueCode(StrEnum):
    AutoScalingGroupNotFound = "AutoScalingGroupNotFound"
    AutoScalingGroupInvalidConfiguration = "AutoScalingGroupInvalidConfiguration"
    Ec2SecurityGroupNotFound = "Ec2SecurityGroupNotFound"
    Ec2SecurityGroupDeletionFailure = "Ec2SecurityGroupDeletionFailure"
    Ec2LaunchTemplateNotFound = "Ec2LaunchTemplateNotFound"
    Ec2LaunchTemplateVersionMismatch = "Ec2LaunchTemplateVersionMismatch"
    Ec2SubnetNotFound = "Ec2SubnetNotFound"
    Ec2SubnetInvalidConfiguration = "Ec2SubnetInvalidConfiguration"
    IamInstanceProfileNotFound = "IamInstanceProfileNotFound"
    Ec2SubnetMissingIpv6Assignment = "Ec2SubnetMissingIpv6Assignment"
    IamLimitExceeded = "IamLimitExceeded"
    IamNodeRoleNotFound = "IamNodeRoleNotFound"
    NodeCreationFailure = "NodeCreationFailure"
    AsgInstanceLaunchFailures = "AsgInstanceLaunchFailures"
    InstanceLimitExceeded = "InstanceLimitExceeded"
    InsufficientFreeAddresses = "InsufficientFreeAddresses"
    AccessDenied = "AccessDenied"
    InternalFailure = "InternalFailure"
    ClusterUnreachable = "ClusterUnreachable"
    AmiIdNotFound = "AmiIdNotFound"
    AutoScalingGroupOptInRequired = "AutoScalingGroupOptInRequired"
    AutoScalingGroupRateLimitExceeded = "AutoScalingGroupRateLimitExceeded"
    Ec2LaunchTemplateDeletionFailure = "Ec2LaunchTemplateDeletionFailure"
    Ec2LaunchTemplateInvalidConfiguration = "Ec2LaunchTemplateInvalidConfiguration"
    Ec2LaunchTemplateMaxLimitExceeded = "Ec2LaunchTemplateMaxLimitExceeded"
    Ec2SubnetListTooLong = "Ec2SubnetListTooLong"
    IamThrottling = "IamThrottling"
    NodeTerminationFailure = "NodeTerminationFailure"
    PodEvictionFailure = "PodEvictionFailure"
    SourceEc2LaunchTemplateNotFound = "SourceEc2LaunchTemplateNotFound"
    LimitExceeded = "LimitExceeded"
    Unknown = "Unknown"
    AutoScalingGroupInstanceRefreshActive = "AutoScalingGroupInstanceRefreshActive"
    KubernetesLabelInvalid = "KubernetesLabelInvalid"
    Ec2LaunchTemplateVersionMaxLimitExceeded = "Ec2LaunchTemplateVersionMaxLimitExceeded"
    Ec2InstanceTypeDoesNotExist = "Ec2InstanceTypeDoesNotExist"

class NodegroupStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    DEGRADED = "DEGRADED"

class NodegroupUpdateStrategies(StrEnum):
    DEFAULT = "DEFAULT"
    MINIMAL = "MINIMAL"

class ProvisionedControlPlaneTier(StrEnum):
    standard = "standard"
    tier_xl = "tier-xl"
    tier_2xl = "tier-2xl"
    tier_4xl = "tier-4xl"

class RepairAction(StrEnum):
    Replace = "Replace"
    Reboot = "Reboot"
    NoAction = "NoAction"

class ResolveConflicts(StrEnum):
    OVERWRITE = "OVERWRITE"
    NONE = "NONE"
    PRESERVE = "PRESERVE"

class SsoIdentityType(StrEnum):
    SSO_USER = "SSO_USER"
    SSO_GROUP = "SSO_GROUP"

class SupportType(StrEnum):
    STANDARD = "STANDARD"
    EXTENDED = "EXTENDED"

class TaintEffect(StrEnum):
    NO_SCHEDULE = "NO_SCHEDULE"
    NO_EXECUTE = "NO_EXECUTE"
    PREFER_NO_SCHEDULE = "PREFER_NO_SCHEDULE"

class UpdateParamType(StrEnum):
    Version = "Version"
    PlatformVersion = "PlatformVersion"
    EndpointPrivateAccess = "EndpointPrivateAccess"
    EndpointPublicAccess = "EndpointPublicAccess"
    ClusterLogging = "ClusterLogging"
    DesiredSize = "DesiredSize"
    LabelsToAdd = "LabelsToAdd"
    LabelsToRemove = "LabelsToRemove"
    TaintsToAdd = "TaintsToAdd"
    TaintsToRemove = "TaintsToRemove"
    MaxSize = "MaxSize"
    MinSize = "MinSize"
    ReleaseVersion = "ReleaseVersion"
    PublicAccessCidrs = "PublicAccessCidrs"
    LaunchTemplateName = "LaunchTemplateName"
    LaunchTemplateVersion = "LaunchTemplateVersion"
    IdentityProviderConfig = "IdentityProviderConfig"
    EncryptionConfig = "EncryptionConfig"
    AddonVersion = "AddonVersion"
    ServiceAccountRoleArn = "ServiceAccountRoleArn"
    ResolveConflicts = "ResolveConflicts"
    MaxUnavailable = "MaxUnavailable"
    MaxUnavailablePercentage = "MaxUnavailablePercentage"
    NodeRepairEnabled = "NodeRepairEnabled"
    UpdateStrategy = "UpdateStrategy"
    ConfigurationValues = "ConfigurationValues"
    SecurityGroups = "SecurityGroups"
    Subnets = "Subnets"
    AuthenticationMode = "AuthenticationMode"
    PodIdentityAssociations = "PodIdentityAssociations"
    UpgradePolicy = "UpgradePolicy"
    ZonalShiftConfig = "ZonalShiftConfig"
    ComputeConfig = "ComputeConfig"
    StorageConfig = "StorageConfig"
    KubernetesNetworkConfig = "KubernetesNetworkConfig"
    RemoteNetworkConfig = "RemoteNetworkConfig"
    DeletionProtection = "DeletionProtection"
    NodeRepairConfig = "NodeRepairConfig"
    UpdatedTier = "UpdatedTier"
    PreviousTier = "PreviousTier"

class UpdateStatus(StrEnum):
    InProgress = "InProgress"
    Failed = "Failed"
    Cancelled = "Cancelled"
    Successful = "Successful"

class UpdateType(StrEnum):
    VersionUpdate = "VersionUpdate"
    EndpointAccessUpdate = "EndpointAccessUpdate"
    LoggingUpdate = "LoggingUpdate"
    ConfigUpdate = "ConfigUpdate"
    AssociateIdentityProviderConfig = "AssociateIdentityProviderConfig"
    DisassociateIdentityProviderConfig = "DisassociateIdentityProviderConfig"
    AssociateEncryptionConfig = "AssociateEncryptionConfig"
    AddonUpdate = "AddonUpdate"
    VpcConfigUpdate = "VpcConfigUpdate"
    AccessConfigUpdate = "AccessConfigUpdate"
    UpgradePolicyUpdate = "UpgradePolicyUpdate"
    ZonalShiftConfigUpdate = "ZonalShiftConfigUpdate"
    AutoModeUpdate = "AutoModeUpdate"
    RemoteNetworkConfigUpdate = "RemoteNetworkConfigUpdate"
    DeletionProtectionUpdate = "DeletionProtectionUpdate"
    ControlPlaneScalingConfigUpdate = "ControlPlaneScalingConfigUpdate"
    VendedLogsUpdate = "VendedLogsUpdate"

class VersionStatus(StrEnum):
    UNSUPPORTED = "UNSUPPORTED"
    STANDARD_SUPPORT = "STANDARD_SUPPORT"
    EXTENDED_SUPPORT = "EXTENDED_SUPPORT"

class configStatus(StrEnum):
    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"

class AccessDeniedException(ServiceException):
    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 403

class BadRequestException(ServiceException):
    code: str = "BadRequestException"
    sender_fault: bool = False
    status_code: int = 400

class ClientException(ServiceException):
    code: str = "ClientException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: String | None
    nodegroupName: String | None
    addonName: String | None
    subscriptionId: String | None

class InvalidParameterException(ServiceException):
    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: String | None
    nodegroupName: String | None
    fargateProfileName: String | None
    addonName: String | None
    subscriptionId: String | None

class InvalidRequestException(ServiceException):
    code: str = "InvalidRequestException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: String | None
    nodegroupName: String | None
    addonName: String | None
    subscriptionId: String | None

class InvalidStateException(ServiceException):
    code: str = "InvalidStateException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: String | None

class NotFoundException(ServiceException):
    code: str = "NotFoundException"
    sender_fault: bool = False
    status_code: int = 404

class ResourceInUseException(ServiceException):
    code: str = "ResourceInUseException"
    sender_fault: bool = False
    status_code: int = 409
    clusterName: String | None
    nodegroupName: String | None
    addonName: String | None

class ResourceLimitExceededException(ServiceException):
    code: str = "ResourceLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: String | None
    nodegroupName: String | None
    subscriptionId: String | None

class ResourceNotFoundException(ServiceException):
    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 404
    clusterName: String | None
    nodegroupName: String | None
    fargateProfileName: String | None
    addonName: String | None
    subscriptionId: String | None

class ResourcePropagationDelayException(ServiceException):
    code: str = "ResourcePropagationDelayException"
    sender_fault: bool = False
    status_code: int = 428

class ServerException(ServiceException):
    code: str = "ServerException"
    sender_fault: bool = False
    status_code: int = 500
    clusterName: String | None
    nodegroupName: String | None
    addonName: String | None
    subscriptionId: String | None

class ServiceUnavailableException(ServiceException):
    code: str = "ServiceUnavailableException"
    sender_fault: bool = False
    status_code: int = 503

class ThrottlingException(ServiceException):
    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 429
    clusterName: String | None

StringList = list[String]
class UnsupportedAvailabilityZoneException(ServiceException):
    code: str = "UnsupportedAvailabilityZoneException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: String | None
    nodegroupName: String | None
    validZones: StringList | None

class AccessConfigResponse(TypedDict, total=False):
    bootstrapClusterCreatorAdminPermissions: BoxedBoolean | None
    authenticationMode: AuthenticationMode | None

TagMap = dict[TagKey, TagValue]
Timestamp = datetime
AccessEntry = TypedDict("AccessEntry", {
    "clusterName": String | None,
    "principalArn": String | None,
    "kubernetesGroups": StringList | None,
    "accessEntryArn": String | None,
    "createdAt": Timestamp | None,
    "modifiedAt": Timestamp | None,
    "tags": TagMap | None,
    "username": String | None,
    "type": String | None,
}, total=False)
class AccessPolicy(TypedDict, total=False):
    name: String | None
    arn: String | None

AccessPoliciesList = list[AccessPolicy]
AccessScope = TypedDict("AccessScope", {
    "type": AccessScopeType | None,
    "namespaces": StringList | None,
}, total=False)
AdditionalInfoMap = dict[String, String]
class AddonNamespaceConfigResponse(TypedDict, total=False):
    namespace: namespace | None

class MarketplaceInformation(TypedDict, total=False):
    productId: String | None
    productUrl: String | None

class AddonIssue(TypedDict, total=False):
    code: AddonIssueCode | None
    message: String | None
    resourceIds: StringList | None

AddonIssueList = list[AddonIssue]
class AddonHealth(TypedDict, total=False):
    issues: AddonIssueList | None

class Addon(TypedDict, total=False):
    addonName: String | None
    clusterName: ClusterName | None
    status: AddonStatus | None
    addonVersion: String | None
    health: AddonHealth | None
    addonArn: String | None
    createdAt: Timestamp | None
    modifiedAt: Timestamp | None
    serviceAccountRoleArn: String | None
    tags: TagMap | None
    publisher: String | None
    owner: String | None
    marketplaceInformation: MarketplaceInformation | None
    configurationValues: String | None
    podIdentityAssociations: StringList | None
    namespaceConfig: AddonNamespaceConfigResponse | None

class AddonCompatibilityDetail(TypedDict, total=False):
    name: String | None
    compatibleVersions: StringList | None

AddonCompatibilityDetails = list[AddonCompatibilityDetail]
class Compatibility(TypedDict, total=False):
    clusterVersion: String | None
    platformVersions: StringList | None
    defaultVersion: Boolean | None

Compatibilities = list[Compatibility]
class AddonVersionInfo(TypedDict, total=False):
    addonVersion: String | None
    architecture: StringList | None
    computeTypes: StringList | None
    compatibilities: Compatibilities | None
    requiresConfiguration: Boolean | None
    requiresIamPermissions: Boolean | None

AddonVersionInfoList = list[AddonVersionInfo]
AddonInfo = TypedDict("AddonInfo", {
    "addonName": String | None,
    "type": String | None,
    "addonVersions": AddonVersionInfoList | None,
    "publisher": String | None,
    "owner": String | None,
    "marketplaceInformation": MarketplaceInformation | None,
    "defaultNamespace": String | None,
}, total=False)
class AddonNamespaceConfigRequest(TypedDict, total=False):
    namespace: namespace | None

class AddonPodIdentityAssociations(TypedDict, total=False):
    serviceAccount: String
    roleArn: String

AddonPodIdentityAssociationsList = list[AddonPodIdentityAssociations]
class AddonPodIdentityConfiguration(TypedDict, total=False):
    serviceAccount: String | None
    recommendedManagedPolicies: StringList | None

AddonPodIdentityConfigurationList = list[AddonPodIdentityConfiguration]
Addons = list[AddonInfo]
class ArgoCdAwsIdcConfigRequest(TypedDict, total=False):
    idcInstanceArn: String
    idcRegion: String | None

class ArgoCdAwsIdcConfigResponse(TypedDict, total=False):
    idcInstanceArn: String | None
    idcRegion: String | None
    idcManagedApplicationArn: String | None

class ArgoCdNetworkAccessConfigRequest(TypedDict, total=False):
    vpceIds: StringList | None

SsoIdentity = TypedDict("SsoIdentity", {
    "id": String,
    "type": SsoIdentityType,
}, total=False)
SsoIdentityList = list[SsoIdentity]
class ArgoCdRoleMapping(TypedDict, total=False):
    role: ArgoCdRole
    identities: SsoIdentityList

ArgoCdRoleMappingList = list[ArgoCdRoleMapping]
class ArgoCdConfigRequest(TypedDict, total=False):
    namespace: String | None
    awsIdc: ArgoCdAwsIdcConfigRequest
    rbacRoleMappings: ArgoCdRoleMappingList | None
    networkAccess: ArgoCdNetworkAccessConfigRequest | None

class ArgoCdNetworkAccessConfigResponse(TypedDict, total=False):
    vpceIds: StringList | None

class ArgoCdConfigResponse(TypedDict, total=False):
    namespace: String | None
    awsIdc: ArgoCdAwsIdcConfigResponse | None
    rbacRoleMappings: ArgoCdRoleMappingList | None
    networkAccess: ArgoCdNetworkAccessConfigResponse | None
    serverUrl: String | None

class AssociateAccessPolicyRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    policyArn: String
    accessScope: AccessScope

class AssociatedAccessPolicy(TypedDict, total=False):
    policyArn: String | None
    accessScope: AccessScope | None
    associatedAt: Timestamp | None
    modifiedAt: Timestamp | None

class AssociateAccessPolicyResponse(TypedDict, total=False):
    clusterName: String | None
    principalArn: String | None
    associatedAccessPolicy: AssociatedAccessPolicy | None

class Provider(TypedDict, total=False):
    keyArn: String | None

class EncryptionConfig(TypedDict, total=False):
    resources: StringList | None
    provider: Provider | None

EncryptionConfigList = list[EncryptionConfig]
class AssociateEncryptionConfigRequest(ServiceRequest):
    clusterName: String
    encryptionConfig: EncryptionConfigList
    clientRequestToken: String | None

class ErrorDetail(TypedDict, total=False):
    errorCode: ErrorCode | None
    errorMessage: String | None
    resourceIds: StringList | None

ErrorDetails = list[ErrorDetail]
UpdateParam = TypedDict("UpdateParam", {
    "type": UpdateParamType | None,
    "value": String | None,
}, total=False)
UpdateParams = list[UpdateParam]
Update = TypedDict("Update", {
    "id": String | None,
    "status": UpdateStatus | None,
    "type": UpdateType | None,
    "params": UpdateParams | None,
    "createdAt": Timestamp | None,
    "errors": ErrorDetails | None,
}, total=False)
class AssociateEncryptionConfigResponse(TypedDict, total=False):
    update: Update | None

requiredClaimsMap = dict[requiredClaimsKey, requiredClaimsValue]
class OidcIdentityProviderConfigRequest(TypedDict, total=False):
    identityProviderConfigName: String
    issuerUrl: String
    clientId: String
    usernameClaim: String | None
    usernamePrefix: String | None
    groupsClaim: String | None
    groupsPrefix: String | None
    requiredClaims: requiredClaimsMap | None

class AssociateIdentityProviderConfigRequest(ServiceRequest):
    clusterName: String
    oidc: OidcIdentityProviderConfigRequest
    tags: TagMap | None
    clientRequestToken: String | None

class AssociateIdentityProviderConfigResponse(TypedDict, total=False):
    update: Update | None
    tags: TagMap | None

AssociatedAccessPoliciesList = list[AssociatedAccessPolicy]
class AutoScalingGroup(TypedDict, total=False):
    name: String | None

AutoScalingGroupList = list[AutoScalingGroup]
class BlockStorage(TypedDict, total=False):
    enabled: BoxedBoolean | None

class CapabilityIssue(TypedDict, total=False):
    code: CapabilityIssueCode | None
    message: String | None

CapabilityIssueList = list[CapabilityIssue]
class CapabilityHealth(TypedDict, total=False):
    issues: CapabilityIssueList | None

class CapabilityConfigurationResponse(TypedDict, total=False):
    argoCd: ArgoCdConfigResponse | None

Capability = TypedDict("Capability", {
    "capabilityName": String | None,
    "arn": String | None,
    "clusterName": String | None,
    "type": CapabilityType | None,
    "roleArn": String | None,
    "status": CapabilityStatus | None,
    "version": String | None,
    "configuration": CapabilityConfigurationResponse | None,
    "tags": TagMap | None,
    "health": CapabilityHealth | None,
    "createdAt": Timestamp | None,
    "modifiedAt": Timestamp | None,
    "deletePropagationPolicy": CapabilityDeletePropagationPolicy | None,
}, total=False)
class CapabilityConfigurationRequest(TypedDict, total=False):
    argoCd: ArgoCdConfigRequest | None

CapabilitySummary = TypedDict("CapabilitySummary", {
    "capabilityName": String | None,
    "arn": String | None,
    "type": CapabilityType | None,
    "status": CapabilityStatus | None,
    "version": String | None,
    "createdAt": Timestamp | None,
    "modifiedAt": Timestamp | None,
}, total=False)
CapabilitySummaryList = list[CapabilitySummary]
CategoryList = list[Category]
class Certificate(TypedDict, total=False):
    data: String | None

class ClientStat(TypedDict, total=False):
    userAgent: String | None
    numberOfRequestsLast30Days: Integer | None
    lastRequestTime: Timestamp | None

ClientStats = list[ClientStat]
class ControlPlaneScalingConfig(TypedDict, total=False):
    tier: ProvisionedControlPlaneTier | None

class StorageConfigResponse(TypedDict, total=False):
    blockStorage: BlockStorage | None

class ComputeConfigResponse(TypedDict, total=False):
    enabled: BoxedBoolean | None
    nodePools: StringList | None
    nodeRoleArn: String | None

class RemotePodNetwork(TypedDict, total=False):
    cidrs: StringList | None

RemotePodNetworkList = list[RemotePodNetwork]
class RemoteNodeNetwork(TypedDict, total=False):
    cidrs: StringList | None

RemoteNodeNetworkList = list[RemoteNodeNetwork]
class RemoteNetworkConfigResponse(TypedDict, total=False):
    remoteNodeNetworks: RemoteNodeNetworkList | None
    remotePodNetworks: RemotePodNetworkList | None

class ZonalShiftConfigResponse(TypedDict, total=False):
    enabled: BoxedBoolean | None

class UpgradePolicyResponse(TypedDict, total=False):
    supportType: SupportType | None

class ControlPlanePlacementResponse(TypedDict, total=False):
    groupName: String | None

class OutpostConfigResponse(TypedDict, total=False):
    outpostArns: StringList
    controlPlaneInstanceType: String
    controlPlanePlacement: ControlPlanePlacementResponse | None

class ClusterIssue(TypedDict, total=False):
    code: ClusterIssueCode | None
    message: String | None
    resourceIds: StringList | None

ClusterIssueList = list[ClusterIssue]
class ClusterHealth(TypedDict, total=False):
    issues: ClusterIssueList | None

class ConnectorConfigResponse(TypedDict, total=False):
    activationId: String | None
    activationCode: String | None
    activationExpiry: Timestamp | None
    provider: String | None
    roleArn: String | None

class OIDC(TypedDict, total=False):
    issuer: String | None

class Identity(TypedDict, total=False):
    oidc: OIDC | None

LogTypes = list[LogType]
class LogSetup(TypedDict, total=False):
    types: LogTypes | None
    enabled: BoxedBoolean | None

LogSetups = list[LogSetup]
class Logging(TypedDict, total=False):
    clusterLogging: LogSetups | None

class ElasticLoadBalancing(TypedDict, total=False):
    enabled: BoxedBoolean | None

class KubernetesNetworkConfigResponse(TypedDict, total=False):
    serviceIpv4Cidr: String | None
    serviceIpv6Cidr: String | None
    ipFamily: IpFamily | None
    elasticLoadBalancing: ElasticLoadBalancing | None

class VpcConfigResponse(TypedDict, total=False):
    subnetIds: StringList | None
    securityGroupIds: StringList | None
    clusterSecurityGroupId: String | None
    vpcId: String | None
    endpointPublicAccess: Boolean | None
    endpointPrivateAccess: Boolean | None
    publicAccessCidrs: StringList | None

class Cluster(TypedDict, total=False):
    name: String | None
    arn: String | None
    createdAt: Timestamp | None
    version: String | None
    endpoint: String | None
    roleArn: String | None
    resourcesVpcConfig: VpcConfigResponse | None
    kubernetesNetworkConfig: KubernetesNetworkConfigResponse | None
    logging: Logging | None
    identity: Identity | None
    status: ClusterStatus | None
    certificateAuthority: Certificate | None
    clientRequestToken: String | None
    platformVersion: String | None
    tags: TagMap | None
    encryptionConfig: EncryptionConfigList | None
    connectorConfig: ConnectorConfigResponse | None
    id: String | None
    health: ClusterHealth | None
    outpostConfig: OutpostConfigResponse | None
    accessConfig: AccessConfigResponse | None
    upgradePolicy: UpgradePolicyResponse | None
    zonalShiftConfig: ZonalShiftConfigResponse | None
    remoteNetworkConfig: RemoteNetworkConfigResponse | None
    computeConfig: ComputeConfigResponse | None
    storageConfig: StorageConfigResponse | None
    deletionProtection: BoxedBoolean | None
    controlPlaneScalingConfig: ControlPlaneScalingConfig | None

class ClusterVersionInformation(TypedDict, total=False):
    clusterVersion: String | None
    clusterType: String | None
    defaultPlatformVersion: String | None
    defaultVersion: Boolean | None
    releaseDate: Timestamp | None
    endOfStandardSupportDate: Timestamp | None
    endOfExtendedSupportDate: Timestamp | None
    status: ClusterVersionStatus | None
    versionStatus: VersionStatus | None
    kubernetesPatchVersion: String | None

ClusterVersionList = list[ClusterVersionInformation]
class ComputeConfigRequest(TypedDict, total=False):
    enabled: BoxedBoolean | None
    nodePools: StringList | None
    nodeRoleArn: String | None

class ConnectorConfigRequest(TypedDict, total=False):
    roleArn: String
    provider: ConnectorConfigProvider

class ControlPlanePlacementRequest(TypedDict, total=False):
    groupName: String | None

class CreateAccessConfigRequest(TypedDict, total=False):
    bootstrapClusterCreatorAdminPermissions: BoxedBoolean | None
    authenticationMode: AuthenticationMode | None

CreateAccessEntryRequest = TypedDict("CreateAccessEntryRequest", {
    "clusterName": String,
    "principalArn": String,
    "kubernetesGroups": StringList | None,
    "tags": TagMap | None,
    "clientRequestToken": String | None,
    "username": String | None,
    "type": String | None,
}, total=False)
class CreateAccessEntryResponse(TypedDict, total=False):
    accessEntry: AccessEntry | None

class CreateAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String
    addonVersion: String | None
    serviceAccountRoleArn: RoleArn | None
    resolveConflicts: ResolveConflicts | None
    clientRequestToken: String | None
    tags: TagMap | None
    configurationValues: String | None
    podIdentityAssociations: AddonPodIdentityAssociationsList | None
    namespaceConfig: AddonNamespaceConfigRequest | None

class CreateAddonResponse(TypedDict, total=False):
    addon: Addon | None

CreateCapabilityRequest = TypedDict("CreateCapabilityRequest", {
    "capabilityName": String,
    "clusterName": String,
    "clientRequestToken": String | None,
    "type": CapabilityType,
    "roleArn": String,
    "configuration": CapabilityConfigurationRequest | None,
    "tags": TagMap | None,
    "deletePropagationPolicy": CapabilityDeletePropagationPolicy,
}, total=False)
class CreateCapabilityResponse(TypedDict, total=False):
    capability: Capability | None

class StorageConfigRequest(TypedDict, total=False):
    blockStorage: BlockStorage | None

class RemoteNetworkConfigRequest(TypedDict, total=False):
    remoteNodeNetworks: RemoteNodeNetworkList | None
    remotePodNetworks: RemotePodNetworkList | None

class ZonalShiftConfigRequest(TypedDict, total=False):
    enabled: BoxedBoolean | None

class UpgradePolicyRequest(TypedDict, total=False):
    supportType: SupportType | None

class OutpostConfigRequest(TypedDict, total=False):
    outpostArns: StringList
    controlPlaneInstanceType: String
    controlPlanePlacement: ControlPlanePlacementRequest | None

class KubernetesNetworkConfigRequest(TypedDict, total=False):
    serviceIpv4Cidr: String | None
    ipFamily: IpFamily | None
    elasticLoadBalancing: ElasticLoadBalancing | None

class VpcConfigRequest(TypedDict, total=False):
    subnetIds: StringList | None
    securityGroupIds: StringList | None
    endpointPublicAccess: BoxedBoolean | None
    endpointPrivateAccess: BoxedBoolean | None
    publicAccessCidrs: StringList | None

class CreateClusterRequest(ServiceRequest):
    name: ClusterName
    version: String | None
    roleArn: String
    resourcesVpcConfig: VpcConfigRequest
    kubernetesNetworkConfig: KubernetesNetworkConfigRequest | None
    logging: Logging | None
    clientRequestToken: String | None
    tags: TagMap | None
    encryptionConfig: EncryptionConfigList | None
    outpostConfig: OutpostConfigRequest | None
    accessConfig: CreateAccessConfigRequest | None
    bootstrapSelfManagedAddons: BoxedBoolean | None
    upgradePolicy: UpgradePolicyRequest | None
    zonalShiftConfig: ZonalShiftConfigRequest | None
    remoteNetworkConfig: RemoteNetworkConfigRequest | None
    computeConfig: ComputeConfigRequest | None
    storageConfig: StorageConfigRequest | None
    deletionProtection: BoxedBoolean | None
    controlPlaneScalingConfig: ControlPlaneScalingConfig | None

class CreateClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class EksAnywhereSubscriptionTerm(TypedDict, total=False):
    duration: Integer | None
    unit: EksAnywhereSubscriptionTermUnit | None

class CreateEksAnywhereSubscriptionRequest(ServiceRequest):
    name: EksAnywhereSubscriptionName
    term: EksAnywhereSubscriptionTerm
    licenseQuantity: Integer | None
    licenseType: EksAnywhereSubscriptionLicenseType | None
    autoRenew: Boolean | None
    clientRequestToken: String | None
    tags: TagMap | None

class License(TypedDict, total=False):
    id: String | None
    token: String | None

LicenseList = list[License]
class EksAnywhereSubscription(TypedDict, total=False):
    id: String | None
    arn: String | None
    createdAt: Timestamp | None
    effectiveDate: Timestamp | None
    expirationDate: Timestamp | None
    licenseQuantity: Integer | None
    licenseType: EksAnywhereSubscriptionLicenseType | None
    term: EksAnywhereSubscriptionTerm | None
    status: String | None
    autoRenew: Boolean | None
    licenseArns: StringList | None
    licenses: LicenseList | None
    tags: TagMap | None

class CreateEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: EksAnywhereSubscription | None

FargateProfileLabel = dict[String, String]
class FargateProfileSelector(TypedDict, total=False):
    namespace: String | None
    labels: FargateProfileLabel | None

FargateProfileSelectors = list[FargateProfileSelector]
class CreateFargateProfileRequest(ServiceRequest):
    fargateProfileName: String
    clusterName: String
    podExecutionRoleArn: String
    subnets: StringList | None
    selectors: FargateProfileSelectors | None
    clientRequestToken: String | None
    tags: TagMap | None

class FargateProfileIssue(TypedDict, total=False):
    code: FargateProfileIssueCode | None
    message: String | None
    resourceIds: StringList | None

FargateProfileIssueList = list[FargateProfileIssue]
class FargateProfileHealth(TypedDict, total=False):
    issues: FargateProfileIssueList | None

class FargateProfile(TypedDict, total=False):
    fargateProfileName: String | None
    fargateProfileArn: String | None
    clusterName: String | None
    createdAt: Timestamp | None
    podExecutionRoleArn: String | None
    subnets: StringList | None
    selectors: FargateProfileSelectors | None
    status: FargateProfileStatus | None
    tags: TagMap | None
    health: FargateProfileHealth | None

class CreateFargateProfileResponse(TypedDict, total=False):
    fargateProfile: FargateProfile | None

class NodeRepairConfigOverrides(TypedDict, total=False):
    nodeMonitoringCondition: String | None
    nodeUnhealthyReason: String | None
    minRepairWaitTimeMins: NonZeroInteger | None
    repairAction: RepairAction | None

NodeRepairConfigOverridesList = list[NodeRepairConfigOverrides]
class NodeRepairConfig(TypedDict, total=False):
    enabled: BoxedBoolean | None
    maxUnhealthyNodeThresholdCount: NonZeroInteger | None
    maxUnhealthyNodeThresholdPercentage: PercentCapacity | None
    maxParallelNodesRepairedCount: NonZeroInteger | None
    maxParallelNodesRepairedPercentage: PercentCapacity | None
    nodeRepairConfigOverrides: NodeRepairConfigOverridesList | None

class NodegroupUpdateConfig(TypedDict, total=False):
    maxUnavailable: NonZeroInteger | None
    maxUnavailablePercentage: PercentCapacity | None
    updateStrategy: NodegroupUpdateStrategies | None

class LaunchTemplateSpecification(TypedDict, total=False):
    name: String | None
    version: String | None
    id: String | None

class Taint(TypedDict, total=False):
    key: taintKey | None
    value: taintValue | None
    effect: TaintEffect | None

taintsList = list[Taint]
labelsMap = dict[labelKey, labelValue]
class RemoteAccessConfig(TypedDict, total=False):
    ec2SshKey: String | None
    sourceSecurityGroups: StringList | None

class NodegroupScalingConfig(TypedDict, total=False):
    minSize: ZeroCapacity | None
    maxSize: Capacity | None
    desiredSize: ZeroCapacity | None

class CreateNodegroupRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String
    scalingConfig: NodegroupScalingConfig | None
    diskSize: BoxedInteger | None
    subnets: StringList
    instanceTypes: StringList | None
    amiType: AMITypes | None
    remoteAccess: RemoteAccessConfig | None
    nodeRole: String
    labels: labelsMap | None
    taints: taintsList | None
    tags: TagMap | None
    clientRequestToken: String | None
    launchTemplate: LaunchTemplateSpecification | None
    updateConfig: NodegroupUpdateConfig | None
    nodeRepairConfig: NodeRepairConfig | None
    capacityType: CapacityTypes | None
    version: String | None
    releaseVersion: String | None

class Issue(TypedDict, total=False):
    code: NodegroupIssueCode | None
    message: String | None
    resourceIds: StringList | None

IssueList = list[Issue]
class NodegroupHealth(TypedDict, total=False):
    issues: IssueList | None

class NodegroupResources(TypedDict, total=False):
    autoScalingGroups: AutoScalingGroupList | None
    remoteAccessSecurityGroup: String | None

class Nodegroup(TypedDict, total=False):
    nodegroupName: String | None
    nodegroupArn: String | None
    clusterName: String | None
    version: String | None
    releaseVersion: String | None
    createdAt: Timestamp | None
    modifiedAt: Timestamp | None
    status: NodegroupStatus | None
    capacityType: CapacityTypes | None
    scalingConfig: NodegroupScalingConfig | None
    instanceTypes: StringList | None
    subnets: StringList | None
    remoteAccess: RemoteAccessConfig | None
    amiType: AMITypes | None
    nodeRole: String | None
    labels: labelsMap | None
    taints: taintsList | None
    resources: NodegroupResources | None
    diskSize: BoxedInteger | None
    health: NodegroupHealth | None
    updateConfig: NodegroupUpdateConfig | None
    nodeRepairConfig: NodeRepairConfig | None
    launchTemplate: LaunchTemplateSpecification | None
    tags: TagMap | None

class CreateNodegroupResponse(TypedDict, total=False):
    nodegroup: Nodegroup | None

class CreatePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    namespace: String
    serviceAccount: String
    roleArn: String
    clientRequestToken: String | None
    tags: TagMap | None
    disableSessionTags: BoxedBoolean | None
    targetRoleArn: String | None
    policy: String | None

class PodIdentityAssociation(TypedDict, total=False):
    clusterName: String | None
    namespace: String | None
    serviceAccount: String | None
    roleArn: String | None
    associationArn: String | None
    associationId: String | None
    tags: TagMap | None
    createdAt: Timestamp | None
    modifiedAt: Timestamp | None
    ownerArn: String | None
    disableSessionTags: BoxedBoolean | None
    targetRoleArn: String | None
    externalId: String | None
    policy: String | None

class CreatePodIdentityAssociationResponse(TypedDict, total=False):
    association: PodIdentityAssociation | None

class DeleteAccessEntryRequest(ServiceRequest):
    clusterName: String
    principalArn: String

class DeleteAccessEntryResponse(TypedDict, total=False):
    pass

class DeleteAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String
    preserve: Boolean | None

class DeleteAddonResponse(TypedDict, total=False):
    addon: Addon | None

class DeleteCapabilityRequest(ServiceRequest):
    clusterName: String
    capabilityName: String

class DeleteCapabilityResponse(TypedDict, total=False):
    capability: Capability | None

class DeleteClusterRequest(ServiceRequest):
    name: String

class DeleteClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class DeleteEksAnywhereSubscriptionRequest(ServiceRequest):
    id: String

class DeleteEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: EksAnywhereSubscription | None

class DeleteFargateProfileRequest(ServiceRequest):
    clusterName: String
    fargateProfileName: String

class DeleteFargateProfileResponse(TypedDict, total=False):
    fargateProfile: FargateProfile | None

class DeleteNodegroupRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String

class DeleteNodegroupResponse(TypedDict, total=False):
    nodegroup: Nodegroup | None

class DeletePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    associationId: String

class DeletePodIdentityAssociationResponse(TypedDict, total=False):
    association: PodIdentityAssociation | None

class DeprecationDetail(TypedDict, total=False):
    usage: String | None
    replacedWith: String | None
    stopServingVersion: String | None
    startServingReplacementVersion: String | None
    clientStats: ClientStats | None

DeprecationDetails = list[DeprecationDetail]
class DeregisterClusterRequest(ServiceRequest):
    name: String

class DeregisterClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class DescribeAccessEntryRequest(ServiceRequest):
    clusterName: String
    principalArn: String

class DescribeAccessEntryResponse(TypedDict, total=False):
    accessEntry: AccessEntry | None

class DescribeAddonConfigurationRequest(ServiceRequest):
    addonName: String
    addonVersion: String

class DescribeAddonConfigurationResponse(TypedDict, total=False):
    addonName: String | None
    addonVersion: String | None
    configurationSchema: String | None
    podIdentityConfiguration: AddonPodIdentityConfigurationList | None

class DescribeAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String

class DescribeAddonResponse(TypedDict, total=False):
    addon: Addon | None

class DescribeAddonVersionsRequest(ServiceRequest):
    kubernetesVersion: String | None
    maxResults: DescribeAddonVersionsRequestMaxResults | None
    nextToken: String | None
    addonName: String | None
    types: StringList | None
    publishers: StringList | None
    owners: StringList | None

class DescribeAddonVersionsResponse(TypedDict, total=False):
    addons: Addons | None
    nextToken: String | None

class DescribeCapabilityRequest(ServiceRequest):
    clusterName: String
    capabilityName: String

class DescribeCapabilityResponse(TypedDict, total=False):
    capability: Capability | None

class DescribeClusterRequest(ServiceRequest):
    name: String

class DescribeClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class DescribeClusterVersionsRequest(ServiceRequest):
    clusterType: String | None
    maxResults: DescribeClusterVersionMaxResults | None
    nextToken: String | None
    defaultOnly: BoxedBoolean | None
    includeAll: BoxedBoolean | None
    clusterVersions: StringList | None
    status: ClusterVersionStatus | None
    versionStatus: VersionStatus | None

class DescribeClusterVersionsResponse(TypedDict, total=False):
    nextToken: String | None
    clusterVersions: ClusterVersionList | None

class DescribeEksAnywhereSubscriptionRequest(ServiceRequest):
    id: String

class DescribeEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: EksAnywhereSubscription | None

class DescribeFargateProfileRequest(ServiceRequest):
    clusterName: String
    fargateProfileName: String

class DescribeFargateProfileResponse(TypedDict, total=False):
    fargateProfile: FargateProfile | None

IdentityProviderConfig = TypedDict("IdentityProviderConfig", {
    "type": String,
    "name": String,
}, total=False)
class DescribeIdentityProviderConfigRequest(ServiceRequest):
    clusterName: String
    identityProviderConfig: IdentityProviderConfig

class OidcIdentityProviderConfig(TypedDict, total=False):
    identityProviderConfigName: String | None
    identityProviderConfigArn: String | None
    clusterName: String | None
    issuerUrl: String | None
    clientId: String | None
    usernameClaim: String | None
    usernamePrefix: String | None
    groupsClaim: String | None
    groupsPrefix: String | None
    requiredClaims: requiredClaimsMap | None
    tags: TagMap | None
    status: configStatus | None

class IdentityProviderConfigResponse(TypedDict, total=False):
    oidc: OidcIdentityProviderConfig | None

class DescribeIdentityProviderConfigResponse(TypedDict, total=False):
    identityProviderConfig: IdentityProviderConfigResponse | None

class DescribeInsightRequest(ServiceRequest):
    clusterName: String
    id: String

class InsightCategorySpecificSummary(TypedDict, total=False):
    deprecationDetails: DeprecationDetails | None
    addonCompatibilityDetails: AddonCompatibilityDetails | None

class InsightStatus(TypedDict, total=False):
    status: InsightStatusValue | None
    reason: String | None

class InsightResourceDetail(TypedDict, total=False):
    insightStatus: InsightStatus | None
    kubernetesResourceUri: String | None
    arn: String | None

InsightResourceDetails = list[InsightResourceDetail]
class Insight(TypedDict, total=False):
    id: String | None
    name: String | None
    category: Category | None
    kubernetesVersion: String | None
    lastRefreshTime: Timestamp | None
    lastTransitionTime: Timestamp | None
    description: String | None
    insightStatus: InsightStatus | None
    recommendation: String | None
    additionalInfo: AdditionalInfoMap | None
    resources: InsightResourceDetails | None
    categorySpecificSummary: InsightCategorySpecificSummary | None

class DescribeInsightResponse(TypedDict, total=False):
    insight: Insight | None

class DescribeInsightsRefreshRequest(ServiceRequest):
    clusterName: String

class DescribeInsightsRefreshResponse(TypedDict, total=False):
    message: String | None
    status: InsightsRefreshStatus | None
    startedAt: Timestamp | None
    endedAt: Timestamp | None

class DescribeNodegroupRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String

class DescribeNodegroupResponse(TypedDict, total=False):
    nodegroup: Nodegroup | None

class DescribePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    associationId: String

class DescribePodIdentityAssociationResponse(TypedDict, total=False):
    association: PodIdentityAssociation | None

class DescribeUpdateRequest(ServiceRequest):
    name: String
    updateId: String
    nodegroupName: String | None
    addonName: String | None
    capabilityName: String | None

class DescribeUpdateResponse(TypedDict, total=False):
    update: Update | None

class DisassociateAccessPolicyRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    policyArn: String

class DisassociateAccessPolicyResponse(TypedDict, total=False):
    pass

class DisassociateIdentityProviderConfigRequest(ServiceRequest):
    clusterName: String
    identityProviderConfig: IdentityProviderConfig
    clientRequestToken: String | None

class DisassociateIdentityProviderConfigResponse(TypedDict, total=False):
    update: Update | None

EksAnywhereSubscriptionList = list[EksAnywhereSubscription]
EksAnywhereSubscriptionStatusValues = list[EksAnywhereSubscriptionStatus]
IdentityProviderConfigs = list[IdentityProviderConfig]
IncludeClustersList = list[String]
InsightStatusValueList = list[InsightStatusValue]
class InsightSummary(TypedDict, total=False):
    id: String | None
    name: String | None
    category: Category | None
    kubernetesVersion: String | None
    lastRefreshTime: Timestamp | None
    lastTransitionTime: Timestamp | None
    description: String | None
    insightStatus: InsightStatus | None

InsightSummaries = list[InsightSummary]
class InsightsFilter(TypedDict, total=False):
    categories: CategoryList | None
    kubernetesVersions: StringList | None
    statuses: InsightStatusValueList | None

class ListAccessEntriesRequest(ServiceRequest):
    clusterName: String
    associatedPolicyArn: String | None
    maxResults: ListAccessEntriesRequestMaxResults | None
    nextToken: String | None

class ListAccessEntriesResponse(TypedDict, total=False):
    accessEntries: StringList | None
    nextToken: String | None

class ListAccessPoliciesRequest(ServiceRequest):
    maxResults: ListAccessPoliciesRequestMaxResults | None
    nextToken: String | None

class ListAccessPoliciesResponse(TypedDict, total=False):
    accessPolicies: AccessPoliciesList | None
    nextToken: String | None

class ListAddonsRequest(ServiceRequest):
    clusterName: ClusterName
    maxResults: ListAddonsRequestMaxResults | None
    nextToken: String | None

class ListAddonsResponse(TypedDict, total=False):
    addons: StringList | None
    nextToken: String | None

class ListAssociatedAccessPoliciesRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    maxResults: ListAssociatedAccessPoliciesRequestMaxResults | None
    nextToken: String | None

class ListAssociatedAccessPoliciesResponse(TypedDict, total=False):
    clusterName: String | None
    principalArn: String | None
    nextToken: String | None
    associatedAccessPolicies: AssociatedAccessPoliciesList | None

class ListCapabilitiesRequest(ServiceRequest):
    clusterName: String
    nextToken: String | None
    maxResults: ListCapabilitiesRequestMaxResults | None

class ListCapabilitiesResponse(TypedDict, total=False):
    capabilities: CapabilitySummaryList | None
    nextToken: String | None

class ListClustersRequest(ServiceRequest):
    maxResults: ListClustersRequestMaxResults | None
    nextToken: String | None
    include: IncludeClustersList | None

class ListClustersResponse(TypedDict, total=False):
    clusters: StringList | None
    nextToken: String | None

class ListEksAnywhereSubscriptionsRequest(ServiceRequest):
    maxResults: ListEksAnywhereSubscriptionsRequestMaxResults | None
    nextToken: String | None
    includeStatus: EksAnywhereSubscriptionStatusValues | None

class ListEksAnywhereSubscriptionsResponse(TypedDict, total=False):
    subscriptions: EksAnywhereSubscriptionList | None
    nextToken: String | None

class ListFargateProfilesRequest(ServiceRequest):
    clusterName: String
    maxResults: FargateProfilesRequestMaxResults | None
    nextToken: String | None

class ListFargateProfilesResponse(TypedDict, total=False):
    fargateProfileNames: StringList | None
    nextToken: String | None

class ListIdentityProviderConfigsRequest(ServiceRequest):
    clusterName: String
    maxResults: ListIdentityProviderConfigsRequestMaxResults | None
    nextToken: String | None

class ListIdentityProviderConfigsResponse(TypedDict, total=False):
    identityProviderConfigs: IdentityProviderConfigs | None
    nextToken: String | None

class ListInsightsRequest(ServiceRequest):
    clusterName: String
    filter: InsightsFilter | None
    maxResults: ListInsightsMaxResults | None
    nextToken: String | None

class ListInsightsResponse(TypedDict, total=False):
    insights: InsightSummaries | None
    nextToken: String | None

class ListNodegroupsRequest(ServiceRequest):
    clusterName: String
    maxResults: ListNodegroupsRequestMaxResults | None
    nextToken: String | None

class ListNodegroupsResponse(TypedDict, total=False):
    nodegroups: StringList | None
    nextToken: String | None

class ListPodIdentityAssociationsRequest(ServiceRequest):
    clusterName: String
    namespace: String | None
    serviceAccount: String | None
    maxResults: ListPodIdentityAssociationsMaxResults | None
    nextToken: String | None

class PodIdentityAssociationSummary(TypedDict, total=False):
    clusterName: String | None
    namespace: String | None
    serviceAccount: String | None
    associationArn: String | None
    associationId: String | None
    ownerArn: String | None

PodIdentityAssociationSummaries = list[PodIdentityAssociationSummary]
class ListPodIdentityAssociationsResponse(TypedDict, total=False):
    associations: PodIdentityAssociationSummaries | None
    nextToken: String | None

class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: String

class ListTagsForResourceResponse(TypedDict, total=False):
    tags: TagMap | None

class ListUpdatesRequest(ServiceRequest):
    name: String
    nodegroupName: String | None
    addonName: String | None
    capabilityName: String | None
    nextToken: String | None
    maxResults: ListUpdatesRequestMaxResults | None

class ListUpdatesResponse(TypedDict, total=False):
    updateIds: StringList | None
    nextToken: String | None

class RegisterClusterRequest(ServiceRequest):
    name: ClusterName
    connectorConfig: ConnectorConfigRequest
    clientRequestToken: String | None
    tags: TagMap | None

class RegisterClusterResponse(TypedDict, total=False):
    cluster: Cluster | None

class StartInsightsRefreshRequest(ServiceRequest):
    clusterName: String

class StartInsightsRefreshResponse(TypedDict, total=False):
    message: String | None
    status: InsightsRefreshStatus | None

TagKeyList = list[TagKey]
class TagResourceRequest(ServiceRequest):
    resourceArn: String
    tags: TagMap

class TagResourceResponse(TypedDict, total=False):
    pass

class UntagResourceRequest(ServiceRequest):
    resourceArn: String
    tagKeys: TagKeyList

class UntagResourceResponse(TypedDict, total=False):
    pass

class UpdateAccessConfigRequest(TypedDict, total=False):
    authenticationMode: AuthenticationMode | None

class UpdateAccessEntryRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    kubernetesGroups: StringList | None
    clientRequestToken: String | None
    username: String | None

class UpdateAccessEntryResponse(TypedDict, total=False):
    accessEntry: AccessEntry | None

class UpdateAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String
    addonVersion: String | None
    serviceAccountRoleArn: RoleArn | None
    resolveConflicts: ResolveConflicts | None
    clientRequestToken: String | None
    configurationValues: String | None
    podIdentityAssociations: AddonPodIdentityAssociationsList | None

class UpdateAddonResponse(TypedDict, total=False):
    update: Update | None

class UpdateRoleMappings(TypedDict, total=False):
    addOrUpdateRoleMappings: ArgoCdRoleMappingList | None
    removeRoleMappings: ArgoCdRoleMappingList | None

class UpdateArgoCdConfig(TypedDict, total=False):
    rbacRoleMappings: UpdateRoleMappings | None
    networkAccess: ArgoCdNetworkAccessConfigRequest | None

class UpdateCapabilityConfiguration(TypedDict, total=False):
    argoCd: UpdateArgoCdConfig | None

class UpdateCapabilityRequest(ServiceRequest):
    clusterName: String
    capabilityName: String
    roleArn: String | None
    configuration: UpdateCapabilityConfiguration | None
    clientRequestToken: String | None
    deletePropagationPolicy: CapabilityDeletePropagationPolicy | None

class UpdateCapabilityResponse(TypedDict, total=False):
    update: Update | None

class UpdateClusterConfigRequest(ServiceRequest):
    name: String
    resourcesVpcConfig: VpcConfigRequest | None
    logging: Logging | None
    clientRequestToken: String | None
    accessConfig: UpdateAccessConfigRequest | None
    upgradePolicy: UpgradePolicyRequest | None
    zonalShiftConfig: ZonalShiftConfigRequest | None
    computeConfig: ComputeConfigRequest | None
    kubernetesNetworkConfig: KubernetesNetworkConfigRequest | None
    storageConfig: StorageConfigRequest | None
    remoteNetworkConfig: RemoteNetworkConfigRequest | None
    deletionProtection: BoxedBoolean | None
    controlPlaneScalingConfig: ControlPlaneScalingConfig | None

class UpdateClusterConfigResponse(TypedDict, total=False):
    update: Update | None

class UpdateClusterVersionRequest(ServiceRequest):
    name: String
    version: String
    clientRequestToken: String | None
    force: Boolean | None

class UpdateClusterVersionResponse(TypedDict, total=False):
    update: Update | None

class UpdateEksAnywhereSubscriptionRequest(ServiceRequest):
    id: String
    autoRenew: Boolean
    clientRequestToken: String | None

class UpdateEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: EksAnywhereSubscription | None

labelsKeyList = list[String]
class UpdateLabelsPayload(TypedDict, total=False):
    addOrUpdateLabels: labelsMap | None
    removeLabels: labelsKeyList | None

class UpdateTaintsPayload(TypedDict, total=False):
    addOrUpdateTaints: taintsList | None
    removeTaints: taintsList | None

class UpdateNodegroupConfigRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String
    labels: UpdateLabelsPayload | None
    taints: UpdateTaintsPayload | None
    scalingConfig: NodegroupScalingConfig | None
    updateConfig: NodegroupUpdateConfig | None
    nodeRepairConfig: NodeRepairConfig | None
    clientRequestToken: String | None

class UpdateNodegroupConfigResponse(TypedDict, total=False):
    update: Update | None

class UpdateNodegroupVersionRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String
    version: String | None
    releaseVersion: String | None
    launchTemplate: LaunchTemplateSpecification | None
    force: Boolean | None
    clientRequestToken: String | None

class UpdateNodegroupVersionResponse(TypedDict, total=False):
    update: Update | None

class UpdatePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    associationId: String
    roleArn: String | None
    clientRequestToken: String | None
    disableSessionTags: BoxedBoolean | None
    targetRoleArn: String | None
    policy: String | None

class UpdatePodIdentityAssociationResponse(TypedDict, total=False):
    association: PodIdentityAssociation | None

class EksApi:

    service: str = "eks"
    version: str = "2017-11-01"

    @handler("AssociateAccessPolicy")
    def associate_access_policy(self, context: RequestContext, cluster_name: String, principal_arn: String, policy_arn: String, access_scope: AccessScope, **kwargs) -> AssociateAccessPolicyResponse:
        raise NotImplementedError

    @handler("AssociateEncryptionConfig")
    def associate_encryption_config(self, context: RequestContext, cluster_name: String, encryption_config: EncryptionConfigList, client_request_token: String | None = None, **kwargs) -> AssociateEncryptionConfigResponse:
        raise NotImplementedError

    @handler("AssociateIdentityProviderConfig")
    def associate_identity_provider_config(self, context: RequestContext, cluster_name: String, oidc: OidcIdentityProviderConfigRequest, tags: TagMap | None = None, client_request_token: String | None = None, **kwargs) -> AssociateIdentityProviderConfigResponse:
        raise NotImplementedError

    @handler("CreateAccessEntry", expand=False)
    def create_access_entry(self, context: RequestContext, request: CreateAccessEntryRequest, **kwargs) -> CreateAccessEntryResponse:
        raise NotImplementedError

    @handler("CreateAddon")
    def create_addon(self, context: RequestContext, cluster_name: ClusterName, addon_name: String, addon_version: String | None = None, service_account_role_arn: RoleArn | None = None, resolve_conflicts: ResolveConflicts | None = None, client_request_token: String | None = None, tags: TagMap | None = None, configuration_values: String | None = None, pod_identity_associations: AddonPodIdentityAssociationsList | None = None, namespace_config: AddonNamespaceConfigRequest | None = None, **kwargs) -> CreateAddonResponse:
        raise NotImplementedError

    @handler("CreateCapability", expand=False)
    def create_capability(self, context: RequestContext, request: CreateCapabilityRequest, **kwargs) -> CreateCapabilityResponse:
        raise NotImplementedError

    @handler("CreateCluster")
    def create_cluster(self, context: RequestContext, name: ClusterName, role_arn: String, resources_vpc_config: VpcConfigRequest, version: String | None = None, kubernetes_network_config: KubernetesNetworkConfigRequest | None = None, logging: Logging | None = None, client_request_token: String | None = None, tags: TagMap | None = None, encryption_config: EncryptionConfigList | None = None, outpost_config: OutpostConfigRequest | None = None, access_config: CreateAccessConfigRequest | None = None, bootstrap_self_managed_addons: BoxedBoolean | None = None, upgrade_policy: UpgradePolicyRequest | None = None, zonal_shift_config: ZonalShiftConfigRequest | None = None, remote_network_config: RemoteNetworkConfigRequest | None = None, compute_config: ComputeConfigRequest | None = None, storage_config: StorageConfigRequest | None = None, deletion_protection: BoxedBoolean | None = None, control_plane_scaling_config: ControlPlaneScalingConfig | None = None, **kwargs) -> CreateClusterResponse:
        raise NotImplementedError

    @handler("CreateEksAnywhereSubscription")
    def create_eks_anywhere_subscription(self, context: RequestContext, name: EksAnywhereSubscriptionName, term: EksAnywhereSubscriptionTerm, license_quantity: Integer | None = None, license_type: EksAnywhereSubscriptionLicenseType | None = None, auto_renew: Boolean | None = None, client_request_token: String | None = None, tags: TagMap | None = None, **kwargs) -> CreateEksAnywhereSubscriptionResponse:
        raise NotImplementedError

    @handler("CreateFargateProfile")
    def create_fargate_profile(self, context: RequestContext, fargate_profile_name: String, cluster_name: String, pod_execution_role_arn: String, subnets: StringList | None = None, selectors: FargateProfileSelectors | None = None, client_request_token: String | None = None, tags: TagMap | None = None, **kwargs) -> CreateFargateProfileResponse:
        raise NotImplementedError

    @handler("CreateNodegroup")
    def create_nodegroup(self, context: RequestContext, cluster_name: String, nodegroup_name: String, subnets: StringList, node_role: String, scaling_config: NodegroupScalingConfig | None = None, disk_size: BoxedInteger | None = None, instance_types: StringList | None = None, ami_type: AMITypes | None = None, remote_access: RemoteAccessConfig | None = None, labels: labelsMap | None = None, taints: taintsList | None = None, tags: TagMap | None = None, client_request_token: String | None = None, launch_template: LaunchTemplateSpecification | None = None, update_config: NodegroupUpdateConfig | None = None, node_repair_config: NodeRepairConfig | None = None, capacity_type: CapacityTypes | None = None, version: String | None = None, release_version: String | None = None, **kwargs) -> CreateNodegroupResponse:
        raise NotImplementedError

    @handler("CreatePodIdentityAssociation")
    def create_pod_identity_association(self, context: RequestContext, cluster_name: String, namespace: String, service_account: String, role_arn: String, client_request_token: String | None = None, tags: TagMap | None = None, disable_session_tags: BoxedBoolean | None = None, target_role_arn: String | None = None, policy: String | None = None, **kwargs) -> CreatePodIdentityAssociationResponse:
        raise NotImplementedError

    @handler("DeleteAccessEntry")
    def delete_access_entry(self, context: RequestContext, cluster_name: String, principal_arn: String, **kwargs) -> DeleteAccessEntryResponse:
        raise NotImplementedError

    @handler("DeleteAddon")
    def delete_addon(self, context: RequestContext, cluster_name: ClusterName, addon_name: String, preserve: Boolean | None = None, **kwargs) -> DeleteAddonResponse:
        raise NotImplementedError

    @handler("DeleteCapability")
    def delete_capability(self, context: RequestContext, cluster_name: String, capability_name: String, **kwargs) -> DeleteCapabilityResponse:
        raise NotImplementedError

    @handler("DeleteCluster")
    def delete_cluster(self, context: RequestContext, name: String, **kwargs) -> DeleteClusterResponse:
        raise NotImplementedError

    @handler("DeleteEksAnywhereSubscription")
    def delete_eks_anywhere_subscription(self, context: RequestContext, id: String, **kwargs) -> DeleteEksAnywhereSubscriptionResponse:
        raise NotImplementedError

    @handler("DeleteFargateProfile")
    def delete_fargate_profile(self, context: RequestContext, cluster_name: String, fargate_profile_name: String, **kwargs) -> DeleteFargateProfileResponse:
        raise NotImplementedError

    @handler("DeleteNodegroup")
    def delete_nodegroup(self, context: RequestContext, cluster_name: String, nodegroup_name: String, **kwargs) -> DeleteNodegroupResponse:
        raise NotImplementedError

    @handler("DeletePodIdentityAssociation")
    def delete_pod_identity_association(self, context: RequestContext, cluster_name: String, association_id: String, **kwargs) -> DeletePodIdentityAssociationResponse:
        raise NotImplementedError

    @handler("DeregisterCluster")
    def deregister_cluster(self, context: RequestContext, name: String, **kwargs) -> DeregisterClusterResponse:
        raise NotImplementedError

    @handler("DescribeAccessEntry")
    def describe_access_entry(self, context: RequestContext, cluster_name: String, principal_arn: String, **kwargs) -> DescribeAccessEntryResponse:
        raise NotImplementedError

    @handler("DescribeAddon")
    def describe_addon(self, context: RequestContext, cluster_name: ClusterName, addon_name: String, **kwargs) -> DescribeAddonResponse:
        raise NotImplementedError

    @handler("DescribeAddonConfiguration")
    def describe_addon_configuration(self, context: RequestContext, addon_name: String, addon_version: String, **kwargs) -> DescribeAddonConfigurationResponse:
        raise NotImplementedError

    @handler("DescribeAddonVersions")
    def describe_addon_versions(self, context: RequestContext, kubernetes_version: String | None = None, max_results: DescribeAddonVersionsRequestMaxResults | None = None, next_token: String | None = None, addon_name: String | None = None, types: StringList | None = None, publishers: StringList | None = None, owners: StringList | None = None, **kwargs) -> DescribeAddonVersionsResponse:
        raise NotImplementedError

    @handler("DescribeCapability")
    def describe_capability(self, context: RequestContext, cluster_name: String, capability_name: String, **kwargs) -> DescribeCapabilityResponse:
        raise NotImplementedError

    @handler("DescribeCluster")
    def describe_cluster(self, context: RequestContext, name: String, **kwargs) -> DescribeClusterResponse:
        raise NotImplementedError

    @handler("DescribeClusterVersions")
    def describe_cluster_versions(self, context: RequestContext, cluster_type: String | None = None, max_results: DescribeClusterVersionMaxResults | None = None, next_token: String | None = None, default_only: BoxedBoolean | None = None, include_all: BoxedBoolean | None = None, cluster_versions: StringList | None = None, status: ClusterVersionStatus | None = None, version_status: VersionStatus | None = None, **kwargs) -> DescribeClusterVersionsResponse:
        raise NotImplementedError

    @handler("DescribeEksAnywhereSubscription")
    def describe_eks_anywhere_subscription(self, context: RequestContext, id: String, **kwargs) -> DescribeEksAnywhereSubscriptionResponse:
        raise NotImplementedError

    @handler("DescribeFargateProfile")
    def describe_fargate_profile(self, context: RequestContext, cluster_name: String, fargate_profile_name: String, **kwargs) -> DescribeFargateProfileResponse:
        raise NotImplementedError

    @handler("DescribeIdentityProviderConfig")
    def describe_identity_provider_config(self, context: RequestContext, cluster_name: String, identity_provider_config: IdentityProviderConfig, **kwargs) -> DescribeIdentityProviderConfigResponse:
        raise NotImplementedError

    @handler("DescribeInsight")
    def describe_insight(self, context: RequestContext, cluster_name: String, id: String, **kwargs) -> DescribeInsightResponse:
        raise NotImplementedError

    @handler("DescribeInsightsRefresh")
    def describe_insights_refresh(self, context: RequestContext, cluster_name: String, **kwargs) -> DescribeInsightsRefreshResponse:
        raise NotImplementedError

    @handler("DescribeNodegroup")
    def describe_nodegroup(self, context: RequestContext, cluster_name: String, nodegroup_name: String, **kwargs) -> DescribeNodegroupResponse:
        raise NotImplementedError

    @handler("DescribePodIdentityAssociation")
    def describe_pod_identity_association(self, context: RequestContext, cluster_name: String, association_id: String, **kwargs) -> DescribePodIdentityAssociationResponse:
        raise NotImplementedError

    @handler("DescribeUpdate")
    def describe_update(self, context: RequestContext, name: String, update_id: String, nodegroup_name: String | None = None, addon_name: String | None = None, capability_name: String | None = None, **kwargs) -> DescribeUpdateResponse:
        raise NotImplementedError

    @handler("DisassociateAccessPolicy")
    def disassociate_access_policy(self, context: RequestContext, cluster_name: String, principal_arn: String, policy_arn: String, **kwargs) -> DisassociateAccessPolicyResponse:
        raise NotImplementedError

    @handler("DisassociateIdentityProviderConfig")
    def disassociate_identity_provider_config(self, context: RequestContext, cluster_name: String, identity_provider_config: IdentityProviderConfig, client_request_token: String | None = None, **kwargs) -> DisassociateIdentityProviderConfigResponse:
        raise NotImplementedError

    @handler("ListAccessEntries")
    def list_access_entries(self, context: RequestContext, cluster_name: String, associated_policy_arn: String | None = None, max_results: ListAccessEntriesRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListAccessEntriesResponse:
        raise NotImplementedError

    @handler("ListAccessPolicies")
    def list_access_policies(self, context: RequestContext, max_results: ListAccessPoliciesRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListAccessPoliciesResponse:
        raise NotImplementedError

    @handler("ListAddons")
    def list_addons(self, context: RequestContext, cluster_name: ClusterName, max_results: ListAddonsRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListAddonsResponse:
        raise NotImplementedError

    @handler("ListAssociatedAccessPolicies")
    def list_associated_access_policies(self, context: RequestContext, cluster_name: String, principal_arn: String, max_results: ListAssociatedAccessPoliciesRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListAssociatedAccessPoliciesResponse:
        raise NotImplementedError

    @handler("ListCapabilities")
    def list_capabilities(self, context: RequestContext, cluster_name: String, next_token: String | None = None, max_results: ListCapabilitiesRequestMaxResults | None = None, **kwargs) -> ListCapabilitiesResponse:
        raise NotImplementedError

    @handler("ListClusters")
    def list_clusters(self, context: RequestContext, max_results: ListClustersRequestMaxResults | None = None, next_token: String | None = None, include: IncludeClustersList | None = None, **kwargs) -> ListClustersResponse:
        raise NotImplementedError

    @handler("ListEksAnywhereSubscriptions")
    def list_eks_anywhere_subscriptions(self, context: RequestContext, max_results: ListEksAnywhereSubscriptionsRequestMaxResults | None = None, next_token: String | None = None, include_status: EksAnywhereSubscriptionStatusValues | None = None, **kwargs) -> ListEksAnywhereSubscriptionsResponse:
        raise NotImplementedError

    @handler("ListFargateProfiles")
    def list_fargate_profiles(self, context: RequestContext, cluster_name: String, max_results: FargateProfilesRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListFargateProfilesResponse:
        raise NotImplementedError

    @handler("ListIdentityProviderConfigs")
    def list_identity_provider_configs(self, context: RequestContext, cluster_name: String, max_results: ListIdentityProviderConfigsRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListIdentityProviderConfigsResponse:
        raise NotImplementedError

    @handler("ListInsights")
    def list_insights(self, context: RequestContext, cluster_name: String, filter: InsightsFilter | None = None, max_results: ListInsightsMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListInsightsResponse:
        raise NotImplementedError

    @handler("ListNodegroups")
    def list_nodegroups(self, context: RequestContext, cluster_name: String, max_results: ListNodegroupsRequestMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListNodegroupsResponse:
        raise NotImplementedError

    @handler("ListPodIdentityAssociations")
    def list_pod_identity_associations(self, context: RequestContext, cluster_name: String, namespace: String | None = None, service_account: String | None = None, max_results: ListPodIdentityAssociationsMaxResults | None = None, next_token: String | None = None, **kwargs) -> ListPodIdentityAssociationsResponse:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(self, context: RequestContext, resource_arn: String, **kwargs) -> ListTagsForResourceResponse:
        raise NotImplementedError

    @handler("ListUpdates")
    def list_updates(self, context: RequestContext, name: String, nodegroup_name: String | None = None, addon_name: String | None = None, capability_name: String | None = None, next_token: String | None = None, max_results: ListUpdatesRequestMaxResults | None = None, **kwargs) -> ListUpdatesResponse:
        raise NotImplementedError

    @handler("RegisterCluster")
    def register_cluster(self, context: RequestContext, name: ClusterName, connector_config: ConnectorConfigRequest, client_request_token: String | None = None, tags: TagMap | None = None, **kwargs) -> RegisterClusterResponse:
        raise NotImplementedError

    @handler("StartInsightsRefresh")
    def start_insights_refresh(self, context: RequestContext, cluster_name: String, **kwargs) -> StartInsightsRefreshResponse:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(self, context: RequestContext, resource_arn: String, tags: TagMap, **kwargs) -> TagResourceResponse:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(self, context: RequestContext, resource_arn: String, tag_keys: TagKeyList, **kwargs) -> UntagResourceResponse:
        raise NotImplementedError

    @handler("UpdateAccessEntry")
    def update_access_entry(self, context: RequestContext, cluster_name: String, principal_arn: String, kubernetes_groups: StringList | None = None, client_request_token: String | None = None, username: String | None = None, **kwargs) -> UpdateAccessEntryResponse:
        raise NotImplementedError

    @handler("UpdateAddon")
    def update_addon(self, context: RequestContext, cluster_name: ClusterName, addon_name: String, addon_version: String | None = None, service_account_role_arn: RoleArn | None = None, resolve_conflicts: ResolveConflicts | None = None, client_request_token: String | None = None, configuration_values: String | None = None, pod_identity_associations: AddonPodIdentityAssociationsList | None = None, **kwargs) -> UpdateAddonResponse:
        raise NotImplementedError

    @handler("UpdateCapability")
    def update_capability(self, context: RequestContext, cluster_name: String, capability_name: String, role_arn: String | None = None, configuration: UpdateCapabilityConfiguration | None = None, client_request_token: String | None = None, delete_propagation_policy: CapabilityDeletePropagationPolicy | None = None, **kwargs) -> UpdateCapabilityResponse:
        raise NotImplementedError

    @handler("UpdateClusterConfig")
    def update_cluster_config(self, context: RequestContext, name: String, resources_vpc_config: VpcConfigRequest | None = None, logging: Logging | None = None, client_request_token: String | None = None, access_config: UpdateAccessConfigRequest | None = None, upgrade_policy: UpgradePolicyRequest | None = None, zonal_shift_config: ZonalShiftConfigRequest | None = None, compute_config: ComputeConfigRequest | None = None, kubernetes_network_config: KubernetesNetworkConfigRequest | None = None, storage_config: StorageConfigRequest | None = None, remote_network_config: RemoteNetworkConfigRequest | None = None, deletion_protection: BoxedBoolean | None = None, control_plane_scaling_config: ControlPlaneScalingConfig | None = None, **kwargs) -> UpdateClusterConfigResponse:
        raise NotImplementedError

    @handler("UpdateClusterVersion")
    def update_cluster_version(self, context: RequestContext, name: String, version: String, client_request_token: String | None = None, force: Boolean | None = None, **kwargs) -> UpdateClusterVersionResponse:
        raise NotImplementedError

    @handler("UpdateEksAnywhereSubscription")
    def update_eks_anywhere_subscription(self, context: RequestContext, id: String, auto_renew: Boolean, client_request_token: String | None = None, **kwargs) -> UpdateEksAnywhereSubscriptionResponse:
        raise NotImplementedError

    @handler("UpdateNodegroupConfig")
    def update_nodegroup_config(self, context: RequestContext, cluster_name: String, nodegroup_name: String, labels: UpdateLabelsPayload | None = None, taints: UpdateTaintsPayload | None = None, scaling_config: NodegroupScalingConfig | None = None, update_config: NodegroupUpdateConfig | None = None, node_repair_config: NodeRepairConfig | None = None, client_request_token: String | None = None, **kwargs) -> UpdateNodegroupConfigResponse:
        raise NotImplementedError

    @handler("UpdateNodegroupVersion")
    def update_nodegroup_version(self, context: RequestContext, cluster_name: String, nodegroup_name: String, version: String | None = None, release_version: String | None = None, launch_template: LaunchTemplateSpecification | None = None, force: Boolean | None = None, client_request_token: String | None = None, **kwargs) -> UpdateNodegroupVersionResponse:
        raise NotImplementedError

    @handler("UpdatePodIdentityAssociation")
    def update_pod_identity_association(self, context: RequestContext, cluster_name: String, association_id: String, role_arn: String | None = None, client_request_token: String | None = None, disable_session_tags: BoxedBoolean | None = None, target_role_arn: String | None = None, policy: String | None = None, **kwargs) -> UpdatePodIdentityAssociationResponse:
        raise NotImplementedError
