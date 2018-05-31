pipeline {
  agent {
    docker {
      image 'retr0h/molecule:latest'
      args  'docker run --rm -i -v $(pwd):/tmp/ansible-role-fail2ban:ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/ansible-role-fail2ban'
    }
  } 
  
  stages {
    stage('Test') {
        parallel {
            stage('Test (default)') {                       
              steps {
                sh "sudo molecule test -s default"
              }              
            }        
            stage('Test (variables)') {
              steps {
                sh "sudo molecule test -s variables"
              }
            }
        }
    }
  }
}
