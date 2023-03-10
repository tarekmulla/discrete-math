output "method_id" {
  value = aws_api_gateway_method.gcd.id
}

output "integration_id" {
  value = aws_api_gateway_integration.gcd_lambda_integration.id
}
