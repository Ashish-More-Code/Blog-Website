![image](https://github.com/user-attachments/assets/6e11e1a6-b0a3-4556-a139-d7c93c1214ad)

<p align="center">Blog Portal</p>
An interactive blog portal where users can post, edit, delete blogs, and engage with others through likes and comments.


<p align="center">Features</p>
**User Authentication**

Users can register and log in to the portal.


<p align="center">Create and Manage Blogs</p>

Post new blogs.

Edit and delete blogs from "My Blogs" section.


<p align="center">Dashboard </p>

View the total number of blogs posted by the user.

View the combined total number of blogs.


<p align="center">Home Page</p>

Browse and read all blogs.

Filter blogs by category.

Like and comment on blogs.

users can like blog only once



<p align="center">Blog Approval System </p>

_**Overview**_

This project features a blog system where users can write and submit blogs. By default, the submitted blogs are not visible on the website until they are reviewed and approved by an admin. This ensures that only appropriate content is published.

_**How It Works**_

User Submission: Users submit blogs through a user interface.

Flagging: The is_active flag for each new blog is automatically set to 0.

Admin Review: Admin users access the Django admin interface to review submitted blogs.

Approval: Admin users can approve blogs by setting the is_active flag to 1.

Visibility: Approved blogs become visible on the website.
