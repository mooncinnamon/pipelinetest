echo "---build start---"

node {
    git poll: true,
    url:'https://github.com/mooncinnamon/pipelinetest.git'

    stage('Pull') {
        git 'https://github.com/mooncinnamon/pipelinetest.git'
        }
    stage('Unit Test') {
        }
    stage('Build') {
        sh(script: 'docker-compose build app')
        }
    stage('Tag') {
        sh(script: '''docker tag shutle_app docker.cinna.dev/shutle:${BUILD_NUMBER}''')
        }
    stage('Push') {
        sh(script: 'docker push docker.cinna.dev/shutle:${BUILD_NUMBER}')
        sh(script: 'docker push docker.cinna.dev/shutle:latest')
        }
    stage('Deploy') {
        sh(script: 'docker-compose up -d production')
        }
}