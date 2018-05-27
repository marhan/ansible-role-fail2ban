pipeline {
  agent { label 'molecule' }

  //environment {
    //PYENVPIPELINE_VIRTUALENV_RELATIVE_DIRECTORY = '/home/buildagent1/molecule/bin/python'
  //}

  stages {
    stage('Activate venv') {
      steps {
        sh "source molecule/bin/activate"
      }
    }
    stage('Test') {
      steps {
        withPythonEnv('/home/buildagent1/molecule/bin/python') {
          pysh "molecule test"
        }
      }
    }
  }
}
