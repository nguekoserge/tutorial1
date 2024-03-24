from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import provider, s3_bucket, s3_bucket_website_configuration

class StaticWebsiteStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Initialize the AWS provider with the correct region
        provider.AwsProvider(self, "Aws", region="us-west-2")  # Adjust the region as needed

        # Create an S3 bucket for the static website
        bucket = s3_bucket.S3Bucket(self, "StaticWebsiteBucket", bucket='serge2s')

        # Define the website configuration for the S3 bucket
        website_config = s3_bucket_website_configuration.S3BucketWebsiteConfiguration(self, "WebsiteConfiguration",
                                                      bucket=bucket.bucket,
                                                      index_document={"suffix": "index.html"},
                                                      error_document={"key": "error.html"}
                                                      )

        # Define Terraform outputs
        TerraformOutput(self, 'WebsiteEndpoint', value=bucket.website_endpoint)

app = App()
StaticWebsiteStack(app, "bobo")
app.synth()
