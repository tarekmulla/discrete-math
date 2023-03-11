locals {
  layers = {
    utility_zip_file = {
      name        = "utility"
      source      = "${path.module}/utility"
      zip         = "${path.root}/../.tmp/utility_layer.zip",
      description = "A lambda layer for utility methods shared with all lambda functions"
    }
  }
}

# Zip the source code so lambda layer use it, the zip should follow specific structure, check aws documentation
data "archive_file" "layer_archive" {
  for_each    = local.layers
  type        = "zip"
  source_dir  = each.value["source"]
  output_path = each.value["zip"]
}

resource "aws_s3_object" "lambda_code_zip" {
  for_each = local.layers
  bucket   = var.bucket_name
  key      = "lambda_zip/layer/${each.key}"
  source   = data.archive_file.layer_archive[each.key].output_path
  etag     = filemd5(data.archive_file.layer_archive[each.key].output_path)
}

# Lambda layer to share methods betwen all lambda functions
module "lambda_layer" {
  depends_on = [
    data.archive_file.layer_archive
  ]
  for_each = local.layers
  source   = "terraform-aws-modules/lambda/aws"
  version  = "4.0.1"

  create_layer = true

  layer_name          = "${var.app}-${each.value["name"]}"
  description         = each.value["description"]
  compatible_runtimes = ["python3.9"]
  create_package      = false
  s3_existing_package = {
    bucket     = var.bucket_name
    key        = aws_s3_object.lambda_code_zip[each.key].id
    version_id = aws_s3_object.lambda_code_zip[each.key].version_id
  }

  cloudwatch_logs_retention_in_days = 14

  environment_variables = {
    APP = var.app
  }

  tags = var.tags
}
