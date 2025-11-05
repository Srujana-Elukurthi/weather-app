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

        stage('Run Docker Container') {
            steps {
                // Stop & remove any existing container
                sh 'docker stop weather-app || true'
                sh 'docker rm weather-app || true'

                // Run the container on host port 5001
                sh 'docker run -d -p 5001:5000 --name weather-app srujanaelukurthi/weather-app:latest'
            }
        }
    }

    post {
        success {
            echo 'Weather App CI/CD Pipeline Succeeded! Open http://localhost:5001 to access it.'
        }
        failure {
            echo 'Pipeline Failed!'
        }
    }
}


            
        
   



