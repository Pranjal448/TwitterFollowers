# TwitterFollowers
Want to get @usernames of all the your followers or all your followings? This git repo is for you. 

1. First clone the git. 

2. Open Firefox. Install "Cookie-Editor" add-on.
Go to https://x.com/<your-username-without-@>/following
Now, click on cookie-editor extension.
Click on Export. Select Netscape. Now the netscape code is copied.

Now create a twitter_cookies.txt file and paste the netscape code in there.


3. Edit create_json.py file.
create_json file needs 3 things from you - your twitter user ID, your url, your authorization token.

a) You can use this website to check your user ID (https://twiteridfinder.com/) and paste in create_json.py

b) Go to https://x.com/<your-username-without-@>/following
Press f12 to open developer tools, make sure to refresh.
Go to network, search/filter https://x.com/i/api/graphql/
Under GET requests, you will find file "Following?=variables...", click that.
Now in the headers section, you will see "filename: /i/api/graphql/<some-string>/Following"
Copy this <some-string>, and replace with <enter-GraphQL-operation-ID>

c) Go to https://x.com/<your-username-without-@>/following
Press f12 to open developer tools, make sure to refresh.
Go to network, search/filter https://x.com/i/api/graphql/
Under GET requests, you will find file "Following?=variables...", click that.
Now in headers section, scroll further down to Request Headers section.
You will see your bearer token there as "Bearer AAAAAAAAAAAAA....", copy this bearer token and replace with <enter-bearer-token>

4. Now just execute the create_json.py file. (make sure you have all imported libraries installed)
python3 create_json.py
It will create a file called all_followings_raw.json

6. Now execute the file extract_usernames.py to extract all @usernames from the all_followings_raw.json file
python3 extract_usernames.py 
