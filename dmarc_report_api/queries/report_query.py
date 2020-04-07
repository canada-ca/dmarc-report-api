import graphene
from graphene import relay

from dmarc_report_api.scalars import URL, EmailAddress


class ReportQuery(graphene.ObjectType):
    """
    Returns a DMARC report from Azure cosmos based on a domain
    """
    class Meta:
        interfaces = (relay.Node)

    id = graphene.ID()
    report_xml_schema = graphene.String(
        description="Report XML schema version.",
        required=True
    )
    report_org_name = graphene.String(
        description="Organization the dmarc report belongs to.",
        required=True
    )
    report_org_email = EmailAddress(
        description="Organization email address.",
        required=True
    )
    report_org_contact_info = EmailAddress(
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
        description="The domain the report was created from.",
        required=True
    )
    policy_adkim = graphene.String(
        description="DKIM policy on reported domain.",
        required=True
    )
    policy_aspf = graphene.String(
        description="SPF policy on reported domain.",
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
        description="DMARC rejection percentage.",
        required=True
    )
    policy_forensic = graphene.String(
        description="DMARC forensic policy percentage.",
        required=True
    )
    source_ip_address = graphene.String(
        description="The source IP which the report was created from.",
        required=True
    )
    source_ip_country = graphene.String(
        description="The country which the IP is located in.",
        required=True
    )
    source_ip_hostname = URL(
        description="Hostname for the source IP.",
        required=True
    )
    source_ip_domain = URL(
        description="The domain for the source IP.",
        required=True
    )
    message_count = graphene.Int(
        description="Amount of emails sent with the DMARC record.",
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
        description="Unknown",
        required=True
    )
    policy_override_reasons = graphene.String(
        description="Policy override reasons.",
        required=True
    )
    policy_override_comments = graphene.String(
        description="Policy override comments.",
        required=True
    )
    envelope_from = URL(
        description="SPF domain used to check alignment.",
        required=True
    )
    header_from = URL(
        description="The domain DMARC uses to check alignment with SPF/DKIM",
        required=True
    )
    envelope_to = URL(
        description='"Envelope Recipient" in the email header.',
        required=True
    )
    dkim_domains = URL(
        description="DKIM domains.",
        required=True
    )
    dkim_selectors = graphene.String(
        description="DKIM selectors.",
        required=True
    )
    dkim_results = graphene.String(
        description="DKIM results.",
        required=True
    )
    spf_domains = URL(
        description="SPF domains.",
        required=True
    )
    spf_scopes = graphene.String(
        description="SPF scopes.",
        required=True
    )
    spf_results = graphene.String(
        description="SPF results.",
        required=True
    )
    index_id = graphene.String(
        description="Index ID.",
        required=True
    )

    @classmethod
    def get_node(cls, info, id):
        return get_report(id)


class ReportQueryConnection(relay.Connection):
    class Meta:
        node = ReportQuery
