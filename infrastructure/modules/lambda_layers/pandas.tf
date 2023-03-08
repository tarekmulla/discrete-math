data "aws_s3_object" "pandas_zip" {
  bucket = var.bucket_name
  key    = "lambda_zip/layer/pandas_layer.zip"
}

# Lambda layer for pandas python library
module "pandas_layer" {
  source              = "terraform-aws-modules/lambda/aws"
  version             = "4.0.1"
  create_layer        = true
  layer_name          = "${var.app}-pandas"
  description         = "A layer for pandas python library"
  compatible_runtimes = ["python3.9"]
  create_package      = false
  s3_existing_package = {
    bucket     = data.aws_s3_object.pandas_zip.bucket
    key        = data.aws_s3_object.pandas_zip.key
    version_id = data.aws_s3_object.pandas_zip.version_id
  }
  tags = var.tags
}
