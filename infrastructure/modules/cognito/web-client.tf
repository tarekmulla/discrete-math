
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
  refresh_token_validity        = 60
  access_token_validity         = 5
  id_token_validity             = 5
  token_validity_units {
    access_token  = "minutes"
    id_token      = "minutes"
    refresh_token = "days"
  }
}

resource "aws_cognito_user_pool_domain" "cognito_domain" {
  domain          = var.cognito_domain
  certificate_arn = var.cognito_certificate_arn
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
