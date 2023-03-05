# create a list of tag to be added to all resources (identify resources related to this question)
locals {
  route53_zone_id     = data.aws_route53_zone.apps.id
  certificate_arn     = data.aws_acm_certificate.domains.arn
  website_domain      = data.aws_ssm_parameter.website_domain.value
  api_endpoint        = data.aws_ssm_parameter.api_endpoint.value
  container_image     = data.aws_ssm_parameter.ecr_image.value
  vpc_id              = data.aws_ssm_parameter.vpc_id.value
  vpc_private_subnets = split(",", replace(replace(replace(data.aws_ssm_parameter.vpc_private_subnets.value, "[", ""), "]", ""), "\"", ""))
  vpc_public_subnets  = split(",", replace(replace(replace(data.aws_ssm_parameter.vpc_public_subnets.value, "[", ""), "]", ""), "\"", ""))

  tags = merge({
    Name        = "${var.app}"
    Application = var.app
  }, var.tags)
}

# Get the HTTPS certificate for the website and API
data "aws_acm_certificate" "domains" {
  domain      = local.website_domain
  types       = ["AMAZON_ISSUED"]
  most_recent = true
}

# Route53 zone for all DNS records
data "aws_route53_zone" "apps" {
  name = var.route53_domain
}

# retrive all ssm parameters related to this app
data "aws_ssm_parameter" "api_endpoint" {
  name = "/${var.app}/api_endpoint"
}
data "aws_ssm_parameter" "ecr_image" {
  name = "/${var.app}/ecr_image"
}
data "aws_ssm_parameter" "vpc_id" {
  name = "/${var.app}/vpc_id"
}
data "aws_ssm_parameter" "vpc_private_subnets" {
  name = "/${var.app}/vpc_private_subnets"
}
data "aws_ssm_parameter" "vpc_public_subnets" {
  name = "/${var.app}/vpc_public_subnets"
}
data "aws_ssm_parameter" "website_domain" {
  name = "/${var.app}/website_domain"
}
