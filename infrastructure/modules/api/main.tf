resource "aws_api_gateway_rest_api" "api" {
  name        = "${var.app}"
  description = "The questions generator API"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_resource" "question" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "question"
}

# Each method has a separate module block

module "generate_question" {
  source           = "./generate_question"
  app              = var.app
  region           = var.region
  api_id           = aws_api_gateway_rest_api.api.id
  resource_id      = aws_api_gateway_resource.question.id
  api_exec_arn     = aws_api_gateway_rest_api.api.execution_arn
  lambda_layer_arn = var.lambda_layer_arn
  tags             = var.tags
}