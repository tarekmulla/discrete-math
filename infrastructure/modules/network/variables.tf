variable "app" {
  description = "The application name"
  type        = string
}

variable "region" {
  type        = string
  description = "The aws region where the resources will be provisioned"
}

variable "tags" {
  description = "AWS Tags to add to all resources created (where possible)"
  type        = map(string)
}

variable "vpc_cidr" {
  type        = string
  description = "The CIDR block for the VPC"
  default     = "172.20.0.0/16"
}

variable "private_subnet_cidr" {
  type        = list(string)
  description = "List of CIDR blocks for private subnets"
  default     = ["172.20.0.0/24", "172.20.1.0/24"]
}

variable "public_subnet_cidr" {
  type        = list(string)
  description = "List of CIDR blocks for public subnets"
  default     = ["172.20.2.0/24", "172.20.3.0/24"]
}

variable "availability_zones" {
  type        = list(string)
  description = "List of availablility zones"
}
