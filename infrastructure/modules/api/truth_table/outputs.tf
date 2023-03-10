output "method_id" {
  value = aws_api_gateway_method.truth_table.id
}

output "integration_id" {
  value = aws_api_gateway_integration.truth_table_lambda_integration.id
}
