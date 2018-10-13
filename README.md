# pencil - made in Python with Django, SQLite, Bootstrap, jQuery, jQueryUI, Ajax
A mockup project of an company website that also sells products.  The site also has basic login and registration, admin console with different user access depends on user's level:
  * Super Admin, Admin, Staff members, Standard users
  * Super Admin account cannot be altered.  Admins may alter access of other users whose level are lower than themselves.
  * Staff have access to product information where they can perform basic CRUD Operations
  * Every user may update their own information including changing password with appropriate validation
  * User may add items to cart, update and delete items from cart
