pipeline {
  agent any

  environment {
    IMAGE_NAME     = "vithupro-hrm"
    CONTAINER_NAME = "vithupro-hrm-container"
    APP_PORT       = "5000"          // change if your app uses a different port
  }

  triggers {
    // Auto every push via polling (no public webhook needed)
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
        sh '''
          set -e
          GIT_SHA=$(git rev-parse --short HEAD)
          echo "Building image ${IMAGE_NAME}:${GIT_SHA}"
          docker build --pull -t ${IMAGE_NAME}:latest -t ${IMAGE_NAME}:${GIT_SHA} .
        '''
      }
    }

    stage('Stop & Remove Old Container') {
      steps {
        sh '''
          set -e
          if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
            echo "Stopping/removing old container: ${CONTAINER_NAME}"
            docker rm -f ${CONTAINER_NAME} || true
          else
            echo "No previous container to remove."
          fi
        '''
      }
    }

    stage('Run New Container') {
      steps {
        sh '''
          set -e
          echo "Starting new container: ${CONTAINER_NAME}"
          docker run -d --name ${CONTAINER_NAME} \
            -p ${APP_PORT}:${APP_PORT} \
            --restart unless-stopped \
            ${IMAGE_NAME}:latest
        '''
      }
    }
  }

  post {
    success {
      echo "✅ Deployed ${IMAGE_NAME}:latest to container ${CONTAINER_NAME}"
      sh 'docker image prune -f || true'   // keep disk tidy
    }
    failure {
      echo "❌ Build/Deploy failed — check Console Output."
    }
  }
}
