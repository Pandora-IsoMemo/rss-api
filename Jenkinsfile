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
        stage('Deploy Python-Package') {
            when { branch 'main' }
            steps {
                sh '''
                echo "Cleaning up"
                docker image prune -f >/dev/null 2>&1 || true

                echo "Building docker image"
                docker build -t tmp-$CUR_PROJ-$TMP_SUFFIX .

                echo "Tagging image"
                GIT_SHA="$(git rev-parse --short=12 HEAD 2>/dev/null || echo unknown)"
                docker tag tmp-$CUR_PROJ-$TMP_SUFFIX "$IMAGE_NAME:$GIT_SHA"

                echo "Login to GHCR"
                echo "$GH_TOKEN_PSW" | docker login "$REGISTRY" -u "${GH_TOKEN_USR:-token}" --password-stdin

                echo "Push image"
                docker push "$IMAGE_NAME:$GIT_SHA"

                echo "Cleaning up"
                docker rmi tmp-$CUR_PROJ-$TMP_SUFFIX || true
                docker rmi "$IMAGE_NAME:$GIT_SHA" || true
                '''
            }
        }
    }
}
