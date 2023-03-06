variable "app" {
  type        = string
  description = "The application name"
}

variable "tags" {
  type        = map(string)
  description = "AWS Tags to add to all resources created (where possible)"
}

variable "cognito_domain" {
  type        = string
  description = "The url for cognito user pool client"
}

variable "callback_urls" {
  type        = list(string)
  description = "cognito callback urls"
}

variable "logout_urls" {
  type        = list(string)
  description = "cognito logout urls"
}

variable "cognito_certificate_arn" {
  type        = string
  description = "The arn for the acm certificate for cognito"
}

variable "route53_zone_id" {
  type        = string
  description = "The route53 zone ID for all applications"
}
