pipeline {
    agent any
    stages {
        stage('Check Docker') {
            steps {
                sh 'docker --version'
                sh 'docker ps'
            }
        }
        stage('Clone Repo') {
            steps {
                sh 'rm -rf jenkin_pro1'
                sh 'git clone https://github.com/sanjeev2201/jenkin_pro1.git'
            }
        }
        stage('Install Python Packages') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Flask App') {
            steps {
                sh 'python run.py'
            }
        }
    }
}
