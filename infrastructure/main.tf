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
  domain_name      = var.domain_name
  certificate_arn  = var.certificate_arn
  tags             = local.tags
}

module "webapp" {
  source             = "./modules/webapp"
  app                = var.app
  region             = var.region
  vpc_id             = var.vpc_id
  public_subnet_ids  = var.vpc_public_subnets
  private_subnet_ids = var.vpc_private_subnets
  domain_name        = var.domain_name
  container_image    = var.container_image
  tags               = local.tags
}
