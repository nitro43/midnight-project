from rest_framework import serializers
from django.db import models
from notebook.models import Contact, Phone


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ('id', 'number')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class ContactSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

    class Meta:
        model = Contact
        fields = ('id', 'name', 'adress', 'phones')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "adress": {
                "required": False,
            },
            "phones": {
                "required": False,
            },
        }

    def create(self, validated_data):
        # Create the contact instance
        phones_data = validated_data.pop('phones')
        contact = Contact.objects.create(**validated_data)
        for phone in phones_data:
            Phone.objects.create(contact=contact, **phone)
        return contact

    def update(self, instance, validated_data):
        # Update the contact instance
        instance.name = validated_data['name']
        if validated_data.get('adress'):
            instance.adress = validated_data['adress']
        instance.save()

        # update and add new phone nums
        phones_db_ids = []
        phone_id_for_del = []
        for item in instance.phones.values('id'):
            phones_db_ids.append(item['id'])

        for item in validated_data['phones']:
            var = item.get('id')
            if var in phones_db_ids:
                phone = Phone.objects.get(pk=var)
                phone.number = item['number']
                phone_id_for_del.append(var)
            else:
                phone = Phone(number=item['number'], contact=instance)
            phone.save()
        # Delete phone numbers not included in the request
        for id in phones_db_ids:
            if id not in phone_id_for_del:
                phone = Phone.objects.get(pk=id)
                phone.delete()
        return instance
