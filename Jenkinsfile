pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    environment {
        FLASK_APP = 'run.py'
        FLASK_ENV = 'development'
        // Optional: Define a Python virtual environment name
        VENV_DIR = 'env'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/sanjeev2201/jenkin_pro1.git', branch: 'main'
            }
        }

        stage('Set up Python') {
            steps {
              sh '''#!/bin/bash
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/Scripts/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                   source ${VENV_DIR}/Scripts/activate
                    flask run --host=0.0.0.0 --port=5000 &
                    sleep 5
                    curl http://localhost:5000 || echo "Flask app is not reachable"
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'pkill -f flask || true'
        }
    }
}
