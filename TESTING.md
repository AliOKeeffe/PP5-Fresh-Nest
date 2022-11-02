# Testing

## User Story Testing

### EPIC | Viewing and Navigation
*As a Site User, I can intuitively navigate around the site so that I can find content.*

- A navigation bar is visible on every page of the site which is fully responsive on different screen sizes.

![header](docs/readme_images/features/header.png)

*As a Site User, I can view a list of products so that I can select a product to view.*

- When the user navigates to the all products page they are presented with a list of all products from the database.

![all products](docs/readme_images/features/products_all.png)

*As a shopper, I can click on a product so that I can read the full product details.*
- When the user clicks on an individual product they are taken to the full product details.

![Product Detail](docs/readme_images/features/product_detail.png)

*As a shopper I can view a specific category of products so I can browse the type of products I'm looking for.*
- When clicking the 'Home Decor' link in the navbar the dropdown menu will show all the different categories. Clicking any of these will take the user to the products page, showing only items from the category selected. The category selected will display as the page heading.

![Categories](docs/readme_images/features/categories.png)

![products](docs/readme_images/features/products.png)
 
*As a shopper I can search all products so that I can find what I am looking for*
- Located above the navbar is a search bar. On smaller screens, this bar becomes a search icon which when clicked will drop down the full bar. Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.

![Search](docs/readme_images/features/search.png)

*As a shopper, I can sort all products so that I can view products based on price or title.*
- A sort box is located on the products page where users can sort all products by price in ascending or descending order and by title (A-Z). 

![sort](docs/readme_images/features/sort.png)

*As a site user, I can view a list of Interior Design Services provided so I can understand what each service entails and make an enquiry if desired.*
- When the user navigates to the Interior Design Services page they are presented with a list of all Interior Design Services from the database along with detailed descriptions. An "Enquire Now" button displays beside each service which will take the user to the Contact form when clicked.

![Design Services](docs/readme_images/features/design_services.png)

*As a site user, I can read testimonials left by other customers so I see what feedback they gave on the Interior Design Services they received.*
- When the user navigates to the Testimonials page they can see testimonials left by previous clients. Each testimonial displays the Design Service they relate to, the date and the user's name.

![Testimonials](docs/readme_images/features/testimonials.png)

*As a site user, I can view pictures of previous interior design projects so that I can see if I like the results and build trust in the service provider.*
- When the user clicks on the Interior Design Projects tab in the nav bar they are taken to a page displaying pictures of previous projects completed by Fresh Nest.
- When the user hovers over the image on Desktop view, the type of design service and location will appear in the centre of the image.
- When the user views the page on mobile, the type of design service and location will display below the image.

![Design Projects](docs/readme_images/features/design_projects.png)


### EPIC | User Account and Profile
*As a site user I can register an account so that I can have a personal account.*
- A sign up button is located in the user options drop down menu in the Navbar. When the user clicks the button they are taken to the sign up page.

![Sign Up](docs/readme_images/features/sign_up.png)

*As a site user I can log in or log out of my account so that I can keep my account secure.*
- If the user has registered an account they can log in or log out by clicking the links in the user options drop down menu in the Navbar.

![Sign In](docs/readme_images/features/sign_in.png)
![Sign Out](docs/readme_images/features/sign_out.png)

*As a site user I can see my login status so that I know if I'm logged in or out.*

- Whenever a user logs in or logs out a toast message will appear notifying the user or their action.
- Their user name will display in the navbar.
- When signed in the options in the user menu will change to show Profile and Log Out buttons.

![Logged In](docs/readme_images/features/logged_in.png)

*As a site user I can save my personal details in my user profile so that I do not have to fill them out for future orders.*
- Users can fill in their personal details on their profile page. This information will be prepopulated for any future orders.
- When placing a new order, a checkbox under the delivery information can be checked to save the information just added.

![Delivery Details](docs/readme_images/features/delivery_info.png)

*As a site user I can view my order history so that I can remember what purchases I've made.*

- Once a user has created an account and placed an order, they can view the order history on their profile page.
- Clicking the order number will take you to a summary page of that order.

![Order History](docs/readme_images/features/order_history.png)

*As a site user I can recover my password in case I forget it so that I can recover access to my account.*
- On the sign-in page, a link to recover your password is located underneath the sign-in button. This uses the AllAuth functionality to reset the user's password. 

### EPIC | Purchasing
*As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.*

- Within the product detail page there is a quantity selector and an Add to Bag button. Shoppers can adjust the quantity by using the buttons located on either side of the input, or by typing in the amount.
- When the user clicks on the add to bag button, the chosen quantity of the product is added to the user's shopping bag.

