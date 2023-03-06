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
