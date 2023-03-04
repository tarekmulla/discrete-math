variable "app" {
  description = "The application name"
  type        = string
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  default     = "172.20.0.0/16"
}

variable "private_subnet_cidr" {
  description = "List of CIDR blocks for private subnets"
  default     = ["172.20.0.0/24", "172.20.1.0/24"]
}

variable "public_subnet_cidr" {
  description = "List of CIDR blocks for public subnets"
  default     = ["172.20.2.0/24", "172.20.3.0/24"]
}

variable "availability_zones" {
  description = "List of availablility zones"
  default     = ["us-east-1a", "us-east-1b"]
}
