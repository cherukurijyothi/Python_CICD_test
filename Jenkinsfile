pipeline {
    agent any
 
    environment {
        IMAGE_NAME = "fastapi"
        CONTAINER_NAME = "fastapi_container"
        APP_PORT = "8000"
    }
    tages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'Kjyothi',  // Your GitHub PAT credentials ID in Jenkins
                    branch: 'main',
                    url: "https://github.com/cherukurijyothi/Python_CICD_test.git"
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
 