![Product Detail](docs/readme_images/features/product_detail.png)

*As a shopper I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.*

- As the user adds products to their bag, a toast message appears in the top right-hand corner of the screen informing the user that the item has been added, giving them a snapshot of the bag contents and the total cost of the bag.

![bag total](docs/readme_images/features/bag_total.png)

*As a shopper I can view the contents of my shopping bag at any time so I can see what is included and the total cost.*
- When the user clicks on the shopping bag icon in the nav bar they are taken to the shopping bag page which shows the products which the user has added to their cart, unit price, quantity and subtotal.
- The bottom of the page shows the bag total, delivery costs and then the grand total.

![shopping bag](docs/readme_images/features/shopping_bag.png)

*As a shopper I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.*
- When the user is viewing the shopping bag, they are able to adjust the quantity of each product line item and update the subtotal by clicking the update icon.
- The user is able to delete the product by clicking the bin icon and the bag should be updated accordingly.

![Update Delete buttons](docs/readme_images/features/update_delete_buttons.png)

*As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.*
- On the Checkout page the user can see a summary of the line items within their order including a thumbnail image, the product name, the quantity, the unit cost and the overall total order cost on the right-hand side.

![checkout](docs/readme_images/features/checkout.png)

*As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.*
- When the user navigates to the checkout page, they can see the Stripe Elements UI where they can enter their card details securely and pay for their order.
- The user receives feedback if the card number is valid/invalid.

*As a shopper checkout as a guest so I don't have to sign up for an account.*
- Shoppers do not need an account to purchase any items. Regardless of whether a user is signed in, the checkout process remains the same.
-  When the user completes the checkout form and presses submit their order should be completed.

*As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.*
- When the user submits the checkout form, they are redirected to a Checkout Success page where they can see an order confirmation and a summary of their order.

![order_confirmation](docs/readme_images/features/order_confirmation.png)

*As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.*
- When the user has submitted their order they will receive a confirmation email to the email address they entered in their order form containing all the details of the order.

### EPIC | Admin & Store Management
*As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.*
- When the site owner is logged in, a Home Decor Management option appears in the User drop-down menu.
- When the site owner navigates to the Home Decor Management page they can add a new product to the store through a user-friendly form. 

![add product](docs/readme_images/features/add_product.png)
- The site owner is able to edit and delete products by clicking buttons on both the main Home Decor page and also the product detail page.
- The edit form is pre-populated with the product information.

![edit product](docs/readme_images/features/edit_product.png)
![delete product](docs/readme_images/features/delete_product.png)

*As a site owner, I can add/edit/delete interior design services provided through an easy-to-use interface so that I can manage the site's contents.*
- When the site owner is logged in, a Design Service Management option appears in the User drop-down menu.
- When the site owner navigates to the Design Service Management page they can add a new design service to the site through a user-friendly form. 

![Add Service](docs/readme_images/features/add_service.png)
- The site owner is able to edit and delete services by clicking buttons on the Interior Design Services page.
-  The edit forms fields are pre-populated with all service information. 

![edit Service](docs/readme_images/features/edit_service.png)
![Delete Service](docs/readme_images/features/delete_service.png)

*As a site owner, I can add/delete images and location of previous design projects so that I can manage the site's contents.*
- When the site owner is logged in, a Previous Project Management option appears in the User drop-down menu.
- When the site owner navigates to the Previous Project Management page they can add details of a previous project to the site. through a user-friendly form. 

![Add Project](docs/readme_images/features/add_project.png)
- The site owner is able to delete project images from the Previous Projects page by clicking the 'x' in the top right-hand corner of the picture.

![Delete Project](docs/readme_images/features/delete_project.png)

*As a site owner, I can view and delete customer enquiries on the front-end without having to access the admin panel.*
- When the site owner is logged in, an Enquiries Management option appears in the User drop-down menu.
- When the site owner navigates to the Enquiries Management page they can see a list of user enquiries sorted from newest to oldest.
- Emails that have been read are greyed out.

![Enquiries Dashboard](docs/readme_images/features/enquiry_dashboard.png)
- When the site owner clicks on an enquiry they are taken to the individual enquiry detail.
- The site owner can choose to delete the enquiry or to go back to the list of enquiries.

![Enquiry Detail](docs/readme_images/features/enquiry_detail.png)

