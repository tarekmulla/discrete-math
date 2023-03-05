variable "app" {
  type        = string
  description = "The application name"
}

variable "tags" {
  description = "AWS Tags to add to all resources created (where possible)"
  type        = map(string)
}

variable "api_id" {
  type        = string
  description = "The API Id"
}

variable "api_resources" {
  description = "API resources"
  type        = map(map(string))
}

variable "api_exec_arn" {
  type        = string
  description = "The arn for API execution"
}

variable "lambda_layer_arn" {
  type        = string
  description = "The Invoke ARN of the Lambda layer"
}

variable "website_domain" {
  type        = string
  description = "The primary domain name of the certificate in ACM"
}
