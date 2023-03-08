output "layer_arns" {
  description = "The Invoke ARNs of the Lambda layers"
  value       = concat([for k, v in module.lambda_layer : v.lambda_layer_arn], [module.pandas_layer.lambda_layer_arn])
}
