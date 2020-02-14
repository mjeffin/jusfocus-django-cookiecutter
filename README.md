
## Mandatory environment variables

### Env vars required by Django

1. DATABASE_URL
2. SSH_PRIVATE_KEY
3. settings module

### Env vars required for anisble deployment
1. PROJECT_CODE
2. ADMIN_EMAIL

echo "GIT_BRANCH: $CI_COMMIT_REF_NAME" >> env.yml
echo "GIT_REPO: $CI_REPOSITORY_URL" >> env.yml
echo "GIT_DEPLOY_KEY: $GIT_DEPLOY_KEY" >> env.yml

### Third party apps

1. Djoser
2. Swagger
3. Sentry
4. CORS
5. django-extensions
6. django debug_toolbar



## .env file template
DATABASE_URL=postgres://<username>:<password>@<hostname>:5432/<dbname>
SENTRY_DSN=
DJANGO_AWS_ACCESS_KEY_ID=
DJANGO_AWS_SECRET_ACCESS_KEY=
DJANGO_AWS_STORAGE_BUCKET_NAME_STATIC=
DJANGO_AWS_STORAGE_BUCKET_NAME=
