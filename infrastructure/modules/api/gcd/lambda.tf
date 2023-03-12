locals {
  function_name = "gcd"
  zip_path      = "${path.root}/../.tmp/${local.function_name}.zip"
}

data "archive_file" "lambda_source_package" {
  type        = "zip"
  source_dir  = "${path.module}/src/"
  output_path = local.zip_path
}

resource "aws_s3_object" "lambda_code_zip" {
  bucket = var.bucket_name
  key    = "lambda_zip/function/${local.function_name}"
  source = local.zip_path
  etag   = data.archive_file.lambda_source_package.output_md5
}

module "gcd_lambda" {
  depends_on = [aws_s3_object.lambda_code_zip]
  source     = "terraform-aws-modules/lambda/aws"
  version    = "4.0.1"

  function_name  = "${var.app}-gcd"
  description    = "lambda function to do gcd operations"
  handler        = "index.lambda_handler"
  runtime        = "python3.9"
  create_package = false
  s3_existing_package = {
    bucket     = var.bucket_name
    key        = aws_s3_object.lambda_code_zip.id
    version_id = aws_s3_object.lambda_code_zip.version_id
  }

  layers = var.lambda_layer_arns

  cloudwatch_logs_retention_in_days = 14

  environment_variables = {
    APP        = var.app,
    WEB_DOMAIN = var.website_domain
  }

  tags = var.tags
}
