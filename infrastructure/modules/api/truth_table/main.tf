resource "aws_api_gateway_method" "truth_table" {
  rest_api_id   = var.api_id
  resource_id   = var.resource_id
  http_method   = "GET"
  authorization = "COGNITO_USER_POOLS"
  authorization_scopes = [
    "email",
    "aws.cognito.signin.user.admin"
  ]
  authorizer_id = var.authorizer_id
}

resource "aws_api_gateway_integration" "truth_table_lambda_integration" {
  rest_api_id = var.api_id
  resource_id = aws_api_gateway_method.truth_table.resource_id
  http_method = aws_api_gateway_method.truth_table.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = module.truth_table_lambda.lambda_function_invoke_arn
}
