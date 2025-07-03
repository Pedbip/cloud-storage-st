from google.cloud import storage

STORAGE_CLIENT = storage.Client.from_service_account_json('C:/Users/games/credenciais/myproject-464800-bbfa9c8f1c37.json')

def upload_archive(bucket_name, source_file_name, destination_blob_name):
    bucket = STORAGE_CLIENT.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f'Archive {source_file_name} sent to {destination_blob_name} on bucket {bucket_name}.')

def list_blobs_in_folder(bucket_name, folder_prefix):
    bucket = STORAGE_CLIENT.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_prefix)
    print("\nList of files in the folder:")
    for blob in blobs:
        print(blob.name)