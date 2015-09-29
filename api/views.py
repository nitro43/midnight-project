from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from notebook.models import Contact
from notebook.models import Phone
from api.serializers import PhoneSerializer
from api.serializers import ContactSerializer
from itertools import chain


@api_view(['POST'])
def contact_search(request, chars):
    # Search by POST (for AJAX)
    try:
        contacts_by_name = Contact.objects.filter(name__contains=chars)
        phones = Phone.objects.filter(number__contains=chars).\
            values_list('contact_id', flat=True)
        contacts_by_phone = Contact.objects.filter(pk__in=phones)
        merged_contacts = contacts_by_name | contacts_by_phone

    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = ContactSerializer(merged_contacts, many=True)
        return Response(serializer.data)


class ContactList(APIView):
    """
    List all contacts, or create a new contacts.
    """
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
    """
    Get, udpate or delete a specific contact
    """
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
