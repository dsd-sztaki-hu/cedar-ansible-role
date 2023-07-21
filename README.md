# cedar-ansible-role

This is a role to deploy the CEDAR metadata template editor with ansible. 
Information on CEDAR can be found at:

 - https://metadatacenter.org/
 - https://github.com/metadatacenter

Currently, it creates three systemd services: cedar-infrastructure, cedar-microservices and cedar-frontend.

It is tested on Debian 12, but should work on Debian 11 and Ubuntu 20.04 or newer.

The upper level cedar.yml is a playbook to copy or symlink to your project.

