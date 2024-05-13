{
    "name": "G2P Service Provider Beneficiary Management",
    "category": "G2P",
    "version": "17.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_service_provider_portal_base",
        "g2p_registry_membership",
        "website",
    ],
    "data": [
        "views/dashboard.xml",
        "views/error_page.xml",
        "views/group_template.xml",
        "views/success_page.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "g2p_service_provider_benificiary_management/static/src/css/style.css",
        ],
        "web.assets_common": [],
        "website.assets_wysiwyg": [],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}