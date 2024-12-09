from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from apps.links.models import Link
from apps.orders.serializers import OrderSerializer
from apps.products.models.products import Product
from apps.products.serializers import ProductSerializer


class CreateOrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = []

    def get(self, request):
        link_id = request.query_params.get('link')
        product_id = request.query_params.get('product')
        if not link_id and not product_id:
            return Response({'error': 'link and product not found'}, status=404)
        if link_id:
            link = get_object_or_404(Link.objects.select_related('product'), id_generate=link_id)
            product = link.product
        if product_id:
            product = get_object_or_404(Product, id=product_id)
        return Response(
            {'id_generate': product.id_generate,
             'name': product.name,
             'price': product.price,
             'description': product.description,
             'video_url': product.video_url,
             'delivery_price': product.delivery_price,
             'like_counts': product.like_counts,
             'view_counts': product.view_counts,
             'comment_counts': product.comment_counts,
             'features': product.get_features(),
             'images': ProductSerializer(product).data['images'],
             })

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)