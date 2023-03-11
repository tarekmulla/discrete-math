# Create deployment if any change detected in methods or API
resource "aws_api_gateway_deployment" "api_deploy" {
  depends_on = [
    aws_api_gateway_account.api_cloudwatch_role,
    module.generate_question
  ]

  rest_api_id = aws_api_gateway_rest_api.api.id

  triggers = {
    redeployment = sha1(jsonencode(concat([
      aws_api_gateway_resource.question.id,
      aws_api_gateway_resource.module.id,
      aws_api_gateway_resource.gcd.id,
      aws_api_gateway_resource.factors.id,
      aws_api_gateway_resource.proposition.id,
      module.generate_question.method_id,
      module.generate_question.integration_id,
      module.gcd.method_id,
      module.gcd.integration_id,
      module.factors.method_id,
      module.factors.integration_id,
      module.proposition.method_id,
      module.proposition.integration_id,
      aws_api_gateway_authorizer.cognito_authorizer.id
      ],
      module.cors_options.cors_method_ids,
      module.cors_options.cors_integration_ids
    )))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "apigw_stage" {
  deployment_id = aws_api_gateway_deployment.api_deploy.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
  stage_name    = "demo"
}
