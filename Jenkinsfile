pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi_student_app"
        CONTAINER_NAME = "fastapi_student_container"
        APP_PORT = "8000"
        DO_USER = "root"              // Change to your DO server user
        DO_HOST = "159.203.98.18"  // Change to your DO server IP
        REMOTE_APP_DIR = "/home/deploy/fastapi-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-pat',  // Your GitHub PAT credentials ID in Jenkins
                    branch: 'main',
                    url: "https://github.com/cherukurijyothi/Python_CICD_test.git"
            }
        }

        stage('Deploy to DigitalOcean') {
            steps {
                sshagent(['do-ssh']) {
                    // Copy the whole workspace to the DO server
                    sh "scp -r * $DO_USER@$DO_HOST:$REMOTE_APP_DIR"

                    // SSH into DO server and build & run docker container
                    sh """
                        ssh $DO_USER@$DO_HOST '
                            cd $REMOTE_APP_DIR &&
                            docker build -t $IMAGE_NAME . &&
                            docker stop $CONTAINER_NAME || true &&
                            docker rm $CONTAINER_NAME || true &&
                            docker run -d --name $CONTAINER_NAME -p $APP_PORT:$APP_PORT $IMAGE_NAME
                        '
                    """
                }
            }
        }
    }
}
