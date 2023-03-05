resource "aws_wafv2_web_acl" "web_acl" {
  name        = "${var.app}-acl"
  description = "AWS Managed Rules for WAF"
  scope       = "REGIONAL"

  default_action {
    allow {}
  }

  # General rules, including those listed in OWASP, CVE, etc.
  rule {
    name     = "${var.app}-rule-common"
    priority = 1

    override_action {
      count {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${var.app}-rule-common-metric"
      sampled_requests_enabled   = true
    }
  }

  # Inspects IPs that have been identified as bots by Amazon threat intelligence
  rule {
    name     = "${var.app}-rule-ip-reputation"
    priority = 2

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesAmazonIpReputationList"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${var.app}-rule-ip-reputation-metric"
      sampled_requests_enabled   = true
    }
  }

  # Inspects for a list of IPs known to anonymize client information (TOR nodes, temporary proxies, etc.)
  rule {
    name     = "${var.app}-rule-anonymous-ip"
    priority = 3

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesAnonymousIpList"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${var.app}-rule-anonymous-ip-metric"
      sampled_requests_enabled   = true
    }
  }

  # block request patterns associated with exploitation of SQL databases, like SQL injection
  rule {
    name     = "${var.app}-rule-sql-rule-set"
    priority = 4

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesSQLiRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${var.app}-rule-sql-rule-set-metric"
      sampled_requests_enabled   = true
    }
  }

  tags     = var.tags
  tags_all = var.tags

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "${var.app}-web-acl"
    sampled_requests_enabled   = true
  }
}

resource "aws_wafv2_web_acl_association" "waf_api" {
  resource_arn = var.api_stage_arn
  web_acl_arn  = aws_wafv2_web_acl.web_acl.arn
}
