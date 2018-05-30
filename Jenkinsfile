pipeline {
  agent { label 'molecule' }

  environment {
    ANSIBLE_ROLE_NAME = "ansible-role-fail2ban"
    DOCKER_COMMAND_PART_1 = "docker run --rm -i -v \$(pwd):/tmp/${ANSIBLE_ROLE_NAME}:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/${ANSIBLE_ROLE_NAME} retr0h/molecule:latest"
  }

  stages {

    stage('Test (default)') {
      steps {
        sh "${DOCKER_COMMAND_PART_1} sudo molecule test -s default"
      }
    }

    stage('Test (variables)') {
      steps {
        sh "${DOCKER_COMMAND_PART_1} sudo molecule test -s variables"
      }
    }

  }
}
