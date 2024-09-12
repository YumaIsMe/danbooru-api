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

Here’s a basic example of how to use the wrapper:

.. code-block:: python

    from danbooru_api import Danbooru

    # Initialize the Danbooru API client
    api = Danbooru(api_key='your_api_key_here')

    # Fetch some posts
    posts = api.get_posts(tags='example_tag')

    # Print the results
    for post in posts:
        print(post)

Features
--------

- Fetch posts by tags
- Retrieve post details
- Handle API errors gracefully

Configuration
--------------

You can configure the wrapper using a configuration file or directly in your code. Here’s an example configuration:

.. code-block:: python

    api = Danbooru(api_key='your_api_key_here', base_url='https://danbooru.example.com')

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
