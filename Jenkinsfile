pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('1ede0dfb-20f1-46cb-9599-1dd484d9b50e')
        IMAGE_NAME = "geraldakenji/employee-image:v-0.0${env.BUILD_NUMBER}-stable"
    }
    stages {
    //    stage("Clean Workspace") {
    //         steps {
    //             cleanWs()
    //         }
    //    }
    //    stage("Git Checkout") {
    //         steps {
    //             checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/GeraldAkenji/Ecommerce-Django.git']])
    //         }
    //    }
    //    stage("Install System Dependencies") {
    //        steps {
    //            sh "apt-get update && apt-get install -y libpq-dev"
    //        }
    //    }
    //    stage("Install Dependencies") {
    //         steps {
    //             script {
    //                 sh "python3 -m venv venv"
    //                 sh ". venv/bin/activate"
    //                 sh "python3 -m pip install -r requirements.txt --no-cache-dir --break-system-packages"
    //             }
    //         }
    //     }
       stage("Docker Login") {
            steps {
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
       }
       stage("Build Docker Image") {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
       }
       stage("Push to DockerHub") {
            steps {
                script {
                    sh "docker push $IMAGE_NAME"
                }
            }
       }
       stage("Deploy to Kubernetes") {
            steps {
                script {
                    dir('./k8s') {
                        withKubeCredentials(kubectlCredentials: [[caCertificate: '', clusterName: '', contextName: '', credentialsId: '3f12ff7b-93cb-4ea5-bc21-79bcf5fb1925', namespace: 'gerald-env', serverUrl: '']]) {
                            sh "sed -i 's|PLEASE_REPLACE_ME|$IMAGE_NAME|g' deployment.yaml"
                            sh "kubectl apply -f ."
                        }
                    }
                }
            }
       }
    }
}
