pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/sanjeev2201/jenkin_pro1.git', branch: 'main'
            }
        }

        stage('Set up Environment') {
            steps {
                bat '''
                    python -m venv env
                    call env\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call env\\Scripts\\activate
                    pytest
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                bat '''
                    call env\\Scripts\\activate
                    start /b python run.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Stopping any running Flask app...'
            bat 'taskkill /F /IM python.exe || exit 0'
        }
    }
}
