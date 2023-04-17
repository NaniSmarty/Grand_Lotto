
import psycopg2.extras
import logging
import pandas as pd
from GILogger import *


def table_data(cur,rows):
    try:
        df_list = []
        row_count = cur.rowcount
        columns = [column[0] for column in cur.description]  # Fetching Table Meta details i.e., Column Name etc
        df_list.append(pd.DataFrame.from_records(rows, columns=columns))    # Converting into DataFrame   
        json_list=[]
        for i in df_list:
            y = i.to_dict(orient='records') # Converting to Dictionary
            json_list.append(y)
        return json_list
    except Exception as e:
        app_log.exception(e)


def DB_select(conn,id):
    try:
        cur = conn.cursor()
        cur.execute(f"""select * from test1 where id = {id};""")  # Executing Query
        rows = cur.fetchall()
        json_list=table_data(cur,rows)
        return json_list
    except Exception as e:
        app_log.exception(e)


def DB_insert(conn,id,name,address,mobile):
    try:
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO public.test1(id, name, address, mobile) VALUES({id}, '{name}', '{address}', {mobile});""")
        return cur.rowcount
    except Exception as e:
        app_log.exception(e)


def DB_update(conn, id, column, value):
    try:
        cur = conn.cursor()
        cur.execute(f"""UPDATE test1 SET {column} = '{value}' where id = {id};""")
        return cur.rowcount
    except Exception as e:
        app_log.exception(e)


def DB_delete(conn,id):
    try:
        cur=conn.cursor()
        cur.execute(f"""DELETE FROM test1 WHERE id = {id}""")
        return cur.rowcount
    except Exception as e:
        app_log.exception(e)
        
def foo(conn,bar):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""select *  from playersession;""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
#############REGISTRATION#########################

def register(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lstrPassWord,lStrTNAME,lStrMail,lStrAPPNAME):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_PLAYER_REG""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
######################OTP############################

def otp(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_CLI_OTPGeneration_Resend""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
#######################OTP VERIFICATION##############

def verify_otp(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrOTP):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_Player_Otp_Verification""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
########################LOGIN#######################

def login(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lstrPassWord,lStrVersion,pstrclientip,lintRetry,lStrTeminalInfo):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_LOGIN""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
#########################GAMES#######################

def availablegames(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lIntRegionId,strVersionID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_GetAvailableGames""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
########################TerminalDetails#################

def terminaldetails(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lstrVersionId):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_TERMDETAILS""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
########################BUY##############################

def buy(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lintGameID,lStrDrawDate,lStrBetStr,lStrTranID,lIntRequest,lintDrawTimeInSec,lintTotalBetCount,lStrStakeAmt,lstrMobile,pstrclientip):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""APP_Buy_MultiBets""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
##########################VIEW RESULT#########################

def view_result(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrFromDate,lStrToDate,lIntFlag):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_ViewResult""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
##########################ACCOUNT#############################

def account_summary(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrFromDate,lStrToDate,lIntFlag,):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute(f"""EXEC APP_REPORT_accounts {pstrTerminalId}""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
###########################FILE DOWNLOAD########################

def filedownload(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_FileDownLoad""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
##########################LAST TRANSACTION######################

def lasttransaction(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lIntGamegroupid,lStrConn):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""APP_GetLast10transaction""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
###########################CHECK WINNING##################

def check_winning(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrMobile,lStrPrizecode):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""exec APP_Checkclaim""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
############################OTP##############################

def otp_(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrMobile,lStrPrizecode):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""exec APP__InitiateOTP""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
###########################PRIZECLAIM#########################

def prize_claim(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrMobile,lStrPrizecode,lstrOTP):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""exec APP_PrizeClaim""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)

############################LOG OUT#############################

def logout(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lintRetry):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_LOGOUT""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
#############################IP UPDATION#############################33#

def ipupdation(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrVersionId):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_IPUpdate""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
################################CHANGE PASSWORD##########################

def change_password(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrOldPwd,lStrnewPwd):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""Exec APP_CHANGEPWD""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
##############################CANCEL TICKET##############################

def cancel_ticket(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrTranId):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""APP_Trans_CANCELL""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
###############################REPRINT###################################

def transacdetails(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrTranId):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""APP_REPRINT""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
###############################SALES SUMMARY#######################

def salessummary(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrFromDate,lStrToDate):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_SalesSummaryReport""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
###############################TERMINAL CREDIT LIMIT##########################

def credit_limit(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_CreditLimt""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
############################TERMINAL QUOTA#############################
#########################GET PA QUOTA############## 
def getpa_quota(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_GET_PAQuota""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)

######################TERMINAL QUOTA ########################3

def terminal_quota(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrPATERMINALID,lIntCrdlimit):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_UPD_TerminalQuota""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
####################GET ALL PAQUOTA######################

def get_all_pa_quota(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrPATERMINALID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_UPD_TerminalQuota""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
########################PA TERMINAL REPORT##########################
def rpt_paterminal(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumberm,lstrConfigID,lStrRptTERMINALID,lStrRptdatetime):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_REPORT_PATerminal""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)

#########################INWARD/OUTWARD########################
def inward_outward(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrTID,lStrPAIDAMT,lStrTxid,pstrclientip):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_INS_Paymentdetails""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
#########################GET APP INFO###############
def get_appinfo(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC Get_Appdetails""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)

#########################FORGET PASSWORD############

def forget_pwd_otp_gen(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_CLI_OTPGeneration_FRGT_PWD""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
#######################OTP VALIDATION####################

def otp_verify(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lStrOTP):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_Player_Otp_Verification_FRGT_PWD""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)
        
#######################WITHDRAWAL#########################

def withdraw_app(conn,pstrTerminalId,lintTVN,lintSessionId,lstrIMEINumber,lstrConfigID,lIntAmt,lStrClntID):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        fetch_all_as_dict = lambda cursor: [dict(row) for row in cursor]
        cur.execute("""EXEC APP_Get_BalanceAmount""")
        result=fetch_all_as_dict(cur)
        return result
    except Exception as e:
        app_log.exception(e)




















#################################################################################

