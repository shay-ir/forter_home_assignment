// ==UserScript==
// @name         Find Google cookie
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  log if the browser is connected to a Google account
// @author       Shay Ingber
// @match        https://www.fiverr.com/
// @grant        none
// ==/UserScript==


// the cookie getter code was found online (stack overflow).
function getCookie(c_name)
{
    var i,x,y,ARRcookies=document.cookie.split(";");

    for (i=0;i<ARRcookies.length;i++)
    {
        x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
        y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
        x=x.replace(/^\s+|\s+$/g,"");
        if (x==c_name)
        {
            return unescape(y);
        }
     }
}

(function() {
    'use strict';
    if (Boolean(getCookie("_gac_UA-12078752-1"))){
	console.log("Connected to a Google account");
} else {
	console.log("Not connected to a Google account");
}
})();