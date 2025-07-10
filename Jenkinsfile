pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-jenkins-app'
    }

    stages {
        stage('Clone source') {
            steps {
                git 'https://github.com/hiepquach2004/lab8jenkins/flask-app.git'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    docker.build(IMAGE_NAME)
                }
            }
        }

        stage('Run Docker container') {
            steps {
                script {
                    sh "docker rm -f flask-container || true"
                    sh "docker run -d --name flask-container -p 5000:5000 ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "🎉 CI/CD pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
