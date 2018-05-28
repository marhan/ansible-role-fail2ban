pipeline {
  agent { label 'molecule' }

  stages {
    stage('Test') {
      steps {
        sh "./tests/test_via_docker.sh"
      }
    }
  }
}
