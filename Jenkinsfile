pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/sanjeev2201/jenkin_pro1.git'
            }
        }
        stage('Set up Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/Scripts/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    source venv/Scripts/activate
                    pytest
                '''
            }
        }
        stage('Run Flask App') {
            steps {
                sh '''
                    source venv/Scripts/activate
                    nohup python run.py &
                '''
            }
        }
    }
}
