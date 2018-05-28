#!/bin/bash
docker run --rm -i -v $(pwd):/tmp/ansible-role-fail2ban:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/ansible-role-fail2ban retr0h/molecule:latest sudo molecule test
