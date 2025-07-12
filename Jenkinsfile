pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/sanjeev2201/jenkin_pro1.git', branch: 'main'
            }
        }

        stage('Show Git Info') {
            steps {
                sh '''
                    echo "Listing files..."
                    ls -a
                    echo "Git last commit:"
                    git log -1
                '''
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    nohup python3 run.py &
                    sleep 5
                    curl http://localhost:5000 || echo "Flask app not reachable"
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up"
            sh "pkill -f run.py || true"
        }
    }
}
