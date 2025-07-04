pipeline {
    agent any
 
    environment {
        IMAGE_NAME = "fastapi_student_app"
        CONTAINER_NAME = "fastapi_student_container"
        APP_PORT = "8000"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: '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',    // Use your Jenkins credential ID for GitHub PAT here
                    branch: 'main',
                    url: "https://github.com/cherukurijyothi/Python_CICD_test.git"
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'  
            }
        }
        stage('Stop & Remove Old Container') {
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
