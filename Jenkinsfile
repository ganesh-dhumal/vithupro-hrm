pipeline {
  agent any

  environment {
    IMAGE_NAME     = 'vithupro-hrm'
    CONTAINER_NAME = 'vithupro-hrm'
    APP_PORT       = '8000'
    DOCKER_BUILDKIT = '0' // avoid buildx requirement in Jenkins container
  }

  triggers {
    // Auto-run on push via polling (no public webhook needed)
    pollSCM('H/2 * * * *')
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Docker Sanity') {
      steps { sh 'docker version && docker ps' }
    }

    stage('Build Image') {
      steps { sh 'docker build -t ${IMAGE_NAME}:latest .' }
    }

    stage('Deploy') {
      steps {
        sh '''
          set -e
          docker rm -f ${CONTAINER_NAME} || true
          docker run -d --name ${CONTAINER_NAME} \
            -p ${APP_PORT}:${APP_PORT} \
            --restart unless-stopped \
            ${IMAGE_NAME}:latest
        '''
      }
    }

    stage('Status') {
      steps {
        sh "docker ps --filter name=${CONTAINER_NAME} --format 'table {{.Names}}\\t{{.Image}}\\t{{.Ports}}\\t{{.Status}}'"
      }
    }
  }

  post {
    success {
      echo "✅ Deployed ${IMAGE_NAME}:latest to ${CONTAINER_NAME}"
      sh 'docker image prune -f || true'
    }
    failure {
      echo "❌ Build/Deploy failed — check Console Output"
    }
  }
}
