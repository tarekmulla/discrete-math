# Create deployment if any change detected in methods or API
resource "aws_api_gateway_deployment" "api_deploy" {
  depends_on = [
    aws_api_gateway_account.api_cloudwatch_role,
    module.generate_question
  ]

  rest_api_id = aws_api_gateway_rest_api.api.id

  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.question.id,
      module.generate_question.method_id,
      module.generate_question.integration_id
    ]))
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
