pipeline {
    agent any
    environment {
        IMAGE_NAME = "vithupro-hrm"
        CONTAINER_NAME = "vithupro-hrm-container"
        APP_PORT = "5000"
    }
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ganesh-dhumal/vithupro-hrm.git'
            }
        }
        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
        stage('Remove Old Container') {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }
        stage('Run New Container') {
            steps {
                sh "docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}:latest"
            }
        }
    }
}
