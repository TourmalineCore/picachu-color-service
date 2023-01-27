"""Сonfiguration
Use env var to override
"""
import os


def get_required_env_variable(variable_name: str):
    env_variable_value = os.getenv(variable_name)
    if env_variable_value is None:
        raise ValueError(f'You should specify environment variable: {variable_name}.')
    return env_variable_value


rabbitmq_host = get_required_env_variable('RABBITMQ_HOST')
rabbitmq_username = get_required_env_variable('RABBITMQ_DEFAULT_USER')
rabbitmq_password = get_required_env_variable('RABBITMQ_DEFAULT_PASS')

rabbitmq_blocked_connection_timeout = int(get_required_env_variable('RABBITMQ_BLOCKED_CONNECTION_TIMEOUT'))
rabbitmq_heartbeat = int(get_required_env_variable('RABBITMQ_HEARTBEAT'))
rabbitmq_models_max_retry_number = int(get_required_env_variable('RABBITMQ_MODELS_MAX_RETRY_NUMBER'))
rabbitmq_models_retry_delay_ms = int(get_required_env_variable('RABBITMQ_MODELS_RETRY_DELAY_MS'))
rabbitmq_requests_exchange_name = get_required_env_variable('RABBITMQ_REQUESTS_EXCHANGE_NAME')
rabbitmq_models_queues_dlx_name = get_required_env_variable('RABBITMQ_MODELS_QUEUES_DLX_NAME')
rabbitmq_models_retry_queue_name = get_required_env_variable('RABBITMQ_MODELS_RETRY_QUEUE_NAME')
rabbitmq_models_retry_queue_dlx_name = get_required_env_variable('RABBITMQ_MODELS_RETRY_QUEUE_DLX_NAME')
rabbitmq_results_queue_name = get_required_env_variable('RABBITMQ_RESULTS_QUEUE_NAME')


s3_endpoint = get_required_env_variable('S3_ENDPOINT')
s3_access_key_id = get_required_env_variable('S3_ACCESS_KEY_ID')
s3_secret_access_key = get_required_env_variable('S3_SECRET_ACCESS_KEY')
s3_bucket_name = get_required_env_variable('S3_BUCKET_NAME')
s3_prefix = os.getenv('S3_PREFIX', default='')
s3_use_ssl = os.getenv('S3_USE_SSL', default='true').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup']

model_type = get_required_env_variable('MODEL_TYPE')
