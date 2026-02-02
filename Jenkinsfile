pipeline {
    agent any
    options { disableConcurrentBuilds() }
    environment {
        CUR_PROJ = 'rss-api' // github repo name
        CUR_PKG_FOLDER = '.' // defaults to root
        TMP_SUFFIX = """${sh(returnStdout: true, script: 'echo `cat /dev/urandom | tr -dc \'a-z\' | fold -w 6 | head -n 1`')}"""
        CREDENTIALS = credentials('rss-api-env')
        GH_TOKEN = credentials("github-isomemo")
        REGISTRY = 'ghcr.io'
        REGISTRY_OWNER = 'Pandora-IsoMemo'
        IMAGE_NAME = "${REGISTRY}/${REGISTRY_OWNER}/${CUR_PROJ}".toLowerCase()
    }
    stages {
        stage('Testing') {
            steps {
                sh '''
                docker build -t tmp-$CUR_PROJ-$TMP_SUFFIX .
                docker run --rm --network host \
                 --env-file $CREDENTIALS \
                 tmp-$CUR_PROJ-$TMP_SUFFIX \
                 pipenv run python -c "import api.main; print('import ok')"
                docker rmi tmp-$CUR_PROJ-$TMP_SUFFIX
                '''
            }
        }
    }
}
