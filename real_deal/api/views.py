from rest_framework import viewsets, response


class OffersViewSet(viewsets.GenericViewSet):
    def get_queryset(self):
        return False

    def list(self, request, *args, **kwargs):
        data = [
            {
                'title': 'Save $10',
                'shortDescription': 'Save $10 on your purchase!',
                'copy': 'Save $10 on purchases that exceed $50 when you use your Visa card',
                'merchants': [
                    {
                        'name': 'Bed Bath and Beyond'
                    }
                ]
            },
            {
                'title': 'Save $50',
                'shortDescription': 'Save $30 on keg purchases',
                'copy': 'Save $30 on the purchase of any keg of beer when you use your Visa card',
                'merchants': [
                    {
                        'name': 'Bed Bath and Beyond'
                    }
                ]
            }
        ]
        return response.Response(data)
