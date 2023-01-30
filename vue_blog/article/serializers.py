from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer
# 父类变成了 ModelSerializer
# class ArticleListSerializer(serializers.ModelSerializer):
  
#     url = serializers.HyperlinkedIdentityField(view_name="article:detail")
  
#     author = UserDescSerializer(read_only=True)
#     class Meta:
#         model = Article
#         fields = [
#             # 'id',
#             'url',
#             'title',
#             'created',
#             'author'
#         ]
# read_only_fields = ['author']
# 自动推断需要序列化的字段及类型
# 提供对字段数据的验证器的默认实现
# 提供了修改数据需要用到的 .create() 、 .update() 方法的默认实现
# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
