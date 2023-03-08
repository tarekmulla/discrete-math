# create a list of tag to be added to all resources (identify resources related to this question)
locals {
  bucket_name         = data.aws_ssm_parameter.bucket_name.value
  route53_zone_id     = data.aws_ssm_parameter.zone_id.value
  certificate_arn     = data.aws_acm_certificate.domains.arn
  website_domain      = data.aws_ssm_parameter.website_domain.value
  api_endpoint        = "api.${local.website_domain}"
  cognito_domain      = "cognito.${local.website_domain}"
  container_image     = data.aws_ssm_parameter.ecr_image.value
  vpc_id              = data.aws_ssm_parameter.vpc_id.value
  vpc_private_subnets = split(",", replace(replace(replace(data.aws_ssm_parameter.vpc_private_subnets.value, "[", ""), "]", ""), "\"", ""))
  vpc_public_subnets  = split(",", replace(replace(replace(data.aws_ssm_parameter.vpc_public_subnets.value, "[", ""), "]", ""), "\"", ""))
  callback_url        = "https://${local.website_domain}/login"
  logout_url          = "https://${local.website_domain}"
  local_callback_url  = "http://localhost/login"
  local_logout_url    = "http://localhost"

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

# retrive all ssm parameters related to this app
data "aws_ssm_parameter" "zone_id" {
  name = "/${var.app}/zone_id"
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
data "aws_ssm_parameter" "bucket_name" {
  name = "/${var.app}/bucket_name"
}
