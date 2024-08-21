import boto3

s3_client = boto3.client('s3')

bucket_name = 'curso-boto3-teste-321'

lifecycle_configuration = {
    'Rules': [
        {
            'ID': 'RegraExpiracao',
            'Prefix': '',
            'Status': 'Enabled',
            'Expiration': {
                'Days': 30
            }
        }
    ]
}

s3_client.put_bucket_lifecycle_configuration(
    Bucket=bucket_name,
    LifecycleConfiguration=lifecycle_configuration
)

print(f"Configuração do ciclo de vida do bucket {bucket_name} atualizada com sucesso.")
