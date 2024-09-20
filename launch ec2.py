from flask import Flask, request, jsonify, render_template
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('launch_ec2.html')

@app.route('/launch_ec2', methods=['POST'])
def launch_ec2():
    data = request.get_json()
    
    aws_access_key = data.get('aws_access_key')
    aws_secret_key = data.get('aws_secret_key')
    region = data.get('region')
    instance_name = data.get('instance_name')

    if not all([aws_access_key, aws_secret_key, region, instance_name]):
        return jsonify({'error': 'All fields are required!'}), 400

    try:
        # Create a new EC2 resource using the provided credentials and region
        ec2 = boto3.resource(
            'ec2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )

        # Launch the EC2 instance
        instance = ec2.create_instances(
            ImageId='ami-0ec0e125bb6c6e8ec',  # Use a valid AMI ID for the region
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='myec2.ppk',  # Replace with a valid key pair
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': instance_name}]
            }]
        )

        # Wait until the instance is running
        instance[0].wait_until_running()

        return jsonify({'message': f'Instance {instance_name} launched successfully!'}), 200

    except NoCredentialsError:
        return jsonify({'error': 'Invalid AWS credentials'}), 401

    except ClientError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
