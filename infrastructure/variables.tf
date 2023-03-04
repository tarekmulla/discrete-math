variable "app" {
  type        = string
  description = "The application name"
  default     = "discrete-math"
}

# A map of the extra tags to apply to aws resources.
# there is already list of tags will be added by default, please
# check locals "tags"
variable "tags" {
  description = "AWS Tags to add to all resources created (where possible)"
  type        = map(string)
  default     = {}
}

variable "region" {
  type        = string
  description = "The aws region where the resources will be provisioned"
  default     = "ap-southeast-2"
}

variable "domain_name" {
  type        = string
  description = "The domain name for the application"
}

variable "certificate_arn" {
  type        = string
  description = "The arn for the acm certificate for the app domain"
}

variable "container_image" {
  type        = string
  description = "The url for the docker image"
}
