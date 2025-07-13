pipeline {
    agent {
    docker {
      image 'python:3.12.10'
    }
  }
  stages {
    stage('Clone Repo') {
      steps {
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
