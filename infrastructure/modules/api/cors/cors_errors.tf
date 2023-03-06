# Support CORS for all possible errors in the API (4xx, 5xx)
locals {
  response_map = {
    ACCESS_DENIED                  = 403
    API_CONFIGURATION_ERROR        = 500
    AUTHORIZER_CONFIGURATION_ERROR = 500
    AUTHORIZER_FAILURE             = 500
    BAD_REQUEST_PARAMETERS         = 400
    BAD_REQUEST_BODY               = 400
    DEFAULT_4XX                    = null
    DEFAULT_5XX                    = null
    EXPIRED_TOKEN                  = 403
    INTEGRATION_FAILURE            = 504
    INTEGRATION_TIMEOUT            = 504
    INVALID_API_KEY                = 403
    INVALID_SIGNATURE              = 403
    MISSING_AUTHENTICATION_TOKEN   = 403
    QUOTA_EXCEEDED                 = 429
    REQUEST_TOO_LARGE              = 413
    RESOURCE_NOT_FOUND             = 404
    THROTTLED                      = 429
    UNAUTHORIZED                   = 401
    UNSUPPORTED_MEDIA_TYPE         = 415
    WAF_FILTERED                   = 403
  }
}

resource "aws_api_gateway_gateway_response" "cors" {
  for_each      = local.response_map
  rest_api_id   = var.api_id
  response_type = each.key
  status_code   = each.value

  response_templates = {
    "application/json" = "{\"message\": $context.error.messageString}"
  }

  response_parameters = {
    "gatewayresponse.header.Access-Control-Allow-Origin"      = "'*'" // allow all origins for errors
    "gatewayresponse.header.Access-Control-Allow-Headers"     = "'Content-Type,Authorization'"
    "gatewayresponse.header.Access-Control-Allow-Methods"     = "'OPTIONS,PUT,POST,GET'"
    "gatewayresponse.header.Access-Control-Allow-Credentials" = "'true'"
  }
}
