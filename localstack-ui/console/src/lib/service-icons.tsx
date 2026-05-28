import type { CSSProperties, SVGProps } from "react";
import type { CloudName } from "@/lib/skins";

const CLOUD_COLOR: Record<CloudName, string> = {
  aws: "#FF9900",
  azure: "#0078D4",
  gcp: "#4285F4",
};

type IconProps = SVGProps<SVGSVGElement> & { title?: string };

function base(props: IconProps, paths: React.ReactNode) {
  const { title, ...rest } = props;
  return (
    <svg
      viewBox="0 0 24 24"
      width={16}
      height={16}
      fill="currentColor"
      role="img"
      aria-label={title}
      {...rest}
    >
      {title && <title>{title}</title>}
      {paths}
    </svg>
  );
}

const Bucket = (p: IconProps) =>
  base(
    p,
    <>
      <path d="M4 6h16l-1.5 13a2 2 0 0 1-2 1.8H7.5a2 2 0 0 1-2-1.8L4 6z" />
      <rect x="4" y="4" width="16" height="2.5" rx="0.5" />
    </>,
  );

const Queue = (p: IconProps) =>
  base(
    p,
    <>
      <rect x="3" y="6" width="18" height="3" rx="1" />
      <rect x="3" y="10.5" width="18" height="3" rx="1" />
      <rect x="3" y="15" width="18" height="3" rx="1" />
    </>,
  );

const Table = (p: IconProps) =>
  base(
    p,
    <>
      <ellipse cx="12" cy="5.5" rx="8" ry="2.5" />
      <path d="M4 5.5v6c0 1.4 3.6 2.5 8 2.5s8-1.1 8-2.5v-6" fill="none" stroke="currentColor" strokeWidth="1.6" />
      <path d="M4 11.5v6c0 1.4 3.6 2.5 8 2.5s8-1.1 8-2.5v-6" fill="none" stroke="currentColor" strokeWidth="1.6" />
    </>,
  );

const Bolt = (p: IconProps) =>
  base(p, <path d="M13 2 4 14h6l-1 8 9-12h-6l1-8z" />);

const Bell = (p: IconProps) =>
  base(
    p,
    <path d="M12 3a6 6 0 0 0-6 6v3l-2 3h16l-2-3V9a6 6 0 0 0-6-6zM9 19a3 3 0 0 0 6 0" />,
  );

const Doc = (p: IconProps) =>
  base(
    p,
    <>
      <path d="M6 2h9l5 5v15H6z" />
      <path d="M14 2v6h6" fill="none" stroke="white" strokeWidth="1" />
    </>,
  );

const Server = (p: IconProps) =>
  base(
    p,
    <>
      <rect x="3" y="4" width="18" height="6" rx="1" />
      <rect x="3" y="14" width="18" height="6" rx="1" />
      <circle cx="6.5" cy="7" r="0.8" fill="white" />
      <circle cx="6.5" cy="17" r="0.8" fill="white" />
    </>,
  );

const Shield = (p: IconProps) =>
  base(p, <path d="M12 2 4 5v6c0 5 3.6 9.4 8 11 4.4-1.6 8-6 8-11V5l-8-3z" />);

const Key = (p: IconProps) =>
  base(
    p,
    <>
      <circle cx="8" cy="14" r="4" fill="none" stroke="currentColor" strokeWidth="2" />
      <path d="M11 12l9-9 2 2-2 2 2 2-2 2-2-2-3 3-2-2z" />
    </>,
  );

const Globe = (p: IconProps) =>
  base(
    p,
    <>
      <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" strokeWidth="1.5" />
      <path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" fill="none" stroke="currentColor" strokeWidth="1.5" />
    </>,
  );

const Group = (p: IconProps) =>
  base(
    p,
    <>
      <rect x="3" y="3" width="8" height="8" rx="1" />
      <rect x="13" y="3" width="8" height="8" rx="1" />
      <rect x="3" y="13" width="8" height="8" rx="1" />
      <rect x="13" y="13" width="8" height="8" rx="1" />
    </>,
  );

const Cube = (p: IconProps) =>
  base(
    p,
    <path d="M12 2 3 7v10l9 5 9-5V7l-9-5zm0 2.3 6.5 3.6L12 11.5 5.5 7.9 12 4.3zM5 9.4l6 3.3v7.5l-6-3.3V9.4zm14 0v7.5l-6 3.3v-7.5l6-3.3z" />,
  );

const EventGrid = (p: IconProps) =>
  base(
    p,
    <>
      <circle cx="6" cy="6" r="2" />
      <circle cx="18" cy="6" r="2" />
      <circle cx="6" cy="18" r="2" />
      <circle cx="18" cy="18" r="2" />
      <circle cx="12" cy="12" r="2" />
      <path d="M6 6l6 6m6-6l-6 6m0 0l-6 6m6-6l6 6" stroke="currentColor" strokeWidth="1" />
    </>,
  );

