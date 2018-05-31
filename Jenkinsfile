pipeline {
  agent {
    docker {
      image 'retr0h/molecule:latest'
      args '-v ${env.PWD}:/tmp/ansible-role-fail2ban:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/ansible-role-fail2ban'
    }

  }
  stages {
    stage('Test') {
      parallel {
        stage('Test (default)') {
          steps {
            sh 'molecule test -s default'
          }
        }
        stage('Test (variables)') {
          steps {
            sh 'molecule test -s variables'
          }
        }
      }
    }
  }
}