### EPIC | User Interaction
*As a site user, I can submit an enquiry form so that I can contact the site owner.*
- A user can open up the contact form by clicking on the "Enquire Now" button on the Interior Design Services page or by clicking the 'Contact' button in the Nav bar.
- The user can select the type of enquiry from a drop-down menu so that the site owner knows what the enquiry is about.
- If the user is logged in, their email address is prepopulated.
- When the form is submitted, the user receives an email confirmation of their enquiry so that they have a record of it.

![Enquiry Form](docs/readme_images/features/enquiry_form.png)

*As a site user, I can add / edit / delete a testimonial in relation to a consultation I received so that I can give my feedback.*
- When a logged-in user clicks on the "Add Testimonial" button on the Testimonials page, they can see a user-friendly form where they can add a new Testimonial to the site.

![Add Testimonial](docs/readme_images/features/add_testimonial.png)
- If the user is not logged in they are redirected to the log-in page.
- The user is able to edit and delete their own testimonials from buttons on the Testimonials Page.
- The edit forms fields are pre-populated with testimonial information.

![Edit Testimonial](docs/readme_images/features/edit_testimonial.png)
![Delete Testimonial](docs/readme_images/features/delete_testimonial.png)
- The completed testimonial is automatically populated with the user's username and date underneath the body.

![Testimonials](docs/readme_images/features/testimonials.png)

*As a user, I can sign up for the website's newsletter so that I can keep up to date with new products and promotions*
- In the footer is a 'Newsletter' section. Here the user can input their email address to sign up.

![footer](docs/readme_images/features/footer.png)

## Validator Testing
### HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                           | Logged Out | Logged In |
|--------------------------------|------------|-----------|
| Home                           | No Errors  | No Errors |
| Products                       | No Errors  | No Errors |
| Product Detail                 | No Errors  | No Errors |
| Add Product                    | N/A        | Note      |
| Edit Product                   | N/A        | Note      |
| Confirm Delete Product         | N/A        | No Errors |
| Bag                            | No Errors  | No Errors |
| Checkout                       | No Errors  | No Errors |
| Checkout Success               | No Errors  | No Errors |
| Profile                        | N/A        | No Errors |
| Order History                  | N/A        | No Errors |
| Interior Design Services       | No Errors  | No Errors |
| Add Interior Design Service    | N/A        | Note      |
| Edit Interior Design Service   | N/A        | Note      |
| Delete Interior Design Service | N/A        | No Errors |
| Interior Design Projects       | No Errors  | No Errors |
| Add Interior Design Project    | N/A        | Note      |
| Delete Interior Design         | N/A        | No Errors |
| Testimonials                   | No Errors  | No Errors |
| Add Testimonial                | N/A        | No Errors |
| Edit Testimonial               | N/A        | No Errors |
| Delete Testimonial             | N/A        | No Errors |
| Contact                        | No Errors  | No Errors |
| Enquiries Dashboard            | N/A        | No Errors |
| Enquiry Detail                 | N/A        | No Errors |
| Sign In                        | No Errors  | N/A       |
| Sign Up                        | No Errors  | N/A       |
| Log Out                        | N/A        | No Errors |
| Password Reset                 | No Errors  | N/A       |
| 400.html                       | No errors  | No errors |
| 403.html                       | N/A        | No errors |
| 404.html                       | No errors  | No errors |
| 500.html                       | No errors  | No errors |

Note: Image upload widget errors

All forms which include an image upload field show the same error below. This relates to the image upload widget on the form and thus changing the code breaks the field.

![HTML Error](docs/readme_images/add_image_html_error.png)

## CSS

No errors were found when passing my CSS files through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

*base.css*
![base.ccs validation](docs/readme_images/base_css_validation.png)

*checkout.css*
![checkout.ccs validation](docs/readme_images/checkout_css_validation.png)

*profile.css*
![profile.ccs validation](docs/readme_images/profile_css_validation.png)


