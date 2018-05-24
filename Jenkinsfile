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
				sh "docker run --rm -it -v $(pwd):/tmp/$(basename "${PWD}"):ro -v /var/run/docker.sock:/var/run/docker.sock -w /tmp/$(basename "${PWD}") retr0h/molecule:latest sudo molecule test"				
			}
		}
  }
}
