pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub_credentials')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-app .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo "$DOCKERHUB_PSW" | docker login -u "$DOCKERHUB_USR" --password-stdin'
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

            
        
   



