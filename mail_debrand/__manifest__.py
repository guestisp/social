# Copyright 2016 Tecnativa - Jairo Llopis
# Copyright 2017 Tecnativa - Pedro M. Baeza
# Copyright 2019 ForgeFlow S.L. - Lois Rilo <lois.rilo@forgeflow.com>
# 2020 NextERP Romania
# Copyright 2021 Tecnativa - João Marques
# Copyright 2024 Modern Logic - Andrew Rahn
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Mail Debrand",
    "summary": """Remove Odoo branding in sent emails
    Removes anchor <a href odoo.com together with it's parent
    (for powered by) from all the templates
    removes any 'odoo' that are in template texts > 20 characters
    """,
    "version": "17.0.0.0.0",
    "category": "Social Network",
    "website": "https://github.com/OCA/social",
    "author": """Modern Logic, Tecnativa, ForgeFlow, Onestein, Sodexis, Nexterp Romania,
             Odoo Community Association (OCA)""",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail"],
    "development_status": "Production/Stable",
    "maintainers": ["pedrobaeza", "joao-p-marques"],
}
