import jwt_decode from 'jwt-decode';
import { apiRequest } from "./api/apiRequest.js";

export default function tokenIsValid() {
    let token =localStorage.getItem('token');
    
    try {
        let dateNow = new Date();
        let decodedToken = jwt_decode(token);
        if(decodedToken.exp < dateNow.getTime() - decodedToken.orig_iat){
            return true;
        }
        return false;
    }
    catch(err) {
        return false;
    }
    
};

export function userFromToken() {
    let token =localStorage.getItem('token');
    let decodedToken = jwt_decode(token);
    let user = {
        id : decodedToken.user_id,
        email : decodedToken.email,
    }
    return user;
};



export function getUserProfileAPIRequest(id) {
let endpoint = "/api/persons/";

let req = new apiRequest();
req.open("GET", `${endpoint}${id}/`);

req.addEventListener("readystatechange", function () {
    if (this.readyState === 4) {
    if (this.status === 200) {
        let profile = JSON.parse(this.responseText)[0];
        document.getElementById("userNameDisplay").innerHTML =
        "Welcome " + profile.firstName + " " + profile.lastName;
    }
    }
});

req.send();
}