terraform {
  required_version = ">= 1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.55.0"
    }
  }

  # S3 bucket to store the terraform state file remotly, the bucket should be created manually
  # DynamoDB to lock the terraform state
  backend "s3" {
    bucket         = "terraform-statebucket-rmit"
    key            = "discrete-math/discrete-math-demo/terraform.tfstate"
    region         = "ap-southeast-2"
    dynamodb_table = "terraform-statelock-rmit"
    encrypt        = true
  }
}
