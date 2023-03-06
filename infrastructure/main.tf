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
  website_domain   = local.website_domain
  api_domain       = local.api_endpoint
  certificate_arn  = local.certificate_arn
  route53_zone_id  = local.route53_zone_id
  cognito_arn      = module.cognito.arn
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
  parameters = {
    api_endpoint          = local.api_endpoint
    cognito_domain        = local.cognito_domain
    logout_urls           = jsonencode(local.logout_urls)
    callback_urls         = jsonencode(local.callback_urls)
    cognito_client_id     = module.cognito.client_id
    cognito_client_secret = module.cognito.client_secret
  }
  tags = local.tags
}

module "cognito" {
  source                  = "./modules/cognito"
  app                     = var.app
  cognito_certificate_arn = var.cognito_certificate_arn
  route53_zone_id         = local.route53_zone_id
  cognito_domain          = local.cognito_domain
  logout_urls             = local.logout_urls
  callback_urls           = local.callback_urls
  tags                    = var.tags
}
