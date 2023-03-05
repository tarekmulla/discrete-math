provider "aws" {
  region = var.region
}

# the lambda layer that containes the shared methods between lambda functions
module "lambda_layer" {
  source = "./modules/lambda_layer"
  app    = var.app
  region = var.region
  tags   = local.tags
}

# The API and its methods
module "question_api" {
  source           = "./modules/api"
  app              = var.app
  region           = var.region
  lambda_layer_arn = module.lambda_layer.layer_arn
  api_domain       = local.api_endpoint
  certificate_arn  = local.certificate_arn
  route53_zone_id  = local.route53_zone_id
  tags             = local.tags
}

module "webapp" {
  source             = "./modules/webapp"
  app                = var.app
  region             = var.region
  vpc_id             = local.vpc_id
  public_subnet_ids  = local.vpc_public_subnets
  private_subnet_ids = local.vpc_private_subnets
  website_domain     = local.website_domain
  container_image    = local.container_image
  certificate_arn    = local.certificate_arn
  route53_zone_id    = local.route53_zone_id
  tags               = local.tags
}
