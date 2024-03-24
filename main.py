from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import provider, s3_bucket, s3_bucket_object

class StaticWebsiteStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Initialize the AWS provider with the correct region
        provider.AwsProvider(self, "Aws", region="us-west-2")  # Adjust the region as needed

        # Create an S3 bucket for the static website
        bucket = s3_bucket.S3Bucket(self, "StaticWebsiteBucket", bucket='serge2s')

        # Upload a local file to the S3 bucket
        s3_bucket_object.S3BucketObject(self, 'indexhtml', bucket=bucket.bucket, key='index.html', source ='index.html')

        # Define Terraform outputs
        TerraformOutput(self, 'WebsiteEndpoint', value=bucket.website_endpoint)

app = App()
StaticWebsiteStack(app, "bobo")
app.synth()
