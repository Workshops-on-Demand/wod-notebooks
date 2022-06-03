# Load HPE GreenLake terraform provider
terraform {
      required_providers {
         hpegl = {
            source  = "hpe/hpegl"
            version = "0.1.7"
         }
      }
   }
# Setup provider environment (location and space)
provider "hpegl" {
      vmaas {
         location   = "HPE"
         space_name = "HPEDEV HackShack workshops"
      }
}

# Retrieve cloud id
data "hpegl_vmaas_cloud" "cloud" {
  name = "HPE GreenLake VMaaS Cloud-Trial4 "
   }

# And a few networks
data "hpegl_vmaas_network" "blue_net" {
  name = "Blue-Network"
   }
data "hpegl_vmaas_network" "green_net" {
  name = "Green-network"
   }
 
data "hpegl_vmaas_cloud_folder" "compute_folder" {
   cloud_id = data.hpegl_vmaas_cloud.cloud.id
   name = "ComputeFolder"
   }
 
# Locate a resource pool
data "hpegl_vmaas_resource_pool" "cl_resource_pool" {
  cloud_id = data.hpegl_vmaas_cloud.cloud.id
  name = "ComputeResourcePool"
   }
 
# And a group
data "hpegl_vmaas_group" "default_group" {
  name = "student{{ STDID }}"
}
 
# Locate a plan
data "hpegl_vmaas_plan" "g1_small" {
  name = "G1-Small"
   }
 
# A layout
data "hpegl_vmaas_layout" "vmware" {
  name               = "VMware VM with vanilla CentOS"
  instance_type_code = "glhc-vanilla-centos"
}
 
# And a template
data "hpegl_vmaas_template" "vanilla" {
  name = "vanilla-centos7-x86_64-09072020"
   }

resource "hpegl_vmaas_instance" "student{{ STDID }}" {
  name               = "student{{ STDID }}"
  cloud_id           = data.hpegl_vmaas_cloud.cloud.id
     group_id           = data.hpegl_vmaas_group.default_group.id
     layout_id          = data.hpegl_vmaas_layout.vmware.id
     plan_id            = data.hpegl_vmaas_plan.g1_small.id
     instance_type_code = data.hpegl_vmaas_layout.vmware.instance_type_code
 
     network {
         id = data.hpegl_vmaas_network.green_net.id
     }
 
     volume {
         name         = "root_vol"
         size         = 15
         datastore_id = "auto"
     }

 
     config {
         resource_pool_id = data.hpegl_vmaas_resource_pool.cl_resource_pool.id
         template_id      = data.hpegl_vmaas_template.vanilla.id
         no_agent         = true
         asset_tag        = "vm_terraform"
         folder_code      = data.hpegl_vmaas_cloud_folder.compute_folder.code
     }
 
     power = "poweron"
     
     labels = ["hackshack", "hpedev"]
     
     tags = {
        team  = "HPE Developer"
        support = "gold"
   }  
  
    snapshot {
    name        = "Snap"
    description = "Snap this VM so we can restart from this state"
  }
}
   
   