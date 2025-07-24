#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from boto3 import client  # Import only the client function from boto3
import logging
from urllib.parse import unquote_plus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = client('s3')

def check_file_type(content):
    """Determine file type using magic bytes."""
    if len(content) >= 2 and content[:2] == b'\xff\xd8':  # JPEG magic bytes
        return 'image/jpeg'
    if len(content) >= 4 and content[:4] == b'%PDF':  # PDF magic bytes
        return 'application/pdf'
    if len(content) >= 4 and content[:4] == b'\x89PNG':  # PNG magic bytes
        return 'image/png'
    return None

import urllib.parse  # Import urllib.parse to sanitize input for logging

def lambda_handler(event, context):
    for record in event.get('Records', []):
        try:
            bucket = record['s3']['bucket']['name']
            key = unquote_plus(record['s3']['object']['key'])  # Decode URL-encoded key
            
            logger.info(f"Processing: s3://{urllib.parse.quote(bucket)}/{urllib.parse.quote(key)}")
            
            # Get first few bytes for type detection
            response = s3.get_object(Bucket=bucket, Key=key, Range='bytes=0-3')
            file_bytes = response['Body'].read()
            
            # Determine correct Content-Type
            correct_content_type = check_file_type(file_bytes)
            if not correct_content_type:
                logger.info(f"Skipping unsupported file type: {urllib.parse.quote(key)}")
                continue
            
            # Get current metadata
            head_response = s3.head_object(Bucket=bucket, Key=key)
            current_content_type = head_response.get('ContentType', '')
            
            # Skip if Content-Type is already correct
            if current_content_type == correct_content_type:
                logger.info(f"File {urllib.parse.quote(key)} already has correct Content-Type: {current_content_type}. Skipping.")
                continue
            
            # Preserve existing user metadata
            user_metadata = head_response.get('Metadata', {})
            
            # Update Content-Type and preserve user metadata
            s3.copy_object(
                Bucket=bucket,
                Key=key,
                CopySource={'Bucket': bucket, 'Key': key},
                ContentType=correct_content_type,
                Metadata=user_metadata,
                MetadataDirective='REPLACE'
            )
            
            logger.info(f"Updated Content-Type for {urllib.parse.quote(key)} to {correct_content_type}")
        
        except Exception as e:
            logger.error(f"Error processing {urllib.parse.quote(key)}: {str(e)}")
