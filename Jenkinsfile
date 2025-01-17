pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 fastapi-app'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed'
        }
    }
}
