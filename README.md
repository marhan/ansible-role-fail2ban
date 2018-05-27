Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

MIT

Used projects
------------------
- This project is implemented with [Ansible](https://www.ansible.com/)
- The test infrastructure is realized with [Molecule](https://molecule.readthedocs.io/en/latest/#)
- Test cases are implemented with [TestInfra](https://testinfra.readthedocs.io/en/latest/index.html)
- The test infrastructure uses [Docker](https://www.docker.com/)

Requirements
------------------

Not noteworthy that you have to install [Ansible](https://www.ansible.com/).

To run the test with molecule you need to install it e.g. by [pip](https://pypi.org/project/pip/). 
```
pip install molecule
pip install docker-py
```

An alternative is, you can use the Docker container from [Docker Hub](https://hub.docker.com/r/retr0h/molecule/). 
The container has Ansible and Molecule already inserted. 

Test
------------------

Ansible syntax check

```
ansible-playbook --syntax-check -i tests/inventory tests/test.yml
```

Molecule test

```
molecule test
```

Docker based molecule test

```
docker run --rm -it \
-v $(pwd):/tmp/$(basename "${PWD}"):ro \
-v /var/run/docker.sock:/var/run/docker.sock \
-w /tmp/$(basename "${PWD}") \
retr0h/molecule:latest sudo molecule test;
```
