from aiohttp import web

from .db.queries import create_comment


async def create_view(request):
    params = await request.json()
    parent_id = params.get('parent_id')
    content = params.get('content')
    if not content:
        return web.json_response(status=400, data={
            'error': 'content cannot be empty'
        })
    async with request.app['db'].acquire() as conn:
        comment_id = await create_comment(conn, content, parent_id)
        return web.json_response({
            'id': comment_id
        })
