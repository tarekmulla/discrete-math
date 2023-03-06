variable "app" {
  type        = string
  description = "The application name"
}

variable "tags" {
  type        = map(string)
  description = "AWS Tags to add to all resources created (where possible)"
}

variable "region" {
  type        = string
  description = "The aws region where the resources will be provisioned"
}
