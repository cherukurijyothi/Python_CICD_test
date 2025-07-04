pipeline {
    agent any
 
    environment {
        IMAGE_NAME = "fastapi"
        CONTAINER_NAME = "fastapi_container"
        APP_PORT = "8000"
    }
    stages {
        stage('clone Repository') {
            steps {
             //   git credentialsId: 'azure-pat',
             //   branch: 'master',
             //   url: "https://rajsunkara@dev.azure.com/rajsunkara/HealthChrono/_git/FASTAPI"
             checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'  
            }
        }
        stage('stop & Remove Old container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''
                docker run -d --name $CONTAINER_NAME -p $APP_PORT:$APP_PORT $IMAGE_NAME
                '''
            }
        }
 
   
    }
}