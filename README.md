# pencil - in progress
A mockup project of an company website that also sells products.  The site also has basic login and registration, admin console with different user access depends on user's level:
  * Super admin can delete and change any user's level.  At the moment, super admin status is set through database from back end, there's no option for setting super admin through the website, nor an option to designating a super admin.
  * Admin has access to everything, including changing other user's level.  An admin can not change the user's level of another admin, and admin account can not be deleted.  (Super admin can change admin to Staff or Standard before deleting the account.)
  * Staff account has access to product page where they can upload products changes product information.
