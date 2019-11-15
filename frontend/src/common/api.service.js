import { CSRF_TOKEN } from "./csrf_token.js";
import axios from 'axios';

async function getJSON(response) {
  if (response.status === 204) return "";
  return response.json();
}

function apiService(endpoint, method, data) {
 if (method == "POST"){
  // eslint-disable-next-line no-console
 //console.log(data.get("content"))
 // eslint-disable-next-line no-console
// console.log(data.get("file"))
  var content_type;

  if (endpoint == "/api/posts/"){
    content_type = "multipart/form-data"
  }
  else{
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

export { apiService };

