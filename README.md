
# Mobile Central
---
permalink: /index.html
---

A online shop's portal specilaized in mobile phones.  
The main typologies of the products on sale are Smartphones and old-fashioned flip phones/lcd display phones, collectively grouped under the nostalgic header "GSM".
Users can avail of navigation menu links to browse the site, search products, look up individual product descriptions, post comments, read and (as registered users) write products reviews, contact the store owner via the contact form.
The Website offers users the option of becoming registred users and thus being able of persisting their carts between visits, post reviews, and view/print their orders history.
It is not necessary to be a registred user to place an order.

The goals of the website are:
* to maximise sales with its presence on the internet; 
* showcasing products and thus raising public awareness of the Business;
* affiliate customers with the conveniences that come with a registered account. 

The goals of the website users are:
* quickly obtain visual clues and information on mobile phones on offer, such as product description and reviews left by other website users;
* easily complete purchase of products of interest.

---


## UX

There types of clientele sought are two : 

* enthusiast mobiles users who are always up to date with latest technologies and fashonable items on the market, these are prepared to spend a substantial amount of money for a well rounded product.
* common mobiles users who see the product more as a neccessity than a fancy thing to have; they will settle for a product that meet their minimal expectations with the least inpact on their finances. 

The website addresses the needs of both with a division in two main categories amd with a clear display of products from each in the landing page. Product descriptions and reviews are available to allow customers to make an informed decision. 
Customers can make specific queries via contact form.

### User Stories

As a .. | I want to .. | So I can ..
 --- | --- | --- 
New customer | Immediately learn the nature of the business | Determine quickly if the product I seek can be found in the store
Potential customer | easily navigate through the site | Find quickly the desired product/related information
Commited customer | easily and clearly be guided through the payment process | Finalize the transaction and secure the desired product
Potential customer | Avail of enough, to-the-point information on the merchandise | Make an informed decision on whether or not I should purchase a product
New/Returning Customer | Send specific queries to the store owner | Obtain more information than what found on the website/Leave feedback on my experience with the site
Registred User | Access my order history | Keep track of my expenses or resolve disputes
Registred User | Have my cart persited between visits | Do without having to restart the entire process when I make a resolute decision to buy
Store clerck | Access the store database | update prices and stock quantities, thus mainataining the information on the website up to date

### Wireframes

* [Landing page](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Landing+page+wireframe.png)
* [Categories](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Categories+page.png)
* [Contact page](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Contact+page+wireframe.png)
* [Contact page signed in](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Contact+page+Signed+In+wireframe.png)
* [Product page](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+product+page+wireframe.png)
* [Sign in page](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Sign+In+page+wireframe.png)
* [Sign up form](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Sign+Up+page+wireframe.png)
* [Cart page](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+cart+page+wireframe.png)
* [Thank You page](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+thank+you+page+wireframe.png)
* [Orders List](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Ordres+List+wireframe.png)
* [Add product](https://mmmp4.s3-eu-west-1.amazonaws.com/mmmp4Wireframes/MM+Add+Product+page+wireframe.png)

---

## Features

* The navigation bar, present at the top of all pages, includes: 
* * A Logo, in the shape of a Smartphone, is situated at the top left of the screen, the first item on the Navbar from the left. shows on all pages. On click, it redirects to a display of all the products on sale.
* * The Business' name "Mobile Central" second from the left on large screens, dead in the middle on small screens. On click, it brings back to the landing page, as a "Home" button would.
* * A collapsible dropdown menu containing links to  other sections of the website, submenus, and a search box. On small screens it shows collapsed as an hamburger button, while on large screens the first level items of the dropdown menu are displayed horizontally along the navbar.
* The Landing or "Home" page. 
* * It displays all products that have been marked by the store with the caption "New Arrival!". On this page, however, the caption does not appear on each product, to avoid a redundant and unsightly repetition.
* * The user is rather informed that these are the latest arrivals by a red header above the products' grid; it reads "Check Out the Latest Arrivals!". 
* * A hero image stands between the navbar and the page header. It contains a slide show of all the latest products. The slide show can be halted by hovering the mouse on it. Clicking on a product's slide will lead to that products's page. The hero slideshow fades away as the user scrolls down the page, and fades back in as the user scrolls back to the top. 
* * Two intuitive buttons just under the header are used to sort by highest or lowest price and by alphabetical or reversed alphabetical order. Once sorted, the sorting status is announced within the header. 
* * The products grid, containing all the products in row and column display. The grid is screen-width responsive. Each product's image is framed in a yellow bordered, rounded edge box with on a white background, with the products name, price and a "+" link at the bottom of the box. The "+" acts like an "Add to cart" button.
* * A "Back to the Top" button shows fixed at the bottom right corner. This only shows on pages higher than 1.5 times the viewport. On click, it scroll the page back to the top in a smooth manner.
* The Show_all_products page.
* * Accessed by clicking on the mobile icon (top left of the navbar), is similar to the landing page, except it diplays all the products on sale.
* * Accordingly, the hero image contains a slide show of all products, and the header reads "Showing all products".
* * All other features identical to the ones on the Landing page.
* The Categories, Brands and Search return pages, have identical structures and features to the landing pages, except:
* * There is no hero slideshow. 
* * The products returned are filtered by product type or brand (by clicking on the appropriate link on the navbar submenus), or are the result of the navbar's search box query.
* * Accordingly, the header reads the products' on display type or brand, or the search terms.
* The individual product page.
* * Accessed by clicking on the product's image from the products grid on each of the above pages.
* * Contains a page with the products image, description, price, relevant reviews, and:
* * an "Add to cart" link that, on click, simultaneously adds the product to and opens up the cart page.
* The cart page.
* * Accessed by the "Add to cart" link on the product page or by clicking on the cart icon on the navbar, which appears after a product is placed in the cart.
* * Composed of two main section,
* * * the first is a series of rows for each product in the cart, with their image, name, SKU, price, quantity in the cart, and cost subtotal, and the " + ", " - ", and trash icons. These icons' functions are to increase, decrease, or remove althogheter the product from the cart.
* * * the second component is the check out panel, with a written request to the user to review his order, the order total, a trash icon with associated cart emptying function on click, a button to initiate the 3rd party Stripe payment function, and a button to return to the landing page.
* * Two main parts are side by side on large screen, check out to the left, stacked on smaller screen, check out at the bottom.
* * On click, the check out button brings up small form from Stripe, where the user can enter his personal and shipping details, along with credit card detais. If the user is authenicated, his/her email will automatically fill the relevant field in the form. This is the key for future order details retrieval. By clicking "Pay" on the form, the transaction is processed, and the user is returned to the "thank You" page, where his order number and details are displayed. Upon loading of this page, an email is fired to the user's address, containing the order's details.

