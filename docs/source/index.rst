.. Danbooru API Wrapper documentation master file, created by
   sphinx-quickstart on Thu Sep 12 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Danbooru API Wrapper's documentation!
=================================================

A lightweight wrapper for the Danbooru API.

Installation
------------

You can install the library via pip:

.. code-block:: shell

    pip install git+https://github.com/YumaIsMe/danbooru-api.git

Usage
-----

Here’s how you can use the Danbooru API Wrapper:

1. **Initialization**:

    You need to initialize the `Danbooru` client with your Danbooru username and API key (optional if no authentication is needed).

    .. code-block:: python

        from danbooru.danbooru import Danbooru

        # Initialize the Danbooru API client
        api = Danbooru(username='your_username', api_key='your_api_key')

2. **Search for Posts**:

    You can search for posts with specific tags and ratings.

    .. code-block:: python

        # Search for posts with the tag 'cute', rating 's' (safe), and limit to 5 results
        posts = api.search_posts(tags='cute', rating='s', limit=5)

        # Print the results
        for post in posts:
            print(post)

3. **Get a Specific Post**:

    Retrieve details of a specific post by its ID.

    .. code-block:: python

        # Get details of post with ID 123
        post = api.get_post(post_id=123)
        print(post)

4. **Retrieve Tags**:

    You can retrieve tags from Danbooru, optionally searching by tag name.

    .. code-block:: python

        # Get a list of tags with a limit of 10
        tags = api.get_tags(limit=10)
        print(tags)

API Reference
-------------

The API provides methods to interact with Danbooru's posts and tags. Below are descriptions of the available methods:

- **`search_posts(tags='', limit=10, rating=None, **kwargs)`**: Search for posts with specified tags and rating.
- **`get_post(post_id)`**: Get details of a specific post by ID.
- **`get_tags(tag_name=None, limit=10)`**: Retrieve tags from Danbooru.

Configuration
-------------

The `Danbooru` client can be configured with optional parameters:

- **`username`**: Your Danbooru username (if authentication is required).
- **`api_key`**: Your Danbooru API key (if authentication is required).

Contributing
------------

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.
