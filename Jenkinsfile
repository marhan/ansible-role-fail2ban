pipeline {
	agent { label 'molecule'}
	stages {
		stage('Test') {
			steps {
				sh "molecule test"
			}
		}
  }
}
