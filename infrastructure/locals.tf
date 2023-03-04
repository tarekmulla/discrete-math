# create a list of tag to be added to all resources (identify resources related to this question)
locals {
  tags = merge({
    Name        = "${var.app}"
    Application = var.app
  }, var.tags)
}
