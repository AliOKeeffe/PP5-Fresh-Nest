# Fixed Bugs

## Update bag quantity

I wanted the bag subtotal to automatically update when the product quantity was changed rather than clicking an 'update' link. To do this I wrote an AJAX Post method to request the 'adjust bag' url and populate it with the updated quantity and item id and reload the page. 

When I first attempted to do this I put a click listener on the + and - buttons so the page would automatically update when these were clicked. However I quickly ran into issues due to the fact that there was already a click listener on those buttons (which updates the quantity in the box). After some research I discovered that this issue is called a race condition "an undesirable situation that occurs when a device or system attempts to perform two or more operations at the same time".

In order to solve this problem I removed the click listener which updated the bag total and instead created a new function 'Update Bag' which is called when the +/- is clicked (but after the quantity box is updated). Two parameters are passed into the function (quantity and item ID) and the AJAX method within the function uses these parameters to update the bag total. 