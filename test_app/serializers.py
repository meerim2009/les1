from rest_framework import serializers

from test_app.models import Post, Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id text post'.split()


class PostsSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = 'id title text created_date comments count'.split()

    def get_comments(self, instance):
        comments = Comment.objects.filter(post_id=instance)
        return CommentSerializer(comments, many=True).data



