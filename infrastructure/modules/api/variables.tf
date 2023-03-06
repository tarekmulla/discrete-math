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

variable "website_domain" {
  type        = string
  description = "The primary domain name of the certificate in ACM"
}

variable "api_domain" {
  type        = string
  description = "The domain name for the api"
}

variable "certificate_arn" {
  type        = string
  description = "The arn for the acm certificate for the app domain"
}

variable "route53_zone_id" {
  type        = string
  description = "The route53 zone ID for all applications"
}

variable "cognito_arn" {
  type        = string
  description = "The cognito user pool arn"
}
