resource "aws_cognito_user_pool_client" "client" {
  name = "${var.app}-client"

  user_pool_id                 = aws_cognito_user_pool.user_pool.id
  supported_identity_providers = ["COGNITO"]
  callback_urls                = var.callback_urls
  logout_urls                  = var.logout_urls

  allowed_oauth_flows                  = ["code"]
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_scopes                 = ["aws.cognito.signin.user.admin", "email", "openid", "phone", "profile"]

  generate_secret               = true
  prevent_user_existence_errors = "ENABLED"
  access_token_validity         = 360 # 6 Hours
  id_token_validity             = 360 # 6 Hours
  refresh_token_validity        = 90  # 3 months
  token_validity_units {
    access_token  = "hours"
    id_token      = "hours"
    refresh_token = "days"
  }
  explicit_auth_flows = [
    "ALLOW_CUSTOM_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_USER_SRP_AUTH",
  ]
}


# Get the ACM certificate from us-east-1, required for cognito
provider "aws" {
  region = "us-east-1"
  alias  = "virginia"
}
data "aws_acm_certificate" "cognito" {
  domain      = var.website_domain
  types       = ["AMAZON_ISSUED"]
  most_recent = true
  provider    = aws.virginia
}

resource "aws_cognito_user_pool_domain" "cognito_domain" {
  domain          = var.cognito_domain
  certificate_arn = data.aws_acm_certificate.cognito.arn
  user_pool_id    = aws_cognito_user_pool.user_pool.id
}

resource "aws_route53_record" "auth-cognito-A" {
  name    = aws_cognito_user_pool_domain.cognito_domain.domain
  type    = "A"
  zone_id = var.route53_zone_id
  alias {
    evaluate_target_health = false
    name                   = aws_cognito_user_pool_domain.cognito_domain.cloudfront_distribution_arn
    # This zone_id is fixed
    zone_id = "Z2FDTNDATAQYW2"
  }
}
