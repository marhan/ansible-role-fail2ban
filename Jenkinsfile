pipeline {
  agent any

  stages {

    stage('Env') {
      steps {
        sh "printenv"
      }
    }

    stage('Test') {
      parallel {

        stage('Test (default)') {
          agent {
            docker {
              image 'retr0h/molecule:latest'
              args '-v $WORKSPACE:/tmp/ansible-role-fail2ban:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/ansible-role-fail2ban'
            }
            steps {
              sh 'molecule test -s default'
            }
          }
        }

        stage('Test (variables)') {
          agent {
            docker {
              image 'retr0h/molecule:latest'
              args '-v $WORKSPACE:/tmp/ansible-role-fail2ban:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/ansible-role-fail2ban'
            }
            steps {
              sh 'molecule test -s variables'
            }
          }
        }

      }
    }
  }
}

