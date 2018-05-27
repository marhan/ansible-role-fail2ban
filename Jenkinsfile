pipeline {
	agent { label 'molecule'}
	stages {
    stage('Activate venv') {
      steps {
        sh "source molecule/bin/activate"
      }
    }
		stage('Test') {
			steps {
				sh "molecule test"
			}
		}
  }
}
