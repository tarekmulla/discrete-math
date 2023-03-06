variable "app" {
  type        = string
  description = "The application name"
  default     = "discrete-math"
}

variable "region" {
  type        = string
  description = "The aws region where the resources will be provisioned"
  default     = "ap-southeast-2"
}

# A map of the extra tags to apply to aws resources.
# there is already list of tags will be added by default, please
# check locals "tags"
variable "tags" {
  type        = map(string)
  description = "AWS Tags to add to all resources created (where possible)"
  default     = {}
}

variable "route53_domain" {
  type        = string
  description = "The route53 domain name where all dns records will be stored"
  default     = "rmit.mulla.au"
}

variable "cognito_certificate_arn" {
  type        = string
  description = "The arn for cognito acm certificate in us-east-1 region"
  default     = "arn:aws:acm:us-east-1:776372263299:certificate/4324c70f-4038-4679-9f5f-f42964d6e539"
}
