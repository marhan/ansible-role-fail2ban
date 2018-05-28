#!/bin/bash
ANSIBLE_ROLE_NAME="ansible-role-fail2ban"
docker run --rm -i -v $(pwd):/tmp/${ANSIBLE_ROLE_NAME}:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/${ANSIBLE_ROLE_NAME} retr0h/molecule:latest sudo molecule test
