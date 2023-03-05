output "cors_method_ids" {
  value = [for k, v in aws_api_gateway_method.options_method : v.id]
}

output "cors_integration_ids" {
  value = [for k, v in aws_api_gateway_integration.options_integration : v.id]
}
