from datetime import datetime
from enum import StrEnum
from typing import IO, TypedDict
from collections.abc import Iterable, Iterator

from localstack.aws.api import handler, RequestContext, ServiceException, ServiceRequest
Arn = str
AuthUserName = str
AwsBackupRecoveryPointArn = str
BlueGreenDeploymentIdentifier = str
BlueGreenDeploymentName = str
BlueGreenDeploymentStatus = str
BlueGreenDeploymentStatusDetails = str
BlueGreenDeploymentTaskName = str
BlueGreenDeploymentTaskStatus = str
Boolean = bool
BooleanOptional = bool
BucketName = str
CustomDBEngineVersionManifest = str
CustomEngineName = str
CustomEngineVersion = str
DBClusterIdentifier = str
DBProxyEndpointName = str
DBProxyName = str
DBProxyTargetGroupName = str
DBShardGroupIdentifier = str
DataFilter = str
DatabaseArn = str
Description = str
Double = float
DoubleOptional = float
Engine = str
GlobalClusterIdentifier = str
Integer = int
IntegerOptional = int
IntegrationArn = str
IntegrationDescription = str
IntegrationIdentifier = str
IntegrationName = str
KmsKeyIdOrArn = str
MajorEngineVersion = str
Marker = str
MaxRecords = int
OperatorSensitiveString = str
PotentiallySensitiveOptionSettingValue = str
PotentiallySensitiveParameterValue = str
SensitiveString = str
SourceArn = str
String = str
String255 = str
SwitchoverDetailStatus = str
SwitchoverTimeout = int
TargetDBClusterParameterGroupName = str
TargetDBInstanceClass = str
TargetDBParameterGroupName = str
TargetEngineVersion = str
TargetStorageType = str
class ActivityStreamMode(StrEnum):
    sync = "sync"
    async_ = "async"

class ActivityStreamPolicyStatus(StrEnum):
    locked = "locked"
    unlocked = "unlocked"
    locking_policy = "locking-policy"
    unlocking_policy = "unlocking-policy"

class ActivityStreamStatus(StrEnum):
    stopped = "stopped"
    starting = "starting"
    started = "started"
    stopping = "stopping"

class ApplyMethod(StrEnum):
    immediate = "immediate"
    pending_reboot = "pending-reboot"

class AuditPolicyState(StrEnum):
    locked = "locked"
    unlocked = "unlocked"

class AuthScheme(StrEnum):
    SECRETS = "SECRETS"

class AutomationMode(StrEnum):
    full = "full"
    all_paused = "all-paused"

class ClientPasswordAuthType(StrEnum):
    MYSQL_NATIVE_PASSWORD = "MYSQL_NATIVE_PASSWORD"
    MYSQL_CACHING_SHA2_PASSWORD = "MYSQL_CACHING_SHA2_PASSWORD"
    POSTGRES_SCRAM_SHA_256 = "POSTGRES_SCRAM_SHA_256"
    POSTGRES_MD5 = "POSTGRES_MD5"
    SQL_SERVER_AUTHENTICATION = "SQL_SERVER_AUTHENTICATION"

class ClusterScalabilityType(StrEnum):
    standard = "standard"
    limitless = "limitless"

class CustomEngineVersionStatus(StrEnum):
    available = "available"
    inactive = "inactive"
    inactive_except_restore = "inactive-except-restore"

class DBProxyEndpointStatus(StrEnum):
    available = "available"
    modifying = "modifying"
    incompatible_network = "incompatible-network"
    insufficient_resource_limits = "insufficient-resource-limits"
    creating = "creating"
    deleting = "deleting"

class DBProxyEndpointTargetRole(StrEnum):
    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"

class DBProxyStatus(StrEnum):
    available = "available"
    modifying = "modifying"
    incompatible_network = "incompatible-network"
    insufficient_resource_limits = "insufficient-resource-limits"
    creating = "creating"
    deleting = "deleting"
    suspended = "suspended"
    suspending = "suspending"
    reactivating = "reactivating"

class DatabaseInsightsMode(StrEnum):
    standard = "standard"
    advanced = "advanced"

class DefaultAuthScheme(StrEnum):
    IAM_AUTH = "IAM_AUTH"
    NONE = "NONE"

