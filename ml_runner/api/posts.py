from flask_restful import Resource, fields, marshal_with

from . import api
from ..models import Post

post_fields = {
    'content': fields.String,
    'creation_date': fields.DateTime,
}
post_list_fields = {
    'posts': fields.List(fields.Nested(post_fields)),
}


class PostsEndpoint(Resource):
    @marshal_with(post_fields, envelope='posts')
    def get(self, **kwargs):
        posts = Post.query.all()
        return posts


class PostEndpoint(Resource):
    @marshal_with(post_fields, envelope='post')
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post


api.add_resource(PostsEndpoint, '/posts/')
api.add_resource(PostEndpoint, '/posts/<int:post_id>/')