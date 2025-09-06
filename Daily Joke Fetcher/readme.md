```python
import requests
response = requests.get("https://official-joke-api.appspot.com/jokes/random")
data = response.json()

print(data)
print(type(data))

print(data["setup"]+"😎")
print(data["punchline"]+"🤣😂")
```  
Output👇
``` 
{'type': 'general', 'setup': 'What do you call fake spaghetti?', 'punchline': 'An impasta.', 'id': 450}
<class 'dict'>
What do you call fake spaghetti?😎
An impasta.🤣😂
```

🟢Repository link of API used 👉[official_joke_api](https://github.com/15Dkatz/official_joke_api?ref=freepublicapis.com) 

code explanation in my own words and researching

```python
import requests
```
- `requests` is a popular python library.
- Used for making **HTTP**(Hypertext Transfer Protocol) requests to webpages,API's,Web servers.
- `requests' is used for:
    - Accessing webpages programatically
    - Consuming REST APIs (GET, POST, PUT, DELETE)
    - Sending data (like form data or JSON) to servers
    - Downloading files from the internet
    - Handling authentication, cookies, and sessions

## More explanation for me about the points  
- **Accessing webpages programatically** - By using a python script(.py file) we can send an HTTP request to a webpage,API,web server WITHOUT having to open a web browser and cliking on the link.  
- **Consuming REST APIs (GET, POST, PUT, DELETE)** - `requests` library is usually used to interact with REST APIs(Representational State Transfer API).  

>Common HTTP methods in REST APIs are: ( GPPD )
>1. GET -> Retrieve data.Used to fetch information from the server.  
>
>2. POST -> Send data.Used to create new data on the server.  
>
>3. PUT -> Update data.Used to replace existing data with new data.  
>
>4. DELETE -> Remove data.Used to delete a record from the server.

- **Sending data (like form data or JSON) to servers** - A server can not only **send information to the user** but also the user can **send information to the server** for processing.Browsers send data(eg: after filling a sign up form) to the server using `form-data` format.Now many APIs use JSON (JavaScript Object Notation)format which is structured text ,it is easier for programs to process.

- **Downloading files from the internet** - We can write a python script for fetching a file from a URL and save it locally without opening a browser typing the link clicking on download.

- **Handling authentication, cookies, and sessions**
    - When a webiste or app is visited the server needs to know who we are.Here **authentication** is used to prove user identity eg:by entering username and password/by providing an API key.Without authentication the server will not allow  use to access private info.
    - After logging into a website or an app the server does not want to keep asking for the password everytime so it gives the user a small piece of information called **Cookie**.This cookie acts like a ticket that tells i am already logged in.The browser or python program sends this cookie back automatically when  user makes another request.
    - A **Session** is a way to keep using those cookies and authentication details across multiple requests.With a session user only has to login once and the site remembers the user as he keep browsing.
        - Session is a _temporary state_ that the server and browser maintains while the user is logged in or interactig with the site.
        - The server creates a session ID(a random string) when user logs in.
        - The session ID is stored in a cookie in the user browser.
        - On every request the user makes(cliking links,opening webpages) te browser sends that cookie back to the server along with the request inside the request header.
        - The server looks at the session ID and says "Oh this is user1234 let me show his account page." if the browser requests for account page. 
```python
response = requests.get("https://official-joke-api.appspot.com/jokes/random")
```
- This line sends an HTTP GET request to the joke API and gets back a random joke in JSON format and stores the response inside the variable `response`
- `requests.get()` 
    - calling the `get` method from the `requests` library.
    - **GET** is an HTTP method used to __retrieve data__ from a server( eg:asking for a webpage or API response).
    - `https://official-joke-api.appspot.com` is the URL where i am  sending the GET request.This URL is of a PUBLIC API that returns joke in `JSON` format.
    - `https://official-joke-api.appspot.com/jokes/random` is the API endpoint(different from above URL this one has .com/jokes/random).When this API endpoint is visited through a browser the server responds with a random joke in JSON {
  "id": 123,
  "type": "general",
  "setup": "Why don't scientists trust atoms?",
  "punchline": "Because they make up everything!"
}  
- `response = `
    - the result of response.get() call is stored in the variable `response`.`reponse` variable is  storing a `Response object`.

```python
data = response.json()
print(data)
print(type(data))
```
- `response.json()` method converts the `response` object got from `requests.get()` but now currently stores in`response` variable from **JSON** text to **Python dictionary**.
- After conversion the it is stored in variable `data`.That variable is now a python dictionary.
- `print(data)` outputs this dictionary with key and values`{'type': 'general', 'setup': 'What do you call fake spaghetti?', 'punchline': 'An impasta.', 'id': 450}`
- `print(type(data))` this code outputs `<class 'dict'>`.This tells it is a dictionary now.

```python
print(data["setup"]+"😎")
print(data["punchline"]+"🤣😂")
```
- `print(data["setup"]+"😎")` means in the dictionary `data` use the key 'setup' and fetch it's value and concatenate the emoji at the end.
- `print(data["punchline"]+"🤣😂")` means in the dictionary `data` use the key 'punchline` and fetch it's value and concatenate the emojis at the end.

Note
about urllib and requests
about REST APIs