import { S3Client, ListBucketsCommand, CreateBucketCommand, DeleteBucketCommand, ListObjectsV2Command } from "@aws-sdk/client-s3";
import { SQSClient, ListQueuesCommand, CreateQueueCommand, DeleteQueueCommand, GetQueueAttributesCommand, ReceiveMessageCommand, SendMessageCommand } from "@aws-sdk/client-sqs";
import { DynamoDBClient, ListTablesCommand, CreateTableCommand, DeleteTableCommand, DescribeTableCommand, ScanCommand } from "@aws-sdk/client-dynamodb";
import { LambdaClient, ListFunctionsCommand, CreateFunctionCommand, DeleteFunctionCommand, GetFunctionCommand, InvokeCommand, type Runtime } from "@aws-sdk/client-lambda";
import { SNSClient, ListTopicsCommand, CreateTopicCommand, DeleteTopicCommand, PublishCommand } from "@aws-sdk/client-sns";
import { CloudWatchLogsClient, DescribeLogGroupsCommand, CreateLogGroupCommand, DeleteLogGroupCommand } from "@aws-sdk/client-cloudwatch-logs";
import { IAMClient, ListUsersCommand, ListRolesCommand, CreateUserCommand, DeleteUserCommand, CreateRoleCommand, DeleteRoleCommand } from "@aws-sdk/client-iam";
import { SecretsManagerClient, ListSecretsCommand, CreateSecretCommand, DeleteSecretCommand, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";
import { EC2Client, DescribeInstancesCommand, RunInstancesCommand, TerminateInstancesCommand, DescribeVpcsCommand, DescribeSecurityGroupsCommand, CreateVpcCommand, DeleteVpcCommand, DescribeSubnetsCommand, CreateSubnetCommand, DeleteSubnetCommand, type _InstanceType } from "@aws-sdk/client-ec2";
import { KMSClient, ListKeysCommand, CreateKeyCommand, ScheduleKeyDeletionCommand, DescribeKeyCommand } from "@aws-sdk/client-kms";
import { CloudFormationClient, ListStacksCommand, CreateStackCommand, DeleteStackCommand, DescribeStacksCommand } from "@aws-sdk/client-cloudformation";
import { ECRClient, DescribeRepositoriesCommand, CreateRepositoryCommand, DeleteRepositoryCommand } from "@aws-sdk/client-ecr";
import { Route53Client, ListHostedZonesCommand, CreateHostedZoneCommand, DeleteHostedZoneCommand } from "@aws-sdk/client-route-53";
import { APIGatewayClient, GetRestApisCommand, CreateRestApiCommand, DeleteRestApiCommand } from "@aws-sdk/client-api-gateway";
import { SFNClient, ListStateMachinesCommand, CreateStateMachineCommand, DeleteStateMachineCommand } from "@aws-sdk/client-sfn";
import { EventBridgeClient, ListEventBusesCommand, CreateEventBusCommand, DeleteEventBusCommand, ListRulesCommand } from "@aws-sdk/client-eventbridge";
import { KinesisClient, ListStreamsCommand, CreateStreamCommand, DeleteStreamCommand, DescribeStreamCommand } from "@aws-sdk/client-kinesis";
import { SSMClient, DescribeParametersCommand, PutParameterCommand, DeleteParameterCommand, GetParameterCommand } from "@aws-sdk/client-ssm";
import { EKSClient, ListClustersCommand as EksListClustersCommand, CreateClusterCommand as EksCreateClusterCommand, DeleteClusterCommand as EksDeleteClusterCommand, DescribeClusterCommand as EksDescribeClusterCommand } from "@aws-sdk/client-eks";
import { ECSClient, ListClustersCommand as EcsListClustersCommand, CreateClusterCommand as EcsCreateClusterCommand, DeleteClusterCommand as EcsDeleteClusterCommand, DescribeClustersCommand as EcsDescribeClustersCommand, ListTaskDefinitionsCommand } from "@aws-sdk/client-ecs";
import { RDSClient, DescribeDBInstancesCommand, CreateDBInstanceCommand, DeleteDBInstanceCommand } from "@aws-sdk/client-rds";

const COMMON = {
  endpoint: "http://localhost:4566",
  region: "us-east-1",
  credentials: { accessKeyId: "test", secretAccessKey: "test" },
};

export const s3 = new S3Client({ ...COMMON, forcePathStyle: true });
export const sqs = new SQSClient(COMMON);
export const dynamo = new DynamoDBClient(COMMON);
export const lambda = new LambdaClient(COMMON);
export const sns = new SNSClient(COMMON);
export const logs = new CloudWatchLogsClient(COMMON);
export const iam = new IAMClient(COMMON);
export const secrets = new SecretsManagerClient(COMMON);
export const ec2 = new EC2Client(COMMON);
export const kms = new KMSClient(COMMON);
export const cfn = new CloudFormationClient(COMMON);
export const ecr = new ECRClient(COMMON);
export const route53 = new Route53Client(COMMON);
export const apigw = new APIGatewayClient(COMMON);
export const sfn = new SFNClient(COMMON);
export const events = new EventBridgeClient(COMMON);
export const kinesis = new KinesisClient(COMMON);
export const ssm = new SSMClient(COMMON);
export const eks = new EKSClient(COMMON);
export const ecs = new ECSClient(COMMON);
export const rds = new RDSClient(COMMON);

export const awsApi = {
  // S3
  listBuckets: async () => (await s3.send(new ListBucketsCommand({}))).Buckets ?? [],
  createBucket: (name: string) => s3.send(new CreateBucketCommand({ Bucket: name })),
  deleteBucket: (name: string) => s3.send(new DeleteBucketCommand({ Bucket: name })),
  listObjects: (bucket: string) =>
    s3.send(new ListObjectsV2Command({ Bucket: bucket })),

  // SQS
  listQueues: async () => (await sqs.send(new ListQueuesCommand({}))).QueueUrls ?? [],
  createQueue: (name: string) => sqs.send(new CreateQueueCommand({ QueueName: name })),
  deleteQueue: (url: string) => sqs.send(new DeleteQueueCommand({ QueueUrl: url })),
  queueAttrs: (url: string) =>
    sqs.send(new GetQueueAttributesCommand({ QueueUrl: url, AttributeNames: ["All"] })),
  receive: (url: string) =>
    sqs.send(new ReceiveMessageCommand({ QueueUrl: url, MaxNumberOfMessages: 10 })),
  send: (url: string, body: string) =>
    sqs.send(new SendMessageCommand({ QueueUrl: url, MessageBody: body })),

  // DynamoDB
  listTables: async () => (await dynamo.send(new ListTablesCommand({}))).TableNames ?? [],
  createTable: (name: string, partitionKey: string, sortKey?: string) =>
    dynamo.send(
      new CreateTableCommand({
        TableName: name,
        BillingMode: "PAY_PER_REQUEST",
        KeySchema: [
          { AttributeName: partitionKey, KeyType: "HASH" },
          ...(sortKey ? [{ AttributeName: sortKey, KeyType: "RANGE" as const }] : []),
        ],
        AttributeDefinitions: [
          { AttributeName: partitionKey, AttributeType: "S" },
          ...(sortKey ? [{ AttributeName: sortKey, AttributeType: "S" as const }] : []),
        ],
      }),
    ),
  deleteTable: (name: string) => dynamo.send(new DeleteTableCommand({ TableName: name })),
  describeTable: (name: string) =>
    dynamo.send(new DescribeTableCommand({ TableName: name })),
  scanTable: (name: string) =>
    dynamo.send(new ScanCommand({ TableName: name, Limit: 50 })),

  // Lambda
  listFunctions: async () =>
    (await lambda.send(new ListFunctionsCommand({}))).Functions ?? [],
  createFunction: (
    name: string,
    runtime: string,
    handler: string,
    zipBase64: string,
  ) =>
    lambda.send(
      new CreateFunctionCommand({
        FunctionName: name,
        Runtime: runtime as Runtime,
        Handler: handler,
        Role: "arn:aws:iam::000000000000:role/lambda-role",
        Code: { ZipFile: Uint8Array.from(atob(zipBase64), (c) => c.charCodeAt(0)) },
      }),
    ),
  deleteFunction: (name: string) =>
    lambda.send(new DeleteFunctionCommand({ FunctionName: name })),
  getFunction: (name: string) =>
    lambda.send(new GetFunctionCommand({ FunctionName: name })),
  invoke: (name: string, payload: string) =>
    lambda.send(
      new InvokeCommand({
        FunctionName: name,
        Payload: new TextEncoder().encode(payload),
      }),
    ),

  // SNS
  listTopics: async () => (await sns.send(new ListTopicsCommand({}))).Topics ?? [],
  createTopic: (name: string) => sns.send(new CreateTopicCommand({ Name: name })),
  deleteTopic: (arn: string) => sns.send(new DeleteTopicCommand({ TopicArn: arn })),
  publishToTopic: (arn: string, message: string) =>
    sns.send(new PublishCommand({ TopicArn: arn, Message: message })),

  // CloudWatch Logs
  listLogGroups: async () =>
    (await logs.send(new DescribeLogGroupsCommand({}))).logGroups ?? [],
  createLogGroup: (name: string) =>
    logs.send(new CreateLogGroupCommand({ logGroupName: name })),
  deleteLogGroup: (name: string) =>
    logs.send(new DeleteLogGroupCommand({ logGroupName: name })),

  // IAM
  listIamUsers: async () => (await iam.send(new ListUsersCommand({}))).Users ?? [],
  listIamRoles: async () => (await iam.send(new ListRolesCommand({}))).Roles ?? [],
  createIamUser: (name: string) => iam.send(new CreateUserCommand({ UserName: name })),
  deleteIamUser: (name: string) => iam.send(new DeleteUserCommand({ UserName: name })),
  createIamRole: (name: string) =>
    iam.send(
      new CreateRoleCommand({
        RoleName: name,
        AssumeRolePolicyDocument: JSON.stringify({
          Version: "2012-10-17",
          Statement: [
            {
              Effect: "Allow",
              Principal: { Service: "lambda.amazonaws.com" },
              Action: "sts:AssumeRole",
            },
          ],
        }),
      }),
    ),
  deleteIamRole: (name: string) => iam.send(new DeleteRoleCommand({ RoleName: name })),

  // Secrets Manager
  listSecrets: async () =>
    (await secrets.send(new ListSecretsCommand({}))).SecretList ?? [],
  createSecret: (name: string, value: string) =>
    secrets.send(new CreateSecretCommand({ Name: name, SecretString: value })),
  deleteSecret: (id: string) =>
    secrets.send(new DeleteSecretCommand({ SecretId: id, ForceDeleteWithoutRecovery: true })),
  getSecret: (id: string) =>
    secrets.send(new GetSecretValueCommand({ SecretId: id })),

  // EC2 + VPC
  listInstances: async () => {
    const res = await ec2.send(new DescribeInstancesCommand({}));
    return (res.Reservations ?? []).flatMap((r) => r.Instances ?? []);
  },
  runInstance: (imageId: string, instanceType = "t2.micro") =>
    ec2.send(
      new RunInstancesCommand({
        ImageId: imageId,
        InstanceType: instanceType as _InstanceType,
        MinCount: 1,
        MaxCount: 1,
      }),
    ),
  terminateInstance: (id: string) =>
    ec2.send(new TerminateInstancesCommand({ InstanceIds: [id] })),
  listVpcs: async () => (await ec2.send(new DescribeVpcsCommand({}))).Vpcs ?? [],
  createVpc: (cidr: string) =>
    ec2.send(new CreateVpcCommand({ CidrBlock: cidr })),
  deleteVpc: (id: string) => ec2.send(new DeleteVpcCommand({ VpcId: id })),
  listSubnets: async () => (await ec2.send(new DescribeSubnetsCommand({}))).Subnets ?? [],
  createSubnet: (vpcId: string, cidr: string) =>
    ec2.send(new CreateSubnetCommand({ VpcId: vpcId, CidrBlock: cidr })),
  deleteSubnet: (id: string) => ec2.send(new DeleteSubnetCommand({ SubnetId: id })),
  listSecurityGroups: async () =>
    (await ec2.send(new DescribeSecurityGroupsCommand({}))).SecurityGroups ?? [],

  // KMS
  listKmsKeys: async () => (await kms.send(new ListKeysCommand({}))).Keys ?? [],
  createKmsKey: (description: string) =>
    kms.send(new CreateKeyCommand({ Description: description })),
  scheduleKmsKeyDeletion: (id: string) =>
    kms.send(new ScheduleKeyDeletionCommand({ KeyId: id, PendingWindowInDays: 7 })),
  describeKmsKey: (id: string) =>
    kms.send(new DescribeKeyCommand({ KeyId: id })),

  // CloudFormation
  listStacks: async () => (await cfn.send(new ListStacksCommand({}))).StackSummaries ?? [],
  describeStack: (name: string) =>
    cfn.send(new DescribeStacksCommand({ StackName: name })),
  createStack: (name: string, templateBody: string) =>
    cfn.send(new CreateStackCommand({ StackName: name, TemplateBody: templateBody })),
  deleteStack: (name: string) => cfn.send(new DeleteStackCommand({ StackName: name })),

  // ECR
  listEcrRepos: async () =>
    (await ecr.send(new DescribeRepositoriesCommand({}))).repositories ?? [],
  createEcrRepo: (name: string) =>
    ecr.send(new CreateRepositoryCommand({ repositoryName: name })),
  deleteEcrRepo: (name: string) =>
    ecr.send(new DeleteRepositoryCommand({ repositoryName: name, force: true })),

  // Route 53
  listHostedZones: async () =>
    (await route53.send(new ListHostedZonesCommand({}))).HostedZones ?? [],
  createHostedZone: (name: string) =>
    route53.send(
      new CreateHostedZoneCommand({
        Name: name,
        CallerReference: `console-${Date.now()}`,
      }),
    ),
  deleteHostedZone: (id: string) =>
    route53.send(new DeleteHostedZoneCommand({ Id: id })),

  // API Gateway
  listRestApis: async () =>
    (await apigw.send(new GetRestApisCommand({}))).items ?? [],
  createRestApi: (name: string) =>
    apigw.send(new CreateRestApiCommand({ name })),
  deleteRestApi: (id: string) =>
    apigw.send(new DeleteRestApiCommand({ restApiId: id })),

  // Step Functions
  listStateMachines: async () =>
    (await sfn.send(new ListStateMachinesCommand({}))).stateMachines ?? [],
  createStateMachine: (name: string, definition: string, roleArn: string) =>
    sfn.send(
      new CreateStateMachineCommand({
        name,
        definition,
        roleArn,
      }),
    ),
  deleteStateMachine: (arn: string) =>
    sfn.send(new DeleteStateMachineCommand({ stateMachineArn: arn })),

  // EventBridge
  listEventBuses: async () =>
    (await events.send(new ListEventBusesCommand({}))).EventBuses ?? [],
  createEventBus: (name: string) =>
    events.send(new CreateEventBusCommand({ Name: name })),
  deleteEventBus: (name: string) =>
    events.send(new DeleteEventBusCommand({ Name: name })),
  listEventRules: async (busName?: string) =>
    (await events.send(new ListRulesCommand({ EventBusName: busName }))).Rules ?? [],

  // Kinesis
  listKinesisStreams: async () =>
    (await kinesis.send(new ListStreamsCommand({}))).StreamNames ?? [],
  createKinesisStream: (name: string, shardCount = 1) =>
    kinesis.send(new CreateStreamCommand({ StreamName: name, ShardCount: shardCount })),
  deleteKinesisStream: (name: string) =>
    kinesis.send(new DeleteStreamCommand({ StreamName: name })),
  describeKinesisStream: (name: string) =>
    kinesis.send(new DescribeStreamCommand({ StreamName: name })),

  // SSM Parameter Store
  listSsmParameters: async () =>
    (await ssm.send(new DescribeParametersCommand({}))).Parameters ?? [],
  putSsmParameter: (name: string, value: string, type: "String" | "SecureString" = "String") =>
    ssm.send(
      new PutParameterCommand({
        Name: name,
        Value: value,
        Type: type,
        Overwrite: true,
      }),
    ),
  deleteSsmParameter: (name: string) =>
    ssm.send(new DeleteParameterCommand({ Name: name })),
  getSsmParameter: (name: string) =>
    ssm.send(new GetParameterCommand({ Name: name, WithDecryption: true })),

  // EKS
  listEksClusters: async () =>
    (await eks.send(new EksListClustersCommand({}))).clusters ?? [],
  describeEksCluster: (name: string) =>
    eks.send(new EksDescribeClusterCommand({ name })),
  createEksCluster: (name: string, subnetIds: string[], securityGroupIds: string[] = []) =>
    eks.send(
      new EksCreateClusterCommand({
        name,
        roleArn: "arn:aws:iam::000000000000:role/eks-role",
        resourcesVpcConfig: { subnetIds, securityGroupIds },
        version: "1.29",
      }),
    ),
  deleteEksCluster: (name: string) =>
    eks.send(new EksDeleteClusterCommand({ name })),

  // ECS
  listEcsClusters: async () =>
    (await ecs.send(new EcsListClustersCommand({}))).clusterArns ?? [],
  describeEcsClusters: (arns: string[]) =>
    ecs.send(new EcsDescribeClustersCommand({ clusters: arns })),
  createEcsCluster: (name: string) =>
    ecs.send(new EcsCreateClusterCommand({ clusterName: name })),
  deleteEcsCluster: (cluster: string) =>
    ecs.send(new EcsDeleteClusterCommand({ cluster })),
  listEcsTaskDefinitions: async () =>
    (await ecs.send(new ListTaskDefinitionsCommand({}))).taskDefinitionArns ?? [],

  // RDS
  listDbInstances: async () =>
    (await rds.send(new DescribeDBInstancesCommand({}))).DBInstances ?? [],
  createDbInstance: (id: string, engine = "postgres", instanceClass = "db.t3.micro") =>
    rds.send(
      new CreateDBInstanceCommand({
        DBInstanceIdentifier: id,
        Engine: engine,
        DBInstanceClass: instanceClass,
        AllocatedStorage: 20,
        MasterUsername: "admin",
        MasterUserPassword: "Password1!",
      }),
    ),
  deleteDbInstance: (id: string) =>
    rds.send(
      new DeleteDBInstanceCommand({
        DBInstanceIdentifier: id,
        SkipFinalSnapshot: true,
      }),
    ),
};
