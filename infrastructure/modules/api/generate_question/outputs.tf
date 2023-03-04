output "method_id" {
  value = aws_api_gateway_method.generate_question.id
}

output "integration_id" {
  value = aws_api_gateway_integration.generate_question_lambda_integration.id
}
