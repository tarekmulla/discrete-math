

# Add an IPv4 DNS record pointing to the loab balancer
resource "aws_route53_record" "ipv4" {
  zone_id = var.route53_zone_id
  name    = var.website_domain
  type    = "A"

  alias {
    name                   = module.alb.lb_dns_name
    zone_id                = module.alb.lb_zone_id
    evaluate_target_health = false
  }
}
