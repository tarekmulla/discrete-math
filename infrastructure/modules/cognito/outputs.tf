output "arn" {
  description = "The ARN of the cognito user pool"
  value       = aws_cognito_user_pool.user_pool.arn
}

output "id" {
  description = "The id of the cognito user pool"
  value       = aws_cognito_user_pool.user_pool.id
}

output "client_id" {
  description = "The id of the cognito user pool client"
  value       = aws_cognito_user_pool_client.client.id
}

output "client_secret" {
  description = "The client secret of the cognito user pool"
  value       = aws_cognito_user_pool_client.client.client_secret
}
