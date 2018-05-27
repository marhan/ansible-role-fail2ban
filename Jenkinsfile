pipeline {
  agent { label 'molecule' }

  //environment {
    //PYENVPIPELINE_VIRTUALENV_RELATIVE_DIRECTORY = '/home/buildagent1/molecule/bin/python'
  //}

  stages {
    stage('Test') {
      steps {
        withPythonEnv('/home/buildagent1/molecule/bin/python') {
          pysh "molecule test"
        }
      }
    }
  }
}
