pipeline {
	agent any
	stages {		
		stage('Test') {
			steps {
				sh "ansible-playbook --syntax-check -i tests/inventory tests/test.yml"				
			}
		}
  }
}
