pipeline {
  agent any
  stages {
    stage('Clone Repo') {
      steps {
        sh 'git clone https://github.com/sanjeev2201/jenkin_pro1.git'
      }
    }
    stage('Install Python Packages') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install -r jenkin_pro1/requirements.txt'
      }
    }
    stage('Run Flask App') {
      steps {
        sh 'python3 jenkin_pro1/run.py'
      }
    }
  }
}
