data "aws_route53_zone" "this" {
  name = var.domain_name
}

# Add an IPv4 DNS record pointing to the loab balancer
resource "aws_route53_record" "ipv4" {
  zone_id = data.aws_route53_zone.this.zone_id
  name    = local.webapp_domain
  type    = "A"

  alias {
    name                   = module.alb.lb_dns_name
    zone_id                = module.alb.lb_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "www" {
  zone_id = data.aws_route53_zone.this.zone_id
  name    = "www"
  type    = "CNAME"
  ttl     = "600"
  records = [local.webapp_domain]
}
