output "layer_arn" {
  description = "The Invoke ARN of the Lambda layer"
  value       = module.lambda_layer.lambda_layer_arn
}
