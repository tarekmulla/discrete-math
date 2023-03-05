# Lambda layer to share methods betwen all lambda functions

module "lambda_layer" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.0.1"

  create_layer = true

  layer_name          = "${var.app}-layer"
  description         = "A layer for all shared methods between lambda functions"
  compatible_runtimes = ["python3.8"]
  create_package      = false
  # get the package (source code) from archive_file block output (the zip file)
  local_existing_package = data.archive_file.layer_archive.output_path

  cloudwatch_logs_retention_in_days = 14

  environment_variables = {
    APP = var.app
  }

  tags = var.tags
}

# Zip the source code so lambda layer use it, the zip should follow specific structure, check aws documentation
data "archive_file" "layer_archive" {
  type = "zip"
  excludes = [
    "__pycache__",
    "venv",
  ]
  source_dir  = "${path.module}/source_code"
  output_path = "${path.module}/source_code.zip"
}
