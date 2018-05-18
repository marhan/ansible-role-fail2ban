#/bin/bash
#==========================================================================================#
# This script is a helper in order to run the tests without any knowledge about ansible.
#==========================================================================================#
echo "RUN ansible with --syntax-check"
echo
ansible-playbook --syntax-check -i inventory test.yml