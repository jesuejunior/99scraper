#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests.auth import HTTPBasicAuth
from core.action.company import company_create
from core.action.extractor import _extract
import requests
from core.list_company import LIST_COMPANY

__author__ = 'jesuejunior'

from splinter import Browser
from lxml import etree

company_xpath = {
        "title": ["//h1[@class='company-title']/a"],
        "rank": ["//aside[@class='aside-company']//div[@class='company-evaluation']//div[@class='company-evaluation-score has-lg-text']"],
        "vacancy": ["//aside[@class='aside-company']//div[@class='company-aside-actions']/div/div[4]//b"],
        "follows": ["//aside[@class='aside-company']//div[@class='company-aside-actions']//div[@class='square-box-body']/b[@class='total-followers']"],
        "mission": ["//div[@class='panel panel-default'][1]/div[@class='panel-body']/div[@class='panel-body-section'][1]/p"],
        "about": ["//div[@class='panel-body']/div[@class='panel-body-section'][2]/p"],
        "thumb": ["//a[@class='company-logo square-box']//img/@src"],
        }


def catch_metadata(xpath, tree):
    for el in xpath:
        go_return = []
        elements = tree.xpath(el)
        if elements:
            for el in elements:
                if isinstance(el, (basestring, unicode)):
                    go_return = [el]
                else:
                    go_return += [text for text in el.itertext(with_tail=True)]

    return "".join(go_return)

html = ""
res = requests.get('https://www.99jobs.com/users/sign_in', auth=HTTPBasicAuth('talkto@jesuejunior.com', 'mamute22'))
companies = []

for comp in LIST_COMPANY:
    if res.status_code == 200:
        link = 'https://www.99jobs.com/{0}'.format(comp)
        parser = etree.HTMLParser(remove_comments=True, encoding='utf-8')

        html = requests.get(link).content
        # with Browser() as browser:
        #      # Visit URL
        #      browser.visit(link)
        #      # Pagina pronta
        #      html = browser.html

        tree = etree.fromstring(html, parser)
        company = {}
        # profile['username'] = user['username']

        for key, value in company_xpath.iteritems():
            company[key] = catch_metadata(value, tree)

        companies.append(company)
        # company_create(company)
        print company['title']
        print company['rank']
        print company['vacancy']
        print company['thumb']
        print "company atualizado com sucesso."

print {"companies": companies}
