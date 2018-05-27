pipeline {
  agent { label 'molecule' }

  //environment {
    //PYENVPIPELINE_VIRTUALENV_RELATIVE_DIRECTORY = '/home/buildagent1/molecule/bin/python'
  //}

  stages {
    stage('Test') {
      steps {
        withPythonEnv('molecule') {
          pysh "molecule test"
        }
      }
    }
  }
}
