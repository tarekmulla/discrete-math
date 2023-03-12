locals {
  # the quizes dynamodb table information
  quizzes_table = {
    "name"      = "${var.app}"
    "attr"      = "UserId, Date, Questions, Grade"
    "hash_key"  = "UserId"
    "range_key" = "Date"
  }
}

resource "aws_dynamodb_table" "quiz" {
  name         = local.quizzes_table["name"]
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = local.quizzes_table["hash_key"]
  range_key    = local.quizzes_table["range_key"]

  attribute {
    name = local.quizzes_table["hash_key"]
    type = "S"
  }

  attribute {
    name = local.quizzes_table["range_key"]
    type = "S"
  }

  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  point_in_time_recovery {
    enabled = false
  }

  tags = var.tags
}
