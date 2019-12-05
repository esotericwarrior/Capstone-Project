import { CSRF_TOKEN } from "./csrf_token.js";
import axios from 'axios';

async function getJSON(response) {
  if (response.status === 204) return "";
  return response.json();
}

function apiService(endpoint, method, data) {
 var content_type;
 if (method == "POST") {

  if (endpoint == "/api/posts/") {
    content_type = "multipart/form-data"
  }
  else {
    content_type = "application/json"
  }

  return axios.post(endpoint,
    data,
    {
       headers: {
          "Content-Type": content_type,
          "X-CSRFTOKEN": CSRF_TOKEN
       }
    })
  }
  else if (method == "PATCH"){

    if (endpoint.includes("/api/posts/")) {
      content_type = "multipart/form-data"
    }
    else {
      content_type = "application/json"
    }

    return axios.patch(endpoint,
      data,
      {
         headers: {
            "Content-Type": content_type,
            "X-CSRFTOKEN": CSRF_TOKEN
         }
      })
  }
  
  else {
    const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      "content-type": "application/json",
     "X-CSRFTOKEN": CSRF_TOKEN
    }
  };
  return (
    fetch(endpoint, config)
      .then(getJSON)
      // eslint-disable-next-line no-console
      .catch(error => console.log(error))
  );
 }
}

async function imgurService(data) {
  return axios.post("https://api.imgur.com/3/image",
    data,
    {
       headers: {
        "Authorization": "Bearer 931ddfab9e19c9a7512147c83459ce1d457e09cf"
       }
    })
}

export { apiService };
export { imgurService };
