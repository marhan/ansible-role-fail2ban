pipeline {
  agent  any

  stages {
      stage('ENV') {        
        steps {
          sh "printenv"
        }
        
      }


   
      
        stage('Test (default)') {
          agent {
    docker {
      image 'retr0h/molecule:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }

  }
          steps {
            sh 'molecule test -s default'
          }
        }        
        stage('Test (variables)') {
          agent {
    docker {
      image 'retr0h/molecule:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }

  }
          steps {
            sh 'molecule test -s variables'
          }
        }
      }
    
  
}