const Bus = (p: IconProps) =>
  base(
    p,
    <>
      <path d="M3 12h18" stroke="currentColor" strokeWidth="2" fill="none" />
      <circle cx="5" cy="12" r="2.5" />
      <circle cx="12" cy="12" r="2.5" />
      <circle cx="19" cy="12" r="2.5" />
    </>,
  );

const Run = (p: IconProps) =>
  base(p, <path d="M5 4l14 8-14 8V4z" />);

const Chart = (p: IconProps) =>
  base(
    p,
    <>
      <rect x="3" y="13" width="4" height="8" />
      <rect x="10" y="8" width="4" height="13" />
      <rect x="17" y="3" width="4" height="18" />
    </>,
  );

const Folder = (p: IconProps) =>
  base(p, <path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6z" />);

const Spark = (p: IconProps) =>
  base(p, <path d="M12 2v8M2 12h8m4 0h8M12 14v8M5 5l5 5m4 4 5 5M19 5l-5 5m-4 4-5 5" stroke="currentColor" strokeWidth="2" fill="none" />);

const ICONS: Record<string, (p: IconProps) => React.JSX.Element> = {
  // AWS
  s3: Bucket,
  sqs: Queue,
  sns: Bell,
  dynamodb: Table,
  lambda: Bolt,
  logs: Doc,
  ec2: Server,
  iam: Shield,
  secretsmanager: Key,
  kms: Key,
  cloudformation: Cube,
  ecr: Cube,
  eks: Cube,
  ecs: Cube,
  rds: Table,
  vpc: Globe,
  route53: Globe,
  apigateway: Bus,
  stepfunctions: Spark,
  events: EventGrid,
  kinesis: Spark,
  ssm: Folder,
  // Azure
  "Microsoft.Resources": Group,
  "Microsoft.Storage": Bucket,
  "Microsoft.Network": Globe,
  "Microsoft.DocumentDB": Cube,
  "Microsoft.EventGrid": EventGrid,
  "Microsoft.Web": Bolt,
  "Microsoft.KeyVault": Key,
  "Microsoft.ServiceBus": Bus,
  "Microsoft.Storage.Tables": Table,
  "Microsoft.ContainerService": Cube,
  "Microsoft.ContainerRegistry": Cube,
  "Microsoft.OperationalInsights": Chart,
  "Microsoft.Cache": Server,
  "Microsoft.Sql": Table,
  // GCP
  storage: Bucket,
  pubsub: EventGrid,
  firestore: Cube,
  functions: Bolt,
  bigquery: Chart,
  run: Run,
  secretmanager: Key,
  "gcp-iam": Shield,
  "gcp-kms": Key,
  dns: Globe,
  gke: Cube,
  container: Cube,
  "compute-networks": Globe,
  compute: Server,
  sqladmin: Table,
  spanner: Table,
  monitoring: Chart,
  cloudscheduler: Bell,
  // generic
  cloud: Globe,
  folder: Folder,
  spark: Spark,
};

// Official provider brand marks (Simple Icons, CC0).
// 24x24 viewBox, single path each, colored via CSS currentColor.
const BRAND_PATHS: Record<CloudName, string> = {
  aws: "M6.763 10.036c0 .296.032.535.088.71.064.176.144.368.256.576.04.063.056.127.056.183 0 .08-.048.16-.152.24l-.503.335a.383.383 0 0 1-.208.072c-.08 0-.16-.04-.239-.112a2.47 2.47 0 0 1-.287-.375 6.18 6.18 0 0 1-.248-.471c-.622.734-1.405 1.101-2.347 1.101-.67 0-1.205-.191-1.596-.574-.391-.384-.59-.894-.59-1.533 0-.678.239-1.23.726-1.644.487-.415 1.133-.623 1.955-.623.272 0 .551.024.846.064.296.04.6.104.918.176v-.583c0-.607-.127-1.03-.375-1.277-.255-.248-.686-.367-1.3-.367-.279 0-.566.031-.86.103-.295.072-.583.16-.862.272a2.287 2.287 0 0 1-.28.104.488.488 0 0 1-.127.023c-.112 0-.168-.08-.168-.247v-.391c0-.128.016-.224.056-.28a.597.597 0 0 1 .224-.167c.279-.144.614-.264 1.005-.36.39-.103.806-.151 1.245-.151.95 0 1.644.216 2.091.647.439.43.662 1.085.662 1.963v2.586zm-3.24 1.214c.263 0 .534-.048.822-.144.287-.096.543-.271.758-.51.128-.152.224-.32.272-.512.047-.191.08-.423.08-.694v-.335a6.66 6.66 0 0 0-.735-.136 6.02 6.02 0 0 0-.75-.048c-.535 0-.926.104-1.19.32-.263.215-.39.518-.39.917 0 .375.095.655.296.846.191.2.47.296.838.296zm6.41.862c-.144 0-.24-.024-.304-.08-.064-.048-.12-.16-.168-.311L7.586 5.55a1.398 1.398 0 0 1-.072-.32c0-.128.064-.2.191-.2h.783c.151 0 .255.025.31.08.065.048.113.16.16.312l1.342 5.284 1.245-5.284c.04-.16.088-.264.151-.312a.549.549 0 0 1 .32-.08h.638c.152 0 .256.025.32.08.063.048.12.16.151.312l1.261 5.348 1.381-5.348c.048-.16.104-.264.16-.312a.52.52 0 0 1 .311-.08h.743c.127 0 .2.065.2.2 0 .04-.009.08-.017.128a1.137 1.137 0 0 1-.056.2l-1.923 6.17c-.048.16-.104.263-.168.311a.51.51 0 0 1-.303.08h-.687c-.151 0-.255-.024-.32-.08-.063-.056-.119-.16-.15-.32l-1.238-5.148-1.23 5.14c-.04.16-.087.264-.15.32-.065.056-.177.08-.32.08zm10.256.215c-.415 0-.83-.048-1.229-.143-.399-.096-.71-.2-.918-.32-.128-.071-.215-.151-.247-.223a.563.563 0 0 1-.048-.224v-.407c0-.167.064-.247.183-.247.048 0 .096.008.144.024.048.016.12.048.2.08.271.12.566.215.878.279.319.064.63.096.95.096.502 0 .894-.088 1.165-.264a.86.86 0 0 0 .415-.758.777.777 0 0 0-.215-.559c-.144-.151-.416-.287-.807-.415l-1.157-.36c-.583-.183-1.014-.454-1.277-.813a1.902 1.902 0 0 1-.4-1.158c0-.335.073-.63.216-.886.144-.255.335-.479.575-.654.24-.184.51-.32.83-.415.32-.096.655-.136 1.006-.136.175 0 .359.008.535.032.183.024.35.056.518.088.16.04.312.08.455.127.144.048.256.096.336.144a.69.69 0 0 1 .24.2.43.43 0 0 1 .071.263v.375c0 .168-.064.256-.184.256a.83.83 0 0 1-.303-.096 3.652 3.652 0 0 0-1.532-.311c-.455 0-.815.071-1.062.223-.248.152-.375.383-.375.71 0 .224.08.416.24.567.159.152.454.304.877.44l1.134.358c.574.184.99.44 1.237.767.247.327.367.702.367 1.117 0 .343-.072.655-.207.926-.144.272-.336.511-.583.703-.248.2-.543.343-.886.447-.36.111-.734.167-1.142.167zM21.698 16.207c-2.626 1.94-6.442 2.969-9.722 2.969-4.598 0-8.74-1.7-11.87-4.526-.247-.223-.024-.527.27-.351 3.384 1.963 7.559 3.153 11.877 3.153 2.914 0 6.114-.607 9.06-1.852.439-.2.814.287.385.607zm1.094-1.252c-.336-.43-2.22-.207-3.074-.103-.255.032-.295-.192-.063-.36 1.5-1.053 3.967-.75 4.254-.399.287.36-.08 2.826-1.485 4.007-.215.184-.423.088-.327-.151.32-.79 1.03-2.57.694-2.994z",
  azure: "M5.483 21.3H24L14.025 4.054l-5.481 9.43 6.43 7.633L5.482 21.3zM7.214 13.65L0 21.299h13.43L7.213 13.65z",
  gcp: "M12.19 2.38a9.344 9.344 0 0 1 9.234 6.893c-.053-.02.055.013 0 0 3.875 2.551 3.922 8.11.7 10.916l-.007-.006.007.006a6.49 6.49 0 0 1-4.388 1.6h-5.252l-.004.005H7.07a7.071 7.071 0 0 1-7.20-4.85 7.038 7.038 0 0 1 2.911-7.694 9.359 9.359 0 0 1 9.6-6.87z",
};

function CloudBrandIcon({
  cloud,
  className,
  style,
}: {
  cloud: CloudName;
  className?: string;
  style?: CSSProperties;
}) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="currentColor"
      role="img"
      aria-label={cloud}
      className={className}
      style={{ width: 16, height: 16, color: CLOUD_COLOR[cloud], flexShrink: 0, ...style }}
    >
      <path d={BRAND_PATHS[cloud]} />
    </svg>
  );
}

export function ServiceIcon({
  id,
  cloud,
  className,
  style,
}: {
  id: string;
  cloud: CloudName;
  className?: string;
  style?: CSSProperties;
}) {
  if (id === "cloud") {
    return <CloudBrandIcon cloud={cloud} className={className} style={style} />;
  }
  const Cmp = ICONS[id] ?? Globe;
  return (
    <Cmp
      title={id}
      className={className}
      style={{ color: CLOUD_COLOR[cloud], flexShrink: 0, ...style }}
    />
  );
}

export const CLOUD_BRAND_COLOR = CLOUD_COLOR;
