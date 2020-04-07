import datetime
from queries.report_query import ReportQuery
from data.azure_connection import fetch_reports


def resolve_report_query(self, info, **kwargs):
    domain = kwargs.get('domain')

    report_list = fetch_reports(domain=domain)

    rtr_list = []
    counter = 1
    for report in report_list:
        rtr_list.append(
            ReportQuery(
                report['report_xml_schema'],
                report['report_org_name'],
                report['report_org_email'],
                report['report_org_contact_info'],
                report['report_id'],
                datetime.datetime.strptime(report['report_begin_date'], '%Y-%m-%d %H:%M:%S'),
                datetime.datetime.strptime(report['report_end_date'], '%Y-%m-%d %H:%M:%S'),
                report['report_errors'],
                report['report_domain'],
                report['policy_adkim'],
                report['policy_aspf'],
                report['policy_domain'],
                report['policy_subdomain'],
                report['policy_percent'],
                report['policy_forensic'],
                report['source_ip_address'],
                report['source_ip_country'],
                report['source_ip_hostname'],
                report['source_ip_domain'],
                report['message_count'],
                report['spf_aligned'],
                report['dkim_aligned'],
                report['dmarc_aligned'],
                report['disposition'],
                report['policy_override_reasons'],
                report['policy_override_comments'],
                report['envelope_from'],
                report['header_from'],
                report['envelope_to'],
                report['dkim_domains'],
                report['dkim_selectors'],
                report['dkim_results'],
                report['spf_domains'],
                report['spf_scopes'],
                report['spf_results']
            )
        )
        counter += 1

    return rtr_list
