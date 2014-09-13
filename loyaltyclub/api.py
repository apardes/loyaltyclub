from tastypie.resources import ModelResource
from club.models import Member, Business, Credit, Transaction
from tastypie.serializers import Serializer 
import simplejson
from django.core.serializers import json
from twilio import twiml

class PrettyJSONSerializer(Serializer):
	json_indent = 4

	def to_json(self, data, options = None):
		options = options or {}
		data = self.to_simple(data, options)
		return simplejson.dumps(data, cls = json.DjangoJSONEncoder, sort_keys = True, ensure_ascii = False, indent = self.json_indent)


class BusinessResource(ModelResource):
	class Meta:
		queryset = Business.objects.all()
		resource_name = "business"
		#serializer = PrettyJSONSerializer()

class TransactionResource(ModelResource):
	class Meta:
		queryset = Transaction.objects.all()
		resource_name = 'transaction'

	def prepend_urls(self):
		return [
			url(r'^(?P<resource_name>%s)/callback%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('callBack'), name = 'callBack'),
			url(r'^(?P<resource_name>%s)/phonecall%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('phoneCall'), name = 'phoneCall'),

			]

	def callBack(self, request, **kwargs):
		self.method_check(request, allowed = ['post'])
		data = self.deserialize(request, request.body, format = request.META.get('CONTENT_TYPE', 'application/json'))


		print "it worked"

		return self.create_response(request, {'success' : True})
			
