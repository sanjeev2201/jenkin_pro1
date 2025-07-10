pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/sanjeev2201/jenkin_pro1.git', branch: 'main'
                
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                    python3 -m virtualenv .jenkinenv
                    source .jenkinenv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source .jenkinenv/bin/activate
                    pytest
                '''
                }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    source .jenkinenv/bin/activate
                    nohup python run.py &
                '''
            }
        }
    }
}
