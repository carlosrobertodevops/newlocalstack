from datetime import datetime
from enum import StrEnum
from typing import IO, TypedDict
from collections.abc import Iterable, Iterator

from localstack.aws.api import handler, RequestContext, ServiceException, ServiceRequest
AccountSettingName = str
AccountSettingValue = str
Arch = str
Arn = str
ArtifactType = str
AttributeKey = str
AttributeValue = str
Author = str
Base64 = str
BaseScore = float
BatchedOperationLayerDigest = str
CredentialArn = str
CustomRoleArn = str
Epoch = int
ExceptionMessage = str
ExploitAvailable = str
FiftyMaxResults = int
FilePath = str
FindingArn = str
FindingDescription = str
FindingName = str
FixAvailable = str
FixedInVersion = str
ForceFlag = bool
ImageCount = int
ImageDigest = str
ImageFailureReason = str
ImageManifest = str
ImageTag = str
ImageTagMutabilityExclusionFilterValue = str
IsPTCRuleValid = bool
KmsError = str
KmsKey = str
KmsKeyForRepositoryCreationTemplate = str
LayerDigest = str
LayerFailureReason = str
LifecyclePolicyRulePriority = int
LifecyclePolicyText = str
LifecyclePolicyTextForRepositoryCreationTemplate = str
LifecyclePreviewMaxResults = int
MaxResults = int
MediaType = str
Metric = str
NextToken = str
PTCValidateFailure = str
PackageManager = str
Platform = str
Prefix = str
PrincipalArn = str
ProxyEndpoint = str
PullThroughCacheRuleRepositoryPrefix = str
Reason = str
RecommendationText = str
Region = str
RegistryId = str
RegistryPolicyText = str
RelatedVulnerability = str
Release = str
ReplicationError = str
RepositoryFilterValue = str
RepositoryName = str
RepositoryPolicyText = str
RepositoryTemplateDescription = str
ResourceId = str
ScanOnPushFlag = bool
ScanStatusDescription = str
ScanningConfigurationFailureReason = str
ScanningRepositoryFilterValue = str
Score = float
ScoringVector = str
Severity = str
SeverityCount = int
SigningProfileArn = str
SigningRepositoryFilterValue = str
SigningStatusFailureCode = str
SigningStatusFailureReason = str
Source = str
SourceLayerHash = str
Status = str
String = str
TagKey = str
TagValue = str
Title = str
Type = str
UploadId = str
Url = str
Version = str
VulnerabilityId = str
VulnerablePackageName = str
class ArtifactStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"

