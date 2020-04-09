import graphene

from dmarc_report_api.scalars import URL, EmailAddress


class ReportQuery(graphene.ObjectType):
    """
    Returns a DMARC report from Azure cosmos based on a domain
    """

    report_xml_schema = graphene.String(
        description="Report XML schema version.",
        required=True
    )
    report_org_name = graphene.String(
        description="Organization that produced the report.",
        required=True
    )
    report_org_email = EmailAddress(
        description="Organization email address.",
        required=True
    )
    report_org_contact_info = graphene.String(
        description="Organizations contact email address.",
        required=True
    )
    report_id = graphene.String(
        description="ID of the DMARC aggregate report.",
        required=True
    )
    report_begin_date = graphene.DateTime(
        description="When the report was started.",
        required=True
    )
    report_end_date = graphene.DateTime(
        description="When the report was completed.",
        required=True
    )
    report_errors = graphene.String(
        description="Any errors generated during the report creation.",
        required=True
    )
    report_domain = URL(
        description="The domain at which the DMARC record was found.",
        required=True
    )
    policy_adkim = graphene.String(
        description="DKIM alignment mode on reported domain.",
        required=True
    )
    policy_aspf = graphene.String(
        description="SPF alignment mode on reported domain.",
        required=True
    )
    policy_domain = graphene.String(
        description="Domains DMARC policy.",
        required=True
    )
    policy_subdomain = graphene.String(
        description="Sub Domains DMARC policy",
        required=True
    )
    policy_percent = graphene.String(
        description="DMARC percentage policy.",
        required=True
    )
    policy_forensic = graphene.String(
        description="DMARC forensic policy.",
        required=True
    )
    source_ip_address = graphene.String(
        description="The IP address from which messages were received.",
        required=True
    )
    source_ip_country = graphene.String(
        description="The country which the IP is located in.",
        required=True
    )
    source_ip_hostname = graphene.String(
        description="Hostname for the source IP.",
        required=True
    )
    source_ip_domain = graphene.String(
        description="The domain for the source IP.",
        required=True
    )
    message_count = graphene.Int(
        description="Count of emails received.",
        required=True
    )
    spf_aligned = graphene.Boolean(
        description="Is the SPF domain aligned with the DMARC domain.",
        required=True
    )
    dkim_aligned = graphene.Boolean(
        description="Is the DKIM domain aligned with the DMARC domain.",
        required=True
    )
    dmarc_aligned = graphene.Boolean(
        description="Is the DMARC domain aligned with SPF and DKIM domains.",
        required=True
    )
    disposition = graphene.String(
        description="The DMARC policy applied by the receiver",
        required=True
    )
    policy_override_reasons = graphene.String(
        description="Reasons why the receiver applied a specific policy.",
        required=True
    )
    policy_override_comments = graphene.String(
        description="Policy override comments.",
        required=True
    )
    envelope_from = graphene.String(
        description="Domain used in the SMTP MAIL FROM field.",
        required=True
    )
    header_from = graphene.String(
        description="Domain used in the FROM header",
        required=True
    )
    envelope_to = graphene.String(
        description="Domain used in the SMTP RCPT TO field",
        required=True
    )
    dkim_domains = graphene.String(
        description="Domains used in DKIM headers",
        required=True
    )
    dkim_selectors = graphene.String(
        description="Selectors used in DKIM headers",
        required=True
    )
    dkim_results = graphene.String(
        description="Results of DKIM validation",
        required=True
    )
    spf_domains = graphene.String(
        description="Domains used in SPF validation",
        required=True
    )
    spf_scopes = graphene.String(
        description="Sources of SPF domains",
        required=True
    )
    spf_results = graphene.String(
        description="Results of SPF validation",
        required=True
    )
