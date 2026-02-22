# Terraform Module Patterns

Standard patterns for writing reusable Terraform modules.

## Directory Structure

```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    README.md
  rds/
    main.tf
    variables.tf
    outputs.tf
```

## Input Variables

Always provide description and type. Use validation blocks for constrained inputs:

```hcl
variable "environment" {
  description = "Deployment environment"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

## Outputs

Expose everything downstream modules might need:

```hcl
output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}
```

## Versioning

Pin module sources to tags, never branches:
```hcl
module "vpc" {
  source = "git::https://github.com/org/terraform-modules.git//vpc?ref=v1.2.0"
}
```

## Composition

Compose small modules into environment-level configs. Keep modules focused — a VPC module shouldn't also create a database.
