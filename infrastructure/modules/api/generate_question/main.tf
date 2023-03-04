resource "aws_api_gateway_method" "generate_question" {
  rest_api_id   = var.api_id
  resource_id   = var.resource_id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "generate_question_lambda_integration" {
  rest_api_id = var.api_id
  resource_id = aws_api_gateway_method.generate_question.resource_id
  http_method = aws_api_gateway_method.generate_question.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = module.generate_question_lambda.lambda_function_invoke_arn
}
