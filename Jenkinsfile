pipeline {
    agent any

    environment {
        DOCKERHUB_USER = credentials('srujanaelukurthi')
        DOCKERHUB_PASS = credentials('dockerhub_password')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Srujana-Elukurthi/weather-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-app .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin'
            }
        }

        stage('Tag & Push Image') {
            steps {
                sh 'docker tag weather-app:latest srujanaelukurthi/weather-app:latest'
                sh 'docker push srujanaelukurthi/weather-app:latest'
            }
        }
    }
}

