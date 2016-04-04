import argparse, csv, pocket

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('consumer')
# parser.add_argument('token')

args = parser.parse_args()

# write here your consumer key and access token
# you can get consumer key by loging to your pocket account and creating an app at getpocket.com/developer 
# to get token you can go to: reader.fxneumann.de/plugins/oneclickpocket/auth.php and paste your consumer key

# consumer_key = raw_input("Write your consumer key: ")
# token = raw_input("Write your secret token:? ")

request_token = Pocket.get_request_token(consumer_key=args.consumer, redirect_uri="localhost")
print request_token
# URL to redirect user to, to authorize your app
auth_url = Pocket.get_auth_url(code=request_token, redirect_uri="localhost")

user_credentials = Pocket.get_credentials(consumer_key=args.consumer, code=request_token)

access_token = user_credentials['access_token']


p = pocket.Pocket(args.consumer, args.token)

dataReader = csv.reader(open(args.filename), delimiter=',', quotechar='"')
for row in dataReader:
    # Adds articles from file
    p.add(row[0])
