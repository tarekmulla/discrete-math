output "method_id" {
  value = aws_api_gateway_method.factors.id
}

output "integration_id" {
  value = aws_api_gateway_integration.factors_lambda_integration.id
}
