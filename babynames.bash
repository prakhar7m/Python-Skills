s3 = boto3.resource('s3')
object = s3.Object('pm1178-labdata', 'summary.txt')
object.put(Body=text)