class EndpointNetworkType(StrEnum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUAL = "DUAL"

class EngineFamily(StrEnum):
    MYSQL = "MYSQL"
    POSTGRESQL = "POSTGRESQL"
    SQLSERVER = "SQLSERVER"

class ExportSourceType(StrEnum):
    SNAPSHOT = "SNAPSHOT"
    CLUSTER = "CLUSTER"

class FailoverStatus(StrEnum):
    pending = "pending"
    failing_over = "failing-over"
    cancelling = "cancelling"

class GlobalClusterMemberSynchronizationStatus(StrEnum):
    connected = "connected"
    pending_resync = "pending-resync"

class IAMAuthMode(StrEnum):
    DISABLED = "DISABLED"
    REQUIRED = "REQUIRED"
    ENABLED = "ENABLED"

class IntegrationStatus(StrEnum):
    creating = "creating"
    active = "active"
    modifying = "modifying"
    failed = "failed"
    deleting = "deleting"
    syncing = "syncing"
    needs_attention = "needs_attention"

class LifecycleSupportName(StrEnum):
    open_source_rds_standard_support = "open-source-rds-standard-support"
    open_source_rds_extended_support = "open-source-rds-extended-support"

class LimitlessDatabaseStatus(StrEnum):
    active = "active"
    not_in_use = "not-in-use"
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"
    modifying_max_capacity = "modifying-max-capacity"
    error = "error"

class LocalWriteForwardingStatus(StrEnum):
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"
    requested = "requested"

class MasterUserAuthenticationType(StrEnum):
    password = "password"
    iam_db_auth = "iam-db-auth"

class ReplicaMode(StrEnum):
    open_read_only = "open-read-only"
    mounted = "mounted"

class SourceType(StrEnum):
    db_instance = "db-instance"
    db_parameter_group = "db-parameter-group"
    db_security_group = "db-security-group"
    db_snapshot = "db-snapshot"
    db_cluster = "db-cluster"
    db_cluster_snapshot = "db-cluster-snapshot"
    custom_engine_version = "custom-engine-version"
    db_proxy = "db-proxy"
    blue_green_deployment = "blue-green-deployment"
    db_shard_group = "db-shard-group"
    zero_etl = "zero-etl"

class StorageEncryptionType(StrEnum):
    none = "none"
    sse_kms = "sse-kms"
    sse_rds = "sse-rds"

class TargetConnectionNetworkType(StrEnum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"

class TargetHealthReason(StrEnum):
    UNREACHABLE = "UNREACHABLE"
    CONNECTION_FAILED = "CONNECTION_FAILED"
    AUTH_FAILURE = "AUTH_FAILURE"
    PENDING_PROXY_CAPACITY = "PENDING_PROXY_CAPACITY"
    INVALID_REPLICATION_STATE = "INVALID_REPLICATION_STATE"
    PROMOTED = "PROMOTED"

class TargetRole(StrEnum):
    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"
    UNKNOWN = "UNKNOWN"

class TargetState(StrEnum):
    REGISTERING = "REGISTERING"
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    UNUSED = "UNUSED"

class TargetType(StrEnum):
    RDS_INSTANCE = "RDS_INSTANCE"
    RDS_SERVERLESS_ENDPOINT = "RDS_SERVERLESS_ENDPOINT"
    TRACKED_CLUSTER = "TRACKED_CLUSTER"

class UpgradeRolloutOrder(StrEnum):
    first = "first"
    second = "second"
    last = "last"

class WriteForwardingStatus(StrEnum):
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"
    unknown = "unknown"

class AuthorizationAlreadyExistsFault(ServiceException):
    code: str = "AuthorizationAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class AuthorizationNotFoundFault(ServiceException):
    code: str = "AuthorizationNotFound"
    sender_fault: bool = True
    status_code: int = 404

class AuthorizationQuotaExceededFault(ServiceException):
    code: str = "AuthorizationQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class BackupPolicyNotFoundFault(ServiceException):
    code: str = "BackupPolicyNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class BlueGreenDeploymentAlreadyExistsFault(ServiceException):
    code: str = "BlueGreenDeploymentAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class BlueGreenDeploymentNotFoundFault(ServiceException):
    code: str = "BlueGreenDeploymentNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class CertificateNotFoundFault(ServiceException):
    code: str = "CertificateNotFound"
    sender_fault: bool = True
    status_code: int = 404

class CreateCustomDBEngineVersionFault(ServiceException):
    code: str = "CreateCustomDBEngineVersionFault"
    sender_fault: bool = True
    status_code: int = 400

class CustomAvailabilityZoneNotFoundFault(ServiceException):
    code: str = "CustomAvailabilityZoneNotFound"
    sender_fault: bool = True
    status_code: int = 404

class CustomDBEngineVersionAlreadyExistsFault(ServiceException):
    code: str = "CustomDBEngineVersionAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class CustomDBEngineVersionNotFoundFault(ServiceException):
    code: str = "CustomDBEngineVersionNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class CustomDBEngineVersionQuotaExceededFault(ServiceException):
    code: str = "CustomDBEngineVersionQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterAlreadyExistsFault(ServiceException):
    code: str = "DBClusterAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterAutomatedBackupNotFoundFault(ServiceException):
    code: str = "DBClusterAutomatedBackupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBClusterAutomatedBackupQuotaExceededFault(ServiceException):
    code: str = "DBClusterAutomatedBackupQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterBacktrackNotFoundFault(ServiceException):
    code: str = "DBClusterBacktrackNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBClusterEndpointAlreadyExistsFault(ServiceException):
    code: str = "DBClusterEndpointAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterEndpointNotFoundFault(ServiceException):
    code: str = "DBClusterEndpointNotFoundFault"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterEndpointQuotaExceededFault(ServiceException):
    code: str = "DBClusterEndpointQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 403

class DBClusterNotFoundFault(ServiceException):
    code: str = "DBClusterNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBClusterParameterGroupNotFoundFault(ServiceException):
    code: str = "DBClusterParameterGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBClusterQuotaExceededFault(ServiceException):
    code: str = "DBClusterQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 403

class DBClusterRoleAlreadyExistsFault(ServiceException):
    code: str = "DBClusterRoleAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterRoleNotFoundFault(ServiceException):
    code: str = "DBClusterRoleNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBClusterRoleQuotaExceededFault(ServiceException):
    code: str = "DBClusterRoleQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterSnapshotAlreadyExistsFault(ServiceException):
    code: str = "DBClusterSnapshotAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class DBClusterSnapshotNotFoundFault(ServiceException):
    code: str = "DBClusterSnapshotNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBInstanceAlreadyExistsFault(ServiceException):
    code: str = "DBInstanceAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBInstanceAutomatedBackupNotFoundFault(ServiceException):
    code: str = "DBInstanceAutomatedBackupNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBInstanceAutomatedBackupQuotaExceededFault(ServiceException):
    code: str = "DBInstanceAutomatedBackupQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class DBInstanceNotFoundFault(ServiceException):
    code: str = "DBInstanceNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBInstanceNotReadyFault(ServiceException):
    code: str = "DBInstanceNotReady"
    sender_fault: bool = True
    status_code: int = 400

class DBInstanceRoleAlreadyExistsFault(ServiceException):
    code: str = "DBInstanceRoleAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBInstanceRoleNotFoundFault(ServiceException):
    code: str = "DBInstanceRoleNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBInstanceRoleQuotaExceededFault(ServiceException):
    code: str = "DBInstanceRoleQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class DBLogFileNotFoundFault(ServiceException):
    code: str = "DBLogFileNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBParameterGroupAlreadyExistsFault(ServiceException):
    code: str = "DBParameterGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBParameterGroupNotFoundFault(ServiceException):
    code: str = "DBParameterGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBParameterGroupQuotaExceededFault(ServiceException):
    code: str = "DBParameterGroupQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class DBProxyAlreadyExistsFault(ServiceException):
    code: str = "DBProxyAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class DBProxyEndpointAlreadyExistsFault(ServiceException):
    code: str = "DBProxyEndpointAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class DBProxyEndpointNotFoundFault(ServiceException):
    code: str = "DBProxyEndpointNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBProxyEndpointQuotaExceededFault(ServiceException):
    code: str = "DBProxyEndpointQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class DBProxyNotFoundFault(ServiceException):
    code: str = "DBProxyNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBProxyQuotaExceededFault(ServiceException):
    code: str = "DBProxyQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class DBProxyTargetAlreadyRegisteredFault(ServiceException):
    code: str = "DBProxyTargetAlreadyRegisteredFault"
    sender_fault: bool = True
    status_code: int = 400

class DBProxyTargetGroupNotFoundFault(ServiceException):
    code: str = "DBProxyTargetGroupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBProxyTargetNotFoundFault(ServiceException):
    code: str = "DBProxyTargetNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBSecurityGroupAlreadyExistsFault(ServiceException):
    code: str = "DBSecurityGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBSecurityGroupNotFoundFault(ServiceException):
    code: str = "DBSecurityGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBSecurityGroupNotSupportedFault(ServiceException):
    code: str = "DBSecurityGroupNotSupported"
    sender_fault: bool = True
    status_code: int = 400

class DBSecurityGroupQuotaExceededFault(ServiceException):
    code: str = "QuotaExceeded.DBSecurityGroup"
    sender_fault: bool = True
    status_code: int = 400

class DBShardGroupAlreadyExistsFault(ServiceException):
    code: str = "DBShardGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBShardGroupNotFoundFault(ServiceException):
    code: str = "DBShardGroupNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBSnapshotAlreadyExistsFault(ServiceException):
    code: str = "DBSnapshotAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBSnapshotNotFoundFault(ServiceException):
    code: str = "DBSnapshotNotFound"
    sender_fault: bool = True
    status_code: int = 404

class DBSnapshotTenantDatabaseNotFoundFault(ServiceException):
    code: str = "DBSnapshotTenantDatabaseNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBSubnetGroupAlreadyExistsFault(ServiceException):
    code: str = "DBSubnetGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class DBSubnetGroupDoesNotCoverEnoughAZs(ServiceException):
    code: str = "DBSubnetGroupDoesNotCoverEnoughAZs"
    sender_fault: bool = True
    status_code: int = 400

class DBSubnetGroupNotAllowedFault(ServiceException):
    code: str = "DBSubnetGroupNotAllowedFault"
    sender_fault: bool = True
    status_code: int = 400

class DBSubnetGroupNotFoundFault(ServiceException):
    code: str = "DBSubnetGroupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class DBSubnetGroupQuotaExceededFault(ServiceException):
    code: str = "DBSubnetGroupQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class DBSubnetQuotaExceededFault(ServiceException):
    code: str = "DBSubnetQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class DBUpgradeDependencyFailureFault(ServiceException):
    code: str = "DBUpgradeDependencyFailure"
    sender_fault: bool = True
    status_code: int = 400

class DomainNotFoundFault(ServiceException):
    code: str = "DomainNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class Ec2ImagePropertiesNotSupportedFault(ServiceException):
    code: str = "Ec2ImagePropertiesNotSupportedFault"
    sender_fault: bool = True
    status_code: int = 400

class EventSubscriptionQuotaExceededFault(ServiceException):
    code: str = "EventSubscriptionQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class ExportTaskAlreadyExistsFault(ServiceException):
    code: str = "ExportTaskAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class ExportTaskNotFoundFault(ServiceException):
    code: str = "ExportTaskNotFound"
    sender_fault: bool = True
    status_code: int = 404

class GlobalClusterAlreadyExistsFault(ServiceException):
    code: str = "GlobalClusterAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class GlobalClusterNotFoundFault(ServiceException):
    code: str = "GlobalClusterNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class GlobalClusterQuotaExceededFault(ServiceException):
    code: str = "GlobalClusterQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class IamRoleMissingPermissionsFault(ServiceException):
    code: str = "IamRoleMissingPermissions"
    sender_fault: bool = True
    status_code: int = 400

class IamRoleNotFoundFault(ServiceException):
    code: str = "IamRoleNotFound"
    sender_fault: bool = True
    status_code: int = 404

class InstanceQuotaExceededFault(ServiceException):
    code: str = "InstanceQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class InsufficientAvailableIPsInSubnetFault(ServiceException):
    code: str = "InsufficientAvailableIPsInSubnetFault"
    sender_fault: bool = True
    status_code: int = 400

class InsufficientDBClusterCapacityFault(ServiceException):
    code: str = "InsufficientDBClusterCapacityFault"
    sender_fault: bool = True
    status_code: int = 403

class InsufficientDBInstanceCapacityFault(ServiceException):
    code: str = "InsufficientDBInstanceCapacity"
    sender_fault: bool = True
    status_code: int = 400

class InsufficientStorageClusterCapacityFault(ServiceException):
    code: str = "InsufficientStorageClusterCapacity"
    sender_fault: bool = True
    status_code: int = 400

class IntegrationAlreadyExistsFault(ServiceException):
    code: str = "IntegrationAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class IntegrationConflictOperationFault(ServiceException):
    code: str = "IntegrationConflictOperationFault"
    sender_fault: bool = True
    status_code: int = 400

class IntegrationNotFoundFault(ServiceException):
    code: str = "IntegrationNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class IntegrationQuotaExceededFault(ServiceException):
    code: str = "IntegrationQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidBlueGreenDeploymentStateFault(ServiceException):
    code: str = "InvalidBlueGreenDeploymentStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidCustomDBEngineVersionStateFault(ServiceException):
    code: str = "InvalidCustomDBEngineVersionStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBClusterAutomatedBackupStateFault(ServiceException):
    code: str = "InvalidDBClusterAutomatedBackupStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBClusterCapacityFault(ServiceException):
    code: str = "InvalidDBClusterCapacityFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBClusterEndpointStateFault(ServiceException):
    code: str = "InvalidDBClusterEndpointStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBClusterSnapshotStateFault(ServiceException):
    code: str = "InvalidDBClusterSnapshotStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBClusterStateFault(ServiceException):
    code: str = "InvalidDBClusterStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBInstanceAutomatedBackupStateFault(ServiceException):
    code: str = "InvalidDBInstanceAutomatedBackupState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBInstanceStateFault(ServiceException):
    code: str = "InvalidDBInstanceState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBParameterGroupStateFault(ServiceException):
    code: str = "InvalidDBParameterGroupState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBProxyEndpointStateFault(ServiceException):
    code: str = "InvalidDBProxyEndpointStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBProxyStateFault(ServiceException):
    code: str = "InvalidDBProxyStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBSecurityGroupStateFault(ServiceException):
    code: str = "InvalidDBSecurityGroupState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBShardGroupStateFault(ServiceException):
    code: str = "InvalidDBShardGroupState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBSnapshotStateFault(ServiceException):
    code: str = "InvalidDBSnapshotState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBSubnetGroupFault(ServiceException):
    code: str = "InvalidDBSubnetGroupFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBSubnetGroupStateFault(ServiceException):
    code: str = "InvalidDBSubnetGroupStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidDBSubnetStateFault(ServiceException):
    code: str = "InvalidDBSubnetStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidEventSubscriptionStateFault(ServiceException):
    code: str = "InvalidEventSubscriptionState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidExportOnlyFault(ServiceException):
    code: str = "InvalidExportOnly"
    sender_fault: bool = True
    status_code: int = 400

class InvalidExportSourceStateFault(ServiceException):
    code: str = "InvalidExportSourceState"
    sender_fault: bool = True
    status_code: int = 400

class InvalidExportTaskStateFault(ServiceException):
    code: str = "InvalidExportTaskStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidGlobalClusterStateFault(ServiceException):
    code: str = "InvalidGlobalClusterStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidIntegrationStateFault(ServiceException):
    code: str = "InvalidIntegrationStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidOptionGroupStateFault(ServiceException):
    code: str = "InvalidOptionGroupStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidResourceStateFault(ServiceException):
    code: str = "InvalidResourceStateFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidRestoreFault(ServiceException):
    code: str = "InvalidRestoreFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidS3BucketFault(ServiceException):
    code: str = "InvalidS3BucketFault"
    sender_fault: bool = True
    status_code: int = 400

class InvalidSubnet(ServiceException):
    code: str = "InvalidSubnet"
    sender_fault: bool = True
    status_code: int = 400

class InvalidVPCNetworkStateFault(ServiceException):
    code: str = "InvalidVPCNetworkStateFault"
    sender_fault: bool = True
    status_code: int = 400

class KMSKeyNotAccessibleFault(ServiceException):
    code: str = "KMSKeyNotAccessibleFault"
    sender_fault: bool = True
    status_code: int = 400

class MaxDBShardGroupLimitReached(ServiceException):
    code: str = "MaxDBShardGroupLimitReached"
    sender_fault: bool = True
    status_code: int = 400

class NetworkTypeNotSupported(ServiceException):
    code: str = "NetworkTypeNotSupported"
    sender_fault: bool = True
    status_code: int = 400

class OptionGroupAlreadyExistsFault(ServiceException):
    code: str = "OptionGroupAlreadyExistsFault"
    sender_fault: bool = True
    status_code: int = 400

class OptionGroupNotFoundFault(ServiceException):
    code: str = "OptionGroupNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class OptionGroupQuotaExceededFault(ServiceException):
    code: str = "OptionGroupQuotaExceededFault"
    sender_fault: bool = True
    status_code: int = 400

class PointInTimeRestoreNotEnabledFault(ServiceException):
    code: str = "PointInTimeRestoreNotEnabled"
    sender_fault: bool = True
    status_code: int = 400

class ProvisionedIopsNotAvailableInAZFault(ServiceException):
    code: str = "ProvisionedIopsNotAvailableInAZFault"
    sender_fault: bool = True
    status_code: int = 400

class ReservedDBInstanceAlreadyExistsFault(ServiceException):
    code: str = "ReservedDBInstanceAlreadyExists"
    sender_fault: bool = True
    status_code: int = 404

class ReservedDBInstanceNotFoundFault(ServiceException):
    code: str = "ReservedDBInstanceNotFound"
    sender_fault: bool = True
    status_code: int = 404

class ReservedDBInstanceQuotaExceededFault(ServiceException):
    code: str = "ReservedDBInstanceQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class ReservedDBInstancesOfferingNotFoundFault(ServiceException):
    code: str = "ReservedDBInstancesOfferingNotFound"
    sender_fault: bool = True
    status_code: int = 404

class ResourceNotFoundFault(ServiceException):
    code: str = "ResourceNotFoundFault"
    sender_fault: bool = True
    status_code: int = 404

class SNSInvalidTopicFault(ServiceException):
    code: str = "SNSInvalidTopic"
    sender_fault: bool = True
    status_code: int = 400

class SNSNoAuthorizationFault(ServiceException):
    code: str = "SNSNoAuthorization"
    sender_fault: bool = True
    status_code: int = 400

class SNSTopicArnNotFoundFault(ServiceException):
    code: str = "SNSTopicArnNotFound"
    sender_fault: bool = True
    status_code: int = 404

class SharedSnapshotQuotaExceededFault(ServiceException):
    code: str = "SharedSnapshotQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class SnapshotQuotaExceededFault(ServiceException):
    code: str = "SnapshotQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class SourceClusterNotSupportedFault(ServiceException):
    code: str = "SourceClusterNotSupportedFault"
    sender_fault: bool = True
    status_code: int = 400

class SourceDatabaseNotSupportedFault(ServiceException):
    code: str = "SourceDatabaseNotSupportedFault"
    sender_fault: bool = True
    status_code: int = 400

class SourceNotFoundFault(ServiceException):
    code: str = "SourceNotFound"
    sender_fault: bool = True
    status_code: int = 404

class StorageQuotaExceededFault(ServiceException):
    code: str = "StorageQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class StorageTypeNotAvailableFault(ServiceException):
    code: str = "StorageTypeNotAvailableFault"
    sender_fault: bool = True
    status_code: int = 400

class StorageTypeNotSupportedFault(ServiceException):
    code: str = "StorageTypeNotSupported"
    sender_fault: bool = True
    status_code: int = 400

class SubnetAlreadyInUse(ServiceException):
    code: str = "SubnetAlreadyInUse"
    sender_fault: bool = True
    status_code: int = 400

class SubscriptionAlreadyExistFault(ServiceException):
    code: str = "SubscriptionAlreadyExist"
    sender_fault: bool = True
    status_code: int = 400

class SubscriptionCategoryNotFoundFault(ServiceException):
    code: str = "SubscriptionCategoryNotFound"
    sender_fault: bool = True
    status_code: int = 404

class SubscriptionNotFoundFault(ServiceException):
    code: str = "SubscriptionNotFound"
    sender_fault: bool = True
    status_code: int = 404

class TenantDatabaseAlreadyExistsFault(ServiceException):
    code: str = "TenantDatabaseAlreadyExists"
    sender_fault: bool = True
    status_code: int = 400

class TenantDatabaseNotFoundFault(ServiceException):
    code: str = "TenantDatabaseNotFound"
    sender_fault: bool = True
    status_code: int = 404

class TenantDatabaseQuotaExceededFault(ServiceException):
    code: str = "TenantDatabaseQuotaExceeded"
    sender_fault: bool = True
    status_code: int = 400

class UnsupportedDBEngineVersionFault(ServiceException):
    code: str = "UnsupportedDBEngineVersion"
    sender_fault: bool = True
    status_code: int = 400

class VpcEncryptionControlViolationException(ServiceException):
    code: str = "VpcEncryptionControlViolationException"
    sender_fault: bool = True
    status_code: int = 400

Long = int
class AccountQuota(TypedDict, total=False):
    AccountQuotaName: String | None
    Used: Long | None
    Max: Long | None

AccountQuotaList = list[AccountQuota]
class AccountAttributesMessage(TypedDict, total=False):
    AccountQuotas: AccountQuotaList | None

ActivityStreamModeList = list[String]
class AddRoleToDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    RoleArn: String
    FeatureName: String | None

class AddRoleToDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    RoleArn: String
    FeatureName: String

class AddSourceIdentifierToSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SourceIdentifier: String

EventCategoriesList = list[String]
SourceIdsList = list[String]
class EventSubscription(TypedDict, total=False):
    CustomerAwsId: String | None
    CustSubscriptionId: String | None
    SnsTopicArn: String | None
    Status: String | None
    SubscriptionCreationTime: String | None
    SourceType: String | None
    SourceIdsList: SourceIdsList | None
    EventCategoriesList: EventCategoriesList | None
    Enabled: Boolean | None
    EventSubscriptionArn: String | None

class AddSourceIdentifierToSubscriptionResult(TypedDict, total=False):
    EventSubscription: EventSubscription | None

class Tag(TypedDict, total=False):
    Key: String | None
    Value: String | None

TagList = list[Tag]
class AddTagsToResourceMessage(ServiceRequest):
    ResourceName: String
    Tags: TagList

class AdditionalStorageVolume(TypedDict, total=False):
    VolumeName: String
    AllocatedStorage: IntegerOptional | None
    IOPS: IntegerOptional | None
    MaxAllocatedStorage: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    StorageType: String | None

class AdditionalStorageVolumeOutput(TypedDict, total=False):
    VolumeName: String | None
    StorageVolumeStatus: String | None
    AllocatedStorage: Integer | None
    IOPS: IntegerOptional | None
    MaxAllocatedStorage: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    StorageType: String | None

AdditionalStorageVolumesList = list[AdditionalStorageVolume]
AdditionalStorageVolumesOutputList = list[AdditionalStorageVolumeOutput]
class ApplyPendingMaintenanceActionMessage(ServiceRequest):
    ResourceIdentifier: String
    ApplyAction: String
    OptInType: String

TStamp = datetime
class PendingMaintenanceAction(TypedDict, total=False):
    Action: String | None
    AutoAppliedAfterDate: TStamp | None
    ForcedApplyDate: TStamp | None
    OptInStatus: String | None
    CurrentApplyDate: TStamp | None
    Description: String | None

PendingMaintenanceActionDetails = list[PendingMaintenanceAction]
class ResourcePendingMaintenanceActions(TypedDict, total=False):
    ResourceIdentifier: String | None
    PendingMaintenanceActionDetails: PendingMaintenanceActionDetails | None

class ApplyPendingMaintenanceActionResult(TypedDict, total=False):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActions | None

AttributeValueList = list[String]
class AuthorizeDBSecurityGroupIngressMessage(ServiceRequest):
    DBSecurityGroupName: String
    CIDRIP: String | None
    EC2SecurityGroupName: String | None
    EC2SecurityGroupId: String | None
    EC2SecurityGroupOwnerId: String | None

class IPRange(TypedDict, total=False):
    Status: String | None
    CIDRIP: String | None

IPRangeList = list[IPRange]
class EC2SecurityGroup(TypedDict, total=False):
    Status: String | None
    EC2SecurityGroupName: String | None
    EC2SecurityGroupId: String | None
    EC2SecurityGroupOwnerId: String | None

EC2SecurityGroupList = list[EC2SecurityGroup]
class DBSecurityGroup(TypedDict, total=False):
    OwnerId: String | None
    DBSecurityGroupName: String | None
    DBSecurityGroupDescription: String | None
    VpcId: String | None
    EC2SecurityGroups: EC2SecurityGroupList | None
    IPRanges: IPRangeList | None
    DBSecurityGroupArn: String | None

class AuthorizeDBSecurityGroupIngressResult(TypedDict, total=False):
    DBSecurityGroup: DBSecurityGroup | None

class AvailabilityZone(TypedDict, total=False):
    Name: String | None

AvailabilityZoneList = list[AvailabilityZone]
AvailabilityZones = list[String]
class AvailableAdditionalStorageVolumesOption(TypedDict, total=False):
    SupportsStorageAutoscaling: Boolean | None
    SupportsStorageThroughput: Boolean | None
    SupportsIops: Boolean | None
    StorageType: String | None
    MinStorageSize: IntegerOptional | None
    MaxStorageSize: IntegerOptional | None
    MinIops: IntegerOptional | None
    MaxIops: IntegerOptional | None
    MinIopsPerGib: DoubleOptional | None
    MaxIopsPerGib: DoubleOptional | None
    MinStorageThroughput: IntegerOptional | None
    MaxStorageThroughput: IntegerOptional | None

AvailableAdditionalStorageVolumesOptionList = list[AvailableAdditionalStorageVolumesOption]
class AvailableProcessorFeature(TypedDict, total=False):
    Name: String | None
    DefaultValue: String | None
    AllowedValues: String | None

AvailableProcessorFeatureList = list[AvailableProcessorFeature]
class BacktrackDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    BacktrackTo: TStamp
    Force: BooleanOptional | None
    UseEarliestTimeOnPointInTimeUnavailable: BooleanOptional | None

class BlueGreenDeploymentTask(TypedDict, total=False):
    Name: BlueGreenDeploymentTaskName | None
    Status: BlueGreenDeploymentTaskStatus | None

BlueGreenDeploymentTaskList = list[BlueGreenDeploymentTask]
class SwitchoverDetail(TypedDict, total=False):
    SourceMember: DatabaseArn | None
    TargetMember: DatabaseArn | None
    Status: SwitchoverDetailStatus | None

SwitchoverDetailList = list[SwitchoverDetail]
class BlueGreenDeployment(TypedDict, total=False):
    BlueGreenDeploymentIdentifier: BlueGreenDeploymentIdentifier | None
    BlueGreenDeploymentName: BlueGreenDeploymentName | None
    Source: DatabaseArn | None
    Target: DatabaseArn | None
    SwitchoverDetails: SwitchoverDetailList | None
    Tasks: BlueGreenDeploymentTaskList | None
    Status: BlueGreenDeploymentStatus | None
    StatusDetails: BlueGreenDeploymentStatusDetails | None
    CreateTime: TStamp | None
    DeleteTime: TStamp | None
    TagList: TagList | None

BlueGreenDeploymentList = list[BlueGreenDeployment]
CACertificateIdentifiersList = list[String]
class CancelExportTaskMessage(ServiceRequest):
    ExportTaskIdentifier: String

class Certificate(TypedDict, total=False):
    CertificateIdentifier: String | None
    CertificateType: String | None
    Thumbprint: String | None
    ValidFrom: TStamp | None
    ValidTill: TStamp | None
    CertificateArn: String | None
    CustomerOverride: BooleanOptional | None
    CustomerOverrideValidTill: TStamp | None

class CertificateDetails(TypedDict, total=False):
    CAIdentifier: String | None
    ValidTill: TStamp | None

CertificateList = list[Certificate]
class CertificateMessage(TypedDict, total=False):
    DefaultCertificateForNewLaunches: String | None
    Certificates: CertificateList | None
    Marker: String | None

class CharacterSet(TypedDict, total=False):
    CharacterSetName: String | None
    CharacterSetDescription: String | None

LogTypeList = list[String]
class CloudwatchLogsExportConfiguration(TypedDict, total=False):
    EnableLogTypes: LogTypeList | None
    DisableLogTypes: LogTypeList | None

class RdsCustomClusterConfiguration(TypedDict, total=False):
    InterconnectSubnetId: String | None
    TransitGatewayMulticastDomainId: String | None
    ReplicaMode: ReplicaMode | None

class PendingCloudwatchLogsExports(TypedDict, total=False):
    LogTypesToEnable: LogTypeList | None
    LogTypesToDisable: LogTypeList | None

class ClusterPendingModifiedValues(TypedDict, total=False):
    PendingCloudwatchLogsExports: PendingCloudwatchLogsExports | None
    DBClusterIdentifier: String | None
    MasterUserPassword: SensitiveString | None
    IAMDatabaseAuthenticationEnabled: BooleanOptional | None
    EngineVersion: String | None
    BackupRetentionPeriod: IntegerOptional | None
    StorageType: String | None
    AllocatedStorage: IntegerOptional | None
    RdsCustomClusterConfiguration: RdsCustomClusterConfiguration | None
    Iops: IntegerOptional | None
    CertificateDetails: CertificateDetails | None

StringList = list[String]
class ConnectionPoolConfiguration(TypedDict, total=False):
    MaxConnectionsPercent: IntegerOptional | None
    MaxIdleConnectionsPercent: IntegerOptional | None
    ConnectionBorrowTimeout: IntegerOptional | None
    SessionPinningFilters: StringList | None
    InitQuery: OperatorSensitiveString | None

class ConnectionPoolConfigurationInfo(TypedDict, total=False):
    MaxConnectionsPercent: Integer | None
    MaxIdleConnectionsPercent: Integer | None
    ConnectionBorrowTimeout: Integer | None
    SessionPinningFilters: StringList | None
    InitQuery: OperatorSensitiveString | None

class ContextAttribute(TypedDict, total=False):
    Key: String | None
    Value: String | None

ContextAttributeList = list[ContextAttribute]
class CopyDBClusterParameterGroupMessage(ServiceRequest):
    SourceDBClusterParameterGroupIdentifier: String
    TargetDBClusterParameterGroupIdentifier: String
    TargetDBClusterParameterGroupDescription: String
    Tags: TagList | None

class DBClusterParameterGroup(TypedDict, total=False):
    DBClusterParameterGroupName: String | None
    DBParameterGroupFamily: String | None
    Description: String | None
    DBClusterParameterGroupArn: String | None

class CopyDBClusterParameterGroupResult(TypedDict, total=False):
    DBClusterParameterGroup: DBClusterParameterGroup | None

class CopyDBClusterSnapshotMessage(ServiceRequest):
    SourceDBClusterSnapshotIdentifier: String
    TargetDBClusterSnapshotIdentifier: String
    KmsKeyId: String | None
    PreSignedUrl: SensitiveString | None
    CopyTags: BooleanOptional | None
    Tags: TagList | None
    SourceRegion: String | None

class DBClusterSnapshot(TypedDict, total=False):
    AvailabilityZones: AvailabilityZones | None
    DBClusterSnapshotIdentifier: String | None
    DBClusterIdentifier: String | None
    SnapshotCreateTime: TStamp | None
    Engine: String | None
    EngineMode: String | None
    AllocatedStorage: Integer | None
    Status: String | None
    Port: Integer | None
    VpcId: String | None
    ClusterCreateTime: TStamp | None
    MasterUsername: String | None
    EngineVersion: String | None
    LicenseModel: String | None
    SnapshotType: String | None
    PercentProgress: Integer | None
    StorageEncrypted: Boolean | None
    StorageEncryptionType: StorageEncryptionType | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    KmsKeyId: String | None
    DBClusterSnapshotArn: String | None
    SourceDBClusterSnapshotArn: String | None
    IAMDatabaseAuthenticationEnabled: Boolean | None
    TagList: TagList | None
    StorageType: String | None
    StorageThroughput: IntegerOptional | None
    DbClusterResourceId: String | None
    DBSystemId: String | None

class CopyDBClusterSnapshotResult(TypedDict, total=False):
    DBClusterSnapshot: DBClusterSnapshot | None

class CopyDBParameterGroupMessage(ServiceRequest):
    SourceDBParameterGroupIdentifier: String
    TargetDBParameterGroupIdentifier: String
    TargetDBParameterGroupDescription: String
    Tags: TagList | None

class DBParameterGroup(TypedDict, total=False):
    DBParameterGroupName: String | None
    DBParameterGroupFamily: String | None
    Description: String | None
    DBParameterGroupArn: String | None

class CopyDBParameterGroupResult(TypedDict, total=False):
    DBParameterGroup: DBParameterGroup | None

class CopyDBSnapshotMessage(ServiceRequest):
    SourceDBSnapshotIdentifier: String
    TargetDBSnapshotIdentifier: String
    KmsKeyId: String | None
    Tags: TagList | None
    CopyTags: BooleanOptional | None
    PreSignedUrl: SensitiveString | None
    OptionGroupName: String | None
    TargetCustomAvailabilityZone: String | None
    SnapshotTarget: String | None
    CopyOptionGroup: BooleanOptional | None
    SnapshotAvailabilityZone: String | None
    SourceRegion: String | None

class ProcessorFeature(TypedDict, total=False):
    Name: String | None
    Value: String | None

ProcessorFeatureList = list[ProcessorFeature]
class DBSnapshot(TypedDict, total=False):
    DBSnapshotIdentifier: String | None
    DBInstanceIdentifier: String | None
    SnapshotCreateTime: TStamp | None
    Engine: String | None
    AllocatedStorage: Integer | None
    Status: String | None
    Port: Integer | None
    AvailabilityZone: String | None
    VpcId: String | None
    InstanceCreateTime: TStamp | None
    MasterUsername: String | None
    EngineVersion: String | None
    LicenseModel: String | None
    SnapshotType: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    PercentProgress: Integer | None
    SourceRegion: String | None
    SourceDBSnapshotIdentifier: String | None
    StorageType: String | None
    TdeCredentialArn: String | None
    Encrypted: Boolean | None
    StorageEncryptionType: StorageEncryptionType | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    KmsKeyId: String | None
    DBSnapshotArn: String | None
    Timezone: String | None
    IAMDatabaseAuthenticationEnabled: Boolean | None
    ProcessorFeatures: ProcessorFeatureList | None
    DbiResourceId: String | None
    TagList: TagList | None
    SnapshotTarget: String | None
    OriginalSnapshotCreateTime: TStamp | None
    SnapshotDatabaseTime: TStamp | None
    DBSystemId: String | None
    MultiTenant: BooleanOptional | None
    DedicatedLogVolume: Boolean | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None
    SnapshotAvailabilityZone: String | None

class CopyDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: DBSnapshot | None

class CopyOptionGroupMessage(ServiceRequest):
    SourceOptionGroupIdentifier: String
    TargetOptionGroupIdentifier: String
    TargetOptionGroupDescription: String
    Tags: TagList | None

class VpcSecurityGroupMembership(TypedDict, total=False):
    VpcSecurityGroupId: String | None
    Status: String | None

VpcSecurityGroupMembershipList = list[VpcSecurityGroupMembership]
class DBSecurityGroupMembership(TypedDict, total=False):
    DBSecurityGroupName: String | None
    Status: String | None

DBSecurityGroupMembershipList = list[DBSecurityGroupMembership]
class OptionSetting(TypedDict, total=False):
    Name: String | None
    Value: PotentiallySensitiveOptionSettingValue | None
    DefaultValue: String | None
    Description: String | None
    ApplyType: String | None
    DataType: String | None
    AllowedValues: String | None
    IsModifiable: Boolean | None
    IsCollection: Boolean | None

OptionSettingConfigurationList = list[OptionSetting]
class Option(TypedDict, total=False):
    OptionName: String | None
    OptionDescription: String | None
    Persistent: Boolean | None
    Permanent: Boolean | None
    Port: IntegerOptional | None
    OptionVersion: String | None
    OptionSettings: OptionSettingConfigurationList | None
    DBSecurityGroupMemberships: DBSecurityGroupMembershipList | None
    VpcSecurityGroupMemberships: VpcSecurityGroupMembershipList | None

OptionsList = list[Option]
class OptionGroup(TypedDict, total=False):
    OptionGroupName: String | None
    OptionGroupDescription: String | None
    EngineName: String | None
    MajorEngineVersion: String | None
    Options: OptionsList | None
    AllowsVpcAndNonVpcInstanceMemberships: Boolean | None
    VpcId: String | None
    OptionGroupArn: String | None
    SourceOptionGroup: String | None
    SourceAccountId: String | None
    CopyTimestamp: TStamp | None

class CopyOptionGroupResult(TypedDict, total=False):
    OptionGroup: OptionGroup | None

class CreateBlueGreenDeploymentRequest(ServiceRequest):
    BlueGreenDeploymentName: BlueGreenDeploymentName
    Source: DatabaseArn
    TargetEngineVersion: TargetEngineVersion | None
    TargetDBParameterGroupName: TargetDBParameterGroupName | None
    TargetDBClusterParameterGroupName: TargetDBClusterParameterGroupName | None
    Tags: TagList | None
    TargetDBInstanceClass: TargetDBInstanceClass | None
    UpgradeTargetStorageConfig: BooleanOptional | None
    TargetIops: IntegerOptional | None
    TargetStorageType: TargetStorageType | None
    TargetAllocatedStorage: IntegerOptional | None
    TargetStorageThroughput: IntegerOptional | None

class CreateBlueGreenDeploymentResponse(TypedDict, total=False):
    BlueGreenDeployment: BlueGreenDeployment | None

class CreateCustomDBEngineVersionMessage(ServiceRequest):
    Engine: CustomEngineName
    EngineVersion: CustomEngineVersion
    DatabaseInstallationFilesS3BucketName: BucketName | None
    DatabaseInstallationFilesS3Prefix: String255 | None
    DatabaseInstallationFiles: StringList | None
    ImageId: String255 | None
    KMSKeyId: KmsKeyIdOrArn | None
    SourceCustomDbEngineVersionIdentifier: String255 | None
    UseAwsProvidedLatestImage: BooleanOptional | None
    Description: Description | None
    Manifest: CustomDBEngineVersionManifest | None
    Tags: TagList | None

class CreateDBClusterEndpointMessage(ServiceRequest):
    DBClusterIdentifier: String
    DBClusterEndpointIdentifier: String
    EndpointType: String
    StaticMembers: StringList | None
    ExcludedMembers: StringList | None
    Tags: TagList | None

class TagSpecification(TypedDict, total=False):
    ResourceType: String | None
    Tags: TagList | None

TagSpecificationList = list[TagSpecification]
class ServerlessV2ScalingConfiguration(TypedDict, total=False):
    MinCapacity: DoubleOptional | None
    MaxCapacity: DoubleOptional | None
    SecondsUntilAutoPause: IntegerOptional | None

class ScalingConfiguration(TypedDict, total=False):
    MinCapacity: IntegerOptional | None
    MaxCapacity: IntegerOptional | None
    AutoPause: BooleanOptional | None
    SecondsUntilAutoPause: IntegerOptional | None
    TimeoutAction: String | None
    SecondsBeforeTimeout: IntegerOptional | None

LongOptional = int
VpcSecurityGroupIdList = list[String]
class CreateDBClusterMessage(ServiceRequest):
    AvailabilityZones: AvailabilityZones | None
    BackupRetentionPeriod: IntegerOptional | None
    CharacterSetName: String | None
    DatabaseName: String | None
    DBClusterIdentifier: String
    DBClusterParameterGroupName: String | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    DBSubnetGroupName: String | None
    Engine: String
    EngineVersion: String | None
    Port: IntegerOptional | None
    MasterUsername: String | None
    MasterUserPassword: SensitiveString | None
    OptionGroupName: String | None
    PreferredBackupWindow: String | None
    PreferredMaintenanceWindow: String | None
    ReplicationSourceIdentifier: String | None
    Tags: TagList | None
    StorageEncrypted: BooleanOptional | None
    KmsKeyId: String | None
    PreSignedUrl: SensitiveString | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    BacktrackWindow: LongOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    EngineMode: String | None
    ScalingConfiguration: ScalingConfiguration | None
    RdsCustomClusterConfiguration: RdsCustomClusterConfiguration | None
    DBClusterInstanceClass: String | None
    AllocatedStorage: IntegerOptional | None
    StorageType: String | None
    Iops: IntegerOptional | None
    PubliclyAccessible: BooleanOptional | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    DeletionProtection: BooleanOptional | None
    GlobalClusterIdentifier: GlobalClusterIdentifier | None
    EnableHttpEndpoint: BooleanOptional | None
    CopyTagsToSnapshot: BooleanOptional | None
    Domain: String | None
    DomainIAMRoleName: String | None
    EnableGlobalWriteForwarding: BooleanOptional | None
    NetworkType: String | None
    ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfiguration | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    EnableLimitlessDatabase: BooleanOptional | None
    ClusterScalabilityType: ClusterScalabilityType | None
    DBSystemId: String | None
    ManageMasterUserPassword: BooleanOptional | None
    EnableLocalWriteForwarding: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    CACertificateIdentifier: String | None
    EngineLifecycleSupport: String | None
    TagSpecifications: TagSpecificationList | None
    MasterUserAuthenticationType: MasterUserAuthenticationType | None
    SourceRegion: String | None

class CreateDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    DBParameterGroupFamily: String
    Description: String
    Tags: TagList | None

class CreateDBClusterParameterGroupResult(TypedDict, total=False):
    DBClusterParameterGroup: DBClusterParameterGroup | None

class LimitlessDatabase(TypedDict, total=False):
    Status: LimitlessDatabaseStatus | None
    MinRequiredACU: DoubleOptional | None

class MasterUserSecret(TypedDict, total=False):
    SecretArn: String | None
    SecretStatus: String | None
    KmsKeyId: String | None

class ServerlessV2ScalingConfigurationInfo(TypedDict, total=False):
    MinCapacity: DoubleOptional | None
    MaxCapacity: DoubleOptional | None
    SecondsUntilAutoPause: IntegerOptional | None

class DomainMembership(TypedDict, total=False):
    Domain: String | None
    Status: String | None
    FQDN: String | None
    IAMRoleName: String | None
    OU: String | None
    AuthSecretArn: String | None
    DnsIps: StringList | None

DomainMembershipList = list[DomainMembership]
class ScalingConfigurationInfo(TypedDict, total=False):
    MinCapacity: IntegerOptional | None
    MaxCapacity: IntegerOptional | None
    AutoPause: BooleanOptional | None
    SecondsUntilAutoPause: IntegerOptional | None
    TimeoutAction: String | None
    SecondsBeforeTimeout: IntegerOptional | None

class DBClusterRole(TypedDict, total=False):
    RoleArn: String | None
    Status: String | None
    FeatureName: String | None

DBClusterRoles = list[DBClusterRole]
class DBClusterMember(TypedDict, total=False):
    DBInstanceIdentifier: String | None
    IsClusterWriter: Boolean | None
    DBClusterParameterGroupStatus: String | None
    PromotionTier: IntegerOptional | None

DBClusterMemberList = list[DBClusterMember]
class DBClusterStatusInfo(TypedDict, total=False):
    StatusType: String | None
    Normal: Boolean | None
    Status: String | None
    Message: String | None

DBClusterStatusInfoList = list[DBClusterStatusInfo]
ReadReplicaIdentifierList = list[String]
class DBClusterOptionGroupStatus(TypedDict, total=False):
    DBClusterOptionGroupName: String | None
    Status: String | None

DBClusterOptionGroupMemberships = list[DBClusterOptionGroupStatus]
class DBCluster(TypedDict, total=False):
    AllocatedStorage: IntegerOptional | None
    AvailabilityZones: AvailabilityZones | None
    BackupRetentionPeriod: IntegerOptional | None
    CharacterSetName: String | None
    DatabaseName: String | None
    DBClusterIdentifier: String | None
    DBClusterParameterGroup: String | None
    DBSubnetGroup: String | None
    Status: String | None
    PercentProgress: String | None
    EarliestRestorableTime: TStamp | None
    Endpoint: String | None
    ReaderEndpoint: String | None
    CustomEndpoints: StringList | None
    MultiAZ: BooleanOptional | None
    Engine: String | None
    EngineVersion: String | None
    LatestRestorableTime: TStamp | None
    Port: IntegerOptional | None
    MasterUsername: String | None
    DBClusterOptionGroupMemberships: DBClusterOptionGroupMemberships | None
    PreferredBackupWindow: String | None
    PreferredMaintenanceWindow: String | None
    UpgradeRolloutOrder: UpgradeRolloutOrder | None
    ReplicationSourceIdentifier: String | None
    ReadReplicaIdentifiers: ReadReplicaIdentifierList | None
    StatusInfos: DBClusterStatusInfoList | None
    DBClusterMembers: DBClusterMemberList | None
    VpcSecurityGroups: VpcSecurityGroupMembershipList | None
    HostedZoneId: String | None
    StorageEncrypted: Boolean | None
    StorageEncryptionType: StorageEncryptionType | None
    KmsKeyId: String | None
    DbClusterResourceId: String | None
    DBClusterArn: String | None
    AssociatedRoles: DBClusterRoles | None
    IAMDatabaseAuthenticationEnabled: BooleanOptional | None
    CloneGroupId: String | None
    ClusterCreateTime: TStamp | None
    EarliestBacktrackTime: TStamp | None
    BacktrackWindow: LongOptional | None
    BacktrackConsumedChangeRecords: LongOptional | None
    EnabledCloudwatchLogsExports: LogTypeList | None
    Capacity: IntegerOptional | None
    PendingModifiedValues: ClusterPendingModifiedValues | None
    EngineMode: String | None
    ScalingConfigurationInfo: ScalingConfigurationInfo | None
    RdsCustomClusterConfiguration: RdsCustomClusterConfiguration | None
    DBClusterInstanceClass: String | None
    StorageType: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    IOOptimizedNextAllowedModificationTime: TStamp | None
    PubliclyAccessible: BooleanOptional | None
    AutoMinorVersionUpgrade: Boolean | None
    DeletionProtection: BooleanOptional | None
    HttpEndpointEnabled: BooleanOptional | None
    ActivityStreamMode: ActivityStreamMode | None
    ActivityStreamStatus: ActivityStreamStatus | None
    ActivityStreamKmsKeyId: String | None
    ActivityStreamKinesisStreamName: String | None
    CopyTagsToSnapshot: BooleanOptional | None
    CrossAccountClone: BooleanOptional | None
    DomainMemberships: DomainMembershipList | None
    TagList: TagList | None
    GlobalClusterIdentifier: GlobalClusterIdentifier | None
    GlobalWriteForwardingStatus: WriteForwardingStatus | None
    GlobalWriteForwardingRequested: BooleanOptional | None
    NetworkType: String | None
    AutomaticRestartTime: TStamp | None
    ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfigurationInfo | None
    ServerlessV2PlatformVersion: String | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    PerformanceInsightsEnabled: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    DBSystemId: String | None
    MasterUserSecret: MasterUserSecret | None
    LocalWriteForwardingStatus: LocalWriteForwardingStatus | None
    AwsBackupRecoveryPointArn: String | None
    LimitlessDatabase: LimitlessDatabase | None
    ClusterScalabilityType: ClusterScalabilityType | None
    CertificateDetails: CertificateDetails | None
    EngineLifecycleSupport: String | None

class CreateDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class CreateDBClusterSnapshotMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String
    DBClusterIdentifier: String
    Tags: TagList | None

class CreateDBClusterSnapshotResult(TypedDict, total=False):
    DBClusterSnapshot: DBClusterSnapshot | None

DBSecurityGroupNameList = list[String]
class CreateDBInstanceMessage(ServiceRequest):
    DBName: String | None
    DBInstanceIdentifier: String
    AllocatedStorage: IntegerOptional | None
    DBInstanceClass: String
    Engine: String
    MasterUsername: String | None
    MasterUserPassword: SensitiveString | None
    DBSecurityGroups: DBSecurityGroupNameList | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    AvailabilityZone: String | None
    DBSubnetGroupName: String | None
    PreferredMaintenanceWindow: String | None
    DBParameterGroupName: String | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    Port: IntegerOptional | None
    MultiAZ: BooleanOptional | None
    EngineVersion: String | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    LicenseModel: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    CharacterSetName: String | None
    NcharCharacterSetName: String | None
    PubliclyAccessible: BooleanOptional | None
    Tags: TagList | None
    DBClusterIdentifier: String | None
    StorageType: String | None
    TdeCredentialArn: String | None
    TdeCredentialPassword: SensitiveString | None
    StorageEncrypted: BooleanOptional | None
    KmsKeyId: String | None
    Domain: String | None
    DomainFqdn: String | None
    DomainOu: String | None
    DomainAuthSecretArn: String | None
    DomainDnsIps: StringList | None
    CopyTagsToSnapshot: BooleanOptional | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    DomainIAMRoleName: String | None
    PromotionTier: IntegerOptional | None
    Timezone: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    ProcessorFeatures: ProcessorFeatureList | None
    DeletionProtection: BooleanOptional | None
    MaxAllocatedStorage: IntegerOptional | None
    EnableCustomerOwnedIp: BooleanOptional | None
    NetworkType: String | None
    BackupTarget: String | None
    CustomIamInstanceProfile: String | None
    DBSystemId: String | None
    CACertificateIdentifier: String | None
    ManageMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    MultiTenant: BooleanOptional | None
    DedicatedLogVolume: BooleanOptional | None
    EngineLifecycleSupport: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None
    TagSpecifications: TagSpecificationList | None
    MasterUserAuthenticationType: MasterUserAuthenticationType | None

class CreateDBInstanceReadReplicaMessage(ServiceRequest):
    DBInstanceIdentifier: String
    SourceDBInstanceIdentifier: String | None
    DBInstanceClass: String | None
    AvailabilityZone: String | None
    Port: IntegerOptional | None
    MultiAZ: BooleanOptional | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    DBParameterGroupName: String | None
    PubliclyAccessible: BooleanOptional | None
    Tags: TagList | None
    DBSubnetGroupName: String | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    StorageType: String | None
    CopyTagsToSnapshot: BooleanOptional | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    KmsKeyId: String | None
    PreSignedUrl: SensitiveString | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    ProcessorFeatures: ProcessorFeatureList | None
    UseDefaultProcessorFeatures: BooleanOptional | None
    DeletionProtection: BooleanOptional | None
    Domain: String | None
    DomainIAMRoleName: String | None
    DomainFqdn: String | None
    DomainOu: String | None
    DomainAuthSecretArn: String | None
    DomainDnsIps: StringList | None
    ReplicaMode: ReplicaMode | None
    EnableCustomerOwnedIp: BooleanOptional | None
    NetworkType: String | None
    MaxAllocatedStorage: IntegerOptional | None
    BackupTarget: String | None
    CustomIamInstanceProfile: String | None
    AllocatedStorage: IntegerOptional | None
    SourceDBClusterIdentifier: String | None
    DedicatedLogVolume: BooleanOptional | None
    UpgradeStorageConfig: BooleanOptional | None
    CACertificateIdentifier: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None
    TagSpecifications: TagSpecificationList | None
    SourceRegion: String | None

class DBInstanceAutomatedBackupsReplication(TypedDict, total=False):
    DBInstanceAutomatedBackupsArn: String | None

DBInstanceAutomatedBackupsReplicationList = list[DBInstanceAutomatedBackupsReplication]
class Endpoint(TypedDict, total=False):
    Address: String | None
    Port: Integer | None
    HostedZoneId: String | None

class DBInstanceRole(TypedDict, total=False):
    RoleArn: String | None
    FeatureName: String | None
    Status: String | None

DBInstanceRoles = list[DBInstanceRole]
class DBInstanceStatusInfo(TypedDict, total=False):
    StatusType: String | None
    Normal: Boolean | None
    Status: String | None
    Message: String | None

DBInstanceStatusInfoList = list[DBInstanceStatusInfo]
class OptionGroupMembership(TypedDict, total=False):
    OptionGroupName: String | None
    Status: String | None

OptionGroupMembershipList = list[OptionGroupMembership]
ReadReplicaDBClusterIdentifierList = list[String]
ReadReplicaDBInstanceIdentifierList = list[String]
class PendingModifiedValues(TypedDict, total=False):
    DBInstanceClass: String | None
    AllocatedStorage: IntegerOptional | None
    MasterUserPassword: SensitiveString | None
    Port: IntegerOptional | None
    BackupRetentionPeriod: IntegerOptional | None
    MultiAZ: BooleanOptional | None
    EngineVersion: String | None
    LicenseModel: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    DBInstanceIdentifier: String | None
    StorageType: String | None
    CACertificateIdentifier: String | None
    DBSubnetGroupName: String | None
    PendingCloudwatchLogsExports: PendingCloudwatchLogsExports | None
    ProcessorFeatures: ProcessorFeatureList | None
    AutomationMode: AutomationMode | None
    ResumeFullAutomationModeTime: TStamp | None
    MultiTenant: BooleanOptional | None
    IAMDatabaseAuthenticationEnabled: BooleanOptional | None
    DedicatedLogVolume: BooleanOptional | None
    Engine: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None

class Outpost(TypedDict, total=False):
    Arn: String | None

class Subnet(TypedDict, total=False):
    SubnetIdentifier: String | None
    SubnetAvailabilityZone: AvailabilityZone | None
    SubnetOutpost: Outpost | None
    SubnetStatus: String | None

SubnetList = list[Subnet]
class DBSubnetGroup(TypedDict, total=False):
    DBSubnetGroupName: String | None
    DBSubnetGroupDescription: String | None
    VpcId: String | None
    SubnetGroupStatus: String | None
    Subnets: SubnetList | None
    DBSubnetGroupArn: String | None
    SupportedNetworkTypes: StringList | None

class DBParameterGroupStatus(TypedDict, total=False):
    DBParameterGroupName: String | None
    ParameterApplyStatus: String | None

DBParameterGroupStatusList = list[DBParameterGroupStatus]
class DBInstance(TypedDict, total=False):
    DBInstanceIdentifier: String | None
    DBInstanceClass: String | None
    Engine: String | None
    DBInstanceStatus: String | None
    MasterUsername: String | None
    DBName: String | None
    Endpoint: Endpoint | None
    AllocatedStorage: Integer | None
    InstanceCreateTime: TStamp | None
    PreferredBackupWindow: String | None
    BackupRetentionPeriod: Integer | None
    DBSecurityGroups: DBSecurityGroupMembershipList | None
    VpcSecurityGroups: VpcSecurityGroupMembershipList | None
    DBParameterGroups: DBParameterGroupStatusList | None
    AvailabilityZone: String | None
    DBSubnetGroup: DBSubnetGroup | None
    PreferredMaintenanceWindow: String | None
    UpgradeRolloutOrder: UpgradeRolloutOrder | None
    PendingModifiedValues: PendingModifiedValues | None
    LatestRestorableTime: TStamp | None
    MultiAZ: Boolean | None
    EngineVersion: String | None
    AutoMinorVersionUpgrade: Boolean | None
    ReadReplicaSourceDBInstanceIdentifier: String | None
    ReadReplicaDBInstanceIdentifiers: ReadReplicaDBInstanceIdentifierList | None
    ReadReplicaDBClusterIdentifiers: ReadReplicaDBClusterIdentifierList | None
    ReplicaMode: ReplicaMode | None
    LicenseModel: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupMemberships: OptionGroupMembershipList | None
    CharacterSetName: String | None
    NcharCharacterSetName: String | None
    SecondaryAvailabilityZone: String | None
    PubliclyAccessible: Boolean | None
    StatusInfos: DBInstanceStatusInfoList | None
    StorageType: String | None
    StorageEncryptionType: StorageEncryptionType | None
    TdeCredentialArn: String | None
    DbInstancePort: Integer | None
    DBClusterIdentifier: String | None
    StorageEncrypted: Boolean | None
    KmsKeyId: String | None
    DbiResourceId: String | None
    CACertificateIdentifier: String | None
    DomainMemberships: DomainMembershipList | None
    CopyTagsToSnapshot: Boolean | None
    MonitoringInterval: IntegerOptional | None
    EnhancedMonitoringResourceArn: String | None
    MonitoringRoleArn: String | None
    PromotionTier: IntegerOptional | None
    DBInstanceArn: String | None
    Timezone: String | None
    IAMDatabaseAuthenticationEnabled: Boolean | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    PerformanceInsightsEnabled: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    EnabledCloudwatchLogsExports: LogTypeList | None
    ProcessorFeatures: ProcessorFeatureList | None
    DeletionProtection: Boolean | None
    AssociatedRoles: DBInstanceRoles | None
    ListenerEndpoint: Endpoint | None
    MaxAllocatedStorage: IntegerOptional | None
    TagList: TagList | None
    AutomationMode: AutomationMode | None
    ResumeFullAutomationModeTime: TStamp | None
    CustomerOwnedIpEnabled: BooleanOptional | None
    NetworkType: String | None
    ActivityStreamStatus: ActivityStreamStatus | None
    ActivityStreamKmsKeyId: String | None
    ActivityStreamKinesisStreamName: String | None
    ActivityStreamMode: ActivityStreamMode | None
    ActivityStreamEngineNativeAuditFieldsIncluded: BooleanOptional | None
    AwsBackupRecoveryPointArn: String | None
    DBInstanceAutomatedBackupsReplications: DBInstanceAutomatedBackupsReplicationList | None
    BackupTarget: String | None
    AutomaticRestartTime: TStamp | None
    CustomIamInstanceProfile: String | None
    ActivityStreamPolicyStatus: ActivityStreamPolicyStatus | None
    CertificateDetails: CertificateDetails | None
    DBSystemId: String | None
    MasterUserSecret: MasterUserSecret | None
    ReadReplicaSourceDBClusterIdentifier: String | None
    PercentProgress: String | None
    MultiTenant: BooleanOptional | None
    DedicatedLogVolume: Boolean | None
    IsStorageConfigUpgradeAvailable: BooleanOptional | None
    EngineLifecycleSupport: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesOutputList | None
    StorageVolumeStatus: String | None

class CreateDBInstanceReadReplicaResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class CreateDBInstanceResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class CreateDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String
    DBParameterGroupFamily: String
    Description: String
    Tags: TagList | None

class CreateDBParameterGroupResult(TypedDict, total=False):
    DBParameterGroup: DBParameterGroup | None

class CreateDBProxyEndpointRequest(ServiceRequest):
    DBProxyName: DBProxyName
    DBProxyEndpointName: DBProxyEndpointName
    VpcSubnetIds: StringList
    VpcSecurityGroupIds: StringList | None
    TargetRole: DBProxyEndpointTargetRole | None
    Tags: TagList | None
    EndpointNetworkType: EndpointNetworkType | None

class DBProxyEndpoint(TypedDict, total=False):
    DBProxyEndpointName: String | None
    DBProxyEndpointArn: String | None
    DBProxyName: String | None
    Status: DBProxyEndpointStatus | None
    VpcId: String | None
    VpcSecurityGroupIds: StringList | None
    VpcSubnetIds: StringList | None
    Endpoint: String | None
    CreatedDate: TStamp | None
    TargetRole: DBProxyEndpointTargetRole | None
    IsDefault: Boolean | None
    EndpointNetworkType: EndpointNetworkType | None

class CreateDBProxyEndpointResponse(TypedDict, total=False):
    DBProxyEndpoint: DBProxyEndpoint | None

class UserAuthConfig(TypedDict, total=False):
    Description: Description | None
    UserName: AuthUserName | None
    AuthScheme: AuthScheme | None
    SecretArn: Arn | None
    IAMAuth: IAMAuthMode | None
    ClientPasswordAuthType: ClientPasswordAuthType | None

UserAuthConfigList = list[UserAuthConfig]
class CreateDBProxyRequest(ServiceRequest):
    DBProxyName: DBProxyName
    EngineFamily: EngineFamily
    DefaultAuthScheme: DefaultAuthScheme | None
    Auth: UserAuthConfigList | None
    RoleArn: Arn
    VpcSubnetIds: StringList
    VpcSecurityGroupIds: StringList | None
    RequireTLS: Boolean | None
    IdleClientTimeout: IntegerOptional | None
    DebugLogging: Boolean | None
    Tags: TagList | None
    EndpointNetworkType: EndpointNetworkType | None
    TargetConnectionNetworkType: TargetConnectionNetworkType | None

class UserAuthConfigInfo(TypedDict, total=False):
    Description: String | None
    UserName: String | None
    AuthScheme: AuthScheme | None
    SecretArn: String | None
    IAMAuth: IAMAuthMode | None
    ClientPasswordAuthType: ClientPasswordAuthType | None

UserAuthConfigInfoList = list[UserAuthConfigInfo]
class DBProxy(TypedDict, total=False):
    DBProxyName: String | None
    DBProxyArn: String | None
    Status: DBProxyStatus | None
    EngineFamily: String | None
    VpcId: String | None
    VpcSecurityGroupIds: StringList | None
    VpcSubnetIds: StringList | None
    DefaultAuthScheme: String | None
    Auth: UserAuthConfigInfoList | None
    RoleArn: String | None
    Endpoint: String | None
    RequireTLS: Boolean | None
    IdleClientTimeout: Integer | None
    DebugLogging: Boolean | None
    CreatedDate: TStamp | None
    UpdatedDate: TStamp | None
    EndpointNetworkType: EndpointNetworkType | None
    TargetConnectionNetworkType: TargetConnectionNetworkType | None

class CreateDBProxyResponse(TypedDict, total=False):
    DBProxy: DBProxy | None

class CreateDBSecurityGroupMessage(ServiceRequest):
    DBSecurityGroupName: String
    DBSecurityGroupDescription: String
    Tags: TagList | None

class CreateDBSecurityGroupResult(TypedDict, total=False):
    DBSecurityGroup: DBSecurityGroup | None

class CreateDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: String
    DBClusterIdentifier: String
    ComputeRedundancy: IntegerOptional | None
    MaxACU: DoubleOptional
    MinACU: DoubleOptional | None
    PubliclyAccessible: BooleanOptional | None
    Tags: TagList | None

class CreateDBSnapshotMessage(ServiceRequest):
    DBSnapshotIdentifier: String
    DBInstanceIdentifier: String
    Tags: TagList | None

class CreateDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: DBSnapshot | None

SubnetIdentifierList = list[String]
class CreateDBSubnetGroupMessage(ServiceRequest):
    DBSubnetGroupName: String
    DBSubnetGroupDescription: String
    SubnetIds: SubnetIdentifierList
    Tags: TagList | None

class CreateDBSubnetGroupResult(TypedDict, total=False):
    DBSubnetGroup: DBSubnetGroup | None

class CreateEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SnsTopicArn: String
    SourceType: String | None
    EventCategories: EventCategoriesList | None
    SourceIds: SourceIdsList | None
    Enabled: BooleanOptional | None
    Tags: TagList | None

class CreateEventSubscriptionResult(TypedDict, total=False):
    EventSubscription: EventSubscription | None

class CreateGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    SourceDBClusterIdentifier: String | None
    Engine: String | None
    EngineVersion: String | None
    EngineLifecycleSupport: String | None
    DeletionProtection: BooleanOptional | None
    DatabaseName: String | None
    StorageEncrypted: BooleanOptional | None
    Tags: TagList | None

class FailoverState(TypedDict, total=False):
    Status: FailoverStatus | None
    FromDbClusterArn: String | None
    ToDbClusterArn: String | None
    IsDataLossAllowed: Boolean | None

ReadersArnList = list[String]
class GlobalClusterMember(TypedDict, total=False):
    DBClusterArn: String | None
    Readers: ReadersArnList | None
    IsWriter: Boolean | None
    GlobalWriteForwardingStatus: WriteForwardingStatus | None
    SynchronizationStatus: GlobalClusterMemberSynchronizationStatus | None

GlobalClusterMemberList = list[GlobalClusterMember]
class GlobalCluster(TypedDict, total=False):
    GlobalClusterIdentifier: GlobalClusterIdentifier | None
    GlobalClusterResourceId: String | None
    GlobalClusterArn: String | None
    Status: String | None
    Engine: String | None
    EngineVersion: String | None
    EngineLifecycleSupport: String | None
    DatabaseName: String | None
    StorageEncrypted: BooleanOptional | None
    StorageEncryptionType: StorageEncryptionType | None
    DeletionProtection: BooleanOptional | None
    GlobalClusterMembers: GlobalClusterMemberList | None
    Endpoint: String | None
    FailoverState: FailoverState | None
    TagList: TagList | None

class CreateGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: GlobalCluster | None

EncryptionContextMap = dict[String, String]
class CreateIntegrationMessage(ServiceRequest):
    SourceArn: SourceArn
    TargetArn: Arn
    IntegrationName: IntegrationName
    KMSKeyId: String | None
    AdditionalEncryptionContext: EncryptionContextMap | None
    Tags: TagList | None
    DataFilter: DataFilter | None
    Description: IntegrationDescription | None

class CreateOptionGroupMessage(ServiceRequest):
    OptionGroupName: String
    EngineName: String
    MajorEngineVersion: String
    OptionGroupDescription: String
    Tags: TagList | None

class CreateOptionGroupResult(TypedDict, total=False):
    OptionGroup: OptionGroup | None

class CreateTenantDatabaseMessage(ServiceRequest):
    DBInstanceIdentifier: String
    TenantDBName: String
    MasterUsername: String
    MasterUserPassword: SensitiveString | None
    CharacterSetName: String | None
    NcharCharacterSetName: String | None
    ManageMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    Tags: TagList | None

class TenantDatabasePendingModifiedValues(TypedDict, total=False):
    MasterUserPassword: SensitiveString | None
    TenantDBName: String | None

class TenantDatabase(TypedDict, total=False):
    TenantDatabaseCreateTime: TStamp | None
    DBInstanceIdentifier: String | None
    TenantDBName: String | None
    Status: String | None
    MasterUsername: String | None
    DbiResourceId: String | None
    TenantDatabaseResourceId: String | None
    TenantDatabaseARN: String | None
    CharacterSetName: String | None
    NcharCharacterSetName: String | None
    DeletionProtection: Boolean | None
    PendingModifiedValues: TenantDatabasePendingModifiedValues | None
    MasterUserSecret: MasterUserSecret | None
    TagList: TagList | None

class CreateTenantDatabaseResult(TypedDict, total=False):
    TenantDatabase: TenantDatabase | None

class CustomDBEngineVersionAMI(TypedDict, total=False):
    ImageId: String | None
    Status: String | None

class RestoreWindow(TypedDict, total=False):
    EarliestTime: TStamp | None
    LatestTime: TStamp | None

class DBClusterAutomatedBackup(TypedDict, total=False):
    Engine: String | None
    VpcId: String | None
    DBClusterAutomatedBackupsArn: String | None
    DBClusterIdentifier: String | None
    RestoreWindow: RestoreWindow | None
    MasterUsername: String | None
    DbClusterResourceId: String | None
    Region: String | None
    LicenseModel: String | None
    Status: String | None
    IAMDatabaseAuthenticationEnabled: Boolean | None
    ClusterCreateTime: TStamp | None
    StorageEncrypted: Boolean | None
    StorageEncryptionType: StorageEncryptionType | None
    AllocatedStorage: Integer | None
    EngineVersion: String | None
    DBClusterArn: String | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    EngineMode: String | None
    AvailabilityZones: AvailabilityZones | None
    Port: Integer | None
    KmsKeyId: String | None
    StorageType: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    AwsBackupRecoveryPointArn: String | None
    TagList: TagList | None

DBClusterAutomatedBackupList = list[DBClusterAutomatedBackup]
class DBClusterAutomatedBackupMessage(TypedDict, total=False):
    Marker: String | None
    DBClusterAutomatedBackups: DBClusterAutomatedBackupList | None

class DBClusterBacktrack(TypedDict, total=False):
    DBClusterIdentifier: String | None
    BacktrackIdentifier: String | None
    BacktrackTo: TStamp | None
    BacktrackedFrom: TStamp | None
    BacktrackRequestCreationTime: TStamp | None
    Status: String | None

DBClusterBacktrackList = list[DBClusterBacktrack]
class DBClusterBacktrackMessage(TypedDict, total=False):
    Marker: String | None
    DBClusterBacktracks: DBClusterBacktrackList | None

class DBClusterCapacityInfo(TypedDict, total=False):
    DBClusterIdentifier: String | None
    PendingCapacity: IntegerOptional | None
    CurrentCapacity: IntegerOptional | None
    SecondsBeforeTimeout: IntegerOptional | None
    TimeoutAction: String | None

class DBClusterEndpoint(TypedDict, total=False):
    DBClusterEndpointIdentifier: String | None
    DBClusterIdentifier: String | None
    DBClusterEndpointResourceIdentifier: String | None
    Endpoint: String | None
    Status: String | None
    EndpointType: String | None
    CustomEndpointType: String | None
    StaticMembers: StringList | None
    ExcludedMembers: StringList | None
    DBClusterEndpointArn: String | None

DBClusterEndpointList = list[DBClusterEndpoint]
class DBClusterEndpointMessage(TypedDict, total=False):
    Marker: String | None
    DBClusterEndpoints: DBClusterEndpointList | None

DBClusterList = list[DBCluster]
class DBClusterMessage(TypedDict, total=False):
    Marker: String | None
    DBClusters: DBClusterList | None

EngineModeList = list[String]
class Parameter(TypedDict, total=False):
    ParameterName: String | None
    ParameterValue: PotentiallySensitiveParameterValue | None
    Description: String | None
    Source: String | None
    ApplyType: String | None
    DataType: String | None
    AllowedValues: String | None
    IsModifiable: Boolean | None
    MinimumEngineVersion: String | None
    ApplyMethod: ApplyMethod | None
    SupportedEngineModes: EngineModeList | None

ParametersList = list[Parameter]
class DBClusterParameterGroupDetails(TypedDict, total=False):
    Parameters: ParametersList | None
    Marker: String | None

DBClusterParameterGroupList = list[DBClusterParameterGroup]
class DBClusterParameterGroupNameMessage(TypedDict, total=False):
    DBClusterParameterGroupName: String | None

class DBClusterParameterGroupsMessage(TypedDict, total=False):
    Marker: String | None
    DBClusterParameterGroups: DBClusterParameterGroupList | None

class DBClusterSnapshotAttribute(TypedDict, total=False):
    AttributeName: String | None
    AttributeValues: AttributeValueList | None

DBClusterSnapshotAttributeList = list[DBClusterSnapshotAttribute]
class DBClusterSnapshotAttributesResult(TypedDict, total=False):
    DBClusterSnapshotIdentifier: String | None
    DBClusterSnapshotAttributes: DBClusterSnapshotAttributeList | None

DBClusterSnapshotList = list[DBClusterSnapshot]
class DBClusterSnapshotMessage(TypedDict, total=False):
    Marker: String | None
    DBClusterSnapshots: DBClusterSnapshotList | None

class ServerlessV2FeaturesSupport(TypedDict, total=False):
    MinCapacity: DoubleOptional | None
    MaxCapacity: DoubleOptional | None

FeatureNameList = list[String]
class Timezone(TypedDict, total=False):
    TimezoneName: String | None

SupportedTimezonesList = list[Timezone]
class UpgradeTarget(TypedDict, total=False):
    Engine: String | None
    EngineVersion: String | None
    Description: String | None
    AutoUpgrade: Boolean | None
    IsMajorVersionUpgrade: Boolean | None
    SupportedEngineModes: EngineModeList | None
    SupportsParallelQuery: BooleanOptional | None
    SupportsGlobalDatabases: BooleanOptional | None
    SupportsBabelfish: BooleanOptional | None
    SupportsLimitlessDatabase: BooleanOptional | None
    SupportsLocalWriteForwarding: BooleanOptional | None
    SupportsIntegrations: BooleanOptional | None

ValidUpgradeTargetList = list[UpgradeTarget]
SupportedCharacterSetsList = list[CharacterSet]
class DBEngineVersion(TypedDict, total=False):
    Engine: String | None
    MajorEngineVersion: String | None
    EngineVersion: String | None
    DatabaseInstallationFilesS3BucketName: String | None
    DatabaseInstallationFilesS3Prefix: String | None
    DatabaseInstallationFiles: StringList | None
    CustomDBEngineVersionManifest: CustomDBEngineVersionManifest | None
    DBParameterGroupFamily: String | None
    DBEngineDescription: String | None
    DBEngineVersionArn: String | None
    DBEngineVersionDescription: String | None
    DefaultCharacterSet: CharacterSet | None
    FailureReason: String | None
    Image: CustomDBEngineVersionAMI | None
    DBEngineMediaType: String | None
    KMSKeyId: String | None
    CreateTime: TStamp | None
    SupportedCharacterSets: SupportedCharacterSetsList | None
    SupportedNcharCharacterSets: SupportedCharacterSetsList | None
    ValidUpgradeTarget: ValidUpgradeTargetList | None
    SupportedTimezones: SupportedTimezonesList | None
    ExportableLogTypes: LogTypeList | None
    SupportsLogExportsToCloudwatchLogs: Boolean | None
    SupportsReadReplica: Boolean | None
    SupportedEngineModes: EngineModeList | None
    SupportedFeatureNames: FeatureNameList | None
    Status: String | None
    SupportsParallelQuery: Boolean | None
    SupportsGlobalDatabases: Boolean | None
    TagList: TagList | None
    SupportsBabelfish: Boolean | None
    SupportsLimitlessDatabase: Boolean | None
    SupportsCertificateRotationWithoutRestart: BooleanOptional | None
    SupportedCACertificateIdentifiers: CACertificateIdentifiersList | None
    SupportsLocalWriteForwarding: BooleanOptional | None
    SupportsIntegrations: Boolean | None
    ServerlessV2FeaturesSupport: ServerlessV2FeaturesSupport | None

DBEngineVersionList = list[DBEngineVersion]
class DBEngineVersionMessage(TypedDict, total=False):
    Marker: String | None
    DBEngineVersions: DBEngineVersionList | None

class DBInstanceAutomatedBackup(TypedDict, total=False):
    DBInstanceArn: String | None
    DbiResourceId: String | None
    Region: String | None
    DBInstanceIdentifier: String | None
    RestoreWindow: RestoreWindow | None
    AllocatedStorage: Integer | None
    Status: String | None
    Port: Integer | None
    AvailabilityZone: String | None
    VpcId: String | None
    InstanceCreateTime: TStamp | None
    MasterUsername: String | None
    Engine: String | None
    EngineVersion: String | None
    LicenseModel: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    TdeCredentialArn: String | None
    Encrypted: Boolean | None
    StorageEncryptionType: StorageEncryptionType | None
    StorageType: String | None
    KmsKeyId: String | None
    Timezone: String | None
    IAMDatabaseAuthenticationEnabled: Boolean | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    DBInstanceAutomatedBackupsArn: String | None
    DBInstanceAutomatedBackupsReplications: DBInstanceAutomatedBackupsReplicationList | None
    BackupTarget: String | None
    MultiTenant: BooleanOptional | None
    AwsBackupRecoveryPointArn: String | None
    TagList: TagList | None
    DedicatedLogVolume: BooleanOptional | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None

DBInstanceAutomatedBackupList = list[DBInstanceAutomatedBackup]
class DBInstanceAutomatedBackupMessage(TypedDict, total=False):
    Marker: String | None
    DBInstanceAutomatedBackups: DBInstanceAutomatedBackupList | None

DBInstanceList = list[DBInstance]
class DBInstanceMessage(TypedDict, total=False):
    Marker: String | None
    DBInstances: DBInstanceList | None

class SupportedEngineLifecycle(TypedDict, total=False):
    LifecycleSupportName: LifecycleSupportName
    LifecycleSupportStartDate: TStamp
    LifecycleSupportEndDate: TStamp

SupportedEngineLifecycleList = list[SupportedEngineLifecycle]
class DBMajorEngineVersion(TypedDict, total=False):
    Engine: String | None
    MajorEngineVersion: String | None
    SupportedEngineLifecycles: SupportedEngineLifecycleList | None

DBMajorEngineVersionsList = list[DBMajorEngineVersion]
class DBParameterGroupDetails(TypedDict, total=False):
    Parameters: ParametersList | None
    Marker: String | None

DBParameterGroupList = list[DBParameterGroup]
class DBParameterGroupNameMessage(TypedDict, total=False):
    DBParameterGroupName: String | None

class DBParameterGroupsMessage(TypedDict, total=False):
    Marker: String | None
    DBParameterGroups: DBParameterGroupList | None

DBProxyEndpointList = list[DBProxyEndpoint]
DBProxyList = list[DBProxy]
class TargetHealth(TypedDict, total=False):
    State: TargetState | None
    Reason: TargetHealthReason | None
    Description: String | None

class DBProxyTarget(TypedDict, total=False):
    TargetArn: String | None
    Endpoint: String | None
    TrackedClusterId: String | None
    RdsResourceId: String | None
    Port: Integer | None
    Type: TargetType | None
    Role: TargetRole | None
    TargetHealth: TargetHealth | None

class DBProxyTargetGroup(TypedDict, total=False):
    DBProxyName: String | None
    TargetGroupName: String | None
    TargetGroupArn: String | None
    IsDefault: Boolean | None
    Status: String | None
    ConnectionPoolConfig: ConnectionPoolConfigurationInfo | None
    CreatedDate: TStamp | None
    UpdatedDate: TStamp | None

class PerformanceInsightsMetricDimensionGroup(TypedDict, total=False):
    Dimensions: StringList | None
    Group: String | None
    Limit: Integer | None

class PerformanceInsightsMetricQuery(TypedDict, total=False):
    GroupBy: PerformanceInsightsMetricDimensionGroup | None
    Metric: String | None

class MetricQuery(TypedDict, total=False):
    PerformanceInsightsMetricQuery: PerformanceInsightsMetricQuery | None

class ScalarReferenceDetails(TypedDict, total=False):
    Value: Double | None

class ReferenceDetails(TypedDict, total=False):
    ScalarReferenceDetails: ScalarReferenceDetails | None

class MetricReference(TypedDict, total=False):
    Name: String | None
    ReferenceDetails: ReferenceDetails | None

MetricReferenceList = list[MetricReference]
class Metric(TypedDict, total=False):
    Name: String | None
    References: MetricReferenceList | None
    StatisticsDetails: String | None
    MetricQuery: MetricQuery | None

MetricList = list[Metric]
class PerformanceIssueDetails(TypedDict, total=False):
    StartTime: TStamp | None
    EndTime: TStamp | None
    Metrics: MetricList | None
    Analysis: String | None

class IssueDetails(TypedDict, total=False):
    PerformanceIssueDetails: PerformanceIssueDetails | None

class DocLink(TypedDict, total=False):
    Text: String | None
    Url: String | None

DocLinkList = list[DocLink]
class RecommendedActionParameter(TypedDict, total=False):
    Key: String | None
    Value: String | None

RecommendedActionParameterList = list[RecommendedActionParameter]
class RecommendedAction(TypedDict, total=False):
    ActionId: String | None
    Title: String | None
    Description: String | None
    Operation: String | None
    Parameters: RecommendedActionParameterList | None
    ApplyModes: StringList | None
    Status: String | None
    IssueDetails: IssueDetails | None
    ContextAttributes: ContextAttributeList | None

RecommendedActionList = list[RecommendedAction]
class DBRecommendation(TypedDict, total=False):
    RecommendationId: String | None
    TypeId: String | None
    Severity: String | None
    ResourceArn: String | None
    Status: String | None
    CreatedTime: TStamp | None
    UpdatedTime: TStamp | None
    Detection: String | None
    Recommendation: String | None
    Description: String | None
    Reason: String | None
    RecommendedActions: RecommendedActionList | None
    Category: String | None
    Source: String | None
    TypeDetection: String | None
    TypeRecommendation: String | None
    Impact: String | None
    AdditionalInfo: String | None
    Links: DocLinkList | None
    IssueDetails: IssueDetails | None

DBRecommendationList = list[DBRecommendation]
class DBRecommendationMessage(TypedDict, total=False):
    DBRecommendation: DBRecommendation | None

class DBRecommendationsMessage(TypedDict, total=False):
    DBRecommendations: DBRecommendationList | None
    Marker: String | None

DBSecurityGroups = list[DBSecurityGroup]
class DBSecurityGroupMessage(TypedDict, total=False):
    Marker: String | None
    DBSecurityGroups: DBSecurityGroups | None

class DBShardGroup(TypedDict, total=False):
    DBShardGroupResourceId: String | None
    DBShardGroupIdentifier: DBShardGroupIdentifier | None
    DBClusterIdentifier: String | None
    MaxACU: DoubleOptional | None
    MinACU: DoubleOptional | None
    ComputeRedundancy: IntegerOptional | None
    Status: String | None
    PubliclyAccessible: BooleanOptional | None
    Endpoint: String | None
    DBShardGroupArn: String | None
    TagList: TagList | None

DBShardGroupsList = list[DBShardGroup]
class DBSnapshotAttribute(TypedDict, total=False):
    AttributeName: String | None
    AttributeValues: AttributeValueList | None

DBSnapshotAttributeList = list[DBSnapshotAttribute]
class DBSnapshotAttributesResult(TypedDict, total=False):
    DBSnapshotIdentifier: String | None
    DBSnapshotAttributes: DBSnapshotAttributeList | None

DBSnapshotList = list[DBSnapshot]
class DBSnapshotMessage(TypedDict, total=False):
    Marker: String | None
    DBSnapshots: DBSnapshotList | None

class DBSnapshotTenantDatabase(TypedDict, total=False):
    DBSnapshotIdentifier: String | None
    DBInstanceIdentifier: String | None
    DbiResourceId: String | None
    EngineName: String | None
    SnapshotType: String | None
    TenantDatabaseCreateTime: TStamp | None
    TenantDBName: String | None
    MasterUsername: String | None
    TenantDatabaseResourceId: String | None
    CharacterSetName: String | None
    DBSnapshotTenantDatabaseARN: String | None
    NcharCharacterSetName: String | None
    TagList: TagList | None

DBSnapshotTenantDatabasesList = list[DBSnapshotTenantDatabase]
class DBSnapshotTenantDatabasesMessage(TypedDict, total=False):
    Marker: String | None
    DBSnapshotTenantDatabases: DBSnapshotTenantDatabasesList | None

DBSubnetGroups = list[DBSubnetGroup]
class DBSubnetGroupMessage(TypedDict, total=False):
    Marker: String | None
    DBSubnetGroups: DBSubnetGroups | None

class DeleteBlueGreenDeploymentRequest(ServiceRequest):
    BlueGreenDeploymentIdentifier: BlueGreenDeploymentIdentifier
    DeleteTarget: BooleanOptional | None

class DeleteBlueGreenDeploymentResponse(TypedDict, total=False):
    BlueGreenDeployment: BlueGreenDeployment | None

class DeleteCustomDBEngineVersionMessage(ServiceRequest):
    Engine: CustomEngineName
    EngineVersion: CustomEngineVersion

class DeleteDBClusterAutomatedBackupMessage(ServiceRequest):
    DbClusterResourceId: String

class DeleteDBClusterAutomatedBackupResult(TypedDict, total=False):
    DBClusterAutomatedBackup: DBClusterAutomatedBackup | None

class DeleteDBClusterEndpointMessage(ServiceRequest):
    DBClusterEndpointIdentifier: String

class DeleteDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    SkipFinalSnapshot: Boolean | None
    FinalDBSnapshotIdentifier: String | None
    DeleteAutomatedBackups: BooleanOptional | None

class DeleteDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String

class DeleteDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class DeleteDBClusterSnapshotMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String

class DeleteDBClusterSnapshotResult(TypedDict, total=False):
    DBClusterSnapshot: DBClusterSnapshot | None

class DeleteDBInstanceAutomatedBackupMessage(ServiceRequest):
    DbiResourceId: String | None
    DBInstanceAutomatedBackupsArn: String | None

class DeleteDBInstanceAutomatedBackupResult(TypedDict, total=False):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackup | None

class DeleteDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    SkipFinalSnapshot: Boolean | None
    FinalDBSnapshotIdentifier: String | None
    DeleteAutomatedBackups: BooleanOptional | None

class DeleteDBInstanceResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class DeleteDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String

class DeleteDBProxyEndpointRequest(ServiceRequest):
    DBProxyEndpointName: DBProxyEndpointName

class DeleteDBProxyEndpointResponse(TypedDict, total=False):
    DBProxyEndpoint: DBProxyEndpoint | None

class DeleteDBProxyRequest(ServiceRequest):
    DBProxyName: DBProxyName

class DeleteDBProxyResponse(TypedDict, total=False):
    DBProxy: DBProxy | None

class DeleteDBSecurityGroupMessage(ServiceRequest):
    DBSecurityGroupName: String

class DeleteDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier

class DeleteDBSnapshotMessage(ServiceRequest):
    DBSnapshotIdentifier: String

class DeleteDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: DBSnapshot | None

class DeleteDBSubnetGroupMessage(ServiceRequest):
    DBSubnetGroupName: String

class DeleteEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String

class DeleteEventSubscriptionResult(TypedDict, total=False):
    EventSubscription: EventSubscription | None

class DeleteGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier

class DeleteGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: GlobalCluster | None

class DeleteIntegrationMessage(ServiceRequest):
    IntegrationIdentifier: IntegrationIdentifier

class DeleteOptionGroupMessage(ServiceRequest):
    OptionGroupName: String

class DeleteTenantDatabaseMessage(ServiceRequest):
    DBInstanceIdentifier: String
    TenantDBName: String
    SkipFinalSnapshot: Boolean | None
    FinalDBSnapshotIdentifier: String | None

class DeleteTenantDatabaseResult(TypedDict, total=False):
    TenantDatabase: TenantDatabase | None

class DeregisterDBProxyTargetsRequest(ServiceRequest):
    DBProxyName: DBProxyName
    TargetGroupName: DBProxyTargetGroupName | None
    DBInstanceIdentifiers: StringList | None
    DBClusterIdentifiers: StringList | None

class DeregisterDBProxyTargetsResponse(TypedDict, total=False):
    pass

class DescribeAccountAttributesMessage(ServiceRequest):
    pass

FilterValueList = list[String]
class Filter(TypedDict, total=False):
    Name: String
    Values: FilterValueList

FilterList = list[Filter]
class DescribeBlueGreenDeploymentsRequest(ServiceRequest):
    BlueGreenDeploymentIdentifier: BlueGreenDeploymentIdentifier | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None

class DescribeBlueGreenDeploymentsResponse(TypedDict, total=False):
    BlueGreenDeployments: BlueGreenDeploymentList | None
    Marker: String | None

class DescribeCertificatesMessage(ServiceRequest):
    CertificateIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBClusterAutomatedBackupsMessage(ServiceRequest):
    DbClusterResourceId: String | None
    DBClusterIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBClusterBacktracksMessage(ServiceRequest):
    DBClusterIdentifier: String
    BacktrackIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBClusterEndpointsMessage(ServiceRequest):
    DBClusterIdentifier: String | None
    DBClusterEndpointIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBClusterParameterGroupsMessage(ServiceRequest):
    DBClusterParameterGroupName: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBClusterParametersMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    Source: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBClusterSnapshotAttributesMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String

class DescribeDBClusterSnapshotAttributesResult(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult | None

class DescribeDBClusterSnapshotsMessage(ServiceRequest):
    DBClusterIdentifier: String | None
    DBClusterSnapshotIdentifier: String | None
    SnapshotType: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    IncludeShared: Boolean | None
    IncludePublic: Boolean | None
    DbClusterResourceId: String | None

class DescribeDBClustersMessage(ServiceRequest):
    DBClusterIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    IncludeShared: Boolean | None

class DescribeDBEngineVersionsMessage(ServiceRequest):
    Engine: String | None
    EngineVersion: String | None
    DBParameterGroupFamily: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    DefaultOnly: Boolean | None
    ListSupportedCharacterSets: BooleanOptional | None
    ListSupportedTimezones: BooleanOptional | None
    IncludeAll: BooleanOptional | None

class DescribeDBInstanceAutomatedBackupsMessage(ServiceRequest):
    DbiResourceId: String | None
    DBInstanceIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    DBInstanceAutomatedBackupsArn: String | None

class DescribeDBInstancesMessage(ServiceRequest):
    DBInstanceIdentifier: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBLogFilesDetails(TypedDict, total=False):
    LogFileName: String | None
    LastWritten: Long | None
    Size: Long | None

DescribeDBLogFilesList = list[DescribeDBLogFilesDetails]
class DescribeDBLogFilesMessage(ServiceRequest):
    DBInstanceIdentifier: String
    FilenameContains: String | None
    FileLastWritten: Long | None
    FileSize: Long | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBLogFilesResponse(TypedDict, total=False):
    DescribeDBLogFiles: DescribeDBLogFilesList | None
    Marker: String | None

class DescribeDBMajorEngineVersionsRequest(ServiceRequest):
    Engine: Engine | None
    MajorEngineVersion: MajorEngineVersion | None
    Marker: Marker | None
    MaxRecords: MaxRecords | None

class DescribeDBMajorEngineVersionsResponse(TypedDict, total=False):
    DBMajorEngineVersions: DBMajorEngineVersionsList | None
    Marker: String | None

class DescribeDBParameterGroupsMessage(ServiceRequest):
    DBParameterGroupName: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBParametersMessage(ServiceRequest):
    DBParameterGroupName: String
    Source: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBProxiesRequest(ServiceRequest):
    DBProxyName: DBProxyName | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None

class DescribeDBProxiesResponse(TypedDict, total=False):
    DBProxies: DBProxyList | None
    Marker: String | None

class DescribeDBProxyEndpointsRequest(ServiceRequest):
    DBProxyName: DBProxyName | None
    DBProxyEndpointName: DBProxyEndpointName | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None

class DescribeDBProxyEndpointsResponse(TypedDict, total=False):
    DBProxyEndpoints: DBProxyEndpointList | None
    Marker: String | None

class DescribeDBProxyTargetGroupsRequest(ServiceRequest):
    DBProxyName: DBProxyName
    TargetGroupName: DBProxyTargetGroupName | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None

TargetGroupList = list[DBProxyTargetGroup]
class DescribeDBProxyTargetGroupsResponse(TypedDict, total=False):
    TargetGroups: TargetGroupList | None
    Marker: String | None

class DescribeDBProxyTargetsRequest(ServiceRequest):
    DBProxyName: DBProxyName
    TargetGroupName: DBProxyTargetGroupName | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None

TargetList = list[DBProxyTarget]
class DescribeDBProxyTargetsResponse(TypedDict, total=False):
    Targets: TargetList | None
    Marker: String | None

class DescribeDBRecommendationsMessage(ServiceRequest):
    LastUpdatedAfter: TStamp | None
    LastUpdatedBefore: TStamp | None
    Locale: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBSecurityGroupsMessage(ServiceRequest):
    DBSecurityGroupName: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeDBShardGroupsMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None

class DescribeDBShardGroupsResponse(TypedDict, total=False):
    DBShardGroups: DBShardGroupsList | None
    Marker: String | None

class DescribeDBSnapshotAttributesMessage(ServiceRequest):
    DBSnapshotIdentifier: String

class DescribeDBSnapshotAttributesResult(TypedDict, total=False):
    DBSnapshotAttributesResult: DBSnapshotAttributesResult | None

class DescribeDBSnapshotTenantDatabasesMessage(ServiceRequest):
    DBInstanceIdentifier: String | None
    DBSnapshotIdentifier: String | None
    SnapshotType: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    DbiResourceId: String | None

class DescribeDBSnapshotsMessage(ServiceRequest):
    DBInstanceIdentifier: String | None
    DBSnapshotIdentifier: String | None
    SnapshotType: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    IncludeShared: Boolean | None
    IncludePublic: Boolean | None
    DbiResourceId: String | None

class DescribeDBSubnetGroupsMessage(ServiceRequest):
    DBSubnetGroupName: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeEngineDefaultClusterParametersMessage(ServiceRequest):
    DBParameterGroupFamily: String
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class EngineDefaults(TypedDict, total=False):
    DBParameterGroupFamily: String | None
    Marker: String | None
    Parameters: ParametersList | None

class DescribeEngineDefaultClusterParametersResult(TypedDict, total=False):
    EngineDefaults: EngineDefaults | None

class DescribeEngineDefaultParametersMessage(ServiceRequest):
    DBParameterGroupFamily: String
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeEngineDefaultParametersResult(TypedDict, total=False):
    EngineDefaults: EngineDefaults | None

class DescribeEventCategoriesMessage(ServiceRequest):
    SourceType: String | None
    Filters: FilterList | None

class DescribeEventSubscriptionsMessage(ServiceRequest):
    SubscriptionName: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeEventsMessage(ServiceRequest):
    SourceIdentifier: String | None
    SourceType: SourceType | None
    StartTime: TStamp | None
    EndTime: TStamp | None
    Duration: IntegerOptional | None
    EventCategories: EventCategoriesList | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeExportTasksMessage(ServiceRequest):
    ExportTaskIdentifier: String | None
    SourceArn: String | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: MaxRecords | None
    SourceType: ExportSourceType | None

class DescribeGlobalClustersMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeIntegrationsMessage(ServiceRequest):
    IntegrationIdentifier: IntegrationIdentifier | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: Marker | None

class IntegrationError(TypedDict, total=False):
    ErrorCode: String
    ErrorMessage: String | None

IntegrationErrorList = list[IntegrationError]
class Integration(TypedDict, total=False):
    SourceArn: SourceArn | None
    TargetArn: Arn | None
    IntegrationName: IntegrationName | None
    IntegrationArn: IntegrationArn | None
    KMSKeyId: String | None
    AdditionalEncryptionContext: EncryptionContextMap | None
    Status: IntegrationStatus | None
    Tags: TagList | None
    DataFilter: DataFilter | None
    Description: IntegrationDescription | None
    CreateTime: TStamp | None
    Errors: IntegrationErrorList | None

IntegrationList = list[Integration]
class DescribeIntegrationsResponse(TypedDict, total=False):
    Marker: Marker | None
    Integrations: IntegrationList | None

class DescribeOptionGroupOptionsMessage(ServiceRequest):
    EngineName: String
    MajorEngineVersion: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeOptionGroupsMessage(ServiceRequest):
    OptionGroupName: String | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: IntegerOptional | None
    EngineName: String | None
    MajorEngineVersion: String | None

class DescribeOrderableDBInstanceOptionsMessage(ServiceRequest):
    Engine: String
    EngineVersion: String | None
    DBInstanceClass: String | None
    LicenseModel: String | None
    AvailabilityZoneGroup: String | None
    Vpc: BooleanOptional | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribePendingMaintenanceActionsMessage(ServiceRequest):
    ResourceIdentifier: String | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: IntegerOptional | None

class DescribeReservedDBInstancesMessage(ServiceRequest):
    ReservedDBInstanceId: String | None
    ReservedDBInstancesOfferingId: String | None
    DBInstanceClass: String | None
    Duration: String | None
    ProductDescription: String | None
    OfferingType: String | None
    MultiAZ: BooleanOptional | None
    LeaseId: String | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeReservedDBInstancesOfferingsMessage(ServiceRequest):
    ReservedDBInstancesOfferingId: String | None
    DBInstanceClass: String | None
    Duration: String | None
    ProductDescription: String | None
    OfferingType: String | None
    MultiAZ: BooleanOptional | None
    Filters: FilterList | None
    MaxRecords: IntegerOptional | None
    Marker: String | None

class DescribeSourceRegionsMessage(ServiceRequest):
    RegionName: String | None
    MaxRecords: IntegerOptional | None
    Marker: String | None
    Filters: FilterList | None

class DescribeTenantDatabasesMessage(ServiceRequest):
    DBInstanceIdentifier: String | None
    TenantDBName: String | None
    Filters: FilterList | None
    Marker: String | None
    MaxRecords: IntegerOptional | None

class DescribeValidDBInstanceModificationsMessage(ServiceRequest):
    DBInstanceIdentifier: String

class DoubleRange(TypedDict, total=False):
    From: Double | None
    To: Double | None

DoubleRangeList = list[DoubleRange]
class Range(TypedDict, total=False):
    From: Integer | None
    To: Integer | None
    Step: IntegerOptional | None

RangeList = list[Range]
class ValidStorageOptions(TypedDict, total=False):
    StorageType: String | None
    StorageSize: RangeList | None
    ProvisionedIops: RangeList | None
    IopsToStorageRatio: DoubleRangeList | None
    ProvisionedStorageThroughput: RangeList | None
    StorageThroughputToIopsRatio: DoubleRangeList | None
    SupportsStorageAutoscaling: Boolean | None

ValidStorageOptionsList = list[ValidStorageOptions]
class ValidVolumeOptions(TypedDict, total=False):
    VolumeName: String | None
    Storage: ValidStorageOptionsList | None

ValidVolumeOptionsList = list[ValidVolumeOptions]
class ValidAdditionalStorageOptions(TypedDict, total=False):
    SupportsAdditionalStorageVolumes: Boolean | None
    Volumes: ValidVolumeOptionsList | None

class ValidDBInstanceModificationsMessage(TypedDict, total=False):
    Storage: ValidStorageOptionsList | None
    ValidProcessorFeatures: AvailableProcessorFeatureList | None
    SupportsDedicatedLogVolume: Boolean | None
    AdditionalStorage: ValidAdditionalStorageOptions | None

class DescribeValidDBInstanceModificationsResult(TypedDict, total=False):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessage | None

class DisableHttpEndpointRequest(ServiceRequest):
    ResourceArn: String

class DisableHttpEndpointResponse(TypedDict, total=False):
    ResourceArn: String | None
    HttpEndpointEnabled: Boolean | None

class DownloadDBLogFilePortionDetails(TypedDict, total=False):
    LogFileData: SensitiveString | None
    Marker: String | None
    AdditionalDataPending: Boolean | None

class DownloadDBLogFilePortionMessage(ServiceRequest):
    DBInstanceIdentifier: String
    LogFileName: String
    Marker: String | None
    NumberOfLines: Integer | None

class EnableHttpEndpointRequest(ServiceRequest):
    ResourceArn: String

class EnableHttpEndpointResponse(TypedDict, total=False):
    ResourceArn: String | None
    HttpEndpointEnabled: Boolean | None

class Event(TypedDict, total=False):
    SourceIdentifier: String | None
    SourceType: SourceType | None
    Message: String | None
    EventCategories: EventCategoriesList | None
    Date: TStamp | None
    SourceArn: String | None

class EventCategoriesMap(TypedDict, total=False):
    SourceType: String | None
    EventCategories: EventCategoriesList | None

EventCategoriesMapList = list[EventCategoriesMap]
class EventCategoriesMessage(TypedDict, total=False):
    EventCategoriesMapList: EventCategoriesMapList | None

EventList = list[Event]
EventSubscriptionsList = list[EventSubscription]
class EventSubscriptionsMessage(TypedDict, total=False):
    Marker: String | None
    EventSubscriptionsList: EventSubscriptionsList | None

class EventsMessage(TypedDict, total=False):
    Marker: String | None
    Events: EventList | None

class ExportTask(TypedDict, total=False):
    ExportTaskIdentifier: String | None
    SourceArn: String | None
    ExportOnly: StringList | None
    SnapshotTime: TStamp | None
    TaskStartTime: TStamp | None
    TaskEndTime: TStamp | None
    S3Bucket: String | None
    S3Prefix: String | None
    IamRoleArn: String | None
    KmsKeyId: String | None
    Status: String | None
    PercentProgress: Integer | None
    TotalExtractedDataInGB: Integer | None
    FailureCause: String | None
    WarningMessage: String | None
    SourceType: ExportSourceType | None

ExportTasksList = list[ExportTask]
class ExportTasksMessage(TypedDict, total=False):
    Marker: String | None
    ExportTasks: ExportTasksList | None

class FailoverDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    TargetDBInstanceIdentifier: String | None

class FailoverDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class FailoverGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    TargetDbClusterIdentifier: DBClusterIdentifier
    AllowDataLoss: BooleanOptional | None
    Switchover: BooleanOptional | None

class FailoverGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: GlobalCluster | None

GlobalClusterList = list[GlobalCluster]
class GlobalClustersMessage(TypedDict, total=False):
    Marker: String | None
    GlobalClusters: GlobalClusterList | None

KeyList = list[String]
class ListTagsForResourceMessage(ServiceRequest):
    ResourceName: String
    Filters: FilterList | None

class MinimumEngineVersionPerAllowedValue(TypedDict, total=False):
    AllowedValue: String | None
    MinimumEngineVersion: String | None

MinimumEngineVersionPerAllowedValueList = list[MinimumEngineVersionPerAllowedValue]
class ModifyActivityStreamRequest(ServiceRequest):
    ResourceArn: String | None
    AuditPolicyState: AuditPolicyState | None

class ModifyActivityStreamResponse(TypedDict, total=False):
    KmsKeyId: String | None
    KinesisStreamName: String | None
    Status: ActivityStreamStatus | None
    Mode: ActivityStreamMode | None
    EngineNativeAuditFieldsIncluded: BooleanOptional | None
    PolicyStatus: ActivityStreamPolicyStatus | None

class ModifyAdditionalStorageVolume(TypedDict, total=False):
    VolumeName: String
    AllocatedStorage: IntegerOptional | None
    IOPS: IntegerOptional | None
    MaxAllocatedStorage: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    StorageType: String | None
    SetForDelete: BooleanOptional | None

ModifyAdditionalStorageVolumesList = list[ModifyAdditionalStorageVolume]
class ModifyCertificatesMessage(ServiceRequest):
    CertificateIdentifier: String | None
    RemoveCustomerOverride: BooleanOptional | None

class ModifyCertificatesResult(TypedDict, total=False):
    Certificate: Certificate | None

class ModifyCurrentDBClusterCapacityMessage(ServiceRequest):
    DBClusterIdentifier: String
    Capacity: IntegerOptional | None
    SecondsBeforeTimeout: IntegerOptional | None
    TimeoutAction: String | None

class ModifyCustomDBEngineVersionMessage(ServiceRequest):
    Engine: CustomEngineName
    EngineVersion: CustomEngineVersion
    Description: Description | None
    Status: CustomEngineVersionStatus | None

class ModifyDBClusterEndpointMessage(ServiceRequest):
    DBClusterEndpointIdentifier: String
    EndpointType: String | None
    StaticMembers: StringList | None
    ExcludedMembers: StringList | None

class ModifyDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    NewDBClusterIdentifier: String | None
    ApplyImmediately: Boolean | None
    BackupRetentionPeriod: IntegerOptional | None
    DBClusterParameterGroupName: String | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    Port: IntegerOptional | None
    MasterUserPassword: SensitiveString | None
    OptionGroupName: String | None
    PreferredBackupWindow: String | None
    PreferredMaintenanceWindow: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    BacktrackWindow: LongOptional | None
    CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfiguration | None
    EngineVersion: String | None
    AllowMajorVersionUpgrade: Boolean | None
    DBInstanceParameterGroupName: String | None
    Domain: String | None
    DomainIAMRoleName: String | None
    ScalingConfiguration: ScalingConfiguration | None
    DeletionProtection: BooleanOptional | None
    EnableHttpEndpoint: BooleanOptional | None
    CopyTagsToSnapshot: BooleanOptional | None
    EnableGlobalWriteForwarding: BooleanOptional | None
    DBClusterInstanceClass: String | None
    AllocatedStorage: IntegerOptional | None
    StorageType: String | None
    Iops: IntegerOptional | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    NetworkType: String | None
    ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfiguration | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    ManageMasterUserPassword: BooleanOptional | None
    RotateMasterUserPassword: BooleanOptional | None
    EnableLocalWriteForwarding: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    EngineMode: String | None
    AllowEngineModeChange: Boolean | None
    AwsBackupRecoveryPointArn: AwsBackupRecoveryPointArn | None
    EnableLimitlessDatabase: BooleanOptional | None
    CACertificateIdentifier: String | None
    MasterUserAuthenticationType: MasterUserAuthenticationType | None

class ModifyDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    Parameters: ParametersList

class ModifyDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class ModifyDBClusterSnapshotAttributeMessage(ServiceRequest):
    DBClusterSnapshotIdentifier: String
    AttributeName: String
    ValuesToAdd: AttributeValueList | None
    ValuesToRemove: AttributeValueList | None

class ModifyDBClusterSnapshotAttributeResult(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult | None

class ModifyDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    AllocatedStorage: IntegerOptional | None
    DBInstanceClass: String | None
    DBSubnetGroupName: String | None
    DBSecurityGroups: DBSecurityGroupNameList | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    ApplyImmediately: Boolean | None
    MasterUserPassword: SensitiveString | None
    DBParameterGroupName: String | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    PreferredMaintenanceWindow: String | None
    MultiAZ: BooleanOptional | None
    EngineVersion: String | None
    AllowMajorVersionUpgrade: Boolean | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    LicenseModel: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    NewDBInstanceIdentifier: String | None
    StorageType: String | None
    TdeCredentialArn: String | None
    TdeCredentialPassword: SensitiveString | None
    CACertificateIdentifier: String | None
    Domain: String | None
    DomainFqdn: String | None
    DomainOu: String | None
    DomainAuthSecretArn: String | None
    DomainDnsIps: StringList | None
    DisableDomain: BooleanOptional | None
    CopyTagsToSnapshot: BooleanOptional | None
    MonitoringInterval: IntegerOptional | None
    DBPortNumber: IntegerOptional | None
    PubliclyAccessible: BooleanOptional | None
    MonitoringRoleArn: String | None
    DomainIAMRoleName: String | None
    PromotionTier: IntegerOptional | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    DatabaseInsightsMode: DatabaseInsightsMode | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfiguration | None
    ProcessorFeatures: ProcessorFeatureList | None
    UseDefaultProcessorFeatures: BooleanOptional | None
    DeletionProtection: BooleanOptional | None
    MaxAllocatedStorage: IntegerOptional | None
    CertificateRotationRestart: BooleanOptional | None
    ReplicaMode: ReplicaMode | None
    AutomationMode: AutomationMode | None
    ResumeFullAutomationModeMinutes: IntegerOptional | None
    EnableCustomerOwnedIp: BooleanOptional | None
    NetworkType: String | None
    AwsBackupRecoveryPointArn: AwsBackupRecoveryPointArn | None
    ManageMasterUserPassword: BooleanOptional | None
    RotateMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    MultiTenant: BooleanOptional | None
    DedicatedLogVolume: BooleanOptional | None
    Engine: String | None
    AdditionalStorageVolumes: ModifyAdditionalStorageVolumesList | None
    TagSpecifications: TagSpecificationList | None
    MasterUserAuthenticationType: MasterUserAuthenticationType | None

class ModifyDBInstanceResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class ModifyDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String
    Parameters: ParametersList

class ModifyDBProxyEndpointRequest(ServiceRequest):
    DBProxyEndpointName: DBProxyEndpointName
    NewDBProxyEndpointName: DBProxyEndpointName | None
    VpcSecurityGroupIds: StringList | None

class ModifyDBProxyEndpointResponse(TypedDict, total=False):
    DBProxyEndpoint: DBProxyEndpoint | None

class ModifyDBProxyRequest(ServiceRequest):
    DBProxyName: DBProxyName
    NewDBProxyName: DBProxyName | None
    DefaultAuthScheme: DefaultAuthScheme | None
    Auth: UserAuthConfigList | None
    RequireTLS: BooleanOptional | None
    IdleClientTimeout: IntegerOptional | None
    DebugLogging: BooleanOptional | None
    RoleArn: Arn | None
    SecurityGroups: StringList | None

class ModifyDBProxyResponse(TypedDict, total=False):
    DBProxy: DBProxy | None

class ModifyDBProxyTargetGroupRequest(ServiceRequest):
    TargetGroupName: DBProxyTargetGroupName
    DBProxyName: DBProxyName
    ConnectionPoolConfig: ConnectionPoolConfiguration | None
    NewName: String | None

class ModifyDBProxyTargetGroupResponse(TypedDict, total=False):
    DBProxyTargetGroup: DBProxyTargetGroup | None

class RecommendedActionUpdate(TypedDict, total=False):
    ActionId: String
    Status: String

RecommendedActionUpdateList = list[RecommendedActionUpdate]
class ModifyDBRecommendationMessage(ServiceRequest):
    RecommendationId: String
    Locale: String | None
    Status: String | None
    RecommendedActionUpdates: RecommendedActionUpdateList | None

class ModifyDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier
    MaxACU: DoubleOptional | None
    MinACU: DoubleOptional | None
    ComputeRedundancy: IntegerOptional | None

class ModifyDBSnapshotAttributeMessage(ServiceRequest):
    DBSnapshotIdentifier: String
    AttributeName: String
    ValuesToAdd: AttributeValueList | None
    ValuesToRemove: AttributeValueList | None

class ModifyDBSnapshotAttributeResult(TypedDict, total=False):
    DBSnapshotAttributesResult: DBSnapshotAttributesResult | None

class ModifyDBSnapshotMessage(ServiceRequest):
    DBSnapshotIdentifier: String
    EngineVersion: String | None
    OptionGroupName: String | None

class ModifyDBSnapshotResult(TypedDict, total=False):
    DBSnapshot: DBSnapshot | None

class ModifyDBSubnetGroupMessage(ServiceRequest):
    DBSubnetGroupName: String
    DBSubnetGroupDescription: String | None
    SubnetIds: SubnetIdentifierList

class ModifyDBSubnetGroupResult(TypedDict, total=False):
    DBSubnetGroup: DBSubnetGroup | None

class ModifyEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SnsTopicArn: String | None
    SourceType: String | None
    EventCategories: EventCategoriesList | None
    Enabled: BooleanOptional | None

class ModifyEventSubscriptionResult(TypedDict, total=False):
    EventSubscription: EventSubscription | None

class ModifyGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    NewGlobalClusterIdentifier: GlobalClusterIdentifier | None
    DeletionProtection: BooleanOptional | None
    EngineVersion: String | None
    AllowMajorVersionUpgrade: BooleanOptional | None

class ModifyGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: GlobalCluster | None

class ModifyIntegrationMessage(ServiceRequest):
    IntegrationIdentifier: IntegrationIdentifier
    IntegrationName: IntegrationName | None
    DataFilter: DataFilter | None
    Description: IntegrationDescription | None

OptionNamesList = list[String]
OptionSettingsList = list[OptionSetting]
class OptionConfiguration(TypedDict, total=False):
    OptionName: String
    Port: IntegerOptional | None
    OptionVersion: String | None
    DBSecurityGroupMemberships: DBSecurityGroupNameList | None
    VpcSecurityGroupMemberships: VpcSecurityGroupIdList | None
    OptionSettings: OptionSettingsList | None

OptionConfigurationList = list[OptionConfiguration]
class ModifyOptionGroupMessage(ServiceRequest):
    OptionGroupName: String
    OptionsToInclude: OptionConfigurationList | None
    OptionsToRemove: OptionNamesList | None
    ApplyImmediately: Boolean | None

class ModifyOptionGroupResult(TypedDict, total=False):
    OptionGroup: OptionGroup | None

class ModifyTenantDatabaseMessage(ServiceRequest):
    DBInstanceIdentifier: String
    TenantDBName: String
    MasterUserPassword: SensitiveString | None
    NewTenantDBName: String | None
    ManageMasterUserPassword: BooleanOptional | None
    RotateMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None

class ModifyTenantDatabaseResult(TypedDict, total=False):
    TenantDatabase: TenantDatabase | None

class OptionVersion(TypedDict, total=False):
    Version: String | None
    IsDefault: Boolean | None

OptionGroupOptionVersionsList = list[OptionVersion]
class OptionGroupOptionSetting(TypedDict, total=False):
    SettingName: String | None
    SettingDescription: String | None
    DefaultValue: String | None
    ApplyType: String | None
    AllowedValues: String | None
    IsModifiable: Boolean | None
    IsRequired: Boolean | None
    MinimumEngineVersionPerAllowedValue: MinimumEngineVersionPerAllowedValueList | None

OptionGroupOptionSettingsList = list[OptionGroupOptionSetting]
OptionsConflictsWith = list[String]
OptionsDependedOn = list[String]
class OptionGroupOption(TypedDict, total=False):
    Name: String | None
    Description: String | None
    EngineName: String | None
    MajorEngineVersion: String | None
    MinimumRequiredMinorEngineVersion: String | None
    PortRequired: Boolean | None
    DefaultPort: IntegerOptional | None
    OptionsDependedOn: OptionsDependedOn | None
    OptionsConflictsWith: OptionsConflictsWith | None
    Persistent: Boolean | None
    Permanent: Boolean | None
    RequiresAutoMinorEngineVersionUpgrade: Boolean | None
    VpcOnly: Boolean | None
    SupportsOptionVersionDowngrade: BooleanOptional | None
    OptionGroupOptionSettings: OptionGroupOptionSettingsList | None
    OptionGroupOptionVersions: OptionGroupOptionVersionsList | None
    CopyableCrossAccount: BooleanOptional | None

OptionGroupOptionsList = list[OptionGroupOption]
class OptionGroupOptionsMessage(TypedDict, total=False):
    OptionGroupOptions: OptionGroupOptionsList | None
    Marker: String | None

OptionGroupsList = list[OptionGroup]
class OptionGroups(TypedDict, total=False):
    OptionGroupsList: OptionGroupsList | None
    Marker: String | None

class OrderableDBInstanceOption(TypedDict, total=False):
    Engine: String | None
    EngineVersion: String | None
    DBInstanceClass: String | None
    LicenseModel: String | None
    AvailabilityZoneGroup: String | None
    AvailabilityZones: AvailabilityZoneList | None
    MultiAZCapable: Boolean | None
    ReadReplicaCapable: Boolean | None
    Vpc: Boolean | None
    SupportsStorageEncryption: Boolean | None
    StorageType: String | None
    SupportsIops: Boolean | None
    SupportsStorageThroughput: Boolean | None
    SupportsEnhancedMonitoring: Boolean | None
    SupportsIAMDatabaseAuthentication: Boolean | None
    SupportsPerformanceInsights: Boolean | None
    MinStorageSize: IntegerOptional | None
    MaxStorageSize: IntegerOptional | None
    MinIopsPerDbInstance: IntegerOptional | None
    MaxIopsPerDbInstance: IntegerOptional | None
    MinIopsPerGib: DoubleOptional | None
    MaxIopsPerGib: DoubleOptional | None
    MinStorageThroughputPerDbInstance: IntegerOptional | None
    MaxStorageThroughputPerDbInstance: IntegerOptional | None
    MinStorageThroughputPerIops: DoubleOptional | None
    MaxStorageThroughputPerIops: DoubleOptional | None
    AvailableProcessorFeatures: AvailableProcessorFeatureList | None
    SupportedEngineModes: EngineModeList | None
    SupportsStorageAutoscaling: BooleanOptional | None
    SupportsKerberosAuthentication: BooleanOptional | None
    OutpostCapable: Boolean | None
    SupportedActivityStreamModes: ActivityStreamModeList | None
    SupportsGlobalDatabases: Boolean | None
    SupportedNetworkTypes: StringList | None
    SupportsClusters: Boolean | None
    SupportsDedicatedLogVolume: Boolean | None
    SupportsAdditionalStorageVolumes: BooleanOptional | None
    SupportsHttpEndpoint: Boolean | None
    AvailableAdditionalStorageVolumesOptions: AvailableAdditionalStorageVolumesOptionList | None

OrderableDBInstanceOptionsList = list[OrderableDBInstanceOption]
class OrderableDBInstanceOptionsMessage(TypedDict, total=False):
    OrderableDBInstanceOptions: OrderableDBInstanceOptionsList | None
    Marker: String | None

PendingMaintenanceActions = list[ResourcePendingMaintenanceActions]
class PendingMaintenanceActionsMessage(TypedDict, total=False):
    PendingMaintenanceActions: PendingMaintenanceActions | None
    Marker: String | None

class PromoteReadReplicaDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String

class PromoteReadReplicaDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class PromoteReadReplicaMessage(ServiceRequest):
    DBInstanceIdentifier: String
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    TagSpecifications: TagSpecificationList | None

class PromoteReadReplicaResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class PurchaseReservedDBInstancesOfferingMessage(ServiceRequest):
    ReservedDBInstancesOfferingId: String
    ReservedDBInstanceId: String | None
    DBInstanceCount: IntegerOptional | None
    Tags: TagList | None

class RecurringCharge(TypedDict, total=False):
    RecurringChargeAmount: Double | None
    RecurringChargeFrequency: String | None

RecurringChargeList = list[RecurringCharge]
class ReservedDBInstance(TypedDict, total=False):
    ReservedDBInstanceId: String | None
    ReservedDBInstancesOfferingId: String | None
    DBInstanceClass: String | None
    StartTime: TStamp | None
    Duration: Integer | None
    FixedPrice: Double | None
    UsagePrice: Double | None
    CurrencyCode: String | None
    DBInstanceCount: Integer | None
    ProductDescription: String | None
    OfferingType: String | None
    MultiAZ: Boolean | None
    State: String | None
    RecurringCharges: RecurringChargeList | None
    ReservedDBInstanceArn: String | None
    LeaseId: String | None

class PurchaseReservedDBInstancesOfferingResult(TypedDict, total=False):
    ReservedDBInstance: ReservedDBInstance | None

class RebootDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String

class RebootDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class RebootDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    ForceFailover: BooleanOptional | None

class RebootDBInstanceResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class RebootDBShardGroupMessage(ServiceRequest):
    DBShardGroupIdentifier: DBShardGroupIdentifier

class RegisterDBProxyTargetsRequest(ServiceRequest):
    DBProxyName: DBProxyName
    TargetGroupName: DBProxyTargetGroupName | None
    DBInstanceIdentifiers: StringList | None
    DBClusterIdentifiers: StringList | None

class RegisterDBProxyTargetsResponse(TypedDict, total=False):
    DBProxyTargets: TargetList | None

class RemoveFromGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    DbClusterIdentifier: String

class RemoveFromGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: GlobalCluster | None

class RemoveRoleFromDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String
    RoleArn: String
    FeatureName: String | None

class RemoveRoleFromDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    RoleArn: String
    FeatureName: String

class RemoveSourceIdentifierFromSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SourceIdentifier: String

class RemoveSourceIdentifierFromSubscriptionResult(TypedDict, total=False):
    EventSubscription: EventSubscription | None

class RemoveTagsFromResourceMessage(ServiceRequest):
    ResourceName: String
    TagKeys: KeyList

ReservedDBInstanceList = list[ReservedDBInstance]
class ReservedDBInstanceMessage(TypedDict, total=False):
    Marker: String | None
    ReservedDBInstances: ReservedDBInstanceList | None

class ReservedDBInstancesOffering(TypedDict, total=False):
    ReservedDBInstancesOfferingId: String | None
    DBInstanceClass: String | None
    Duration: Integer | None
    FixedPrice: Double | None
    UsagePrice: Double | None
    CurrencyCode: String | None
    ProductDescription: String | None
    OfferingType: String | None
    MultiAZ: Boolean | None
    RecurringCharges: RecurringChargeList | None

ReservedDBInstancesOfferingList = list[ReservedDBInstancesOffering]
class ReservedDBInstancesOfferingMessage(TypedDict, total=False):
    Marker: String | None
    ReservedDBInstancesOfferings: ReservedDBInstancesOfferingList | None

class ResetDBClusterParameterGroupMessage(ServiceRequest):
    DBClusterParameterGroupName: String
    ResetAllParameters: Boolean | None
    Parameters: ParametersList | None

class ResetDBParameterGroupMessage(ServiceRequest):
    DBParameterGroupName: String
    ResetAllParameters: Boolean | None
    Parameters: ParametersList | None

class RestoreDBClusterFromS3Message(ServiceRequest):
    AvailabilityZones: AvailabilityZones | None
    BackupRetentionPeriod: IntegerOptional | None
    CharacterSetName: String | None
    DatabaseName: String | None
    DBClusterIdentifier: String
    DBClusterParameterGroupName: String | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    DBSubnetGroupName: String | None
    Engine: String
    EngineVersion: String | None
    Port: IntegerOptional | None
    MasterUsername: String
    MasterUserPassword: SensitiveString | None
    OptionGroupName: String | None
    PreferredBackupWindow: String | None
    PreferredMaintenanceWindow: String | None
    Tags: TagList | None
    StorageEncrypted: BooleanOptional | None
    KmsKeyId: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    SourceEngine: String
    SourceEngineVersion: String
    S3BucketName: String
    S3Prefix: String | None
    S3IngestionRoleArn: String
    BacktrackWindow: LongOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    DeletionProtection: BooleanOptional | None
    CopyTagsToSnapshot: BooleanOptional | None
    Domain: String | None
    DomainIAMRoleName: String | None
    StorageType: String | None
    NetworkType: String | None
    ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfiguration | None
    ManageMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    EngineLifecycleSupport: String | None
    TagSpecifications: TagSpecificationList | None

class RestoreDBClusterFromS3Result(TypedDict, total=False):
    DBCluster: DBCluster | None

class RestoreDBClusterFromSnapshotMessage(ServiceRequest):
    AvailabilityZones: AvailabilityZones | None
    DBClusterIdentifier: String
    SnapshotIdentifier: String
    Engine: String
    EngineVersion: String | None
    Port: IntegerOptional | None
    DBSubnetGroupName: String | None
    DatabaseName: String | None
    OptionGroupName: String | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    Tags: TagList | None
    KmsKeyId: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    BacktrackWindow: LongOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    EngineMode: String | None
    ScalingConfiguration: ScalingConfiguration | None
    DBClusterParameterGroupName: String | None
    DeletionProtection: BooleanOptional | None
    CopyTagsToSnapshot: BooleanOptional | None
    Domain: String | None
    DomainIAMRoleName: String | None
    DBClusterInstanceClass: String | None
    StorageType: String | None
    Iops: IntegerOptional | None
    PubliclyAccessible: BooleanOptional | None
    NetworkType: String | None
    ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfiguration | None
    RdsCustomClusterConfiguration: RdsCustomClusterConfiguration | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    EngineLifecycleSupport: String | None
    TagSpecifications: TagSpecificationList | None

class RestoreDBClusterFromSnapshotResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class RestoreDBClusterToPointInTimeMessage(ServiceRequest):
    DBClusterIdentifier: String
    RestoreType: String | None
    SourceDBClusterIdentifier: String | None
    RestoreToTime: TStamp | None
    UseLatestRestorableTime: Boolean | None
    Port: IntegerOptional | None
    DBSubnetGroupName: String | None
    OptionGroupName: String | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    Tags: TagList | None
    KmsKeyId: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    BacktrackWindow: LongOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    DBClusterParameterGroupName: String | None
    DeletionProtection: BooleanOptional | None
    CopyTagsToSnapshot: BooleanOptional | None
    Domain: String | None
    DomainIAMRoleName: String | None
    DBClusterInstanceClass: String | None
    StorageType: String | None
    PubliclyAccessible: BooleanOptional | None
    Iops: IntegerOptional | None
    NetworkType: String | None
    SourceDbClusterResourceId: String | None
    ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfiguration | None
    ScalingConfiguration: ScalingConfiguration | None
    EngineMode: String | None
    RdsCustomClusterConfiguration: RdsCustomClusterConfiguration | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    EngineLifecycleSupport: String | None
    TagSpecifications: TagSpecificationList | None

class RestoreDBClusterToPointInTimeResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class RestoreDBInstanceFromDBSnapshotMessage(ServiceRequest):
    DBInstanceIdentifier: String
    DBSnapshotIdentifier: String | None
    DBInstanceClass: String | None
    Port: IntegerOptional | None
    AvailabilityZone: String | None
    DBSubnetGroupName: String | None
    MultiAZ: BooleanOptional | None
    PubliclyAccessible: BooleanOptional | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    LicenseModel: String | None
    DBName: String | None
    Engine: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    Tags: TagList | None
    StorageType: String | None
    TdeCredentialArn: String | None
    TdeCredentialPassword: SensitiveString | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    Domain: String | None
    DomainFqdn: String | None
    DomainOu: String | None
    DomainAuthSecretArn: String | None
    DomainDnsIps: StringList | None
    CopyTagsToSnapshot: BooleanOptional | None
    DomainIAMRoleName: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    ProcessorFeatures: ProcessorFeatureList | None
    UseDefaultProcessorFeatures: BooleanOptional | None
    DBParameterGroupName: String | None
    DeletionProtection: BooleanOptional | None
    EnableCustomerOwnedIp: BooleanOptional | None
    NetworkType: String | None
    BackupTarget: String | None
    CustomIamInstanceProfile: String | None
    AllocatedStorage: IntegerOptional | None
    DBClusterSnapshotIdentifier: String | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    DedicatedLogVolume: BooleanOptional | None
    CACertificateIdentifier: String | None
    EngineLifecycleSupport: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None
    TagSpecifications: TagSpecificationList | None
    ManageMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None

class RestoreDBInstanceFromDBSnapshotResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class RestoreDBInstanceFromS3Message(ServiceRequest):
    DBName: String | None
    DBInstanceIdentifier: String
    AllocatedStorage: IntegerOptional | None
    DBInstanceClass: String
    Engine: String
    MasterUsername: String | None
    MasterUserPassword: SensitiveString | None
    DBSecurityGroups: DBSecurityGroupNameList | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    AvailabilityZone: String | None
    DBSubnetGroupName: String | None
    PreferredMaintenanceWindow: String | None
    DBParameterGroupName: String | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    Port: IntegerOptional | None
    MultiAZ: BooleanOptional | None
    EngineVersion: String | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    LicenseModel: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    PubliclyAccessible: BooleanOptional | None
    Tags: TagList | None
    StorageType: String | None
    StorageEncrypted: BooleanOptional | None
    KmsKeyId: String | None
    CopyTagsToSnapshot: BooleanOptional | None
    MonitoringInterval: IntegerOptional | None
    MonitoringRoleArn: String | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    SourceEngine: String
    SourceEngineVersion: String
    S3BucketName: String
    S3Prefix: String | None
    S3IngestionRoleArn: String
    DatabaseInsightsMode: DatabaseInsightsMode | None
    EnablePerformanceInsights: BooleanOptional | None
    PerformanceInsightsKMSKeyId: String | None
    PerformanceInsightsRetentionPeriod: IntegerOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    ProcessorFeatures: ProcessorFeatureList | None
    UseDefaultProcessorFeatures: BooleanOptional | None
    DeletionProtection: BooleanOptional | None
    MaxAllocatedStorage: IntegerOptional | None
    NetworkType: String | None
    ManageMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None
    DedicatedLogVolume: BooleanOptional | None
    CACertificateIdentifier: String | None
    EngineLifecycleSupport: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None
    TagSpecifications: TagSpecificationList | None

class RestoreDBInstanceFromS3Result(TypedDict, total=False):
    DBInstance: DBInstance | None

class RestoreDBInstanceToPointInTimeMessage(ServiceRequest):
    SourceDBInstanceIdentifier: String | None
    TargetDBInstanceIdentifier: String
    RestoreTime: TStamp | None
    UseLatestRestorableTime: Boolean | None
    DBInstanceClass: String | None
    Port: IntegerOptional | None
    AvailabilityZone: String | None
    DBSubnetGroupName: String | None
    MultiAZ: BooleanOptional | None
    PubliclyAccessible: BooleanOptional | None
    AutoMinorVersionUpgrade: BooleanOptional | None
    LicenseModel: String | None
    DBName: String | None
    Engine: String | None
    Iops: IntegerOptional | None
    StorageThroughput: IntegerOptional | None
    OptionGroupName: String | None
    CopyTagsToSnapshot: BooleanOptional | None
    Tags: TagList | None
    StorageType: String | None
    TdeCredentialArn: String | None
    TdeCredentialPassword: SensitiveString | None
    VpcSecurityGroupIds: VpcSecurityGroupIdList | None
    Domain: String | None
    DomainIAMRoleName: String | None
    DomainFqdn: String | None
    DomainOu: String | None
    DomainAuthSecretArn: String | None
    DomainDnsIps: StringList | None
    EnableIAMDatabaseAuthentication: BooleanOptional | None
    EnableCloudwatchLogsExports: LogTypeList | None
    ProcessorFeatures: ProcessorFeatureList | None
    UseDefaultProcessorFeatures: BooleanOptional | None
    DBParameterGroupName: String | None
    DeletionProtection: BooleanOptional | None
    SourceDbiResourceId: String | None
    MaxAllocatedStorage: IntegerOptional | None
    EnableCustomerOwnedIp: BooleanOptional | None
    NetworkType: String | None
    SourceDBInstanceAutomatedBackupsArn: String | None
    BackupTarget: String | None
    CustomIamInstanceProfile: String | None
    AllocatedStorage: IntegerOptional | None
    BackupRetentionPeriod: IntegerOptional | None
    PreferredBackupWindow: String | None
    DedicatedLogVolume: BooleanOptional | None
    CACertificateIdentifier: String | None
    EngineLifecycleSupport: String | None
    AdditionalStorageVolumes: AdditionalStorageVolumesList | None
    TagSpecifications: TagSpecificationList | None
    ManageMasterUserPassword: BooleanOptional | None
    MasterUserSecretKmsKeyId: String | None

class RestoreDBInstanceToPointInTimeResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class RevokeDBSecurityGroupIngressMessage(ServiceRequest):
    DBSecurityGroupName: String
    CIDRIP: String | None
    EC2SecurityGroupName: String | None
    EC2SecurityGroupId: String | None
    EC2SecurityGroupOwnerId: String | None

class RevokeDBSecurityGroupIngressResult(TypedDict, total=False):
    DBSecurityGroup: DBSecurityGroup | None

class SourceRegion(TypedDict, total=False):
    RegionName: String | None
    Endpoint: String | None
    Status: String | None
    SupportsDBInstanceAutomatedBackupsReplication: Boolean | None

SourceRegionList = list[SourceRegion]
class SourceRegionMessage(TypedDict, total=False):
    Marker: String | None
    SourceRegions: SourceRegionList | None

class StartActivityStreamRequest(ServiceRequest):
    ResourceArn: String
    Mode: ActivityStreamMode
    KmsKeyId: String
    ApplyImmediately: BooleanOptional | None
    EngineNativeAuditFieldsIncluded: BooleanOptional | None

class StartActivityStreamResponse(TypedDict, total=False):
    KmsKeyId: String | None
    KinesisStreamName: String | None
    Status: ActivityStreamStatus | None
    Mode: ActivityStreamMode | None
    EngineNativeAuditFieldsIncluded: BooleanOptional | None
    ApplyImmediately: Boolean | None

class StartDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String

class StartDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class StartDBInstanceAutomatedBackupsReplicationMessage(ServiceRequest):
    SourceDBInstanceArn: String
    BackupRetentionPeriod: IntegerOptional | None
    KmsKeyId: String | None
    PreSignedUrl: SensitiveString | None
    Tags: TagList | None
    SourceRegion: String | None

class StartDBInstanceAutomatedBackupsReplicationResult(TypedDict, total=False):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackup | None

class StartDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String

class StartDBInstanceResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class StartExportTaskMessage(ServiceRequest):
    ExportTaskIdentifier: String
    SourceArn: String
    S3BucketName: String
    IamRoleArn: String
    KmsKeyId: String
    S3Prefix: String | None
    ExportOnly: StringList | None

class StopActivityStreamRequest(ServiceRequest):
    ResourceArn: String
    ApplyImmediately: BooleanOptional | None

class StopActivityStreamResponse(TypedDict, total=False):
    KmsKeyId: String | None
    KinesisStreamName: String | None
    Status: ActivityStreamStatus | None

class StopDBClusterMessage(ServiceRequest):
    DBClusterIdentifier: String

class StopDBClusterResult(TypedDict, total=False):
    DBCluster: DBCluster | None

class StopDBInstanceAutomatedBackupsReplicationMessage(ServiceRequest):
    SourceDBInstanceArn: String

class StopDBInstanceAutomatedBackupsReplicationResult(TypedDict, total=False):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackup | None

class StopDBInstanceMessage(ServiceRequest):
    DBInstanceIdentifier: String
    DBSnapshotIdentifier: String | None

class StopDBInstanceResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class SwitchoverBlueGreenDeploymentRequest(ServiceRequest):
    BlueGreenDeploymentIdentifier: BlueGreenDeploymentIdentifier
    SwitchoverTimeout: SwitchoverTimeout | None

class SwitchoverBlueGreenDeploymentResponse(TypedDict, total=False):
    BlueGreenDeployment: BlueGreenDeployment | None

class SwitchoverGlobalClusterMessage(ServiceRequest):
    GlobalClusterIdentifier: GlobalClusterIdentifier
    TargetDbClusterIdentifier: DBClusterIdentifier

class SwitchoverGlobalClusterResult(TypedDict, total=False):
    GlobalCluster: GlobalCluster | None

class SwitchoverReadReplicaMessage(ServiceRequest):
    DBInstanceIdentifier: String

class SwitchoverReadReplicaResult(TypedDict, total=False):
    DBInstance: DBInstance | None

class TagListMessage(TypedDict, total=False):
    TagList: TagList | None

TenantDatabasesList = list[TenantDatabase]
class TenantDatabasesMessage(TypedDict, total=False):
    Marker: String | None
    TenantDatabases: TenantDatabasesList | None

class RdsApi:

    service: str = "rds"
    version: str = "2014-10-31"

    @handler("AddRoleToDBCluster")
    def add_role_to_db_cluster(self, context: RequestContext, db_cluster_identifier: String, role_arn: String, feature_name: String | None = None, **kwargs) -> None:
        raise NotImplementedError

    @handler("AddRoleToDBInstance")
    def add_role_to_db_instance(self, context: RequestContext, db_instance_identifier: String, role_arn: String, feature_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("AddSourceIdentifierToSubscription")
    def add_source_identifier_to_subscription(self, context: RequestContext, subscription_name: String, source_identifier: String, **kwargs) -> AddSourceIdentifierToSubscriptionResult:
        raise NotImplementedError

    @handler("AddTagsToResource")
    def add_tags_to_resource(self, context: RequestContext, resource_name: String, tags: TagList, **kwargs) -> None:
        raise NotImplementedError

    @handler("ApplyPendingMaintenanceAction")
    def apply_pending_maintenance_action(self, context: RequestContext, resource_identifier: String, apply_action: String, opt_in_type: String, **kwargs) -> ApplyPendingMaintenanceActionResult:
        raise NotImplementedError

    @handler("AuthorizeDBSecurityGroupIngress")
    def authorize_db_security_group_ingress(self, context: RequestContext, db_security_group_name: String, cidrip: String | None = None, ec2_security_group_name: String | None = None, ec2_security_group_id: String | None = None, ec2_security_group_owner_id: String | None = None, **kwargs) -> AuthorizeDBSecurityGroupIngressResult:
        raise NotImplementedError

    @handler("BacktrackDBCluster")
    def backtrack_db_cluster(self, context: RequestContext, db_cluster_identifier: String, backtrack_to: TStamp, force: BooleanOptional | None = None, use_earliest_time_on_point_in_time_unavailable: BooleanOptional | None = None, **kwargs) -> DBClusterBacktrack:
        raise NotImplementedError

    @handler("CancelExportTask")
    def cancel_export_task(self, context: RequestContext, export_task_identifier: String, **kwargs) -> ExportTask:
        raise NotImplementedError

    @handler("CopyDBClusterParameterGroup")
    def copy_db_cluster_parameter_group(self, context: RequestContext, source_db_cluster_parameter_group_identifier: String, target_db_cluster_parameter_group_identifier: String, target_db_cluster_parameter_group_description: String, tags: TagList | None = None, **kwargs) -> CopyDBClusterParameterGroupResult:
        raise NotImplementedError

    @handler("CopyDBClusterSnapshot")
    def copy_db_cluster_snapshot(self, context: RequestContext, source_db_cluster_snapshot_identifier: String, target_db_cluster_snapshot_identifier: String, kms_key_id: String | None = None, pre_signed_url: SensitiveString | None = None, copy_tags: BooleanOptional | None = None, tags: TagList | None = None, source_region: String | None = None, **kwargs) -> CopyDBClusterSnapshotResult:
        raise NotImplementedError

    @handler("CopyDBParameterGroup")
    def copy_db_parameter_group(self, context: RequestContext, source_db_parameter_group_identifier: String, target_db_parameter_group_identifier: String, target_db_parameter_group_description: String, tags: TagList | None = None, **kwargs) -> CopyDBParameterGroupResult:
        raise NotImplementedError

    @handler("CopyDBSnapshot")
    def copy_db_snapshot(self, context: RequestContext, source_db_snapshot_identifier: String, target_db_snapshot_identifier: String, kms_key_id: String | None = None, tags: TagList | None = None, copy_tags: BooleanOptional | None = None, pre_signed_url: SensitiveString | None = None, option_group_name: String | None = None, target_custom_availability_zone: String | None = None, snapshot_target: String | None = None, copy_option_group: BooleanOptional | None = None, snapshot_availability_zone: String | None = None, source_region: String | None = None, **kwargs) -> CopyDBSnapshotResult:
        raise NotImplementedError

    @handler("CopyOptionGroup")
    def copy_option_group(self, context: RequestContext, source_option_group_identifier: String, target_option_group_identifier: String, target_option_group_description: String, tags: TagList | None = None, **kwargs) -> CopyOptionGroupResult:
        raise NotImplementedError

    @handler("CreateBlueGreenDeployment")
    def create_blue_green_deployment(self, context: RequestContext, blue_green_deployment_name: BlueGreenDeploymentName, source: DatabaseArn, target_engine_version: TargetEngineVersion | None = None, target_db_parameter_group_name: TargetDBParameterGroupName | None = None, target_db_cluster_parameter_group_name: TargetDBClusterParameterGroupName | None = None, tags: TagList | None = None, target_db_instance_class: TargetDBInstanceClass | None = None, upgrade_target_storage_config: BooleanOptional | None = None, target_iops: IntegerOptional | None = None, target_storage_type: TargetStorageType | None = None, target_allocated_storage: IntegerOptional | None = None, target_storage_throughput: IntegerOptional | None = None, **kwargs) -> CreateBlueGreenDeploymentResponse:
        raise NotImplementedError

    @handler("CreateCustomDBEngineVersion")
    def create_custom_db_engine_version(self, context: RequestContext, engine: CustomEngineName, engine_version: CustomEngineVersion, database_installation_files_s3_bucket_name: BucketName | None = None, database_installation_files_s3_prefix: String255 | None = None, database_installation_files: StringList | None = None, image_id: String255 | None = None, kms_key_id: KmsKeyIdOrArn | None = None, source_custom_db_engine_version_identifier: String255 | None = None, use_aws_provided_latest_image: BooleanOptional | None = None, description: Description | None = None, manifest: CustomDBEngineVersionManifest | None = None, tags: TagList | None = None, **kwargs) -> DBEngineVersion:
        raise NotImplementedError

    @handler("CreateDBCluster")
    def create_db_cluster(self, context: RequestContext, db_cluster_identifier: String, engine: String, availability_zones: AvailabilityZones | None = None, backup_retention_period: IntegerOptional | None = None, character_set_name: String | None = None, database_name: String | None = None, db_cluster_parameter_group_name: String | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, db_subnet_group_name: String | None = None, engine_version: String | None = None, port: IntegerOptional | None = None, master_username: String | None = None, master_user_password: SensitiveString | None = None, option_group_name: String | None = None, preferred_backup_window: String | None = None, preferred_maintenance_window: String | None = None, replication_source_identifier: String | None = None, tags: TagList | None = None, storage_encrypted: BooleanOptional | None = None, kms_key_id: String | None = None, pre_signed_url: SensitiveString | None = None, enable_iam_database_authentication: BooleanOptional | None = None, backtrack_window: LongOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, engine_mode: String | None = None, scaling_configuration: ScalingConfiguration | None = None, rds_custom_cluster_configuration: RdsCustomClusterConfiguration | None = None, db_cluster_instance_class: String | None = None, allocated_storage: IntegerOptional | None = None, storage_type: String | None = None, iops: IntegerOptional | None = None, publicly_accessible: BooleanOptional | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, deletion_protection: BooleanOptional | None = None, global_cluster_identifier: GlobalClusterIdentifier | None = None, enable_http_endpoint: BooleanOptional | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, enable_global_write_forwarding: BooleanOptional | None = None, network_type: String | None = None, serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, database_insights_mode: DatabaseInsightsMode | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, enable_limitless_database: BooleanOptional | None = None, cluster_scalability_type: ClusterScalabilityType | None = None, db_system_id: String | None = None, manage_master_user_password: BooleanOptional | None = None, enable_local_write_forwarding: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, ca_certificate_identifier: String | None = None, engine_lifecycle_support: String | None = None, tag_specifications: TagSpecificationList | None = None, master_user_authentication_type: MasterUserAuthenticationType | None = None, source_region: String | None = None, **kwargs) -> CreateDBClusterResult:
        raise NotImplementedError

    @handler("CreateDBClusterEndpoint")
    def create_db_cluster_endpoint(self, context: RequestContext, db_cluster_identifier: String, db_cluster_endpoint_identifier: String, endpoint_type: String, static_members: StringList | None = None, excluded_members: StringList | None = None, tags: TagList | None = None, **kwargs) -> DBClusterEndpoint:
        raise NotImplementedError

    @handler("CreateDBClusterParameterGroup")
    def create_db_cluster_parameter_group(self, context: RequestContext, db_cluster_parameter_group_name: String, db_parameter_group_family: String, description: String, tags: TagList | None = None, **kwargs) -> CreateDBClusterParameterGroupResult:
        raise NotImplementedError

    @handler("CreateDBClusterSnapshot")
    def create_db_cluster_snapshot(self, context: RequestContext, db_cluster_snapshot_identifier: String, db_cluster_identifier: String, tags: TagList | None = None, **kwargs) -> CreateDBClusterSnapshotResult:
        raise NotImplementedError

    @handler("CreateDBInstance")
    def create_db_instance(self, context: RequestContext, db_instance_identifier: String, db_instance_class: String, engine: String, db_name: String | None = None, allocated_storage: IntegerOptional | None = None, master_username: String | None = None, master_user_password: SensitiveString | None = None, db_security_groups: DBSecurityGroupNameList | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, availability_zone: String | None = None, db_subnet_group_name: String | None = None, preferred_maintenance_window: String | None = None, db_parameter_group_name: String | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, port: IntegerOptional | None = None, multi_az: BooleanOptional | None = None, engine_version: String | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, license_model: String | None = None, iops: IntegerOptional | None = None, storage_throughput: IntegerOptional | None = None, option_group_name: String | None = None, character_set_name: String | None = None, nchar_character_set_name: String | None = None, publicly_accessible: BooleanOptional | None = None, tags: TagList | None = None, db_cluster_identifier: String | None = None, storage_type: String | None = None, tde_credential_arn: String | None = None, tde_credential_password: SensitiveString | None = None, storage_encrypted: BooleanOptional | None = None, kms_key_id: String | None = None, domain: String | None = None, domain_fqdn: String | None = None, domain_ou: String | None = None, domain_auth_secret_arn: String | None = None, domain_dns_ips: StringList | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, domain_iam_role_name: String | None = None, promotion_tier: IntegerOptional | None = None, timezone: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, database_insights_mode: DatabaseInsightsMode | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, processor_features: ProcessorFeatureList | None = None, deletion_protection: BooleanOptional | None = None, max_allocated_storage: IntegerOptional | None = None, enable_customer_owned_ip: BooleanOptional | None = None, network_type: String | None = None, backup_target: String | None = None, custom_iam_instance_profile: String | None = None, db_system_id: String | None = None, ca_certificate_identifier: String | None = None, manage_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, multi_tenant: BooleanOptional | None = None, dedicated_log_volume: BooleanOptional | None = None, engine_lifecycle_support: String | None = None, additional_storage_volumes: AdditionalStorageVolumesList | None = None, tag_specifications: TagSpecificationList | None = None, master_user_authentication_type: MasterUserAuthenticationType | None = None, **kwargs) -> CreateDBInstanceResult:
        raise NotImplementedError

    @handler("CreateDBInstanceReadReplica")
    def create_db_instance_read_replica(self, context: RequestContext, db_instance_identifier: String, source_db_instance_identifier: String | None = None, db_instance_class: String | None = None, availability_zone: String | None = None, port: IntegerOptional | None = None, multi_az: BooleanOptional | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, iops: IntegerOptional | None = None, storage_throughput: IntegerOptional | None = None, option_group_name: String | None = None, db_parameter_group_name: String | None = None, publicly_accessible: BooleanOptional | None = None, tags: TagList | None = None, db_subnet_group_name: String | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, storage_type: String | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, kms_key_id: String | None = None, pre_signed_url: SensitiveString | None = None, enable_iam_database_authentication: BooleanOptional | None = None, database_insights_mode: DatabaseInsightsMode | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, processor_features: ProcessorFeatureList | None = None, use_default_processor_features: BooleanOptional | None = None, deletion_protection: BooleanOptional | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, domain_fqdn: String | None = None, domain_ou: String | None = None, domain_auth_secret_arn: String | None = None, domain_dns_ips: StringList | None = None, replica_mode: ReplicaMode | None = None, enable_customer_owned_ip: BooleanOptional | None = None, network_type: String | None = None, max_allocated_storage: IntegerOptional | None = None, backup_target: String | None = None, custom_iam_instance_profile: String | None = None, allocated_storage: IntegerOptional | None = None, source_db_cluster_identifier: String | None = None, dedicated_log_volume: BooleanOptional | None = None, upgrade_storage_config: BooleanOptional | None = None, ca_certificate_identifier: String | None = None, additional_storage_volumes: AdditionalStorageVolumesList | None = None, tag_specifications: TagSpecificationList | None = None, source_region: String | None = None, **kwargs) -> CreateDBInstanceReadReplicaResult:
        raise NotImplementedError

    @handler("CreateDBParameterGroup")
    def create_db_parameter_group(self, context: RequestContext, db_parameter_group_name: String, db_parameter_group_family: String, description: String, tags: TagList | None = None, **kwargs) -> CreateDBParameterGroupResult:
        raise NotImplementedError

    @handler("CreateDBProxy")
    def create_db_proxy(self, context: RequestContext, db_proxy_name: DBProxyName, engine_family: EngineFamily, role_arn: Arn, vpc_subnet_ids: StringList, default_auth_scheme: DefaultAuthScheme | None = None, auth: UserAuthConfigList | None = None, vpc_security_group_ids: StringList | None = None, require_tls: Boolean | None = None, idle_client_timeout: IntegerOptional | None = None, debug_logging: Boolean | None = None, tags: TagList | None = None, endpoint_network_type: EndpointNetworkType | None = None, target_connection_network_type: TargetConnectionNetworkType | None = None, **kwargs) -> CreateDBProxyResponse:
        raise NotImplementedError

    @handler("CreateDBProxyEndpoint")
    def create_db_proxy_endpoint(self, context: RequestContext, db_proxy_name: DBProxyName, db_proxy_endpoint_name: DBProxyEndpointName, vpc_subnet_ids: StringList, vpc_security_group_ids: StringList | None = None, target_role: DBProxyEndpointTargetRole | None = None, tags: TagList | None = None, endpoint_network_type: EndpointNetworkType | None = None, **kwargs) -> CreateDBProxyEndpointResponse:
        raise NotImplementedError

    @handler("CreateDBSecurityGroup")
    def create_db_security_group(self, context: RequestContext, db_security_group_name: String, db_security_group_description: String, tags: TagList | None = None, **kwargs) -> CreateDBSecurityGroupResult:
        raise NotImplementedError

    @handler("CreateDBShardGroup")
    def create_db_shard_group(self, context: RequestContext, db_shard_group_identifier: String, db_cluster_identifier: String, max_acu: DoubleOptional, compute_redundancy: IntegerOptional | None = None, min_acu: DoubleOptional | None = None, publicly_accessible: BooleanOptional | None = None, tags: TagList | None = None, **kwargs) -> DBShardGroup:
        raise NotImplementedError

    @handler("CreateDBSnapshot")
    def create_db_snapshot(self, context: RequestContext, db_snapshot_identifier: String, db_instance_identifier: String, tags: TagList | None = None, **kwargs) -> CreateDBSnapshotResult:
        raise NotImplementedError

    @handler("CreateDBSubnetGroup")
    def create_db_subnet_group(self, context: RequestContext, db_subnet_group_name: String, db_subnet_group_description: String, subnet_ids: SubnetIdentifierList, tags: TagList | None = None, **kwargs) -> CreateDBSubnetGroupResult:
        raise NotImplementedError

    @handler("CreateEventSubscription")
    def create_event_subscription(self, context: RequestContext, subscription_name: String, sns_topic_arn: String, source_type: String | None = None, event_categories: EventCategoriesList | None = None, source_ids: SourceIdsList | None = None, enabled: BooleanOptional | None = None, tags: TagList | None = None, **kwargs) -> CreateEventSubscriptionResult:
        raise NotImplementedError

    @handler("CreateGlobalCluster")
    def create_global_cluster(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier, source_db_cluster_identifier: String | None = None, engine: String | None = None, engine_version: String | None = None, engine_lifecycle_support: String | None = None, deletion_protection: BooleanOptional | None = None, database_name: String | None = None, storage_encrypted: BooleanOptional | None = None, tags: TagList | None = None, **kwargs) -> CreateGlobalClusterResult:
        raise NotImplementedError

    @handler("CreateIntegration")
    def create_integration(self, context: RequestContext, source_arn: SourceArn, target_arn: Arn, integration_name: IntegrationName, kms_key_id: String | None = None, additional_encryption_context: EncryptionContextMap | None = None, tags: TagList | None = None, data_filter: DataFilter | None = None, description: IntegrationDescription | None = None, **kwargs) -> Integration:
        raise NotImplementedError

    @handler("CreateOptionGroup")
    def create_option_group(self, context: RequestContext, option_group_name: String, engine_name: String, major_engine_version: String, option_group_description: String, tags: TagList | None = None, **kwargs) -> CreateOptionGroupResult:
        raise NotImplementedError

    @handler("CreateTenantDatabase")
    def create_tenant_database(self, context: RequestContext, db_instance_identifier: String, tenant_db_name: String, master_username: String, master_user_password: SensitiveString | None = None, character_set_name: String | None = None, nchar_character_set_name: String | None = None, manage_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, tags: TagList | None = None, **kwargs) -> CreateTenantDatabaseResult:
        raise NotImplementedError

    @handler("DeleteBlueGreenDeployment")
    def delete_blue_green_deployment(self, context: RequestContext, blue_green_deployment_identifier: BlueGreenDeploymentIdentifier, delete_target: BooleanOptional | None = None, **kwargs) -> DeleteBlueGreenDeploymentResponse:
        raise NotImplementedError

    @handler("DeleteCustomDBEngineVersion")
    def delete_custom_db_engine_version(self, context: RequestContext, engine: CustomEngineName, engine_version: CustomEngineVersion, **kwargs) -> DBEngineVersion:
        raise NotImplementedError

    @handler("DeleteDBCluster")
    def delete_db_cluster(self, context: RequestContext, db_cluster_identifier: String, skip_final_snapshot: Boolean | None = None, final_db_snapshot_identifier: String | None = None, delete_automated_backups: BooleanOptional | None = None, **kwargs) -> DeleteDBClusterResult:
        raise NotImplementedError

    @handler("DeleteDBClusterAutomatedBackup")
    def delete_db_cluster_automated_backup(self, context: RequestContext, db_cluster_resource_id: String, **kwargs) -> DeleteDBClusterAutomatedBackupResult:
        raise NotImplementedError

    @handler("DeleteDBClusterEndpoint")
    def delete_db_cluster_endpoint(self, context: RequestContext, db_cluster_endpoint_identifier: String, **kwargs) -> DBClusterEndpoint:
        raise NotImplementedError

    @handler("DeleteDBClusterParameterGroup")
    def delete_db_cluster_parameter_group(self, context: RequestContext, db_cluster_parameter_group_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("DeleteDBClusterSnapshot")
    def delete_db_cluster_snapshot(self, context: RequestContext, db_cluster_snapshot_identifier: String, **kwargs) -> DeleteDBClusterSnapshotResult:
        raise NotImplementedError

    @handler("DeleteDBInstance")
    def delete_db_instance(self, context: RequestContext, db_instance_identifier: String, skip_final_snapshot: Boolean | None = None, final_db_snapshot_identifier: String | None = None, delete_automated_backups: BooleanOptional | None = None, **kwargs) -> DeleteDBInstanceResult:
        raise NotImplementedError

    @handler("DeleteDBInstanceAutomatedBackup")
    def delete_db_instance_automated_backup(self, context: RequestContext, dbi_resource_id: String | None = None, db_instance_automated_backups_arn: String | None = None, **kwargs) -> DeleteDBInstanceAutomatedBackupResult:
        raise NotImplementedError

    @handler("DeleteDBParameterGroup")
    def delete_db_parameter_group(self, context: RequestContext, db_parameter_group_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("DeleteDBProxy")
    def delete_db_proxy(self, context: RequestContext, db_proxy_name: DBProxyName, **kwargs) -> DeleteDBProxyResponse:
        raise NotImplementedError

    @handler("DeleteDBProxyEndpoint")
    def delete_db_proxy_endpoint(self, context: RequestContext, db_proxy_endpoint_name: DBProxyEndpointName, **kwargs) -> DeleteDBProxyEndpointResponse:
        raise NotImplementedError

    @handler("DeleteDBSecurityGroup")
    def delete_db_security_group(self, context: RequestContext, db_security_group_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("DeleteDBShardGroup")
    def delete_db_shard_group(self, context: RequestContext, db_shard_group_identifier: DBShardGroupIdentifier, **kwargs) -> DBShardGroup:
        raise NotImplementedError

    @handler("DeleteDBSnapshot")
    def delete_db_snapshot(self, context: RequestContext, db_snapshot_identifier: String, **kwargs) -> DeleteDBSnapshotResult:
        raise NotImplementedError

    @handler("DeleteDBSubnetGroup")
    def delete_db_subnet_group(self, context: RequestContext, db_subnet_group_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("DeleteEventSubscription")
    def delete_event_subscription(self, context: RequestContext, subscription_name: String, **kwargs) -> DeleteEventSubscriptionResult:
        raise NotImplementedError

    @handler("DeleteGlobalCluster")
    def delete_global_cluster(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier, **kwargs) -> DeleteGlobalClusterResult:
        raise NotImplementedError

    @handler("DeleteIntegration")
    def delete_integration(self, context: RequestContext, integration_identifier: IntegrationIdentifier, **kwargs) -> Integration:
        raise NotImplementedError

    @handler("DeleteOptionGroup")
    def delete_option_group(self, context: RequestContext, option_group_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("DeleteTenantDatabase")
    def delete_tenant_database(self, context: RequestContext, db_instance_identifier: String, tenant_db_name: String, skip_final_snapshot: Boolean | None = None, final_db_snapshot_identifier: String | None = None, **kwargs) -> DeleteTenantDatabaseResult:
        raise NotImplementedError

    @handler("DeregisterDBProxyTargets")
    def deregister_db_proxy_targets(self, context: RequestContext, db_proxy_name: DBProxyName, target_group_name: DBProxyTargetGroupName | None = None, db_instance_identifiers: StringList | None = None, db_cluster_identifiers: StringList | None = None, **kwargs) -> DeregisterDBProxyTargetsResponse:
        raise NotImplementedError

    @handler("DescribeAccountAttributes")
    def describe_account_attributes(self, context: RequestContext, **kwargs) -> AccountAttributesMessage:
        raise NotImplementedError

    @handler("DescribeBlueGreenDeployments")
    def describe_blue_green_deployments(self, context: RequestContext, blue_green_deployment_identifier: BlueGreenDeploymentIdentifier | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeBlueGreenDeploymentsResponse:
        raise NotImplementedError

    @handler("DescribeCertificates")
    def describe_certificates(self, context: RequestContext, certificate_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> CertificateMessage:
        raise NotImplementedError

    @handler("DescribeDBClusterAutomatedBackups")
    def describe_db_cluster_automated_backups(self, context: RequestContext, db_cluster_resource_id: String | None = None, db_cluster_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBClusterAutomatedBackupMessage:
        raise NotImplementedError

    @handler("DescribeDBClusterBacktracks")
    def describe_db_cluster_backtracks(self, context: RequestContext, db_cluster_identifier: String, backtrack_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBClusterBacktrackMessage:
        raise NotImplementedError

    @handler("DescribeDBClusterEndpoints")
    def describe_db_cluster_endpoints(self, context: RequestContext, db_cluster_identifier: String | None = None, db_cluster_endpoint_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBClusterEndpointMessage:
        raise NotImplementedError

    @handler("DescribeDBClusterParameterGroups")
    def describe_db_cluster_parameter_groups(self, context: RequestContext, db_cluster_parameter_group_name: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBClusterParameterGroupsMessage:
        raise NotImplementedError

    @handler("DescribeDBClusterParameters")
    def describe_db_cluster_parameters(self, context: RequestContext, db_cluster_parameter_group_name: String, source: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBClusterParameterGroupDetails:
        raise NotImplementedError

    @handler("DescribeDBClusterSnapshotAttributes")
    def describe_db_cluster_snapshot_attributes(self, context: RequestContext, db_cluster_snapshot_identifier: String, **kwargs) -> DescribeDBClusterSnapshotAttributesResult:
        raise NotImplementedError

    @handler("DescribeDBClusterSnapshots")
    def describe_db_cluster_snapshots(self, context: RequestContext, db_cluster_identifier: String | None = None, db_cluster_snapshot_identifier: String | None = None, snapshot_type: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, include_shared: Boolean | None = None, include_public: Boolean | None = None, db_cluster_resource_id: String | None = None, **kwargs) -> DBClusterSnapshotMessage:
        raise NotImplementedError

    @handler("DescribeDBClusters")
    def describe_db_clusters(self, context: RequestContext, db_cluster_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, include_shared: Boolean | None = None, **kwargs) -> DBClusterMessage:
        raise NotImplementedError

    @handler("DescribeDBEngineVersions")
    def describe_db_engine_versions(self, context: RequestContext, engine: String | None = None, engine_version: String | None = None, db_parameter_group_family: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, default_only: Boolean | None = None, list_supported_character_sets: BooleanOptional | None = None, list_supported_timezones: BooleanOptional | None = None, include_all: BooleanOptional | None = None, **kwargs) -> DBEngineVersionMessage:
        raise NotImplementedError

    @handler("DescribeDBInstanceAutomatedBackups")
    def describe_db_instance_automated_backups(self, context: RequestContext, dbi_resource_id: String | None = None, db_instance_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, db_instance_automated_backups_arn: String | None = None, **kwargs) -> DBInstanceAutomatedBackupMessage:
        raise NotImplementedError

    @handler("DescribeDBInstances")
    def describe_db_instances(self, context: RequestContext, db_instance_identifier: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBInstanceMessage:
        raise NotImplementedError

    @handler("DescribeDBLogFiles")
    def describe_db_log_files(self, context: RequestContext, db_instance_identifier: String, filename_contains: String | None = None, file_last_written: Long | None = None, file_size: Long | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DescribeDBLogFilesResponse:
        raise NotImplementedError

    @handler("DescribeDBMajorEngineVersions")
    def describe_db_major_engine_versions(self, context: RequestContext, engine: Engine | None = None, major_engine_version: MajorEngineVersion | None = None, marker: Marker | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeDBMajorEngineVersionsResponse:
        raise NotImplementedError

    @handler("DescribeDBParameterGroups")
    def describe_db_parameter_groups(self, context: RequestContext, db_parameter_group_name: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBParameterGroupsMessage:
        raise NotImplementedError

    @handler("DescribeDBParameters")
    def describe_db_parameters(self, context: RequestContext, db_parameter_group_name: String, source: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBParameterGroupDetails:
        raise NotImplementedError

    @handler("DescribeDBProxies")
    def describe_db_proxies(self, context: RequestContext, db_proxy_name: DBProxyName | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeDBProxiesResponse:
        raise NotImplementedError

    @handler("DescribeDBProxyEndpoints")
    def describe_db_proxy_endpoints(self, context: RequestContext, db_proxy_name: DBProxyName | None = None, db_proxy_endpoint_name: DBProxyEndpointName | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeDBProxyEndpointsResponse:
        raise NotImplementedError

    @handler("DescribeDBProxyTargetGroups")
    def describe_db_proxy_target_groups(self, context: RequestContext, db_proxy_name: DBProxyName, target_group_name: DBProxyTargetGroupName | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeDBProxyTargetGroupsResponse:
        raise NotImplementedError

    @handler("DescribeDBProxyTargets")
    def describe_db_proxy_targets(self, context: RequestContext, db_proxy_name: DBProxyName, target_group_name: DBProxyTargetGroupName | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeDBProxyTargetsResponse:
        raise NotImplementedError

    @handler("DescribeDBRecommendations")
    def describe_db_recommendations(self, context: RequestContext, last_updated_after: TStamp | None = None, last_updated_before: TStamp | None = None, locale: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBRecommendationsMessage:
        raise NotImplementedError

    @handler("DescribeDBSecurityGroups")
    def describe_db_security_groups(self, context: RequestContext, db_security_group_name: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBSecurityGroupMessage:
        raise NotImplementedError

    @handler("DescribeDBShardGroups")
    def describe_db_shard_groups(self, context: RequestContext, db_shard_group_identifier: DBShardGroupIdentifier | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, **kwargs) -> DescribeDBShardGroupsResponse:
        raise NotImplementedError

    @handler("DescribeDBSnapshotAttributes")
    def describe_db_snapshot_attributes(self, context: RequestContext, db_snapshot_identifier: String, **kwargs) -> DescribeDBSnapshotAttributesResult:
        raise NotImplementedError

    @handler("DescribeDBSnapshotTenantDatabases")
    def describe_db_snapshot_tenant_databases(self, context: RequestContext, db_instance_identifier: String | None = None, db_snapshot_identifier: String | None = None, snapshot_type: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, dbi_resource_id: String | None = None, **kwargs) -> DBSnapshotTenantDatabasesMessage:
        raise NotImplementedError

    @handler("DescribeDBSnapshots")
    def describe_db_snapshots(self, context: RequestContext, db_instance_identifier: String | None = None, db_snapshot_identifier: String | None = None, snapshot_type: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, include_shared: Boolean | None = None, include_public: Boolean | None = None, dbi_resource_id: String | None = None, **kwargs) -> DBSnapshotMessage:
        raise NotImplementedError

    @handler("DescribeDBSubnetGroups")
    def describe_db_subnet_groups(self, context: RequestContext, db_subnet_group_name: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DBSubnetGroupMessage:
        raise NotImplementedError

    @handler("DescribeEngineDefaultClusterParameters")
    def describe_engine_default_cluster_parameters(self, context: RequestContext, db_parameter_group_family: String, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DescribeEngineDefaultClusterParametersResult:
        raise NotImplementedError

    @handler("DescribeEngineDefaultParameters")
    def describe_engine_default_parameters(self, context: RequestContext, db_parameter_group_family: String, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> DescribeEngineDefaultParametersResult:
        raise NotImplementedError

    @handler("DescribeEventCategories")
    def describe_event_categories(self, context: RequestContext, source_type: String | None = None, filters: FilterList | None = None, **kwargs) -> EventCategoriesMessage:
        raise NotImplementedError

    @handler("DescribeEventSubscriptions")
    def describe_event_subscriptions(self, context: RequestContext, subscription_name: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> EventSubscriptionsMessage:
        raise NotImplementedError

    @handler("DescribeEvents")
    def describe_events(self, context: RequestContext, source_identifier: String | None = None, source_type: SourceType | None = None, start_time: TStamp | None = None, end_time: TStamp | None = None, duration: IntegerOptional | None = None, event_categories: EventCategoriesList | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> EventsMessage:
        raise NotImplementedError

    @handler("DescribeExportTasks")
    def describe_export_tasks(self, context: RequestContext, export_task_identifier: String | None = None, source_arn: String | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: MaxRecords | None = None, source_type: ExportSourceType | None = None, **kwargs) -> ExportTasksMessage:
        raise NotImplementedError

    @handler("DescribeGlobalClusters")
    def describe_global_clusters(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> GlobalClustersMessage:
        raise NotImplementedError

    @handler("DescribeIntegrations")
    def describe_integrations(self, context: RequestContext, integration_identifier: IntegrationIdentifier | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: Marker | None = None, **kwargs) -> DescribeIntegrationsResponse:
        raise NotImplementedError

    @handler("DescribeOptionGroupOptions")
    def describe_option_group_options(self, context: RequestContext, engine_name: String, major_engine_version: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> OptionGroupOptionsMessage:
        raise NotImplementedError

    @handler("DescribeOptionGroups")
    def describe_option_groups(self, context: RequestContext, option_group_name: String | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: IntegerOptional | None = None, engine_name: String | None = None, major_engine_version: String | None = None, **kwargs) -> OptionGroups:
        raise NotImplementedError

    @handler("DescribeOrderableDBInstanceOptions")
    def describe_orderable_db_instance_options(self, context: RequestContext, engine: String, engine_version: String | None = None, db_instance_class: String | None = None, license_model: String | None = None, availability_zone_group: String | None = None, vpc: BooleanOptional | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> OrderableDBInstanceOptionsMessage:
        raise NotImplementedError

    @handler("DescribePendingMaintenanceActions")
    def describe_pending_maintenance_actions(self, context: RequestContext, resource_identifier: String | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: IntegerOptional | None = None, **kwargs) -> PendingMaintenanceActionsMessage:
        raise NotImplementedError

    @handler("DescribeReservedDBInstances")
    def describe_reserved_db_instances(self, context: RequestContext, reserved_db_instance_id: String | None = None, reserved_db_instances_offering_id: String | None = None, db_instance_class: String | None = None, duration: String | None = None, product_description: String | None = None, offering_type: String | None = None, multi_az: BooleanOptional | None = None, lease_id: String | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> ReservedDBInstanceMessage:
        raise NotImplementedError

    @handler("DescribeReservedDBInstancesOfferings")
    def describe_reserved_db_instances_offerings(self, context: RequestContext, reserved_db_instances_offering_id: String | None = None, db_instance_class: String | None = None, duration: String | None = None, product_description: String | None = None, offering_type: String | None = None, multi_az: BooleanOptional | None = None, filters: FilterList | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, **kwargs) -> ReservedDBInstancesOfferingMessage:
        raise NotImplementedError

    @handler("DescribeSourceRegions")
    def describe_source_regions(self, context: RequestContext, region_name: String | None = None, max_records: IntegerOptional | None = None, marker: String | None = None, filters: FilterList | None = None, **kwargs) -> SourceRegionMessage:
        raise NotImplementedError

    @handler("DescribeTenantDatabases")
    def describe_tenant_databases(self, context: RequestContext, db_instance_identifier: String | None = None, tenant_db_name: String | None = None, filters: FilterList | None = None, marker: String | None = None, max_records: IntegerOptional | None = None, **kwargs) -> TenantDatabasesMessage:
        raise NotImplementedError

    @handler("DescribeValidDBInstanceModifications")
    def describe_valid_db_instance_modifications(self, context: RequestContext, db_instance_identifier: String, **kwargs) -> DescribeValidDBInstanceModificationsResult:
        raise NotImplementedError

    @handler("DisableHttpEndpoint")
    def disable_http_endpoint(self, context: RequestContext, resource_arn: String, **kwargs) -> DisableHttpEndpointResponse:
        raise NotImplementedError

    @handler("DownloadDBLogFilePortion")
    def download_db_log_file_portion(self, context: RequestContext, db_instance_identifier: String, log_file_name: String, marker: String | None = None, number_of_lines: Integer | None = None, **kwargs) -> DownloadDBLogFilePortionDetails:
        raise NotImplementedError

    @handler("EnableHttpEndpoint")
    def enable_http_endpoint(self, context: RequestContext, resource_arn: String, **kwargs) -> EnableHttpEndpointResponse:
        raise NotImplementedError

    @handler("FailoverDBCluster")
    def failover_db_cluster(self, context: RequestContext, db_cluster_identifier: String, target_db_instance_identifier: String | None = None, **kwargs) -> FailoverDBClusterResult:
        raise NotImplementedError

    @handler("FailoverGlobalCluster")
    def failover_global_cluster(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier, target_db_cluster_identifier: DBClusterIdentifier, allow_data_loss: BooleanOptional | None = None, switchover: BooleanOptional | None = None, **kwargs) -> FailoverGlobalClusterResult:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(self, context: RequestContext, resource_name: String, filters: FilterList | None = None, **kwargs) -> TagListMessage:
        raise NotImplementedError

    @handler("ModifyActivityStream")
    def modify_activity_stream(self, context: RequestContext, resource_arn: String | None = None, audit_policy_state: AuditPolicyState | None = None, **kwargs) -> ModifyActivityStreamResponse:
        raise NotImplementedError

    @handler("ModifyCertificates")
    def modify_certificates(self, context: RequestContext, certificate_identifier: String | None = None, remove_customer_override: BooleanOptional | None = None, **kwargs) -> ModifyCertificatesResult:
        raise NotImplementedError

    @handler("ModifyCurrentDBClusterCapacity")
    def modify_current_db_cluster_capacity(self, context: RequestContext, db_cluster_identifier: String, capacity: IntegerOptional | None = None, seconds_before_timeout: IntegerOptional | None = None, timeout_action: String | None = None, **kwargs) -> DBClusterCapacityInfo:
        raise NotImplementedError

    @handler("ModifyCustomDBEngineVersion")
    def modify_custom_db_engine_version(self, context: RequestContext, engine: CustomEngineName, engine_version: CustomEngineVersion, description: Description | None = None, status: CustomEngineVersionStatus | None = None, **kwargs) -> DBEngineVersion:
        raise NotImplementedError

    @handler("ModifyDBCluster")
    def modify_db_cluster(self, context: RequestContext, db_cluster_identifier: String, new_db_cluster_identifier: String | None = None, apply_immediately: Boolean | None = None, backup_retention_period: IntegerOptional | None = None, db_cluster_parameter_group_name: String | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, port: IntegerOptional | None = None, master_user_password: SensitiveString | None = None, option_group_name: String | None = None, preferred_backup_window: String | None = None, preferred_maintenance_window: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, backtrack_window: LongOptional | None = None, cloudwatch_logs_export_configuration: CloudwatchLogsExportConfiguration | None = None, engine_version: String | None = None, allow_major_version_upgrade: Boolean | None = None, db_instance_parameter_group_name: String | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, scaling_configuration: ScalingConfiguration | None = None, deletion_protection: BooleanOptional | None = None, enable_http_endpoint: BooleanOptional | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, enable_global_write_forwarding: BooleanOptional | None = None, db_cluster_instance_class: String | None = None, allocated_storage: IntegerOptional | None = None, storage_type: String | None = None, iops: IntegerOptional | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, network_type: String | None = None, serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, database_insights_mode: DatabaseInsightsMode | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, manage_master_user_password: BooleanOptional | None = None, rotate_master_user_password: BooleanOptional | None = None, enable_local_write_forwarding: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, engine_mode: String | None = None, allow_engine_mode_change: Boolean | None = None, aws_backup_recovery_point_arn: AwsBackupRecoveryPointArn | None = None, enable_limitless_database: BooleanOptional | None = None, ca_certificate_identifier: String | None = None, master_user_authentication_type: MasterUserAuthenticationType | None = None, **kwargs) -> ModifyDBClusterResult:
        raise NotImplementedError

    @handler("ModifyDBClusterEndpoint")
    def modify_db_cluster_endpoint(self, context: RequestContext, db_cluster_endpoint_identifier: String, endpoint_type: String | None = None, static_members: StringList | None = None, excluded_members: StringList | None = None, **kwargs) -> DBClusterEndpoint:
        raise NotImplementedError

    @handler("ModifyDBClusterParameterGroup")
    def modify_db_cluster_parameter_group(self, context: RequestContext, db_cluster_parameter_group_name: String, parameters: ParametersList, **kwargs) -> DBClusterParameterGroupNameMessage:
        raise NotImplementedError

    @handler("ModifyDBClusterSnapshotAttribute")
    def modify_db_cluster_snapshot_attribute(self, context: RequestContext, db_cluster_snapshot_identifier: String, attribute_name: String, values_to_add: AttributeValueList | None = None, values_to_remove: AttributeValueList | None = None, **kwargs) -> ModifyDBClusterSnapshotAttributeResult:
        raise NotImplementedError

    @handler("ModifyDBInstance")
    def modify_db_instance(self, context: RequestContext, db_instance_identifier: String, allocated_storage: IntegerOptional | None = None, db_instance_class: String | None = None, db_subnet_group_name: String | None = None, db_security_groups: DBSecurityGroupNameList | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, apply_immediately: Boolean | None = None, master_user_password: SensitiveString | None = None, db_parameter_group_name: String | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, preferred_maintenance_window: String | None = None, multi_az: BooleanOptional | None = None, engine_version: String | None = None, allow_major_version_upgrade: Boolean | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, license_model: String | None = None, iops: IntegerOptional | None = None, storage_throughput: IntegerOptional | None = None, option_group_name: String | None = None, new_db_instance_identifier: String | None = None, storage_type: String | None = None, tde_credential_arn: String | None = None, tde_credential_password: SensitiveString | None = None, ca_certificate_identifier: String | None = None, domain: String | None = None, domain_fqdn: String | None = None, domain_ou: String | None = None, domain_auth_secret_arn: String | None = None, domain_dns_ips: StringList | None = None, disable_domain: BooleanOptional | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, monitoring_interval: IntegerOptional | None = None, db_port_number: IntegerOptional | None = None, publicly_accessible: BooleanOptional | None = None, monitoring_role_arn: String | None = None, domain_iam_role_name: String | None = None, promotion_tier: IntegerOptional | None = None, enable_iam_database_authentication: BooleanOptional | None = None, database_insights_mode: DatabaseInsightsMode | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, cloudwatch_logs_export_configuration: CloudwatchLogsExportConfiguration | None = None, processor_features: ProcessorFeatureList | None = None, use_default_processor_features: BooleanOptional | None = None, deletion_protection: BooleanOptional | None = None, max_allocated_storage: IntegerOptional | None = None, certificate_rotation_restart: BooleanOptional | None = None, replica_mode: ReplicaMode | None = None, automation_mode: AutomationMode | None = None, resume_full_automation_mode_minutes: IntegerOptional | None = None, enable_customer_owned_ip: BooleanOptional | None = None, network_type: String | None = None, aws_backup_recovery_point_arn: AwsBackupRecoveryPointArn | None = None, manage_master_user_password: BooleanOptional | None = None, rotate_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, multi_tenant: BooleanOptional | None = None, dedicated_log_volume: BooleanOptional | None = None, engine: String | None = None, additional_storage_volumes: ModifyAdditionalStorageVolumesList | None = None, tag_specifications: TagSpecificationList | None = None, master_user_authentication_type: MasterUserAuthenticationType | None = None, **kwargs) -> ModifyDBInstanceResult:
        raise NotImplementedError

    @handler("ModifyDBParameterGroup")
    def modify_db_parameter_group(self, context: RequestContext, db_parameter_group_name: String, parameters: ParametersList, **kwargs) -> DBParameterGroupNameMessage:
        raise NotImplementedError

    @handler("ModifyDBProxy")
    def modify_db_proxy(self, context: RequestContext, db_proxy_name: DBProxyName, new_db_proxy_name: DBProxyName | None = None, default_auth_scheme: DefaultAuthScheme | None = None, auth: UserAuthConfigList | None = None, require_tls: BooleanOptional | None = None, idle_client_timeout: IntegerOptional | None = None, debug_logging: BooleanOptional | None = None, role_arn: Arn | None = None, security_groups: StringList | None = None, **kwargs) -> ModifyDBProxyResponse:
        raise NotImplementedError

    @handler("ModifyDBProxyEndpoint")
    def modify_db_proxy_endpoint(self, context: RequestContext, db_proxy_endpoint_name: DBProxyEndpointName, new_db_proxy_endpoint_name: DBProxyEndpointName | None = None, vpc_security_group_ids: StringList | None = None, **kwargs) -> ModifyDBProxyEndpointResponse:
        raise NotImplementedError

    @handler("ModifyDBProxyTargetGroup")
    def modify_db_proxy_target_group(self, context: RequestContext, target_group_name: DBProxyTargetGroupName, db_proxy_name: DBProxyName, connection_pool_config: ConnectionPoolConfiguration | None = None, new_name: String | None = None, **kwargs) -> ModifyDBProxyTargetGroupResponse:
        raise NotImplementedError

    @handler("ModifyDBRecommendation")
    def modify_db_recommendation(self, context: RequestContext, recommendation_id: String, locale: String | None = None, status: String | None = None, recommended_action_updates: RecommendedActionUpdateList | None = None, **kwargs) -> DBRecommendationMessage:
        raise NotImplementedError

    @handler("ModifyDBShardGroup")
    def modify_db_shard_group(self, context: RequestContext, db_shard_group_identifier: DBShardGroupIdentifier, max_acu: DoubleOptional | None = None, min_acu: DoubleOptional | None = None, compute_redundancy: IntegerOptional | None = None, **kwargs) -> DBShardGroup:
        raise NotImplementedError

    @handler("ModifyDBSnapshot")
    def modify_db_snapshot(self, context: RequestContext, db_snapshot_identifier: String, engine_version: String | None = None, option_group_name: String | None = None, **kwargs) -> ModifyDBSnapshotResult:
        raise NotImplementedError

    @handler("ModifyDBSnapshotAttribute")
    def modify_db_snapshot_attribute(self, context: RequestContext, db_snapshot_identifier: String, attribute_name: String, values_to_add: AttributeValueList | None = None, values_to_remove: AttributeValueList | None = None, **kwargs) -> ModifyDBSnapshotAttributeResult:
        raise NotImplementedError

    @handler("ModifyDBSubnetGroup")
    def modify_db_subnet_group(self, context: RequestContext, db_subnet_group_name: String, subnet_ids: SubnetIdentifierList, db_subnet_group_description: String | None = None, **kwargs) -> ModifyDBSubnetGroupResult:
        raise NotImplementedError

    @handler("ModifyEventSubscription")
    def modify_event_subscription(self, context: RequestContext, subscription_name: String, sns_topic_arn: String | None = None, source_type: String | None = None, event_categories: EventCategoriesList | None = None, enabled: BooleanOptional | None = None, **kwargs) -> ModifyEventSubscriptionResult:
        raise NotImplementedError

    @handler("ModifyGlobalCluster")
    def modify_global_cluster(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier, new_global_cluster_identifier: GlobalClusterIdentifier | None = None, deletion_protection: BooleanOptional | None = None, engine_version: String | None = None, allow_major_version_upgrade: BooleanOptional | None = None, **kwargs) -> ModifyGlobalClusterResult:
        raise NotImplementedError

    @handler("ModifyIntegration")
    def modify_integration(self, context: RequestContext, integration_identifier: IntegrationIdentifier, integration_name: IntegrationName | None = None, data_filter: DataFilter | None = None, description: IntegrationDescription | None = None, **kwargs) -> Integration:
        raise NotImplementedError

    @handler("ModifyOptionGroup")
    def modify_option_group(self, context: RequestContext, option_group_name: String, options_to_include: OptionConfigurationList | None = None, options_to_remove: OptionNamesList | None = None, apply_immediately: Boolean | None = None, **kwargs) -> ModifyOptionGroupResult:
        raise NotImplementedError

    @handler("ModifyTenantDatabase")
    def modify_tenant_database(self, context: RequestContext, db_instance_identifier: String, tenant_db_name: String, master_user_password: SensitiveString | None = None, new_tenant_db_name: String | None = None, manage_master_user_password: BooleanOptional | None = None, rotate_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, **kwargs) -> ModifyTenantDatabaseResult:
        raise NotImplementedError

    @handler("PromoteReadReplica")
    def promote_read_replica(self, context: RequestContext, db_instance_identifier: String, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, tag_specifications: TagSpecificationList | None = None, **kwargs) -> PromoteReadReplicaResult:
        raise NotImplementedError

    @handler("PromoteReadReplicaDBCluster")
    def promote_read_replica_db_cluster(self, context: RequestContext, db_cluster_identifier: String, **kwargs) -> PromoteReadReplicaDBClusterResult:
        raise NotImplementedError

    @handler("PurchaseReservedDBInstancesOffering")
    def purchase_reserved_db_instances_offering(self, context: RequestContext, reserved_db_instances_offering_id: String, reserved_db_instance_id: String | None = None, db_instance_count: IntegerOptional | None = None, tags: TagList | None = None, **kwargs) -> PurchaseReservedDBInstancesOfferingResult:
        raise NotImplementedError

    @handler("RebootDBCluster")
    def reboot_db_cluster(self, context: RequestContext, db_cluster_identifier: String, **kwargs) -> RebootDBClusterResult:
        raise NotImplementedError

    @handler("RebootDBInstance")
    def reboot_db_instance(self, context: RequestContext, db_instance_identifier: String, force_failover: BooleanOptional | None = None, **kwargs) -> RebootDBInstanceResult:
        raise NotImplementedError

    @handler("RebootDBShardGroup")
    def reboot_db_shard_group(self, context: RequestContext, db_shard_group_identifier: DBShardGroupIdentifier, **kwargs) -> DBShardGroup:
        raise NotImplementedError

    @handler("RegisterDBProxyTargets")
    def register_db_proxy_targets(self, context: RequestContext, db_proxy_name: DBProxyName, target_group_name: DBProxyTargetGroupName | None = None, db_instance_identifiers: StringList | None = None, db_cluster_identifiers: StringList | None = None, **kwargs) -> RegisterDBProxyTargetsResponse:
        raise NotImplementedError

    @handler("RemoveFromGlobalCluster")
    def remove_from_global_cluster(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier, db_cluster_identifier: String, **kwargs) -> RemoveFromGlobalClusterResult:
        raise NotImplementedError

    @handler("RemoveRoleFromDBCluster")
    def remove_role_from_db_cluster(self, context: RequestContext, db_cluster_identifier: String, role_arn: String, feature_name: String | None = None, **kwargs) -> None:
        raise NotImplementedError

    @handler("RemoveRoleFromDBInstance")
    def remove_role_from_db_instance(self, context: RequestContext, db_instance_identifier: String, role_arn: String, feature_name: String, **kwargs) -> None:
        raise NotImplementedError

    @handler("RemoveSourceIdentifierFromSubscription")
    def remove_source_identifier_from_subscription(self, context: RequestContext, subscription_name: String, source_identifier: String, **kwargs) -> RemoveSourceIdentifierFromSubscriptionResult:
        raise NotImplementedError

    @handler("RemoveTagsFromResource")
    def remove_tags_from_resource(self, context: RequestContext, resource_name: String, tag_keys: KeyList, **kwargs) -> None:
        raise NotImplementedError

    @handler("ResetDBClusterParameterGroup")
    def reset_db_cluster_parameter_group(self, context: RequestContext, db_cluster_parameter_group_name: String, reset_all_parameters: Boolean | None = None, parameters: ParametersList | None = None, **kwargs) -> DBClusterParameterGroupNameMessage:
        raise NotImplementedError

    @handler("ResetDBParameterGroup")
    def reset_db_parameter_group(self, context: RequestContext, db_parameter_group_name: String, reset_all_parameters: Boolean | None = None, parameters: ParametersList | None = None, **kwargs) -> DBParameterGroupNameMessage:
        raise NotImplementedError

    @handler("RestoreDBClusterFromS3")
    def restore_db_cluster_from_s3(self, context: RequestContext, db_cluster_identifier: String, engine: String, master_username: String, source_engine: String, source_engine_version: String, s3_bucket_name: String, s3_ingestion_role_arn: String, availability_zones: AvailabilityZones | None = None, backup_retention_period: IntegerOptional | None = None, character_set_name: String | None = None, database_name: String | None = None, db_cluster_parameter_group_name: String | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, db_subnet_group_name: String | None = None, engine_version: String | None = None, port: IntegerOptional | None = None, master_user_password: SensitiveString | None = None, option_group_name: String | None = None, preferred_backup_window: String | None = None, preferred_maintenance_window: String | None = None, tags: TagList | None = None, storage_encrypted: BooleanOptional | None = None, kms_key_id: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, s3_prefix: String | None = None, backtrack_window: LongOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, deletion_protection: BooleanOptional | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, storage_type: String | None = None, network_type: String | None = None, serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None, manage_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, engine_lifecycle_support: String | None = None, tag_specifications: TagSpecificationList | None = None, **kwargs) -> RestoreDBClusterFromS3Result:
        raise NotImplementedError

    @handler("RestoreDBClusterFromSnapshot")
    def restore_db_cluster_from_snapshot(self, context: RequestContext, db_cluster_identifier: String, snapshot_identifier: String, engine: String, availability_zones: AvailabilityZones | None = None, engine_version: String | None = None, port: IntegerOptional | None = None, db_subnet_group_name: String | None = None, database_name: String | None = None, option_group_name: String | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, tags: TagList | None = None, kms_key_id: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, backtrack_window: LongOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, engine_mode: String | None = None, scaling_configuration: ScalingConfiguration | None = None, db_cluster_parameter_group_name: String | None = None, deletion_protection: BooleanOptional | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, db_cluster_instance_class: String | None = None, storage_type: String | None = None, iops: IntegerOptional | None = None, publicly_accessible: BooleanOptional | None = None, network_type: String | None = None, serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None, rds_custom_cluster_configuration: RdsCustomClusterConfiguration | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, engine_lifecycle_support: String | None = None, tag_specifications: TagSpecificationList | None = None, **kwargs) -> RestoreDBClusterFromSnapshotResult:
        raise NotImplementedError

    @handler("RestoreDBClusterToPointInTime")
    def restore_db_cluster_to_point_in_time(self, context: RequestContext, db_cluster_identifier: String, restore_type: String | None = None, source_db_cluster_identifier: String | None = None, restore_to_time: TStamp | None = None, use_latest_restorable_time: Boolean | None = None, port: IntegerOptional | None = None, db_subnet_group_name: String | None = None, option_group_name: String | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, tags: TagList | None = None, kms_key_id: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, backtrack_window: LongOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, db_cluster_parameter_group_name: String | None = None, deletion_protection: BooleanOptional | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, db_cluster_instance_class: String | None = None, storage_type: String | None = None, publicly_accessible: BooleanOptional | None = None, iops: IntegerOptional | None = None, network_type: String | None = None, source_db_cluster_resource_id: String | None = None, serverless_v2_scaling_configuration: ServerlessV2ScalingConfiguration | None = None, scaling_configuration: ScalingConfiguration | None = None, engine_mode: String | None = None, rds_custom_cluster_configuration: RdsCustomClusterConfiguration | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, engine_lifecycle_support: String | None = None, tag_specifications: TagSpecificationList | None = None, **kwargs) -> RestoreDBClusterToPointInTimeResult:
        raise NotImplementedError

    @handler("RestoreDBInstanceFromDBSnapshot")
    def restore_db_instance_from_db_snapshot(self, context: RequestContext, db_instance_identifier: String, db_snapshot_identifier: String | None = None, db_instance_class: String | None = None, port: IntegerOptional | None = None, availability_zone: String | None = None, db_subnet_group_name: String | None = None, multi_az: BooleanOptional | None = None, publicly_accessible: BooleanOptional | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, license_model: String | None = None, db_name: String | None = None, engine: String | None = None, iops: IntegerOptional | None = None, storage_throughput: IntegerOptional | None = None, option_group_name: String | None = None, tags: TagList | None = None, storage_type: String | None = None, tde_credential_arn: String | None = None, tde_credential_password: SensitiveString | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, domain: String | None = None, domain_fqdn: String | None = None, domain_ou: String | None = None, domain_auth_secret_arn: String | None = None, domain_dns_ips: StringList | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, domain_iam_role_name: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, processor_features: ProcessorFeatureList | None = None, use_default_processor_features: BooleanOptional | None = None, db_parameter_group_name: String | None = None, deletion_protection: BooleanOptional | None = None, enable_customer_owned_ip: BooleanOptional | None = None, network_type: String | None = None, backup_target: String | None = None, custom_iam_instance_profile: String | None = None, allocated_storage: IntegerOptional | None = None, db_cluster_snapshot_identifier: String | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, dedicated_log_volume: BooleanOptional | None = None, ca_certificate_identifier: String | None = None, engine_lifecycle_support: String | None = None, additional_storage_volumes: AdditionalStorageVolumesList | None = None, tag_specifications: TagSpecificationList | None = None, manage_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, **kwargs) -> RestoreDBInstanceFromDBSnapshotResult:
        raise NotImplementedError

    @handler("RestoreDBInstanceFromS3")
    def restore_db_instance_from_s3(self, context: RequestContext, db_instance_identifier: String, db_instance_class: String, engine: String, source_engine: String, source_engine_version: String, s3_bucket_name: String, s3_ingestion_role_arn: String, db_name: String | None = None, allocated_storage: IntegerOptional | None = None, master_username: String | None = None, master_user_password: SensitiveString | None = None, db_security_groups: DBSecurityGroupNameList | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, availability_zone: String | None = None, db_subnet_group_name: String | None = None, preferred_maintenance_window: String | None = None, db_parameter_group_name: String | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, port: IntegerOptional | None = None, multi_az: BooleanOptional | None = None, engine_version: String | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, license_model: String | None = None, iops: IntegerOptional | None = None, storage_throughput: IntegerOptional | None = None, option_group_name: String | None = None, publicly_accessible: BooleanOptional | None = None, tags: TagList | None = None, storage_type: String | None = None, storage_encrypted: BooleanOptional | None = None, kms_key_id: String | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, monitoring_interval: IntegerOptional | None = None, monitoring_role_arn: String | None = None, enable_iam_database_authentication: BooleanOptional | None = None, s3_prefix: String | None = None, database_insights_mode: DatabaseInsightsMode | None = None, enable_performance_insights: BooleanOptional | None = None, performance_insights_kms_key_id: String | None = None, performance_insights_retention_period: IntegerOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, processor_features: ProcessorFeatureList | None = None, use_default_processor_features: BooleanOptional | None = None, deletion_protection: BooleanOptional | None = None, max_allocated_storage: IntegerOptional | None = None, network_type: String | None = None, manage_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, dedicated_log_volume: BooleanOptional | None = None, ca_certificate_identifier: String | None = None, engine_lifecycle_support: String | None = None, additional_storage_volumes: AdditionalStorageVolumesList | None = None, tag_specifications: TagSpecificationList | None = None, **kwargs) -> RestoreDBInstanceFromS3Result:
        raise NotImplementedError

    @handler("RestoreDBInstanceToPointInTime")
    def restore_db_instance_to_point_in_time(self, context: RequestContext, target_db_instance_identifier: String, source_db_instance_identifier: String | None = None, restore_time: TStamp | None = None, use_latest_restorable_time: Boolean | None = None, db_instance_class: String | None = None, port: IntegerOptional | None = None, availability_zone: String | None = None, db_subnet_group_name: String | None = None, multi_az: BooleanOptional | None = None, publicly_accessible: BooleanOptional | None = None, auto_minor_version_upgrade: BooleanOptional | None = None, license_model: String | None = None, db_name: String | None = None, engine: String | None = None, iops: IntegerOptional | None = None, storage_throughput: IntegerOptional | None = None, option_group_name: String | None = None, copy_tags_to_snapshot: BooleanOptional | None = None, tags: TagList | None = None, storage_type: String | None = None, tde_credential_arn: String | None = None, tde_credential_password: SensitiveString | None = None, vpc_security_group_ids: VpcSecurityGroupIdList | None = None, domain: String | None = None, domain_iam_role_name: String | None = None, domain_fqdn: String | None = None, domain_ou: String | None = None, domain_auth_secret_arn: String | None = None, domain_dns_ips: StringList | None = None, enable_iam_database_authentication: BooleanOptional | None = None, enable_cloudwatch_logs_exports: LogTypeList | None = None, processor_features: ProcessorFeatureList | None = None, use_default_processor_features: BooleanOptional | None = None, db_parameter_group_name: String | None = None, deletion_protection: BooleanOptional | None = None, source_dbi_resource_id: String | None = None, max_allocated_storage: IntegerOptional | None = None, enable_customer_owned_ip: BooleanOptional | None = None, network_type: String | None = None, source_db_instance_automated_backups_arn: String | None = None, backup_target: String | None = None, custom_iam_instance_profile: String | None = None, allocated_storage: IntegerOptional | None = None, backup_retention_period: IntegerOptional | None = None, preferred_backup_window: String | None = None, dedicated_log_volume: BooleanOptional | None = None, ca_certificate_identifier: String | None = None, engine_lifecycle_support: String | None = None, additional_storage_volumes: AdditionalStorageVolumesList | None = None, tag_specifications: TagSpecificationList | None = None, manage_master_user_password: BooleanOptional | None = None, master_user_secret_kms_key_id: String | None = None, **kwargs) -> RestoreDBInstanceToPointInTimeResult:
        raise NotImplementedError

    @handler("RevokeDBSecurityGroupIngress")
    def revoke_db_security_group_ingress(self, context: RequestContext, db_security_group_name: String, cidrip: String | None = None, ec2_security_group_name: String | None = None, ec2_security_group_id: String | None = None, ec2_security_group_owner_id: String | None = None, **kwargs) -> RevokeDBSecurityGroupIngressResult:
        raise NotImplementedError

    @handler("StartActivityStream")
    def start_activity_stream(self, context: RequestContext, resource_arn: String, mode: ActivityStreamMode, kms_key_id: String, apply_immediately: BooleanOptional | None = None, engine_native_audit_fields_included: BooleanOptional | None = None, **kwargs) -> StartActivityStreamResponse:
        raise NotImplementedError

    @handler("StartDBCluster")
    def start_db_cluster(self, context: RequestContext, db_cluster_identifier: String, **kwargs) -> StartDBClusterResult:
        raise NotImplementedError

    @handler("StartDBInstance")
    def start_db_instance(self, context: RequestContext, db_instance_identifier: String, **kwargs) -> StartDBInstanceResult:
        raise NotImplementedError

    @handler("StartDBInstanceAutomatedBackupsReplication")
    def start_db_instance_automated_backups_replication(self, context: RequestContext, source_db_instance_arn: String, backup_retention_period: IntegerOptional | None = None, kms_key_id: String | None = None, pre_signed_url: SensitiveString | None = None, tags: TagList | None = None, source_region: String | None = None, **kwargs) -> StartDBInstanceAutomatedBackupsReplicationResult:
        raise NotImplementedError

    @handler("StartExportTask")
    def start_export_task(self, context: RequestContext, export_task_identifier: String, source_arn: String, s3_bucket_name: String, iam_role_arn: String, kms_key_id: String, s3_prefix: String | None = None, export_only: StringList | None = None, **kwargs) -> ExportTask:
        raise NotImplementedError

    @handler("StopActivityStream")
    def stop_activity_stream(self, context: RequestContext, resource_arn: String, apply_immediately: BooleanOptional | None = None, **kwargs) -> StopActivityStreamResponse:
        raise NotImplementedError

    @handler("StopDBCluster")
    def stop_db_cluster(self, context: RequestContext, db_cluster_identifier: String, **kwargs) -> StopDBClusterResult:
        raise NotImplementedError

    @handler("StopDBInstance")
    def stop_db_instance(self, context: RequestContext, db_instance_identifier: String, db_snapshot_identifier: String | None = None, **kwargs) -> StopDBInstanceResult:
        raise NotImplementedError

    @handler("StopDBInstanceAutomatedBackupsReplication")
    def stop_db_instance_automated_backups_replication(self, context: RequestContext, source_db_instance_arn: String, **kwargs) -> StopDBInstanceAutomatedBackupsReplicationResult:
        raise NotImplementedError

    @handler("SwitchoverBlueGreenDeployment")
    def switchover_blue_green_deployment(self, context: RequestContext, blue_green_deployment_identifier: BlueGreenDeploymentIdentifier, switchover_timeout: SwitchoverTimeout | None = None, **kwargs) -> SwitchoverBlueGreenDeploymentResponse:
        raise NotImplementedError

    @handler("SwitchoverGlobalCluster")
    def switchover_global_cluster(self, context: RequestContext, global_cluster_identifier: GlobalClusterIdentifier, target_db_cluster_identifier: DBClusterIdentifier, **kwargs) -> SwitchoverGlobalClusterResult:
        raise NotImplementedError

    @handler("SwitchoverReadReplica")
    def switchover_read_replica(self, context: RequestContext, db_instance_identifier: String, **kwargs) -> SwitchoverReadReplicaResult:
        raise NotImplementedError
