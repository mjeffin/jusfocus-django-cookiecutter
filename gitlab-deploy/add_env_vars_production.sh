echo "DATABASE_URL: $PRODUCTION_DATABASE_URL" >> env.yml
echo "DEPLOY_ENVIRON: PRODUCTION" >> env.yml
echo "DJANGO_AWS_STORAGE_BUCKET_NAME: $DJANGO_AWS_STORAGE_BUCKET_NAME_PROD_MEDIA" >> env.yml
echo "DJANGO_AWS_STORAGE_BUCKET_NAME_STATIC: $DJANGO_AWS_STORAGE_BUCKET_NAME_PROD_STATIC" >> env.yml