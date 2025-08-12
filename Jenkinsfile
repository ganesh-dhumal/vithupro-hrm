pipeline {
    agent any

    environment {
        IMAGE_NAME = "vithupro-hrm"
        CONTAINER_NAME = "vithupro-hrm-container"
        APP_PORT = "5000"  // Change this if your app uses another port
    }

    triggers {
        // Poll GitHub every 2 minutes (works without webhook/public Jenkins)
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ganesh-dhumal/vithupro-hrm.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh """
                    if [ \$(docker ps -q -f name=${CONTAINER_NAME}) ]; then
                        echo "Stopping and removing old container..."
                        docker stop ${CONTAINER_NAME}
                        docker rm ${CONTAINER_NAME}
                    fi
                    """
                }
            }
        }

        stage('Run New Container') {
            steps {
                sh """
                echo "Starting new container..."
                docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo "Deployment completed successfully."
        }
        failure {
            echo "Deployment failed. Please check the Jenkins logs."
        }
    }
}