## JSHINT
All Javascript was passed through [Jshint](https://jshint.com/) with no issues.

**Base**

![base.html JS validation](docs/readme_images/js_validation/base.html_js.png)

**Products**

![products.html JS validation](docs/readme_images/js_validation/products_js.png)

**Profile**

![profile JS validation](docs/readme_images/js_validation/profile_js.png)

**Checkout**

![Checkout JS validation](docs/readme_images/js_validation/stripe_elements.js_js.png)

**Bag**

![Bag JS validation](docs/readme_images/js_validation/bag.html_js.png)

**Quantity Input**

![Quantity Input JS validation](docs/readme_images/js_validation/quantity_input_script.html_js.png)

**Image Selector**

![Image Selector JS validation](docs/readme_images/js_validation/add_image_js.png)


## Python Validation - Pycodestyle
Python testing was done using Pycodestyle to ensure there were no syntax errors.

The only errors displayed (as per below screenshot) can be ignored as the are within automatically generated files with the exception of env.py. 

I have ignored the the formatting errors related to env.py as they relate to my Secret Keys and Database URL being to long. This file is not committed to github.

![Python Linter Errors](docs/readme_images/python_linter_errors.png)

## Fixed Bugs

### Update bag quantity

I wanted the bag subtotal to automatically update when the product quantity was changed rather than clicking an 'update' link. To do this I wrote an AJAX Post method to request the 'adjust bag' url and populate it with the updated quantity and item id and reload the page. 

When I first attempted to do this I put a click listener on the + and - buttons so the page would automatically update when these were clicked. However I quickly ran into issues due to the fact that there was already a click listener on those buttons (which updates the quantity in the box). After some research I discovered that this issue is called a race condition "an undesirable situation that occurs when a device or system attempts to perform two or more operations at the same time".

In order to solve this problem I removed the click listener which updated the bag total and instead created a new function 'Update Bag' which is called when the +/- is clicked (but after the quantity box is updated). Two parameters are passed into the function (quantity and item ID) and the AJAX method within the function uses these parameters to update the bag total. 

### Deployment

When I initially attempted to deploy to Heroku the build would fail with the error message "Could not build wheels for backports.zoneinfo". This was due to the fact that Heroku by default uses python version 3.10 which isn't compatible with backports.zoneinfo. In order to fix this I had to create a runtime.txt to specify the Python version for Heroku to install (python-3.8.13). However the next time I tried to deploy I got a further error "Requested runtime 'python-3.8.13' is not available for this stack (heroku-22)". After some research I realised that in order to use this version of Python I would have to use heroku-20 instead of heroku-22. I was able to downgrade the heroku version using the command `heroku stack:set heroku-20 -a app name` which resolved the issue and I was able to deploy the site. 

prevent whitespace 
https://stackoverflow.com/questions/19619428/html5-form-validation-pattern-alphanumeric-with-spaces

### Checkout form
When testing the Checkout Form, I was able to input white space into into the form text fields and enter text into the phone number field and still submit the form. This would then return a 500 error however the Stripe payment would still get processed. I had followed the steps in the Boutique Ado project for the checkout app and when I tested the Boutique Ado project and a number of other students projects the same situation would arise when I submitted with form with just whitespace in the form fields. 

I wrote a custom `clean_fieldname` method for a number of the form fields in order to `trim` whitespace from the form fields during form validation. 

``` 
    def clean_full_name(self):
        if not self.cleaned_data['full_name'].strip():
            raise ValidationError("You must enter a fullname")
        return self.cleaned_data['full_name']
```

However this didn't solve the issue as I realised that the form validation wasn't actually getting called before the payment was processed. 

After a bit of digging I discovered that the reason for this is due to the fact the Stripe Javascript is called when the submit button is clicked due to the event listener on the submit button. The Javascript prevents the default form submission meaning that the card is actually charged before any form validation is done. 

When the response comes back from Stripe, the `.then()` part of the JS runs, which checks to see if the card was charged successfully, and if so, the form is then submitted and validation is ran. If the form is valid, it saves the order to the database. If the validation fails webhook will create the order in the database anyway.

As a work around in the short term I was able to add a widget to the form fields in the Checkout Form to specify the pattern attribute of the HTML input. This prevents the form from submitted if there is whitespace at the beginning of a text input or if there is letters in the phone field.

```
        self.fields['full_name'].widget.attrs[
            'pattern'] = "([^\\s][A-z0-9À-ž\x27\\s]+)"
        self.fields['street_address1'].widget.attrs[
            'pattern'] = "([^\\s][A-z0-9À-ž\x27\\s]+)"
        self.fields['town_or_city'].widget.attrs[
            'pattern'] = "([^\\s][A-z0-9À-ž\x27\\s]+)"
```

I found [this](https://stackoverflow.com/questions/19619428/html5-form-validation-pattern-alphanumeric-with-spaces) stackoverflow post helpful when learning about the pattern attribute.

Ideally I would have preferred to find a way to perform full form validation before the payment is processed however due to time contraints I was unable to figure out a work around for the purpose of this project. A suggestion would be to create the order in the database `on submit` with a status of "Pending" and then process the Payment. Once the payment is processed successfully, update the order status to "complete" in the database. 

