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

variable "lambda_layer_arn" {
  type        = string
  description = "The Invoke ARN of the Lambda layer"
}

variable "domain_name" {
  type        = string
  description = "The domain name for the app"
}

variable "certificate_arn" {
  type        = string
  description = "The arn for the acm certificate for the app domain"
}
