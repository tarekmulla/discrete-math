provider "aws" {
  region = var.region
}

# the lambda layer that containes the shared methods between lambda functions
module "lambda_layers" {
  source      = "./modules/lambda_layers"
  app         = var.app
  region      = var.region
  bucket_name = local.bucket_name
  tags        = local.tags
}

# The API and its methods
module "question_api" {
  source            = "./modules/api"
  app               = var.app
  region            = var.region
  lambda_layer_arns = module.lambda_layers.layer_arns
  website_domain    = local.website_domain
  api_domain        = local.api_endpoint
  certificate_arn   = local.certificate_arn
  route53_zone_id   = local.route53_zone_id
  cognito_arn       = module.cognito.arn
  bucket_name       = local.bucket_name
  tags              = local.tags
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
    website_domain        = local.website_domain
    logout_url            = local.logout_url
    callback_url          = local.callback_url
    cognito_client_id     = module.cognito.client_id
    cognito_client_secret = module.cognito.client_secret
  }
  tags = local.tags
}

module "cognito" {
  source          = "./modules/cognito"
  app             = var.app
  route53_zone_id = local.route53_zone_id
  website_domain  = local.website_domain
  cognito_domain  = local.cognito_domain
  logout_urls     = [local.logout_url, local.local_logout_url]
  callback_urls   = [local.callback_url, local_callback_url]
  tags            = var.tags
}
