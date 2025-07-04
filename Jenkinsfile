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
                echo "📥 Checking out source code..."
                git url: 'https://github.com/cherukurijyothi/Python_CICD_test.git', 
                    credentialsId: 'cherukurijyothi'
            }
        }

        stage('Verify Docker') {
            steps {
                echo "🔍 Verifying Docker installation..."
                sh 'docker --version'
                sh 'whoami'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🔨 Building Docker image: $IMAGE_NAME"
                sh 'ls -la'  // Check contents to confirm Dockerfile is present
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Replace Running Container') {
            steps {
                echo "♻️ Replacing running container: $CONTAINER_NAME"
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p $APP_PORT:$APP_PORT $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment succeeded — App is live on port $APP_PORT"
        }
        failure {
            echo "❌ Deployment failed — Check above logs for details"
        }
    }
}
