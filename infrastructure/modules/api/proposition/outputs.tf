output "method_id" {
  value = aws_api_gateway_method.proposition.id
}

output "integration_id" {
  value = aws_api_gateway_integration.proposition_lambda_integration.id
}
