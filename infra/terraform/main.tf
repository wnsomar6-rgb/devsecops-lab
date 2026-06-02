terraform {
  required_version = ">= 1.5.0"
}

provider "local" {}

resource "local_file" "devsecops_demo" {
  filename = "${path.module}/devsecops.txt"
  content  = "DevSecOps infrastructure simulated successfully"
}