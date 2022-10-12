## User Experience (UX)

A visitor to Fresh Nest would be someone who is most likely an adult who....

### User Stories

#### EPIC | Viewing and Navigation
- As a Site User, I can intuitively navigate around the site so that I can find content.
- As a Site User, I can view a paginated list of products so that I can select a product to view.
- As a shopper, I can click on a product so that I can read the full product details.
- As a shopper I can view a specific category of products so I can browse the type of products I'm looking for.
- As a shopper I can search all products so that I can find what I am looking for.
- As a shopper, I can sort all products so that I can view products based on price or title.
- As a site user, I can view a list of Interior Design Services provided so I can understand what each service entails and make an enquiry if desired.
- As a site user, I can read testimonials left by other customers so I see what feedback they gave on the Interior Design Services they received.
- As a site user, I can view pictures of previous interior design projects so that I can see if I like the results and build trust in the service provider.

#### EPIC | User Account and Profile
- As a site user I can register an account so that I can have a personal account.
- As a site user I can log in or log out of my account so that I can keep my account secure.
- As a site user I can see my login status so that I know if I'm logged in or out.
- As a site user I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- As a site user I can view my order history so that I can remember what purchases I've made.
- As a site user I can recover my password in case I forget it so that I can recover access to my account.

#### EPIC | Purchasing
- As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.
- As a shopper I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.
- As a shopper I can view a the contents of my shopping bag at any time so I can see what is included and the total cost.
- As a shopper I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.
- As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
- As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.
- As a shopper checkout as a guest so I don't have to sign up for an account.
- As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.
- As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.


#### EPIC | Admin & Store Management
- As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.
- As a site owner, I can add/edit/delete interior design services provided through an easy-to-use interface so that I can manage the site's contents.
- As a site owner, I can add/delete images and location of previous design projects so that I can manage the site's contents.
- As a site owner, I can view and delete customer enquiries on the front-end without having to access the admin panel.

#### EPIC | User Interaction
- As a site user, I can submit an enquiry form so that I can enquire about a design consultation.
- As a site user, I can add / edit / delete a testimonial in relation to a consultation I received so that I can give my feedback.


#### User stories not yet implemented
- As a shopper I can add products to my saved items so that I can go back and view them at a later date.
- As a shopper I can view my saved products so I can find them easily in the one location.













# Fixed Bugs

## Update bag quantity

I wanted the bag subtotal to automatically update when the product quantity was changed rather than clicking an 'update' link. To do this I wrote an AJAX Post method to request the 'adjust bag' url and populate it with the updated quantity and item id and reload the page. 

When I first attempted to do this I put a click listener on the + and - buttons so the page would automatically update when these were clicked. However I quickly ran into issues due to the fact that there was already a click listener on those buttons (which updates the quantity in the box). After some research I discovered that this issue is called a race condition "an undesirable situation that occurs when a device or system attempts to perform two or more operations at the same time".

In order to solve this problem I removed the click listener which updated the bag total and instead created a new function 'Update Bag' which is called when the +/- is clicked (but after the quantity box is updated). Two parameters are passed into the function (quantity and item ID) and the AJAX method within the function uses these parameters to update the bag total. 

## Deployment

When I initially attempted to deploy to Heroku the build would fail with the error message "Could not build wheels for backports.zoneinfo". This was due to the fact that Heroku by default uses python version 3.10 which isn't compatible with backports.zoneinfo. In order to fix this I had to create a runtime.txt to specify the Python version for Heroku to install (python-3.8.13). However the next time I tried to deploy I got a further error "Requested runtime 'python-3.8.13' is not available for this stack (heroku-22)". After some research I realised that in order to use this version of Python I would have to use heroku-20 instead of heroku-22. I was able to downgrade the heroku version using the command `heroku stack:set heroku-20 -a app name` which resolved the issue and I was able to deploy the site. 



## Marketing Strategy

A number of different marketing strategies have been utilised to promote Fresh Nest including SEO, content marketing, social media marketing and email marketing. Each of these strategies have been discussed individually below:  

### SEO
Several SEO techniques were undertaken in order to ensure the site ranks highly in search engine results:

**Keywords:** 

A mixture of short tail and long tail keywords were carefully considered for the site. Keyword research was performed by checking Google search results, looking at competitor's keywords and by utilising wordtracker.com. 

An initial list of topics and keywords generated can be seen below. This list was then refined based on relevance and authority.

The most relevant keywords have been added to the site's meta-keywords and meta-description. These keywords have also been carefully included in page titles, headings, site content, `<strong></strong>` tags, image alt attributes and anchor tag links across the site. 

 ![Keywords](docs/readme_images/seo_keywords.png)

**External Links:**

Included in the site footer are links to other high quality relevant websites including Houzz, Institute of Designers Ireland, and The Interiors Association. Thes links show search engines that the page is of good quality improving the site's ranking futher. 

**Building Trust:**

In order to build brand trust, a testimonal page for interior design services has been included in the site with a link to the page being included in the page footer as well as the main nav bar. 

The page footer also includes links to the privacy policy to inform users about how their data is being collected and processed.

**Sitemap and robots.txt**

A sitemap file with a list of important page URLs was created to ensure that search engines are able to understand the site's structure and easily navigate through the site. This was made using xml-sitemaps.com.

A robots.txt file was created to tell search engines where the are not allowed to go on the website. This improves SEO by increasing the quality of the site

### Content marketing 
The site showcases high quality images of previous interior design projects projects in order to attract potential new clients. The photos allow the business to show off their expertise and style and build up trust with the customer.

### Social Media Marketing 
For this site, a Facebook business page has been created for organic social media marketing. The Facebook page includes a 'Shop Now' button which takes the user to the Fresh Nest website. The page pairs well with the content media marketing on the main site as images of previous projects and new product arrivals can be shared easily.

![Facebook Page](docs/readme_images/facebook_page.png)

### Email Marketing
Visitors to the site can sign up to the newsletter and do not need to have an account to do so. A signup box is included in the footer of the site. This allows the business to share news with customers and potential customers including new products/services and special offers. Mailchimp was used to create this service. 
