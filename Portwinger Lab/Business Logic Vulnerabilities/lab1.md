# Lab: Excessive trust in client-side controls
url: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls

# Overview:
- This lab doesnt adequately validate user input
- You can exploit a logic flaw in its purchasing workflow to buy item for an unintended price
- Buy a "Lightweight l33t leather jacket"
- credentials: wiener:peter

# Analysis:

workflow: view item -> add item to cart(param: item Id, price(can exploit here)) -> open cart -> purchase

- intercept the POST request to our cart
- and then change price number field
-> <ok>

# How to avoid:
- validate user input to confirm the correct price of items

