# Load HPE GreenLake terraform provider
terraform {
      required_providers {
         hpegl = {
            source  = "hpe/hpegl"
            version = "0.1.7"
         }
      }
   }