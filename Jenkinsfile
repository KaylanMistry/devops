pipeline {
    
    environment {
            DOCKERHUB_CREDENTIALS = credentials('kaylanmistry-Monkeys182!')
        }
    agent { any { image 'python:3.8' } }
    stages {
        stage('Clearing processes') {
            steps {
                echo "-=- clearing processes -=-"
                sh "docker stop \044(docker ps -a -q)"
                sh "docker rm \044(docker ps -a -q)"
            }
        } 
        stage('Getting files') {
            steps {
                echo "-=- getting files -=-"
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/KaylanMistry/devops.git']]])
            }
        }
        stage('Building Docker image') {
            steps {
                echo "-=- building Docker image -=-"
                sh "docker build -t kaylan-server:latest ."
            }
        }
        stage('Running Docker image') {
            steps {
                echo "-=- run Docker image -=-"
                sh "docker run -d -p 8888:8888 kaylan-server"
            }
        } 
        
        stage('Pushing to Dockerhub') {
            steps {
                echo "-=- pushing to Dockerhub -=-"
                sh "docker tag kaylan-server:latest kaylanmistry/kaylan-server:latest"
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                sh "docker push kaylanmistry/kaylan-server:latest"
            }
        }    
    }
}