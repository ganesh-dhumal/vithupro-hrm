pipeline {
    agent any

    environment {
        IMAGE_NAME = "vithupro-hrm"
        CONTAINER_NAME = "vithupro-hrm-container"
        APP_PORT = "5000" // Change if your app uses a different port
    }

    triggers {
        // Poll GitHub every 2 minutes (replace with webhook for faster builds)
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
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
                sh """
                if [ \$(docker ps -q -f name=${CONTAINER_NAME}) ]; then
                    docker stop ${CONTAINER_NAME}
                    docker rm ${CONTAINER_NAME}
                fi
                """
            }
        }

        stage('Run New Container') {
            steps {
                sh """
                docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}:latest
                """
            }
        }
    }
}

