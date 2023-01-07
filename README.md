<h2> SendMailWithApiGateway</h2>
<hr>
<b>step 1: </b>create a lambda function with sending mail code.<br>
<b>step 2:</b> create API gateway with Http protocol.<br>
<b>step 3:</b> Trigger API gatway with Lambda function.<br>
<b>step 4: </b>send Http request with suffix url lambda function name and parameter ex. "https://dy159uexecute-api.us-east-1.amazonaws.com/regSuccess?name=nameofperson&email=emailofperson ".<br>


