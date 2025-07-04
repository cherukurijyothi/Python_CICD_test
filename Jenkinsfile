pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-jenkins"
        CONTAINER_NAME = "fastapi_app"
        APP_PORT = "8000"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "📋 Latest commit info:"
                sh 'git log -1 --oneline'
                echo "📂 Workspace contents:"
                sh 'ls -la'
                echo "📄 First 10 lines of main.py:"
                sh 'head -10 main.py'
            }
        }

        stage('Verify Docker') {
            steps {
                echo "🔍 Verifying Docker installation and user permissions..."
                sh 'docker --version'
                sh 'whoami'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🔨 Building Docker image: ${IMAGE_NAME}"
                sh "docker build --no-cache -t ${IMAGE_NAME} ."
            }
        }

        stage('Replace Running Container') {
            steps {
                echo "♻️ Replacing running container: ${CONTAINER_NAME}"
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}
                    echo "🚀 Current running containers:"
                    docker ps -a
                    echo "🖼️ Docker images with name ${IMAGE_NAME}:"
                    docker images | grep ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment succeeded — App is live on port ${APP_PORT}"
        }
        failure {
            echo "❌ Deployment failed — Check above logs for details"
        }
    }
}
