output "arn" {
  description = "The ARN of the expenses dynamodb table"
  value       = aws_dynamodb_table.quiz.arn
}

output "info" {
  description = "The expenses dynamodb table information"
  value       = local.quizzes_table
}
