resource "aws_lambda_permission" "lambda_permession" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = module.factors_lambda.lambda_function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${var.api_exec_arn}/*/*"
}
