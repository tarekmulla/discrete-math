variable "app" {
  type        = string
  description = "The application name"
}

variable "tags" {
  description = "AWS Tags to add to all resources created (where possible)"
  type        = map(string)
}

variable "region" {
  type        = string
  description = "The aws region where the resources will be provisioned"
}

variable "api_id" {
  type        = string
  description = "The API Id"
}

variable "resource_id" {
  type        = string
  description = "The container resource Id"
}

variable "api_exec_arn" {
  type        = string
  description = "The arn for API execution"
}

variable "lambda_layer_arn" {
  type        = string
  description = "The Invoke ARN of the Lambda layer"
}
