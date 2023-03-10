locals {
  env_vars = [for k, v in var.parameters : { "name" : k, "value" : v }]
}

module "ecs" {
  source = "terraform-aws-modules/ecs/aws"

  cluster_name = var.app

  cluster_configuration = {
    execute_command_configuration = {
      logging = "OVERRIDE"
      log_configuration = {
        cloud_watch_log_group_name = "/aws/ecs/aws-ec2"
      }
    }
  }

  fargate_capacity_providers = {
    FARGATE = {
      default_capacity_provider_strategy = {
        weight = 50
      }
    }
    FARGATE_SPOT = {
      default_capacity_provider_strategy = {
        weight = 50
      }
    }
  }
}

resource "aws_ecs_service" "web-app" {
  name            = var.app
  cluster         = module.ecs.cluster_id
  task_definition = aws_ecs_task_definition.web-app.arn
  desired_count   = var.ecs_tasks_count
  launch_type     = "FARGATE"

  load_balancer {
    target_group_arn = module.alb.target_group_arns[0]
    container_name   = var.app
    container_port   = var.container_port
  }

  network_configuration {
    security_groups = [
      aws_security_group.fargate.id
    ]
    subnets          = var.private_subnet_ids
    assign_public_ip = false
  }
  health_check_grace_period_seconds = 300
}

resource "aws_ecs_task_definition" "web-app" {
  family                   = var.app
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  cpu                      = 256
  memory                   = 2048
  container_definitions = jsonencode([
    {
      name                   = "${var.app}"
      image                  = var.container_image
      essential              = true
      readonlyRootFilesystem = false
      environment            = local.env_vars
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = "/fargate/service/${var.app}-fargate-log"
          awslogs-stream-prefix = "ecs"
          awslogs-region        = var.region
        }
      }
      portMappings = [
        {
          containerPort = var.container_port
          hostPort      = var.container_port
        }
      ]
    }
  ])
}
