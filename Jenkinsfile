pipeline {
  agent { label 'molecule' }

  environment {
    PYENVPIPELINE_VIRTUALENV_RELATIVE_DIRECTORY = 'molecule'
  }

  stages {
    stage('Test') {
      steps {
        withPythonEnv('python3') {
          pysh "molecule test"
        }
      }
    }
  }
}
