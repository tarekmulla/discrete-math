# Adding OPTIONS method for resource to allow call API from external origins
resource "aws_api_gateway_method" "options_method" {
  for_each      = var.api_resources
  rest_api_id   = var.api_id
  resource_id   = each.value.id
  http_method   = "OPTIONS"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "options_integration" {
  for_each    = var.api_resources
  rest_api_id = var.api_id
  resource_id = each.value.id
  http_method = aws_api_gateway_method.options_method[each.key].http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = module.cors_lambda.lambda_function_invoke_arn

  depends_on = [aws_api_gateway_method.options_method]
}
