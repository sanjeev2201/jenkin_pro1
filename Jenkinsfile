pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the Git repository
                git url: 'https://github.com/sanjeev2201/jenkin_pro1.git', branch: 'main'
            }
        }

        stage('Test') {
            steps {
                echo 'Pipeline is working!'
            }
        }
    }
}