class ArtifactStatusFilter(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"
    ANY = "ANY"

class EncryptionType(StrEnum):
    AES256 = "AES256"
    KMS = "KMS"
    KMS_DSSE = "KMS_DSSE"

class FindingSeverity(StrEnum):
    INFORMATIONAL = "INFORMATIONAL"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"
    UNDEFINED = "UNDEFINED"

class ImageActionType(StrEnum):
    EXPIRE = "EXPIRE"
    TRANSITION = "TRANSITION"

class ImageFailureCode(StrEnum):
    InvalidImageDigest = "InvalidImageDigest"
    InvalidImageTag = "InvalidImageTag"
    ImageTagDoesNotMatchDigest = "ImageTagDoesNotMatchDigest"
    ImageNotFound = "ImageNotFound"
    MissingDigestAndTag = "MissingDigestAndTag"
    ImageReferencedByManifestList = "ImageReferencedByManifestList"
    KmsError = "KmsError"
    UpstreamAccessDenied = "UpstreamAccessDenied"
    UpstreamTooManyRequests = "UpstreamTooManyRequests"
    UpstreamUnavailable = "UpstreamUnavailable"
    ImageInaccessible = "ImageInaccessible"

class ImageStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"

class ImageStatusFilter(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"
    ANY = "ANY"

class ImageTagMutability(StrEnum):
    MUTABLE = "MUTABLE"
    IMMUTABLE = "IMMUTABLE"
    IMMUTABLE_WITH_EXCLUSION = "IMMUTABLE_WITH_EXCLUSION"
    MUTABLE_WITH_EXCLUSION = "MUTABLE_WITH_EXCLUSION"

class ImageTagMutabilityExclusionFilterType(StrEnum):
    WILDCARD = "WILDCARD"

class LayerAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    ARCHIVED = "ARCHIVED"

class LayerFailureCode(StrEnum):
    InvalidLayerDigest = "InvalidLayerDigest"
    MissingLayerDigest = "MissingLayerDigest"

class LifecyclePolicyPreviewStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"

class LifecyclePolicyStorageClass(StrEnum):
    ARCHIVE = "ARCHIVE"
    STANDARD = "STANDARD"

class LifecyclePolicyTargetStorageClass(StrEnum):
    ARCHIVE = "ARCHIVE"

class RCTAppliedFor(StrEnum):
    REPLICATION = "REPLICATION"
    PULL_THROUGH_CACHE = "PULL_THROUGH_CACHE"
    CREATE_ON_PUSH = "CREATE_ON_PUSH"

class ReplicationStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"

class RepositoryFilterType(StrEnum):
    PREFIX_MATCH = "PREFIX_MATCH"

class ScanFrequency(StrEnum):
    SCAN_ON_PUSH = "SCAN_ON_PUSH"
    CONTINUOUS_SCAN = "CONTINUOUS_SCAN"
    MANUAL = "MANUAL"

class ScanStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    UNSUPPORTED_IMAGE = "UNSUPPORTED_IMAGE"
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    SCAN_ELIGIBILITY_EXPIRED = "SCAN_ELIGIBILITY_EXPIRED"
    FINDINGS_UNAVAILABLE = "FINDINGS_UNAVAILABLE"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    IMAGE_ARCHIVED = "IMAGE_ARCHIVED"

class ScanType(StrEnum):
    BASIC = "BASIC"
    ENHANCED = "ENHANCED"

class ScanningConfigurationFailureCode(StrEnum):
    REPOSITORY_NOT_FOUND = "REPOSITORY_NOT_FOUND"

class ScanningRepositoryFilterType(StrEnum):
    WILDCARD = "WILDCARD"

class SigningRepositoryFilterType(StrEnum):
    WILDCARD_MATCH = "WILDCARD_MATCH"

class SigningStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"

class TagStatus(StrEnum):
    TAGGED = "TAGGED"
    UNTAGGED = "UNTAGGED"
    ANY = "ANY"

class TargetStorageClass(StrEnum):
    STANDARD = "STANDARD"
    ARCHIVE = "ARCHIVE"

class UpstreamRegistry(StrEnum):
    ecr = "ecr"
    ecr_public = "ecr-public"
    quay = "quay"
    k8s = "k8s"
    docker_hub = "docker-hub"
    github_container_registry = "github-container-registry"
    azure_container_registry = "azure-container-registry"
    gitlab_container_registry = "gitlab-container-registry"

class BlockedByOrganizationPolicyException(ServiceException):
    code: str = "BlockedByOrganizationPolicyException"
    sender_fault: bool = False
    status_code: int = 400

class EmptyUploadException(ServiceException):
    code: str = "EmptyUploadException"
    sender_fault: bool = False
    status_code: int = 400

class ExclusionAlreadyExistsException(ServiceException):
    code: str = "ExclusionAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class ExclusionNotFoundException(ServiceException):
    code: str = "ExclusionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ImageAlreadyExistsException(ServiceException):
    code: str = "ImageAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class ImageArchivedException(ServiceException):
    code: str = "ImageArchivedException"
    sender_fault: bool = False
    status_code: int = 400

class ImageDigestDoesNotMatchException(ServiceException):
    code: str = "ImageDigestDoesNotMatchException"
    sender_fault: bool = False
    status_code: int = 400

class ImageNotFoundException(ServiceException):
    code: str = "ImageNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ImageStorageClassUpdateNotSupportedException(ServiceException):
    code: str = "ImageStorageClassUpdateNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400

class ImageTagAlreadyExistsException(ServiceException):
    code: str = "ImageTagAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class InvalidLayerException(ServiceException):
    code: str = "InvalidLayerException"
    sender_fault: bool = False
    status_code: int = 400

PartSize = int
class InvalidLayerPartException(ServiceException):
    code: str = "InvalidLayerPartException"
    sender_fault: bool = False
    status_code: int = 400
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    uploadId: UploadId | None
    lastValidByteReceived: PartSize | None

class InvalidParameterException(ServiceException):
    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400

class InvalidTagParameterException(ServiceException):
    code: str = "InvalidTagParameterException"
    sender_fault: bool = False
    status_code: int = 400

class KmsException(ServiceException):
    code: str = "KmsException"
    sender_fault: bool = False
    status_code: int = 400
    kmsError: KmsError | None

class LayerAlreadyExistsException(ServiceException):
    code: str = "LayerAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class LayerInaccessibleException(ServiceException):
    code: str = "LayerInaccessibleException"
    sender_fault: bool = False
    status_code: int = 400

class LayerPartTooSmallException(ServiceException):
    code: str = "LayerPartTooSmallException"
    sender_fault: bool = False
    status_code: int = 400

class LayersNotFoundException(ServiceException):
    code: str = "LayersNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class LifecyclePolicyNotFoundException(ServiceException):
    code: str = "LifecyclePolicyNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class LifecyclePolicyPreviewInProgressException(ServiceException):
    code: str = "LifecyclePolicyPreviewInProgressException"
    sender_fault: bool = False
    status_code: int = 400

class LifecyclePolicyPreviewNotFoundException(ServiceException):
    code: str = "LifecyclePolicyPreviewNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class LimitExceededException(ServiceException):
    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400

class PullThroughCacheRuleAlreadyExistsException(ServiceException):
    code: str = "PullThroughCacheRuleAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class PullThroughCacheRuleNotFoundException(ServiceException):
    code: str = "PullThroughCacheRuleNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ReferencedImagesNotFoundException(ServiceException):
    code: str = "ReferencedImagesNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class RegistryPolicyNotFoundException(ServiceException):
    code: str = "RegistryPolicyNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class RepositoryAlreadyExistsException(ServiceException):
    code: str = "RepositoryAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class RepositoryNotEmptyException(ServiceException):
    code: str = "RepositoryNotEmptyException"
    sender_fault: bool = False
    status_code: int = 400

class RepositoryNotFoundException(ServiceException):
    code: str = "RepositoryNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class RepositoryPolicyNotFoundException(ServiceException):
    code: str = "RepositoryPolicyNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ScanNotFoundException(ServiceException):
    code: str = "ScanNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class SecretNotFoundException(ServiceException):
    code: str = "SecretNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ServerException(ServiceException):
    code: str = "ServerException"
    sender_fault: bool = False
    status_code: int = 400

class SigningConfigurationNotFoundException(ServiceException):
    code: str = "SigningConfigurationNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class TemplateAlreadyExistsException(ServiceException):
    code: str = "TemplateAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400

class TemplateNotFoundException(ServiceException):
    code: str = "TemplateNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class TooManyTagsException(ServiceException):
    code: str = "TooManyTagsException"
    sender_fault: bool = False
    status_code: int = 400

class UnableToAccessSecretException(ServiceException):
    code: str = "UnableToAccessSecretException"
    sender_fault: bool = False
    status_code: int = 400

class UnableToDecryptSecretValueException(ServiceException):
    code: str = "UnableToDecryptSecretValueException"
    sender_fault: bool = False
    status_code: int = 400

class UnableToGetUpstreamImageException(ServiceException):
    code: str = "UnableToGetUpstreamImageException"
    sender_fault: bool = False
    status_code: int = 400

class UnableToGetUpstreamLayerException(ServiceException):
    code: str = "UnableToGetUpstreamLayerException"
    sender_fault: bool = False
    status_code: int = 400

class UnsupportedImageTypeException(ServiceException):
    code: str = "UnsupportedImageTypeException"
    sender_fault: bool = False
    status_code: int = 400

class UnsupportedUpstreamRegistryException(ServiceException):
    code: str = "UnsupportedUpstreamRegistryException"
    sender_fault: bool = False
    status_code: int = 400

class UploadNotFoundException(ServiceException):
    code: str = "UploadNotFoundException"
    sender_fault: bool = False
    status_code: int = 400

class ValidationException(ServiceException):
    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400

Annotations = dict[String, String]
ArtifactTypeList = list[ArtifactType]
class Attribute(TypedDict, total=False):
    key: AttributeKey
    value: AttributeValue | None

AttributeList = list[Attribute]
ExpirationTimestamp = datetime
class AuthorizationData(TypedDict, total=False):
    authorizationToken: Base64 | None
    expiresAt: ExpirationTimestamp | None
    proxyEndpoint: ProxyEndpoint | None

AuthorizationDataList = list[AuthorizationData]
InUseCount = int
Date = datetime
ImageTagsList = list[ImageTag]
class AwsEcrContainerImageDetails(TypedDict, total=False):
    architecture: Arch | None
    author: Author | None
    imageHash: ImageDigest | None
    imageTags: ImageTagsList | None
    platform: Platform | None
    pushedAt: Date | None
    lastInUseAt: Date | None
    inUseCount: InUseCount | None
    registry: RegistryId | None
    repositoryName: RepositoryName | None

BatchedOperationLayerDigestList = list[BatchedOperationLayerDigest]
class BatchCheckLayerAvailabilityRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    layerDigests: BatchedOperationLayerDigestList

class LayerFailure(TypedDict, total=False):
    layerDigest: BatchedOperationLayerDigest | None
    failureCode: LayerFailureCode | None
    failureReason: LayerFailureReason | None

LayerFailureList = list[LayerFailure]
LayerSizeInBytes = int
class Layer(TypedDict, total=False):
    layerDigest: LayerDigest | None
    layerAvailability: LayerAvailability | None
    layerSize: LayerSizeInBytes | None
    mediaType: MediaType | None

LayerList = list[Layer]
class BatchCheckLayerAvailabilityResponse(TypedDict, total=False):
    layers: LayerList | None
    failures: LayerFailureList | None

class ImageIdentifier(TypedDict, total=False):
    imageDigest: ImageDigest | None
    imageTag: ImageTag | None

ImageIdentifierList = list[ImageIdentifier]
class BatchDeleteImageRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageIds: ImageIdentifierList

class ImageFailure(TypedDict, total=False):
    imageId: ImageIdentifier | None
    failureCode: ImageFailureCode | None
    failureReason: ImageFailureReason | None

ImageFailureList = list[ImageFailure]
class BatchDeleteImageResponse(TypedDict, total=False):
    imageIds: ImageIdentifierList | None
    failures: ImageFailureList | None

MediaTypeList = list[MediaType]
class BatchGetImageRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageIds: ImageIdentifierList
    acceptedMediaTypes: MediaTypeList | None

class Image(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageId: ImageIdentifier | None
    imageManifest: ImageManifest | None
    imageManifestMediaType: MediaType | None

ImageList = list[Image]
class BatchGetImageResponse(TypedDict, total=False):
    images: ImageList | None
    failures: ImageFailureList | None

ScanningConfigurationRepositoryNameList = list[RepositoryName]
class BatchGetRepositoryScanningConfigurationRequest(ServiceRequest):
    repositoryNames: ScanningConfigurationRepositoryNameList

class RepositoryScanningConfigurationFailure(TypedDict, total=False):
    repositoryName: RepositoryName | None
    failureCode: ScanningConfigurationFailureCode | None
    failureReason: ScanningConfigurationFailureReason | None

RepositoryScanningConfigurationFailureList = list[RepositoryScanningConfigurationFailure]
class ScanningRepositoryFilter(TypedDict, total=False):
    filter: ScanningRepositoryFilterValue
    filterType: ScanningRepositoryFilterType

ScanningRepositoryFilterList = list[ScanningRepositoryFilter]
class RepositoryScanningConfiguration(TypedDict, total=False):
    repositoryArn: Arn | None
    repositoryName: RepositoryName | None
    scanOnPush: ScanOnPushFlag | None
    scanFrequency: ScanFrequency | None
    appliedScanFilters: ScanningRepositoryFilterList | None

RepositoryScanningConfigurationList = list[RepositoryScanningConfiguration]
class BatchGetRepositoryScanningConfigurationResponse(TypedDict, total=False):
    scanningConfigurations: RepositoryScanningConfigurationList | None
    failures: RepositoryScanningConfigurationFailureList | None

LayerDigestList = list[LayerDigest]
class CompleteLayerUploadRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    uploadId: UploadId
    layerDigests: LayerDigestList

class CompleteLayerUploadResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    uploadId: UploadId | None
    layerDigest: LayerDigest | None

class CreatePullThroughCacheRuleRequest(ServiceRequest):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix
    upstreamRegistryUrl: Url
    registryId: RegistryId | None
    upstreamRegistry: UpstreamRegistry | None
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None
    upstreamRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None

CreationTimestamp = datetime
class CreatePullThroughCacheRuleResponse(TypedDict, total=False):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    upstreamRegistryUrl: Url | None
    createdAt: CreationTimestamp | None
    registryId: RegistryId | None
    upstreamRegistry: UpstreamRegistry | None
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None
    upstreamRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None

RCTAppliedForList = list[RCTAppliedFor]
class ImageTagMutabilityExclusionFilter(TypedDict, total=False):
    filterType: ImageTagMutabilityExclusionFilterType
    filter: ImageTagMutabilityExclusionFilterValue

ImageTagMutabilityExclusionFilters = list[ImageTagMutabilityExclusionFilter]
class Tag(TypedDict, total=False):
    Key: TagKey
    Value: TagValue

TagList = list[Tag]
class EncryptionConfigurationForRepositoryCreationTemplate(TypedDict, total=False):
    encryptionType: EncryptionType
    kmsKey: KmsKeyForRepositoryCreationTemplate | None

class CreateRepositoryCreationTemplateRequest(ServiceRequest):
    prefix: Prefix
    description: RepositoryTemplateDescription | None
    encryptionConfiguration: EncryptionConfigurationForRepositoryCreationTemplate | None
    resourceTags: TagList | None
    imageTagMutability: ImageTagMutability | None
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None
    repositoryPolicy: RepositoryPolicyText | None
    lifecyclePolicy: LifecyclePolicyTextForRepositoryCreationTemplate | None
    appliedFor: RCTAppliedForList
    customRoleArn: CustomRoleArn | None

class RepositoryCreationTemplate(TypedDict, total=False):
    prefix: Prefix | None
    description: RepositoryTemplateDescription | None
    encryptionConfiguration: EncryptionConfigurationForRepositoryCreationTemplate | None
    resourceTags: TagList | None
    imageTagMutability: ImageTagMutability | None
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None
    repositoryPolicy: RepositoryPolicyText | None
    lifecyclePolicy: LifecyclePolicyTextForRepositoryCreationTemplate | None
    appliedFor: RCTAppliedForList | None
    customRoleArn: CustomRoleArn | None
    createdAt: Date | None
    updatedAt: Date | None

class CreateRepositoryCreationTemplateResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryCreationTemplate: RepositoryCreationTemplate | None

class EncryptionConfiguration(TypedDict, total=False):
    encryptionType: EncryptionType
    kmsKey: KmsKey | None

class ImageScanningConfiguration(TypedDict, total=False):
    scanOnPush: ScanOnPushFlag | None

class CreateRepositoryRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    tags: TagList | None
    imageTagMutability: ImageTagMutability | None
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None
    imageScanningConfiguration: ImageScanningConfiguration | None
    encryptionConfiguration: EncryptionConfiguration | None

class Repository(TypedDict, total=False):
    repositoryArn: Arn | None
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    repositoryUri: Url | None
    createdAt: CreationTimestamp | None
    imageTagMutability: ImageTagMutability | None
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None
    imageScanningConfiguration: ImageScanningConfiguration | None
    encryptionConfiguration: EncryptionConfiguration | None

class CreateRepositoryResponse(TypedDict, total=False):
    repository: Repository | None

class CvssScore(TypedDict, total=False):
    baseScore: BaseScore | None
    scoringVector: ScoringVector | None
    source: Source | None
    version: Version | None

class CvssScoreAdjustment(TypedDict, total=False):
    metric: Metric | None
    reason: Reason | None

CvssScoreAdjustmentList = list[CvssScoreAdjustment]
class CvssScoreDetails(TypedDict, total=False):
    adjustments: CvssScoreAdjustmentList | None
    score: Score | None
    scoreSource: Source | None
    scoringVector: ScoringVector | None
    version: Version | None

CvssScoreList = list[CvssScore]
class DeleteLifecyclePolicyRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName

EvaluationTimestamp = datetime
class DeleteLifecyclePolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    lifecyclePolicyText: LifecyclePolicyText | None
    lastEvaluatedAt: EvaluationTimestamp | None

class DeletePullThroughCacheRuleRequest(ServiceRequest):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix
    registryId: RegistryId | None

class DeletePullThroughCacheRuleResponse(TypedDict, total=False):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    upstreamRegistryUrl: Url | None
    createdAt: CreationTimestamp | None
    registryId: RegistryId | None
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None
    upstreamRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None

class DeleteRegistryPolicyRequest(ServiceRequest):
    pass

class DeleteRegistryPolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    policyText: RegistryPolicyText | None

class DeleteRepositoryCreationTemplateRequest(ServiceRequest):
    prefix: Prefix

class DeleteRepositoryCreationTemplateResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryCreationTemplate: RepositoryCreationTemplate | None

class DeleteRepositoryPolicyRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName

class DeleteRepositoryPolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    policyText: RepositoryPolicyText | None

class DeleteRepositoryRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    force: ForceFlag | None

class DeleteRepositoryResponse(TypedDict, total=False):
    repository: Repository | None

class DeleteSigningConfigurationRequest(ServiceRequest):
    pass

class SigningRepositoryFilter(TypedDict, total=False):
    filter: SigningRepositoryFilterValue
    filterType: SigningRepositoryFilterType

SigningRepositoryFilterList = list[SigningRepositoryFilter]
class SigningRule(TypedDict, total=False):
    signingProfileArn: SigningProfileArn
    repositoryFilters: SigningRepositoryFilterList | None

SigningRuleList = list[SigningRule]
class SigningConfiguration(TypedDict, total=False):
    rules: SigningRuleList

class DeleteSigningConfigurationResponse(TypedDict, total=False):
    registryId: RegistryId | None
    signingConfiguration: SigningConfiguration | None

class DeregisterPullTimeUpdateExclusionRequest(ServiceRequest):
    principalArn: PrincipalArn

class DeregisterPullTimeUpdateExclusionResponse(TypedDict, total=False):
    principalArn: PrincipalArn | None

class DescribeImageReplicationStatusRequest(ServiceRequest):
    repositoryName: RepositoryName
    imageId: ImageIdentifier
    registryId: RegistryId | None

class ImageReplicationStatus(TypedDict, total=False):
    region: Region | None
    registryId: RegistryId | None
    status: ReplicationStatus | None
    failureCode: ReplicationError | None

ImageReplicationStatusList = list[ImageReplicationStatus]
class DescribeImageReplicationStatusResponse(TypedDict, total=False):
    repositoryName: RepositoryName | None
    imageId: ImageIdentifier | None
    replicationStatuses: ImageReplicationStatusList | None

class DescribeImageScanFindingsRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageId: ImageIdentifier
    nextToken: NextToken | None
    maxResults: MaxResults | None

class ScoreDetails(TypedDict, total=False):
    cvss: CvssScoreDetails | None

Tags = dict[TagKey, TagValue]
class ResourceDetails(TypedDict, total=False):
    awsEcrContainerImage: AwsEcrContainerImageDetails | None

Resource = TypedDict("Resource", {
    "details": ResourceDetails | None,
    "id": ResourceId | None,
    "tags": Tags | None,
    "type": Type | None,
}, total=False)
ResourceList = list[Resource]
class Recommendation(TypedDict, total=False):
    url: Url | None
    text: RecommendationText | None

class Remediation(TypedDict, total=False):
    recommendation: Recommendation | None

class VulnerablePackage(TypedDict, total=False):
    arch: Arch | None
    epoch: Epoch | None
    filePath: FilePath | None
    name: VulnerablePackageName | None
    packageManager: PackageManager | None
    release: Release | None
    sourceLayerHash: SourceLayerHash | None
    version: Version | None
    fixedInVersion: FixedInVersion | None

VulnerablePackagesList = list[VulnerablePackage]
RelatedVulnerabilitiesList = list[RelatedVulnerability]
ReferenceUrlsList = list[Url]
class PackageVulnerabilityDetails(TypedDict, total=False):
    cvss: CvssScoreList | None
    referenceUrls: ReferenceUrlsList | None
    relatedVulnerabilities: RelatedVulnerabilitiesList | None
    source: Source | None
    sourceUrl: Url | None
    vendorCreatedAt: Date | None
    vendorSeverity: Severity | None
    vendorUpdatedAt: Date | None
    vulnerabilityId: VulnerabilityId | None
    vulnerablePackages: VulnerablePackagesList | None

EnhancedImageScanFinding = TypedDict("EnhancedImageScanFinding", {
    "awsAccountId": RegistryId | None,
    "description": FindingDescription | None,
    "findingArn": FindingArn | None,
    "firstObservedAt": Date | None,
    "lastObservedAt": Date | None,
    "packageVulnerabilityDetails": PackageVulnerabilityDetails | None,
    "remediation": Remediation | None,
    "resources": ResourceList | None,
    "score": Score | None,
    "scoreDetails": ScoreDetails | None,
    "severity": Severity | None,
    "status": Status | None,
    "title": Title | None,
    "type": Type | None,
    "updatedAt": Date | None,
    "fixAvailable": FixAvailable | None,
    "exploitAvailable": ExploitAvailable | None,
}, total=False)
EnhancedImageScanFindingList = list[EnhancedImageScanFinding]
class ImageScanFinding(TypedDict, total=False):
    name: FindingName | None
    description: FindingDescription | None
    uri: Url | None
    severity: FindingSeverity | None
    attributes: AttributeList | None

ImageScanFindingList = list[ImageScanFinding]
FindingSeverityCounts = dict[FindingSeverity, SeverityCount]
VulnerabilitySourceUpdateTimestamp = datetime
ScanTimestamp = datetime
class ImageScanFindings(TypedDict, total=False):
    imageScanCompletedAt: ScanTimestamp | None
    vulnerabilitySourceUpdatedAt: VulnerabilitySourceUpdateTimestamp | None
    findingSeverityCounts: FindingSeverityCounts | None
    findings: ImageScanFindingList | None
    enhancedFindings: EnhancedImageScanFindingList | None

class ImageScanStatus(TypedDict, total=False):
    status: ScanStatus | None
    description: ScanStatusDescription | None

class DescribeImageScanFindingsResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageId: ImageIdentifier | None
    imageScanStatus: ImageScanStatus | None
    imageScanFindings: ImageScanFindings | None
    nextToken: NextToken | None

class DescribeImageSigningStatusRequest(ServiceRequest):
    repositoryName: RepositoryName
    imageId: ImageIdentifier
    registryId: RegistryId | None

class ImageSigningStatus(TypedDict, total=False):
    signingProfileArn: SigningProfileArn | None
    failureCode: SigningStatusFailureCode | None
    failureReason: SigningStatusFailureReason | None
    status: SigningStatus | None

ImageSigningStatusList = list[ImageSigningStatus]
class DescribeImageSigningStatusResponse(TypedDict, total=False):
    repositoryName: RepositoryName | None
    imageId: ImageIdentifier | None
    registryId: RegistryId | None
    signingStatuses: ImageSigningStatusList | None

class DescribeImagesFilter(TypedDict, total=False):
    tagStatus: TagStatus | None
    imageStatus: ImageStatusFilter | None

class DescribeImagesRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageIds: ImageIdentifierList | None
    nextToken: NextToken | None
    maxResults: MaxResults | None
    filter: DescribeImagesFilter | None

LastActivatedAtTimestamp = datetime
LastArchivedAtTimestamp = datetime
RecordedPullTimestamp = datetime
class ImageScanFindingsSummary(TypedDict, total=False):
    imageScanCompletedAt: ScanTimestamp | None
    vulnerabilitySourceUpdatedAt: VulnerabilitySourceUpdateTimestamp | None
    findingSeverityCounts: FindingSeverityCounts | None

PushTimestamp = datetime
ImageSizeInBytes = int
ImageTagList = list[ImageTag]
class ImageDetail(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageDigest: ImageDigest | None
    imageTags: ImageTagList | None
    imageSizeInBytes: ImageSizeInBytes | None
    imagePushedAt: PushTimestamp | None
    imageScanStatus: ImageScanStatus | None
    imageScanFindingsSummary: ImageScanFindingsSummary | None
    imageManifestMediaType: MediaType | None
    artifactMediaType: MediaType | None
    lastRecordedPullTime: RecordedPullTimestamp | None
    subjectManifestDigest: ImageDigest | None
    imageStatus: ImageStatus | None
    lastArchivedAt: LastArchivedAtTimestamp | None
    lastActivatedAt: LastActivatedAtTimestamp | None

ImageDetailList = list[ImageDetail]
class DescribeImagesResponse(TypedDict, total=False):
    imageDetails: ImageDetailList | None
    nextToken: NextToken | None

PullThroughCacheRuleRepositoryPrefixList = list[PullThroughCacheRuleRepositoryPrefix]
class DescribePullThroughCacheRulesRequest(ServiceRequest):
    registryId: RegistryId | None
    ecrRepositoryPrefixes: PullThroughCacheRuleRepositoryPrefixList | None
    nextToken: NextToken | None
    maxResults: MaxResults | None

UpdatedTimestamp = datetime
class PullThroughCacheRule(TypedDict, total=False):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    upstreamRegistryUrl: Url | None
    createdAt: CreationTimestamp | None
    registryId: RegistryId | None
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None
    upstreamRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    upstreamRegistry: UpstreamRegistry | None
    updatedAt: UpdatedTimestamp | None

PullThroughCacheRuleList = list[PullThroughCacheRule]
class DescribePullThroughCacheRulesResponse(TypedDict, total=False):
    pullThroughCacheRules: PullThroughCacheRuleList | None
    nextToken: NextToken | None

class DescribeRegistryRequest(ServiceRequest):
    pass

class RepositoryFilter(TypedDict, total=False):
    filter: RepositoryFilterValue
    filterType: RepositoryFilterType

RepositoryFilterList = list[RepositoryFilter]
class ReplicationDestination(TypedDict, total=False):
    region: Region
    registryId: RegistryId

ReplicationDestinationList = list[ReplicationDestination]
class ReplicationRule(TypedDict, total=False):
    destinations: ReplicationDestinationList
    repositoryFilters: RepositoryFilterList | None

ReplicationRuleList = list[ReplicationRule]
class ReplicationConfiguration(TypedDict, total=False):
    rules: ReplicationRuleList

class DescribeRegistryResponse(TypedDict, total=False):
    registryId: RegistryId | None
    replicationConfiguration: ReplicationConfiguration | None

RepositoryNameList = list[RepositoryName]
class DescribeRepositoriesRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryNames: RepositoryNameList | None
    nextToken: NextToken | None
    maxResults: MaxResults | None

RepositoryList = list[Repository]
class DescribeRepositoriesResponse(TypedDict, total=False):
    repositories: RepositoryList | None
    nextToken: NextToken | None

PrefixList = list[Prefix]
class DescribeRepositoryCreationTemplatesRequest(ServiceRequest):
    prefixes: PrefixList | None
    nextToken: NextToken | None
    maxResults: MaxResults | None

RepositoryCreationTemplateList = list[RepositoryCreationTemplate]
class DescribeRepositoryCreationTemplatesResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryCreationTemplates: RepositoryCreationTemplateList | None
    nextToken: NextToken | None

class GetAccountSettingRequest(ServiceRequest):
    name: AccountSettingName

class GetAccountSettingResponse(TypedDict, total=False):
    name: AccountSettingName | None
    value: AccountSettingName | None

GetAuthorizationTokenRegistryIdList = list[RegistryId]
class GetAuthorizationTokenRequest(ServiceRequest):
    registryIds: GetAuthorizationTokenRegistryIdList | None

class GetAuthorizationTokenResponse(TypedDict, total=False):
    authorizationData: AuthorizationDataList | None

class GetDownloadUrlForLayerRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    layerDigest: LayerDigest

class GetDownloadUrlForLayerResponse(TypedDict, total=False):
    downloadUrl: Url | None
    layerDigest: LayerDigest | None

class LifecyclePolicyPreviewFilter(TypedDict, total=False):
    tagStatus: TagStatus | None

class GetLifecyclePolicyPreviewRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageIds: ImageIdentifierList | None
    nextToken: NextToken | None
    maxResults: LifecyclePreviewMaxResults | None
    filter: LifecyclePolicyPreviewFilter | None

class TransitioningImageTotalCount(TypedDict, total=False):
    targetStorageClass: LifecyclePolicyTargetStorageClass | None
    imageTotalCount: ImageCount | None

TransitioningImageTotalCounts = list[TransitioningImageTotalCount]
class LifecyclePolicyPreviewSummary(TypedDict, total=False):
    expiringImageTotalCount: ImageCount | None
    transitioningImageTotalCounts: TransitioningImageTotalCounts | None

LifecyclePolicyRuleAction = TypedDict("LifecyclePolicyRuleAction", {
    "type": ImageActionType | None,
    "targetStorageClass": LifecyclePolicyTargetStorageClass | None,
}, total=False)
class LifecyclePolicyPreviewResult(TypedDict, total=False):
    imageTags: ImageTagList | None
    imageDigest: ImageDigest | None
    imagePushedAt: PushTimestamp | None
    action: LifecyclePolicyRuleAction | None
    appliedRulePriority: LifecyclePolicyRulePriority | None
    storageClass: LifecyclePolicyStorageClass | None

LifecyclePolicyPreviewResultList = list[LifecyclePolicyPreviewResult]
class GetLifecyclePolicyPreviewResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    lifecyclePolicyText: LifecyclePolicyText | None
    status: LifecyclePolicyPreviewStatus | None
    nextToken: NextToken | None
    previewResults: LifecyclePolicyPreviewResultList | None
    summary: LifecyclePolicyPreviewSummary | None

class GetLifecyclePolicyRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName

class GetLifecyclePolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    lifecyclePolicyText: LifecyclePolicyText | None
    lastEvaluatedAt: EvaluationTimestamp | None

class GetRegistryPolicyRequest(ServiceRequest):
    pass

class GetRegistryPolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    policyText: RegistryPolicyText | None

class GetRegistryScanningConfigurationRequest(ServiceRequest):
    pass

class RegistryScanningRule(TypedDict, total=False):
    scanFrequency: ScanFrequency
    repositoryFilters: ScanningRepositoryFilterList

RegistryScanningRuleList = list[RegistryScanningRule]
class RegistryScanningConfiguration(TypedDict, total=False):
    scanType: ScanType | None
    rules: RegistryScanningRuleList | None

class GetRegistryScanningConfigurationResponse(TypedDict, total=False):
    registryId: RegistryId | None
    scanningConfiguration: RegistryScanningConfiguration | None

class GetRepositoryPolicyRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName

class GetRepositoryPolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    policyText: RepositoryPolicyText | None

class GetSigningConfigurationRequest(ServiceRequest):
    pass

class GetSigningConfigurationResponse(TypedDict, total=False):
    registryId: RegistryId | None
    signingConfiguration: SigningConfiguration | None

class ImageReferrer(TypedDict, total=False):
    digest: ImageDigest
    mediaType: MediaType
    artifactType: ArtifactType | None
    size: ImageSizeInBytes
    annotations: Annotations | None
    artifactStatus: ArtifactStatus | None

ImageReferrerList = list[ImageReferrer]
class InitiateLayerUploadRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName

class InitiateLayerUploadResponse(TypedDict, total=False):
    uploadId: UploadId | None
    partSize: PartSize | None

LayerPartBlob = bytes
class ListImageReferrersFilter(TypedDict, total=False):
    artifactTypes: ArtifactTypeList | None
    artifactStatus: ArtifactStatusFilter | None

class SubjectIdentifier(TypedDict, total=False):
    imageDigest: ImageDigest

class ListImageReferrersRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    subjectId: SubjectIdentifier
    filter: ListImageReferrersFilter | None
    nextToken: NextToken | None
    maxResults: FiftyMaxResults | None

class ListImageReferrersResponse(TypedDict, total=False):
    referrers: ImageReferrerList | None
    nextToken: NextToken | None

class ListImagesFilter(TypedDict, total=False):
    tagStatus: TagStatus | None
    imageStatus: ImageStatusFilter | None

class ListImagesRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    nextToken: NextToken | None
    maxResults: MaxResults | None
    filter: ListImagesFilter | None

class ListImagesResponse(TypedDict, total=False):
    imageIds: ImageIdentifierList | None
    nextToken: NextToken | None

class ListPullTimeUpdateExclusionsRequest(ServiceRequest):
    maxResults: MaxResults | None
    nextToken: NextToken | None

PullTimeUpdateExclusionList = list[PrincipalArn]
class ListPullTimeUpdateExclusionsResponse(TypedDict, total=False):
    pullTimeUpdateExclusions: PullTimeUpdateExclusionList | None
    nextToken: NextToken | None

class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: Arn

class ListTagsForResourceResponse(TypedDict, total=False):
    tags: TagList | None

class PutAccountSettingRequest(ServiceRequest):
    name: AccountSettingName
    value: AccountSettingValue

class PutAccountSettingResponse(TypedDict, total=False):
    name: AccountSettingName | None
    value: AccountSettingValue | None

class PutImageRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageManifest: ImageManifest
    imageManifestMediaType: MediaType | None
    imageTag: ImageTag | None
    imageDigest: ImageDigest | None

class PutImageResponse(TypedDict, total=False):
    image: Image | None

class PutImageScanningConfigurationRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageScanningConfiguration: ImageScanningConfiguration

class PutImageScanningConfigurationResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageScanningConfiguration: ImageScanningConfiguration | None

class PutImageTagMutabilityRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageTagMutability: ImageTagMutability
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None

class PutImageTagMutabilityResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageTagMutability: ImageTagMutability | None
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None

class PutLifecyclePolicyRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    lifecyclePolicyText: LifecyclePolicyText

class PutLifecyclePolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    lifecyclePolicyText: LifecyclePolicyText | None

class PutRegistryPolicyRequest(ServiceRequest):
    policyText: RegistryPolicyText

class PutRegistryPolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    policyText: RegistryPolicyText | None

class PutRegistryScanningConfigurationRequest(ServiceRequest):
    scanType: ScanType | None
    rules: RegistryScanningRuleList | None

class PutRegistryScanningConfigurationResponse(TypedDict, total=False):
    registryScanningConfiguration: RegistryScanningConfiguration | None

class PutReplicationConfigurationRequest(ServiceRequest):
    replicationConfiguration: ReplicationConfiguration

class PutReplicationConfigurationResponse(TypedDict, total=False):
    replicationConfiguration: ReplicationConfiguration | None

class PutSigningConfigurationRequest(ServiceRequest):
    signingConfiguration: SigningConfiguration

class PutSigningConfigurationResponse(TypedDict, total=False):
    signingConfiguration: SigningConfiguration | None

class RegisterPullTimeUpdateExclusionRequest(ServiceRequest):
    principalArn: PrincipalArn

class RegisterPullTimeUpdateExclusionResponse(TypedDict, total=False):
    principalArn: PrincipalArn | None
    createdAt: CreationTimestamp | None

class SetRepositoryPolicyRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    policyText: RepositoryPolicyText
    force: ForceFlag | None

class SetRepositoryPolicyResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    policyText: RepositoryPolicyText | None

class StartImageScanRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageId: ImageIdentifier

class StartImageScanResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageId: ImageIdentifier | None
    imageScanStatus: ImageScanStatus | None

class StartLifecyclePolicyPreviewRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    lifecyclePolicyText: LifecyclePolicyText | None

class StartLifecyclePolicyPreviewResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    lifecyclePolicyText: LifecyclePolicyText | None
    status: LifecyclePolicyPreviewStatus | None

TagKeyList = list[TagKey]
class TagResourceRequest(ServiceRequest):
    resourceArn: Arn
    tags: TagList

class TagResourceResponse(TypedDict, total=False):
    pass

class UntagResourceRequest(ServiceRequest):
    resourceArn: Arn
    tagKeys: TagKeyList

class UntagResourceResponse(TypedDict, total=False):
    pass

class UpdateImageStorageClassRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    imageId: ImageIdentifier
    targetStorageClass: TargetStorageClass

class UpdateImageStorageClassResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    imageId: ImageIdentifier | None
    imageStatus: ImageStatus | None

class UpdatePullThroughCacheRuleRequest(ServiceRequest):
    registryId: RegistryId | None
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None

class UpdatePullThroughCacheRuleResponse(TypedDict, total=False):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    registryId: RegistryId | None
    updatedAt: UpdatedTimestamp | None
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None
    upstreamRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None

class UpdateRepositoryCreationTemplateRequest(ServiceRequest):
    prefix: Prefix
    description: RepositoryTemplateDescription | None
    encryptionConfiguration: EncryptionConfigurationForRepositoryCreationTemplate | None
    resourceTags: TagList | None
    imageTagMutability: ImageTagMutability | None
    imageTagMutabilityExclusionFilters: ImageTagMutabilityExclusionFilters | None
    repositoryPolicy: RepositoryPolicyText | None
    lifecyclePolicy: LifecyclePolicyTextForRepositoryCreationTemplate | None
    appliedFor: RCTAppliedForList | None
    customRoleArn: CustomRoleArn | None

class UpdateRepositoryCreationTemplateResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryCreationTemplate: RepositoryCreationTemplate | None

class UploadLayerPartRequest(ServiceRequest):
    registryId: RegistryId | None
    repositoryName: RepositoryName
    uploadId: UploadId
    partFirstByte: PartSize
    partLastByte: PartSize
    layerPartBlob: LayerPartBlob

class UploadLayerPartResponse(TypedDict, total=False):
    registryId: RegistryId | None
    repositoryName: RepositoryName | None
    uploadId: UploadId | None
    lastByteReceived: PartSize | None

class ValidatePullThroughCacheRuleRequest(ServiceRequest):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix
    registryId: RegistryId | None

class ValidatePullThroughCacheRuleResponse(TypedDict, total=False):
    ecrRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    registryId: RegistryId | None
    upstreamRegistryUrl: Url | None
    credentialArn: CredentialArn | None
    customRoleArn: CustomRoleArn | None
    upstreamRepositoryPrefix: PullThroughCacheRuleRepositoryPrefix | None
    isValid: IsPTCRuleValid | None
    failure: PTCValidateFailure | None

class EcrApi:

    service: str = "ecr"
    version: str = "2015-09-21"

    @handler("BatchCheckLayerAvailability")
    def batch_check_layer_availability(self, context: RequestContext, repository_name: RepositoryName, layer_digests: BatchedOperationLayerDigestList, registry_id: RegistryId | None = None, **kwargs) -> BatchCheckLayerAvailabilityResponse:
        raise NotImplementedError

    @handler("BatchDeleteImage")
    def batch_delete_image(self, context: RequestContext, repository_name: RepositoryName, image_ids: ImageIdentifierList, registry_id: RegistryId | None = None, **kwargs) -> BatchDeleteImageResponse:
        raise NotImplementedError

    @handler("BatchGetImage")
    def batch_get_image(self, context: RequestContext, repository_name: RepositoryName, image_ids: ImageIdentifierList, registry_id: RegistryId | None = None, accepted_media_types: MediaTypeList | None = None, **kwargs) -> BatchGetImageResponse:
        raise NotImplementedError

    @handler("BatchGetRepositoryScanningConfiguration")
    def batch_get_repository_scanning_configuration(self, context: RequestContext, repository_names: ScanningConfigurationRepositoryNameList, **kwargs) -> BatchGetRepositoryScanningConfigurationResponse:
        raise NotImplementedError

    @handler("CompleteLayerUpload")
    def complete_layer_upload(self, context: RequestContext, repository_name: RepositoryName, upload_id: UploadId, layer_digests: LayerDigestList, registry_id: RegistryId | None = None, **kwargs) -> CompleteLayerUploadResponse:
        raise NotImplementedError

    @handler("CreatePullThroughCacheRule")
    def create_pull_through_cache_rule(self, context: RequestContext, ecr_repository_prefix: PullThroughCacheRuleRepositoryPrefix, upstream_registry_url: Url, registry_id: RegistryId | None = None, upstream_registry: UpstreamRegistry | None = None, credential_arn: CredentialArn | None = None, custom_role_arn: CustomRoleArn | None = None, upstream_repository_prefix: PullThroughCacheRuleRepositoryPrefix | None = None, **kwargs) -> CreatePullThroughCacheRuleResponse:
        raise NotImplementedError

    @handler("CreateRepository")
    def create_repository(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, tags: TagList | None = None, image_tag_mutability: ImageTagMutability | None = None, image_tag_mutability_exclusion_filters: ImageTagMutabilityExclusionFilters | None = None, image_scanning_configuration: ImageScanningConfiguration | None = None, encryption_configuration: EncryptionConfiguration | None = None, **kwargs) -> CreateRepositoryResponse:
        raise NotImplementedError

    @handler("CreateRepositoryCreationTemplate")
    def create_repository_creation_template(self, context: RequestContext, prefix: Prefix, applied_for: RCTAppliedForList, description: RepositoryTemplateDescription | None = None, encryption_configuration: EncryptionConfigurationForRepositoryCreationTemplate | None = None, resource_tags: TagList | None = None, image_tag_mutability: ImageTagMutability | None = None, image_tag_mutability_exclusion_filters: ImageTagMutabilityExclusionFilters | None = None, repository_policy: RepositoryPolicyText | None = None, lifecycle_policy: LifecyclePolicyTextForRepositoryCreationTemplate | None = None, custom_role_arn: CustomRoleArn | None = None, **kwargs) -> CreateRepositoryCreationTemplateResponse:
        raise NotImplementedError

    @handler("DeleteLifecyclePolicy")
    def delete_lifecycle_policy(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, **kwargs) -> DeleteLifecyclePolicyResponse:
        raise NotImplementedError

    @handler("DeletePullThroughCacheRule")
    def delete_pull_through_cache_rule(self, context: RequestContext, ecr_repository_prefix: PullThroughCacheRuleRepositoryPrefix, registry_id: RegistryId | None = None, **kwargs) -> DeletePullThroughCacheRuleResponse:
        raise NotImplementedError

    @handler("DeleteRegistryPolicy")
    def delete_registry_policy(self, context: RequestContext, **kwargs) -> DeleteRegistryPolicyResponse:
        raise NotImplementedError

    @handler("DeleteRepository")
    def delete_repository(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, force: ForceFlag | None = None, **kwargs) -> DeleteRepositoryResponse:
        raise NotImplementedError

    @handler("DeleteRepositoryCreationTemplate")
    def delete_repository_creation_template(self, context: RequestContext, prefix: Prefix, **kwargs) -> DeleteRepositoryCreationTemplateResponse:
        raise NotImplementedError

    @handler("DeleteRepositoryPolicy")
    def delete_repository_policy(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, **kwargs) -> DeleteRepositoryPolicyResponse:
        raise NotImplementedError

    @handler("DeleteSigningConfiguration")
    def delete_signing_configuration(self, context: RequestContext, **kwargs) -> DeleteSigningConfigurationResponse:
        raise NotImplementedError

    @handler("DeregisterPullTimeUpdateExclusion")
    def deregister_pull_time_update_exclusion(self, context: RequestContext, principal_arn: PrincipalArn, **kwargs) -> DeregisterPullTimeUpdateExclusionResponse:
        raise NotImplementedError

    @handler("DescribeImageReplicationStatus")
    def describe_image_replication_status(self, context: RequestContext, repository_name: RepositoryName, image_id: ImageIdentifier, registry_id: RegistryId | None = None, **kwargs) -> DescribeImageReplicationStatusResponse:
        raise NotImplementedError

    @handler("DescribeImageScanFindings")
    def describe_image_scan_findings(self, context: RequestContext, repository_name: RepositoryName, image_id: ImageIdentifier, registry_id: RegistryId | None = None, next_token: NextToken | None = None, max_results: MaxResults | None = None, **kwargs) -> DescribeImageScanFindingsResponse:
        raise NotImplementedError

    @handler("DescribeImageSigningStatus")
    def describe_image_signing_status(self, context: RequestContext, repository_name: RepositoryName, image_id: ImageIdentifier, registry_id: RegistryId | None = None, **kwargs) -> DescribeImageSigningStatusResponse:
        raise NotImplementedError

    @handler("DescribeImages")
    def describe_images(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, image_ids: ImageIdentifierList | None = None, next_token: NextToken | None = None, max_results: MaxResults | None = None, filter: DescribeImagesFilter | None = None, **kwargs) -> DescribeImagesResponse:
        raise NotImplementedError

    @handler("DescribePullThroughCacheRules")
    def describe_pull_through_cache_rules(self, context: RequestContext, registry_id: RegistryId | None = None, ecr_repository_prefixes: PullThroughCacheRuleRepositoryPrefixList | None = None, next_token: NextToken | None = None, max_results: MaxResults | None = None, **kwargs) -> DescribePullThroughCacheRulesResponse:
        raise NotImplementedError

    @handler("DescribeRegistry")
    def describe_registry(self, context: RequestContext, **kwargs) -> DescribeRegistryResponse:
        raise NotImplementedError

    @handler("DescribeRepositories")
    def describe_repositories(self, context: RequestContext, registry_id: RegistryId | None = None, repository_names: RepositoryNameList | None = None, next_token: NextToken | None = None, max_results: MaxResults | None = None, **kwargs) -> DescribeRepositoriesResponse:
        raise NotImplementedError

    @handler("DescribeRepositoryCreationTemplates")
    def describe_repository_creation_templates(self, context: RequestContext, prefixes: PrefixList | None = None, next_token: NextToken | None = None, max_results: MaxResults | None = None, **kwargs) -> DescribeRepositoryCreationTemplatesResponse:
        raise NotImplementedError

    @handler("GetAccountSetting")
    def get_account_setting(self, context: RequestContext, name: AccountSettingName, **kwargs) -> GetAccountSettingResponse:
        raise NotImplementedError

    @handler("GetAuthorizationToken")
    def get_authorization_token(self, context: RequestContext, registry_ids: GetAuthorizationTokenRegistryIdList | None = None, **kwargs) -> GetAuthorizationTokenResponse:
        raise NotImplementedError

    @handler("GetDownloadUrlForLayer")
    def get_download_url_for_layer(self, context: RequestContext, repository_name: RepositoryName, layer_digest: LayerDigest, registry_id: RegistryId | None = None, **kwargs) -> GetDownloadUrlForLayerResponse:
        raise NotImplementedError

    @handler("GetLifecyclePolicy")
    def get_lifecycle_policy(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, **kwargs) -> GetLifecyclePolicyResponse:
        raise NotImplementedError

    @handler("GetLifecyclePolicyPreview")
    def get_lifecycle_policy_preview(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, image_ids: ImageIdentifierList | None = None, next_token: NextToken | None = None, max_results: LifecyclePreviewMaxResults | None = None, filter: LifecyclePolicyPreviewFilter | None = None, **kwargs) -> GetLifecyclePolicyPreviewResponse:
        raise NotImplementedError

    @handler("GetRegistryPolicy")
    def get_registry_policy(self, context: RequestContext, **kwargs) -> GetRegistryPolicyResponse:
        raise NotImplementedError

    @handler("GetRegistryScanningConfiguration")
    def get_registry_scanning_configuration(self, context: RequestContext, **kwargs) -> GetRegistryScanningConfigurationResponse:
        raise NotImplementedError

    @handler("GetRepositoryPolicy")
    def get_repository_policy(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, **kwargs) -> GetRepositoryPolicyResponse:
        raise NotImplementedError

    @handler("GetSigningConfiguration")
    def get_signing_configuration(self, context: RequestContext, **kwargs) -> GetSigningConfigurationResponse:
        raise NotImplementedError

    @handler("InitiateLayerUpload")
    def initiate_layer_upload(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, **kwargs) -> InitiateLayerUploadResponse:
        raise NotImplementedError

    @handler("ListImageReferrers")
    def list_image_referrers(self, context: RequestContext, repository_name: RepositoryName, subject_id: SubjectIdentifier, registry_id: RegistryId | None = None, filter: ListImageReferrersFilter | None = None, next_token: NextToken | None = None, max_results: FiftyMaxResults | None = None, **kwargs) -> ListImageReferrersResponse:
        raise NotImplementedError

    @handler("ListImages")
    def list_images(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, next_token: NextToken | None = None, max_results: MaxResults | None = None, filter: ListImagesFilter | None = None, **kwargs) -> ListImagesResponse:
        raise NotImplementedError

    @handler("ListPullTimeUpdateExclusions")
    def list_pull_time_update_exclusions(self, context: RequestContext, max_results: MaxResults | None = None, next_token: NextToken | None = None, **kwargs) -> ListPullTimeUpdateExclusionsResponse:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(self, context: RequestContext, resource_arn: Arn, **kwargs) -> ListTagsForResourceResponse:
        raise NotImplementedError

    @handler("PutAccountSetting")
    def put_account_setting(self, context: RequestContext, name: AccountSettingName, value: AccountSettingValue, **kwargs) -> PutAccountSettingResponse:
        raise NotImplementedError

    @handler("PutImage")
    def put_image(self, context: RequestContext, repository_name: RepositoryName, image_manifest: ImageManifest, registry_id: RegistryId | None = None, image_manifest_media_type: MediaType | None = None, image_tag: ImageTag | None = None, image_digest: ImageDigest | None = None, **kwargs) -> PutImageResponse:
        raise NotImplementedError

    @handler("PutImageScanningConfiguration")
    def put_image_scanning_configuration(self, context: RequestContext, repository_name: RepositoryName, image_scanning_configuration: ImageScanningConfiguration, registry_id: RegistryId | None = None, **kwargs) -> PutImageScanningConfigurationResponse:
        raise NotImplementedError

    @handler("PutImageTagMutability")
    def put_image_tag_mutability(self, context: RequestContext, repository_name: RepositoryName, image_tag_mutability: ImageTagMutability, registry_id: RegistryId | None = None, image_tag_mutability_exclusion_filters: ImageTagMutabilityExclusionFilters | None = None, **kwargs) -> PutImageTagMutabilityResponse:
        raise NotImplementedError

    @handler("PutLifecyclePolicy")
    def put_lifecycle_policy(self, context: RequestContext, repository_name: RepositoryName, lifecycle_policy_text: LifecyclePolicyText, registry_id: RegistryId | None = None, **kwargs) -> PutLifecyclePolicyResponse:
        raise NotImplementedError

    @handler("PutRegistryPolicy")
    def put_registry_policy(self, context: RequestContext, policy_text: RegistryPolicyText, **kwargs) -> PutRegistryPolicyResponse:
        raise NotImplementedError

    @handler("PutRegistryScanningConfiguration")
    def put_registry_scanning_configuration(self, context: RequestContext, scan_type: ScanType | None = None, rules: RegistryScanningRuleList | None = None, **kwargs) -> PutRegistryScanningConfigurationResponse:
        raise NotImplementedError

    @handler("PutReplicationConfiguration")
    def put_replication_configuration(self, context: RequestContext, replication_configuration: ReplicationConfiguration, **kwargs) -> PutReplicationConfigurationResponse:
        raise NotImplementedError

    @handler("PutSigningConfiguration")
    def put_signing_configuration(self, context: RequestContext, signing_configuration: SigningConfiguration, **kwargs) -> PutSigningConfigurationResponse:
        raise NotImplementedError

    @handler("RegisterPullTimeUpdateExclusion")
    def register_pull_time_update_exclusion(self, context: RequestContext, principal_arn: PrincipalArn, **kwargs) -> RegisterPullTimeUpdateExclusionResponse:
        raise NotImplementedError

    @handler("SetRepositoryPolicy")
    def set_repository_policy(self, context: RequestContext, repository_name: RepositoryName, policy_text: RepositoryPolicyText, registry_id: RegistryId | None = None, force: ForceFlag | None = None, **kwargs) -> SetRepositoryPolicyResponse:
        raise NotImplementedError

    @handler("StartImageScan")
    def start_image_scan(self, context: RequestContext, repository_name: RepositoryName, image_id: ImageIdentifier, registry_id: RegistryId | None = None, **kwargs) -> StartImageScanResponse:
        raise NotImplementedError

    @handler("StartLifecyclePolicyPreview")
    def start_lifecycle_policy_preview(self, context: RequestContext, repository_name: RepositoryName, registry_id: RegistryId | None = None, lifecycle_policy_text: LifecyclePolicyText | None = None, **kwargs) -> StartLifecyclePolicyPreviewResponse:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(self, context: RequestContext, resource_arn: Arn, tags: TagList, **kwargs) -> TagResourceResponse:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(self, context: RequestContext, resource_arn: Arn, tag_keys: TagKeyList, **kwargs) -> UntagResourceResponse:
        raise NotImplementedError

    @handler("UpdateImageStorageClass")
    def update_image_storage_class(self, context: RequestContext, repository_name: RepositoryName, image_id: ImageIdentifier, target_storage_class: TargetStorageClass, registry_id: RegistryId | None = None, **kwargs) -> UpdateImageStorageClassResponse:
        raise NotImplementedError

    @handler("UpdatePullThroughCacheRule")
    def update_pull_through_cache_rule(self, context: RequestContext, ecr_repository_prefix: PullThroughCacheRuleRepositoryPrefix, registry_id: RegistryId | None = None, credential_arn: CredentialArn | None = None, custom_role_arn: CustomRoleArn | None = None, **kwargs) -> UpdatePullThroughCacheRuleResponse:
        raise NotImplementedError

    @handler("UpdateRepositoryCreationTemplate")
    def update_repository_creation_template(self, context: RequestContext, prefix: Prefix, description: RepositoryTemplateDescription | None = None, encryption_configuration: EncryptionConfigurationForRepositoryCreationTemplate | None = None, resource_tags: TagList | None = None, image_tag_mutability: ImageTagMutability | None = None, image_tag_mutability_exclusion_filters: ImageTagMutabilityExclusionFilters | None = None, repository_policy: RepositoryPolicyText | None = None, lifecycle_policy: LifecyclePolicyTextForRepositoryCreationTemplate | None = None, applied_for: RCTAppliedForList | None = None, custom_role_arn: CustomRoleArn | None = None, **kwargs) -> UpdateRepositoryCreationTemplateResponse:
        raise NotImplementedError

    @handler("UploadLayerPart")
    def upload_layer_part(self, context: RequestContext, repository_name: RepositoryName, upload_id: UploadId, part_first_byte: PartSize, part_last_byte: PartSize, layer_part_blob: LayerPartBlob, registry_id: RegistryId | None = None, **kwargs) -> UploadLayerPartResponse:
        raise NotImplementedError

    @handler("ValidatePullThroughCacheRule")
    def validate_pull_through_cache_rule(self, context: RequestContext, ecr_repository_prefix: PullThroughCacheRuleRepositoryPrefix, registry_id: RegistryId | None = None, **kwargs) -> ValidatePullThroughCacheRuleResponse:
        raise NotImplementedError
