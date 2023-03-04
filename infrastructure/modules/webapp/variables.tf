variable "app" {
  type        = string
  description = "The application name"
}

variable "region" {
  type        = string
  description = "The aws region where the resources will be provisioned"
}

variable "tags" {
  description = "AWS Tags to add to all resources created (where possible)"
  type        = map(string)
}

variable "vpc_id" {
  type        = string
  description = "VPC ID for the network"
}

variable "public_subnet_ids" {
  type        = list(string)
  description = "VPC - Public Subnet ID"
}

variable "private_subnet_ids" {
  type        = list(string)
  description = "VPC - Private Subnet ID"
}

variable "container_port" {
  type        = number
  description = "Container port"
  default     = 80
}

variable "container_image" {
  type        = string
  description = "The url for the docker image"
}

variable "domain_name" {
  type        = string
  description = "The primary domain name of the certificate in ACM"
}

variable "ecs_tasks_count" {
  type        = number
  description = "The desired number of ECS tasks"
  default     = 1
}
