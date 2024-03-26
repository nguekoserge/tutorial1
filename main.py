from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import s3_bucket, s3_bucket_website_configuration
from cdktf_cdktf_provider_aws.provider import AwsProvider

class WebsiteStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # Define the AWS provider
        aws_provider = AwsProvider(self, 'aws', region='us-west-2')

        # Create an S3 bucket for the static website
        bucket = s3_bucket.S3Bucket(self, "StaticWebsiteBucket", bucket='joanbb', provider=aws_provider)

        # Define the website configuration for the S3 bucket
        website_config = s3_bucket_website_configuration.S3BucketWebsiteConfiguration(self, "WebsiteConfiguration",
                                                      bucket=bucket.bucket,
                                                      index_document={"suffix": "index.html"},
                                                      error_document={"key": "error.html"},
                                                      routing_rules=None,
                                                      provider=aws_provider
                                                      )

        # Define Terraform outputs
        TerraformOutput(self, 'WebsiteEndpoint', value=bucket.website_endpoint)

# Instantiate the app
app = App()

# Instantiate the stack
WebsiteStack(app, "bobo")

# Synthesize the app
app.synth()
