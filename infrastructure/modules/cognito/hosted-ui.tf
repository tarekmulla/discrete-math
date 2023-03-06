resource "aws_cognito_user_pool_ui_customization" "ui" {
  client_id = aws_cognito_user_pool_client.client.id

  css        = ".label-customizable {font-weight: 400;}"
  image_file = filebase64("../docs/images/math-logo.png")

  user_pool_id = aws_cognito_user_pool_domain.cognito_domain.user_pool_id
}
