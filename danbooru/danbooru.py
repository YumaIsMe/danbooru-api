import requests
from requests.auth import HTTPBasicAuth

class Danbooru:
    def __init__(self, username=None, api_key=None):
        """
        Initialize the Danbooru client.

        :param username: Your Danbooru username (optional if no authentication is needed).
        :param api_key: Your Danbooru API key (optional if no authentication is needed).
        """
        self.base_url = 'https://danbooru.donmai.us'
        self.username = username
        self.api_key = api_key

    def _get(self, endpoint, params=None):
        """
        Helper method to make GET requests to the Danbooru API.

        :param endpoint: API endpoint to make the request to.
        :param params: Query parameters for the API request.
        :return: Parsed JSON response, or None if the request fails.
        """
        url = f'{self.base_url}/{endpoint}'
        headers = {}
        auth = None
        if self.username and self.api_key:
            auth = HTTPBasicAuth(self.username, self.api_key)
        try:
            response = requests.get(url, headers=headers, params=params, auth=auth)
            print(f"Request URL: {response.url}")  # Print the request URL
            print(f"Response Status Code: {response.status_code}")  # Print status code
            response.raise_for_status()
            result = response.json()
            print(f"Response Data: {result}")  # Print the response data
            return result
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def search_posts(self, tags='', limit=10, rating=None, **kwargs):
        """
        Search for posts with the specified tags and rating.

        :param tags: Tags to search for (e.g., 'cute', 'landscape').
        :param limit: Number of results to return (default is 10).
        :param rating: Filter posts by rating. Valid options are 's' (safe), 'q' (questionable), 'e' (explicit).
        :param kwargs: Additional parameters for the search (e.g., 'page' for pagination).
        :return: List of posts matching the search criteria or None if an error occurs.

        Example:
            api = Danbooru(username='your_username', api_key='your_api_key')
            posts = api.search_posts(tags='cute', rating='s', limit=5)
        """
        params = {'tags': tags, 'limit': limit, **kwargs}
        if rating:
            params['rating'] = rating  # Add rating as a separate parameter
        
        return self._get('posts.json', params=params)

    def get_post(self, post_id):
        """
        Get details of a specific post by ID.

        :param post_id: ID of the post to retrieve.
        :return: Details of the specified post or None if an error occurs.
        """
        return self._get(f'posts/{post_id}.json')

    def get_tags(self, tag_name=None, limit=10):
        """
        Retrieve tags from Danbooru.

        :param tag_name: Name of the tag to search for (optional).
        :param limit: Number of results to return.
        :return: List of tags or None if an error occurs.
        """
        params = {'name': tag_name, 'limit': limit}
        return self._get('tags.json', params=params)
