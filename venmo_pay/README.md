# Function for venmo payment


## Context


## Details



### Input Arguments
```
venmo_handle: <str> The Venmo handle of the person to whom we are going to make the payment.
amount: <str> The amount to be sent to the person.
```

### Behaviour
It does the following:
1. Logs into Venmo
2. Go to `https://account.venmo.com/pay`
3. Click on `To`
2. Enter the venmo_handle.
4. Enters the message in `What's this for?`.
5. Clicks on `Pay`.
6. (UNSURE), there might be a step where you are asked to verify / warnings. Click on Send Anyway.


### Response