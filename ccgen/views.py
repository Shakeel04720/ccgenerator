from urllib.parse import scheme_chars
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

from requests import get

def check(cc):
    r 	= get(f"https://lookup.binlist.net/{cc}", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', "Accept-Version": "3"}).json()

    
    if r:
        # for scheme
        schemes = r.get('scheme')
        if schemes:
            scheme = str(schemes)
        else:
            scheme = "None"

        # for type
        typess = r.get('type')
        if typess:
            types = str(typess)
        else:
            types = "None"

            # for brand
        brands = r.get('brand')
        if brands:
            brand = str(brands)
        else:
            brand = "None"


        # for prepaid

        prepaids = r.get('prepaid')
        if prepaids:
            prepaid = str(prepaids)
        else:
            prepaid = "None"


        # for country
        countries = r.get('country')
        if countries:
            countryname= countries.get('name')
            if countryname:
                country = str(countryname)


                # for country emoji
                CountryemojiName = countries.get('emoji')
                if CountryemojiName:
                    emoji = str(CountryemojiName)

                # for country currency
                currency = countries.get('currency')
                if currency:
                    currency = str(currency)
        else:
            country = "None"
            emoji = "None"
            currency = "None"


        bank = r.get('bank')
        if bank:
            #for bank Pname
            bank_name= bank.get('name')
            if bank_name:
                bankname = str(bank_name)
                
            # for bank url
            bankUrl = bank.get('url')
            if bankUrl:
                url = str(bankUrl)

            #  for bannk phone
            bankPhone = bank.get('phone')
            if bankPhone:
                phone = str(bankPhone)
        else:
            bankname = "None"
            url = "None"
            phone = "None"
    else:
        return "Wrong Bin"
    return scheme , brand , cc , types , prepaids , country , emoji , currency , bankname , url , phone


def index(request):
    if request.method == "GET":
        binNo = request.GET['binNo']

        binchecked = check(binNo)
        return HttpResponse(f"{binchecked}")

    else:
        return HttpResponse("No Bin")

#
#
#
#
#CC validator
# 
# 
# 
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10


def ccvalidator(request):
    if request.method == "GET":
        card_number = request.GET['cardNo']

        if luhn_checksum(card_number)==0:
            status = True
        else:
            status = False
        return HttpResponse(f"{status}")

    else:
        return HttpResponse("No Bin")
