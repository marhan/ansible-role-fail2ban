pipeline {
  agent { label 'molecule' }

  stages {
    stage('Test') {
      steps {
        sh "./test_via_docker.sh"
      }
    }
  }
}
