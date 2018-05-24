#!/bin/bash

ansible-playbook --syntax-check -i tests/inventory tests/test.yml
