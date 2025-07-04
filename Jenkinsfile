pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/cherukurijyothi/Python_CICD_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
