pipeline {
    agent any 
    
    environment {
        ALLURE_SERVER_ID = 'anny_testops' 
        ALLURE_CREDENTIALS_ID = 'anny_testops' 
        ALLURE_PROJECT_ID = '1878' 
        ALLURE_RESULTS_PATH = 'build/allure-results' 
    }
    
    stages {
        stage('Reproduce Conflict') {
            steps {
                sh "mkdir -p ${env.ALLURE_RESULTS_PATH}" 
                
                withAllureUpload(
                    serverId: env.ALLURE_SERVER_ID,
                    credentialsId: env.ALLURE_CREDENTIALS_ID,
                    projectId: env.ALLURE_PROJECT_ID,
                    results: [[path: env.ALLURE_RESULTS_PATH]]
                ) {
                    echo "--- ПЕРВАЯ ОТПРАВКА ---"
                }
            }
        }
    }
    
    post {
        always {
            echo '--- ВТОРАЯ ОТПРАВКА: Конфликтный плагин ---'
            allure includeProperties: false, 
                   results: [[path: env.ALLURE_RESULTS_PATH]]
                   
            echo 'Проверь TestOps на дублирование!'
        }
    }
}
