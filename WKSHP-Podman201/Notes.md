# To do list

 - Section 4 > Quadlets are not able to start. HPE Env uses RHEL 8.8 and Podman 4.4.1 while I'm using RHEL 9.3 and Podman 4.6.1. Update Podman package is enough? Is container-tools installed? (sudo dnf module install -y container-tools). Update: tested on RHEL8.8 with Podman 4.6.1 and works like a charm, let's see if the update solves the issue.
 - Section 6 > Podman generate kube doesn't take "--replica" option. May be solved by updating Podman. Should be  solved updating to Podman 4.6.1 in RHEL 8.8.
 - Deploy and configure OpenShift in HPE Environment. Missing pieces: configure LDAP, create project template (with quota, resourcelimit and networkpolicy) and create global quotas.
 - Test all the Podman commands in Jupyter environment once Podman is in version 4.6.1
 - Test all the OpenShift commands in Jupyter environment
