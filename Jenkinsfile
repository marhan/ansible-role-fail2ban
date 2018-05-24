pipeline {
	agent any
	stages {		
		stage('Test (syntax)') {
			steps {
				sh "ansible-playbook --syntax-check -i tests/inventory tests/test.yml"				
			}
		}
		stage('Test (molecule)') {
			steps {
				sh "molecule test"				
			}
		}
  }
}
