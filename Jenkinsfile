pipeline {
    agent { label 'Jenkins' }
    
    environment {
        ALLURE_SERVER_ID = 'anny_testops' 
        ALLURE_CREDENTIALS_ID = 'anny_testops' 
        ALLURE_PROJECT_ID = '1878' 
        ALLURE_RESULTS_PATH = 'build/allure-results' 
    }
    
    stages {
        stage('Setup and Run Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh "mkdir -p ${env.ALLURE_RESULTS_PATH}"

                withAllureUpload(
                    serverId: env.ALLURE_SERVER_ID,
                    credentialsId: env.ALLURE_CREDENTIALS_ID,
                    projectId: env.ALLURE_PROJECT_ID,
                    results: [[path: env.ALLURE_RESULTS_PATH]]
                ) {
                    echo "--- Запуск тестов и первая отправка через withAllureUpload ---"
                    sh "pytest --alluredir=${env.ALLURE_RESULTS_PATH} || true"
                }
            }
        }
    }
    
    post {
        always {
            echo '--- Сработал блок post { always } - ВТОРАЯ ПУБЛИКАЦИЯ ---'
            allure includeProperties: false, 
                   results: [[path: env.ALLURE_RESULTS_PATH]]
                   
            echo 'Проверка TestOps на дубликаты завершена.'
        }
    }
}
