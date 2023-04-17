from urllib import request
from DBWrapper import *
from BusinessC import *


def data_extractor(data):
    try:
        sub_str = data.split(' ')
        if len(sub_str) > 1:
            strresult = parsedata(sub_str[0], sub_str[1])
        else:
            strresult = "invalid method"
        return strresult
    except Exception as e:
        app_log.exception(e)


def business_method(methodname, sub_str):
    try:
        if methodname=="GRANDLOTTO":
            ret_data="GRANDLOTTO TCP port Running"
            return ret_data
        ret_data = methodname + "`" + sub_str[0] + "`"
        connection = DB_connect()
        if methodname == "100": # Checking Connectivity
            strquery = "CALL cli_connectivityinfo(%s, %s);"
            strquery1 = sub_str[1], sub_str[2]
        elif methodname == "101": # TermDetails
             strquery = "CALL getterminaldetails_login_v2(%s, %s);"
             strquery1 = sub_str[1], sub_str[2]
        elif methodname == "102": # Login
             strquery = "CALL cli_logincheck_handheld_v4(%s, %s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[3], sub_str[6], sub_str[4], sub_str[5]
        elif methodname == "103": # ChangePassword
             strquery = "CALL cli_changepwd(%s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "104": # IPUpdation
             strquery = "CALL CLI_DynamicIPUpdate(%s, %s);"
             strquery1 = sub_str[1], sub_str[2]
        elif methodname == "105": # FileDownload
             strquery = "CALL CLI_FileDownLoad(%s);"
             strquery1 = sub_str[1],sub_str[1]
        elif methodname == "106": # Version UPDation Checking
             strquery = "CALL M380CheckNewVersion_Handheld(%s);"
             strquery1 = sub_str[1],sub_str[1]
        elif methodname == "107": # VErsion UPDation
             strquery = "CALL CLI_VERSIONUPDATED_HandHeldV1(%s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[2]
        elif methodname == "200": # GAME
            strquery = "CALL getavailablegames_v3(%s, %s, %s);"
            strquery1 = sub_str[2], sub_str[1], sub_str[3]
        elif methodname == "300": # BUY
             strquery = "CALL TRA_PickThreeAndKenoSales_Handheld_V3(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4], sub_str[5], sub_str[6], sub_str[7], sub_str[8], sub_str[9], sub_str[10], sub_str[11]
        elif methodname == "301": # POOLS BUY
             strquery = "CALL tra_pickthreeandkenosales_handheld_v4(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4], sub_str[6], sub_str[5], sub_str[11], sub_str[7], sub_str[8], sub_str[9],sub_str[9], sub_str[10]
        elif methodname == "400": # Direct Claim
             strquery = "CALL cli_winner_checkandprizeclaim(%s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[2], sub_str[1], sub_str[3], sub_str[4], sub_str[6], sub_str[5]
        elif methodname == "401": # Winning Check
             strquery = "CALL CLI_Winner_CheckClaim(%s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[2], sub_str[1], sub_str[3], sub_str[4], sub_str[6], sub_str[5]
        elif methodname == "402": # Claim
             strquery = "CALL CLI_Winner_PrizeClaim(%s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[2], sub_str[1], int(sub_str[3]), sub_str[4], sub_str[6], sub_str[5]
        elif methodname == "403": # PATerminalBlock
             strquery = "CALL RPT_UPD_PA_TerminalClaimBlock(%s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[0]
        elif methodname == "500": # ViewResult
             strquery = "CALL CLI_ViewResult_V3(%s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4], sub_str[5], sub_str[6]
        elif methodname == "501": # ViewResultSoccer
             strquery = "CALL CLI_ViewResult_V3_soc(%s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4], sub_str[5], sub_str[6]
        elif methodname == "502": # SOCCER Winner list
             strquery = "CALL CLI_Winnerlist_Soc(%s, %s);"
             strquery1 = sub_str[1], sub_str[2]
        elif methodname == "503": # ViewResult drawnumberwise
             strquery = "CALL CLI_ViewResult_drawno(%s, %s, %s, %s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4], sub_str[5], sub_str[6], sub_str[7]
        elif methodname == "600": # OPERATORCASH
             strquery = "CALL cli_report_operator_cash_v2(%s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "601":  # Accounts Summary
            strquery = "CALL cli_report_accounts_v2(%s, %s, %s);"
            strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "602":  # SALESSUMMARY
            strquery = "CALL cli_report_salessummary(%s, %s, %s);"
            strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "603":  # TerminalGamewise
            strquery = "CALL cli_gamesummary_v1(%s, %s);"
            strquery1 = sub_str[1], sub_str[2]
        elif methodname == "604": # PATerminalReport
             strquery = "CALL CLI_REPORT_PATerminal(%s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "606": # Soccer Match Details
             strquery = "CALL Cli_get_SoccermatchDetails_hh(%s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "607": # Soccer Match Details
             strquery = "CALL CLI_REPORT_accounts_V2_soc(%s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "608": # Coupon Scheme
             strquery = "CALL Cli_view_soccerscheme_Coupan(%s, %s, %s, %s);"
             strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4]
        elif methodname == "609":  # Account Soccer Weekly
            strquery = "CALL CLI_REPORT_accounts_V2_soc_weekly(%s, %s);"
            strquery1 = sub_str[1], sub_str[2]
        elif methodname == "610":  # GameName and DrawNo
            strquery = "CALL CLI_CBO_Get_GameAndDrawno(%s, %s, %s, %s);"
            strquery1 = sub_str[1], sub_str[2], sub_str[3], sub_str[4]
        elif methodname == "611":  # Soccer Match Details NEW
            strquery = "CALL Cli_get_SoccermatchDetails_hh_New(%s, %s, %s);"
            strquery1 = sub_str[1], sub_str[2], sub_str[3]
        elif methodname == "700":  # LastTransactionwith
            strquery = "CALL getlast10transaction_gameid(%s, %s);"
            strquery1 = sub_str[1],sub_str[1]
        elif methodname == "701":  # LastTransactionwith
            strquery = "CALL gettransactiondetails_v1(%s, %s);"
            strquery1 = sub_str[2],sub_str[1]
        elif methodname == "702":  # Cancel
            strquery = "CALL transaction_cancel(%s, %s);"
            strquery1 = sub_str[2],sub_str[1]
        elif methodname == "703":  # Soccer Scheme Coupon
            strquery = "CALL Cli_view_soccerscheme_Coupan_v2(%s, %s);"
            strquery1 = sub_str[1], sub_str[2]
        elif methodname == "800":  # LOGOUT
            strquery = "CALL CLI_LOGOUT_RETRY_V2(%s, %s);"
            strquery1 = sub_str[1], sub_str[2]
        else :
            strquery= ""

        if len(strquery)>2 :
            result = DB_callsp(connection, strquery, strquery1)
            ret_data += result
        else :
            ret_data ="-1"
    except Exception as e:
        app_log.exception(e)
    finally:
        if connection:
            DB_commit(connection)
            DB_close(connection)
        ret_data=ret_data+"*"
        return ret_data


def parsedata(methodname, data):
    try:
        sub_str = data.split('~')
        return business_method(methodname, sub_str)
    except Exception as e:
        app_log.exception(e)
