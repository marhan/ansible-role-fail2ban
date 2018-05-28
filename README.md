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
         - { role: marhan.ansible, x: 42 }

License
-------

MIT

Test Requirements
------------------

Not noteworthy that you have to install [Ansible](https://www.ansible.com/).

To run tests with Molecule you need to install it.

**Installation via pip**

```
pip install molecule
pip install docker-py
```

An alternative is, you can use a Docker container from [Docker Hub](https://hub.docker.com/r/retr0h/molecule/). 
The container has all dependencies like Ansible and Molecule included.

Run tests
------------------

Run Molecule.

```
molecule test
```

Run Molecule via Docker container.

```
./test_via_docker.sh
```

Relevant projects
------------------
- This project is implemented with [Ansible](https://www.ansible.com/)
- The test infrastructure is realized with [Molecule](https://molecule.readthedocs.io/en/latest/#)
- Test cases are implemented with [TestInfra](https://testinfra.readthedocs.io/en/latest/index.html)
- The test infrastructure uses [Docker](https://www.docker.com/)

Interesting Resources
------------------
- [Setup virtual python environment](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04) 
- [Permissions Calculator](http://permissions-calculator.org/)


