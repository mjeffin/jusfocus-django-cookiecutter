# eval database_url='$'${CI_COMMIT_REF_NAME}_DATABASE_URL
# echo "DATABASE_URL: $database_url" >> env.yml
echo "DATABASE_URL: $MASTER_DATABASE_URL" >> env.yml
echo "DEPLOY_ENVIRON: MASTER" >> env.yml
echo "DJANGO_AWS_STORAGE_BUCKET_NAME: $DJANGO_AWS_STORAGE_BUCKET_NAME_DEV_MEDIA" >> env.yml
echo "DJANGO_AWS_STORAGE_BUCKET_NAME_STATIC: $DJANGO_AWS_STORAGE_BUCKET_NAME_DEV_STATIC" >> env.yml