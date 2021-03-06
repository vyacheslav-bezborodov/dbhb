from closure_table.comments.views import (
    comment_get_tree_view,
    comment_create_view,
    comment_delete_view,
    comment_update_view,
    comment_get_view,
    comment_search_view,
)

ENDPOINT = '/comments'


def setup_routes(app):
    comment_collection = app.router.add_resource(ENDPOINT)
    comment_collection.add_route('GET', comment_get_view)
    comment_collection.add_route('POST', comment_create_view)

    comment = app.router.add_resource(ENDPOINT + '/{id}')
    comment.add_route('GET', comment_get_tree_view)
    comment.add_route('PATCH', comment_update_view)
    comment.add_route('DELETE', comment_delete_view)

    app.router.add_route('GET', ENDPOINT + '/search/{text}', comment_search_view)
