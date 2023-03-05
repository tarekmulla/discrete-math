variable "app" {
  type        = string
  description = "The application name"
}

variable "tags" {
  description = "AWS Tags to add to all resources created (where possible)"
  type        = map(string)
}

variable "api_stage_arn" {
  type        = string
  description = "The API stage ARN to apply the web ACL to it"
}
