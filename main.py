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
        "title": ["//div[@class='row']/aside[@class='aside-company']/div[@class='aside-company-inner affix-top']/div[1]/header/h1[@class='company-title']/a"],
        "rank": ["//aside[@class='aside-company']/div[@class='aside-company-inner affix']/div[1]/div[@class='company-evaluation']/div[@class='company-evaluation-score has-lg-text']"],
        "vacancy": ["//div[@class='square-box is-half is-odd'][2]/div[@class='square-box-body']/b"],
        "follows": ["//div[@class='square-box is-half'][1]/div[@class='square-box-body']/b[@class='total-followers']"],
        "mission": ["//div[@class='panel panel-default'][1]/div[@class='panel-body']/div[@class='panel-body-section'][1]/p"],
        "about": ["//div[@class='panel-body']/div[@class='panel-body-section'][2]/p",
                  "//main/section[@class='section section-company']/div[@class='panel panel-default'][1]/div[@class='panel-body']/div[@class='panel-body-section']/p"],
        "thumb": ["//div[@class='aside-company-inner affix-top']/a[@class='company-logo square-box']/div[@class='square-box-body']/img/@src"],
        }

def catch_metadata(xpath, tree):
    go_return = None

    for el in xpath:
        elements = tree.xpath(el)
        if elements:
            for el in elements:
                for text in el.itertext(with_tail=True):
                    clean_text = text
                    if clean_text:
                        go_return = clean_text
    return go_return

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

        for key,value in company_xpath.iteritems():
            company[key] = catch_metadata(value, tree)

        companies.append(company)

        # company_create(company)
        print company['title']
        print company['rank']
        print company['vacancy']
        print company['thumb']
        print "company atualizado com sucesso."

print {"companies": companies}
