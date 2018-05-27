pipeline {
  agent { label 'molecule' }

  environment {
    PYENVPIPELINE_VIRTUALENV_RELATIVE_DIRECTORY = '../../../'
  }

  stages {
    stage('Activate venv') {
      steps {
        sh "source molecule/bin/activate"
      }
    }
    stage('Test') {
      steps {
        withPythonEnv('molecule') {
          pysh "molecule test"
        }
      }
    }
  }
}
