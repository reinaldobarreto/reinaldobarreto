const repo = "reinaldobarreto";

const nextConfig = {
  output: "export",
  trailingSlash: true,
  basePath: `/${repo}`,
  assetPrefix: `/${repo}/`,
  images: {
    unoptimized: true
  }
};

export default nextConfig;

