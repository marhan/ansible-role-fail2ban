pipeline {
	agent any
	stages {
		stage('Test (syntax)') {
			steps {
				sh "./test-syntax.sh"
			}
		}
		stage('Test (molecule)') {
			steps {
				sh './test-function.sh'
			}
		}
  }
}
