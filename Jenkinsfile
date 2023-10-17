pipeline {
    agent any

    stages {
        stage('Pull from GitHub') {
            steps {
                git url: 'https://github.com/Mouhib-hero/First-pipeline', branch: 'main',
                credentialsId: 'GitHubCredentials' //jenkins-github-creds
                sh "ls -ltr"
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t starprophecy/simplewebapp .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHubCredentials', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                    sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                    sh 'docker push starprophecy/simplewebapp'
                }
            }
        }
    }
}
