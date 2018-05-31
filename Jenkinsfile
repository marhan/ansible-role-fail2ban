pipeline {
  agent {
    docker {
      image 'retr0h/molecule:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
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