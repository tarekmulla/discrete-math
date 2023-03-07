module "cors_lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.0.1"

  function_name = "${var.app}-cors"
  description   = "lambda function to generate empty response for options method"
  handler       = "index.lambda_handler"
  runtime       = "python3.9"
  source_path   = "${path.module}/index.py"

  layers = [var.lambda_layer_arn]

  cloudwatch_logs_retention_in_days = 14

  environment_variables = {
    APP        = var.app,
    WEB_DOMAIN = var.website_domain
  }

  tags = var.tags
}
