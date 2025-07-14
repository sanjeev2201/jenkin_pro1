pipeline {
    agent {
        docker {
            image 'python:3.12.10'  // or use your custom image
        }
    }
    stages {
        stage('Clone Repo') {
            steps {
                sh 'rm -rf jenkin_pro1'
                sh 'git clone https://github.com/sanjeev2201/jenkin_pro1.git'
            }
        }
        stage('Install Python Packages') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                // sh 'python app/test_app.py'
                sh'python tests/test.py'
            }
        }

        stage('Docker Build & Run') {
            steps {
                sh 'docker build -t flask-ci-app .'
                sh 'docker-compose up -d'
            }
        }
    

    }
}
